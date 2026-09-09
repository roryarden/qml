"""Pull the latest quantum-machine-learning papers from arXiv into a digest.

Run this once a day. The digest is a metadata-only staging list (nothing is
downloaded or converted) so you can skim it and promote interesting entries into
the library with:

    uv run scripts/sync_library.py <arxiv-id>

The ledger (papers/ledger.json) is a *permanent rolling accumulation*: each run
merges the latest arXiv hits into it (deduped by arXiv id, recording arXiv's own
submission and revision timestamps in `published` and `last_updated`). Entries
are never removed and its construction is
independent of the library — promoting a paper into papers/index.md leaves its
ledger record untouched.

Retrieval is a gap-free incremental sync: each run pages backward through the
lastUpdatedDate-descending feed until it reaches the newest `last_updated`
already in the ledger. Miss a day (or several) and the next run simply pages
further back to catch everything in between, bounded by MAX_PAGES.

The human-readable papers/digest.md is a fresh snapshot of exactly the papers
that changed in that run — both newly seen papers and revisions (v1→v2) that
resurfaced — as a flat list sorted by last-updated timestamp (most recent first).
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sync_library import ATOM_NS, fetch

ARXIV_API = "http://export.arxiv.org/api/query"
DIGEST_PATH = Path("papers/digest.md")
LEDGER_PATH = Path("papers/ledger.json")

# Categories + keywords that scope the feed to quantum machine learning.
SEARCH_QUERY = (
    "(cat:quant-ph OR cat:cs.LG OR cat:cs.AI) AND "
    '(all:"quantum machine learning" OR all:"quantum neural network" '
    'OR all:"variational quantum" OR all:"quantum kernel")'
)
# One arXiv page; pages are walked back until the ledger watermark is reached.
PAGE_SIZE = 100
MAX_PAGES = 10  # hard cap so a long gap (or first run) can't runaway-page.
PAGE_DELAY = 3.0  # seconds between page requests (arXiv asks for ~3s).


def _collapse(text: str | None) -> str:
    return " ".join(text.split()) if text else ""


def _display_author(authors: list[str]) -> str:
    if not authors:
        return "Unknown"
    last_name = authors[0].split()[-1]
    return f"{last_name} et al." if len(authors) > 1 else last_name


def parse_entries(xml: str) -> list[dict[str, Any]]:
    """Parse arXiv Atom results into digest entries."""
    entries: list[dict[str, Any]] = []
    for entry in ET.fromstring(xml).findall("atom:entry", ATOM_NS):
        def text(tag: str) -> str:
            return _collapse(entry.findtext(tag, namespaces=ATOM_NS))

        abs_url = text("atom:id")
        match = re.search(r"/abs/(\S+)$", abs_url)
        versioned_id = match.group(1) if match else ""
        primary = entry.find("arxiv:primary_category", ATOM_NS)
        entries.append(
            {
                "versioned_id": versioned_id,
                "base_id": re.sub(r"v\d+$", "", versioned_id),
                "title": text("atom:title"),
                "authors": [
                    _collapse(a.findtext("atom:name", namespaces=ATOM_NS))
                    for a in entry.findall("atom:author", ATOM_NS)
                ],
                "published": text("atom:published"),
                "last_updated": text("atom:updated"),
                "primary_category": (
                    primary.attrib.get("term", "") if primary is not None else ""
                ),
                "abstract": text("atom:summary"),
                "abs_url": abs_url,
            }
        )
    return entries


def ledger_watermark(ledger: dict[str, dict[str, Any]]) -> str | None:
    """Newest arXiv revision timestamp already ingested, or None if empty."""
    stamps = [
        e["last_updated"] for e in ledger.values() if e.get("last_updated")
    ]
    return max(stamps) if stamps else None


def fetch_pages(watermark: str | None) -> list[dict[str, Any]] | None:
    """Page the lastUpdatedDate feed until it crosses the ledger watermark.

    With no watermark (first run) a single page is fetched. Otherwise pages are
    walked back until the oldest entry on a page is at or before the watermark,
    or MAX_PAGES is hit. Returns None only if the very first page fails.
    """
    collected: list[dict[str, Any]] = []
    for page in range(MAX_PAGES):
        query = urllib.parse.urlencode(
            {
                "search_query": SEARCH_QUERY,
                # arXiv accepts one sort key; lastUpdatedDate surfaces revisions.
                "sortBy": "lastUpdatedDate",
                "sortOrder": "descending",
                "start": page * PAGE_SIZE,
                "max_results": PAGE_SIZE,
            }
        )
        xml = fetch(f"{ARXIV_API}?{query}")
        if xml is None:
            return None if page == 0 else collected
        entries = parse_entries(xml)
        if not entries:
            break
        collected.extend(entries)
        # Stop once we've paged into already-ingested territory or ran short.
        oldest = entries[-1]["last_updated"]
        if len(entries) < PAGE_SIZE or watermark is None or oldest <= watermark:
            break
        time.sleep(PAGE_DELAY)
    return collected


def load_ledger() -> dict[str, dict[str, Any]]:
    """Load the accumulated digest ledger, keyed by version-less arXiv id."""
    if not LEDGER_PATH.exists():
        return {}
    data = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    return {entry["base_id"]: entry for entry in data}


def save_ledger(ledger: dict[str, dict[str, Any]]) -> None:
    # Newest submission first.
    data = sorted(ledger.values(), key=lambda e: e["published"], reverse=True)
    LEDGER_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def merge_entries(
    ledger: dict[str, dict[str, Any]],
    fetched: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Merge fetched entries into the ledger.

    Returns (new_entries, revised_entries) — exactly the records that changed in
    this run, which is what the digest renders. An unchanged paper is left
    untouched.
    """
    new_entries: list[dict[str, Any]] = []
    revised_entries: list[dict[str, Any]] = []
    for entry in fetched:
        existing = ledger.get(entry["base_id"])
        if existing is None:
            ledger[entry["base_id"]] = entry
            new_entries.append(entry)
        elif entry["versioned_id"] != existing.get("versioned_id"):
            ledger[entry["base_id"]] = entry
            revised_entries.append(entry)
        # Unchanged: leave the stored record as-is.
    return new_entries, revised_entries


def render_digest(
    entries: list[dict[str, Any]], revised_ids: set[str]
) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        "# arXiv QML Digest",
        "",
        f"Quantum-machine-learning papers that changed in the {today} retrieval",
        "(new submissions and resurfaced revisions), newest first. Metadata only",
        "— promote an entry into the library with:",
        "",
        "```sh",
        "uv run scripts/sync_library.py <arxiv-id>",
        "```",
        "",
        f"_Retrieved: {today} · {len(entries)} changed today · full history in "
        "ledger.json_",
        "",
    ]
    for entry in entries:
        author = _display_author(entry["authors"])
        tag = " · ↻ revised" if entry["base_id"] in revised_ids else ""
        lines.append(f"### {author} — {entry['title']}")
        lines.append(
            f"[{entry['versioned_id']}]({entry['abs_url']}) · "
            f"{entry['last_updated'][:10]} · {entry['primary_category']}{tag}"
        )
        lines.append("")
        lines.append(f"> {entry['abstract']}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ledger = load_ledger()
    watermark = ledger_watermark(ledger)

    print("Querying arXiv ...", file=sys.stderr)
    fetched = fetch_pages(watermark)
    if fetched is None:
        print("arXiv query failed; digest not updated.", file=sys.stderr)
        return 1

    new_entries, revised_entries = merge_entries(ledger, fetched)

    # digest.md renders exactly what changed in this run (new + revised).
    changed = new_entries + revised_entries
    revised_ids = {e["base_id"] for e in revised_entries}
    changed.sort(key=lambda e: e["last_updated"], reverse=True)

    DIGEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    save_ledger(ledger)
    DIGEST_PATH.write_text(render_digest(changed, revised_ids), encoding="utf-8")
    print(
        f"{len(new_entries)} new, {len(revised_entries)} revised, "
        f"{len(ledger)} in ledger, {len(changed)} in {DIGEST_PATH}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
