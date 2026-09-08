"""Add an arXiv paper to the library from its id.

Given an arXiv id, this:
  1. fetches structured metadata from the arXiv API (also an existence check),
  2. downloads the latest-version PDF into papers/pdfs/,
  3. fetches the paper's HTML (arXiv native, then ar5iv), converts it to
     Markdown with pandoc (MathML -> LaTeX), and writes it to papers/md/ with
     a YAML metadata header.

The filename is generated from the metadata as
<year>-<first-author>-<title-slug>-arxiv<id>v<N>, shared by the PDF and the
Markdown. Any version in the input is ignored; the latest version is used.

Usage:
    uv run scripts/sync_library.py                 # process all ids in the index
    uv run scripts/sync_library.py 2412.07626      # add one paper
    uv run scripts/sync_library.py 2412.07626 1706.03762   # add several
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

USER_AGENT = "roryarden/qml/0.1 (https://arxiv.org; contact: local script)"

PDF_DIR = Path("papers/pdfs")
MD_DIR = Path("papers/md")
INDEX_PATH = Path("papers/index.md")
LUA_FILTER = Path(__file__).parent / "clean.lua"

INDEX_HEADER = (
    "# Paper Library Index\n\n"
    "Source of truth for the library, keyed by arXiv id. PDFs and Markdown under\n"
    "`pdfs/` and `md/` are a regenerable cache \u2014 rebuild any paper with:\n\n"
    "```sh\n"
    "uv run scripts/sync_library.py <arxiv-id>\n"
    "```\n\n"
    "## Papers\n\n"
    "| Year | Author | Title | arXiv |\n"
    "|------|--------|-------|-------|"
)

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


def fetch(url: str) -> str | None:
    """Return the page body if the URL responds 200, else None."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        print(f"  {url} -> HTTP {exc.code}", file=sys.stderr)
    except urllib.error.URLError as exc:
        print(f"  {url} -> {exc.reason}", file=sys.stderr)
    return None


def fetch_bytes(url: str) -> bytes | None:
    """Return the raw response body if the URL responds 200, else None."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        print(f"  {url} -> HTTP {exc.code}", file=sys.stderr)
    except urllib.error.URLError as exc:
        print(f"  {url} -> {exc.reason}", file=sys.stderr)
    return None


def extract_article(html: str) -> str:
    """Return just the LaTeXML article body, dropping arXiv site chrome."""
    match = re.search(
        r"<article\b[^>]*>(.*)</article>", html, re.DOTALL | re.IGNORECASE
    )
    return match.group(1) if match else html


def absolutize_urls(html: str, base_url: str) -> str:
    """Rewrite relative src/href URLs to absolute so images resolve on GitHub."""

    def repl(match: re.Match[str]) -> str:
        attr, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "data:", "#", "mailto:")):
            return match.group(0)
        return f'{attr}="{urllib.parse.urljoin(base_url, url)}"'

    return re.sub(r'(src|href)="([^"]*)"', repl, html)


def strip_inline_graphics(html: str) -> str:
    """Remove LaTeXML inline SVG and base64 data-URI images.

    arXiv renders TikZ diagrams and callout boxes as inline <svg>; pandoc would
    otherwise base64-encode each into a huge data-URI <img>. Real figure images
    (http/https <img>) and <figcaption>s are left intact.
    """
    html = re.sub(r"<svg\b.*?</svg>", "", html, flags=re.DOTALL | re.IGNORECASE)
    return re.sub(r'<img\b[^>]*\bsrc="data:[^"]*"[^>]*>', "", html)


def display_math_to_dollars(text: str) -> str:
    """Convert pandoc's ``` math fenced blocks to $$...$$ for GitHub."""
    pattern = re.compile(r"^``` ?math\n(.*?)\n```$", re.MULTILINE | re.DOTALL)
    return pattern.sub(lambda m: f"$$\n{m.group(1)}\n$$", text)


def html_to_markdown(html: str) -> str:
    """Convert HTML to GitHub-flavored Markdown, keeping math as $...$.

    Disabling native_divs/native_spans makes pandoc unwrap LaTeXML's <div> and
    <span class="ltx_..."> wrappers instead of passing them through as raw HTML.
    """
    if shutil.which("pandoc") is None:
        raise RuntimeError("pandoc not found. Install it with: brew install pandoc")
    result = subprocess.run(
        [
            "pandoc",
            "-f",
            "html-native_divs-native_spans",
            "-t",
            "gfm+tex_math_dollars",
            "--wrap=none",
            "--lua-filter",
            str(LUA_FILTER),
        ],
        input=html,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def slugify(text: str) -> str:
    """Lowercase, hyphenate, and strip a string for use in a filename."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_stem(meta: dict[str, Any], versioned_id: str) -> str:
    """Build the shared PDF/Markdown filename stem from metadata."""
    year = meta["published"][:4] if meta["published"] else ""
    authors = meta["authors"]
    last_name = slugify(authors[0].split()[-1]) if authors and authors[0] else "unknown"
    slug = slugify(meta["title"])[:60].strip("-")
    parts = [p for p in (year, last_name, slug) if p]
    return "-".join(parts) + f"-arxiv{versioned_id}"


def download_pdf(versioned_id: str, pdf_path: Path) -> bool:
    """Download the PDF for a specific version; return True on success."""
    url = f"https://arxiv.org/pdf/{versioned_id}"
    print(f"Downloading PDF {url} ...", file=sys.stderr)
    data = fetch_bytes(url)
    if data is None:
        return False
    if not data.startswith(b"%PDF"):
        print("  response was not a PDF; skipping", file=sys.stderr)
        return False
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.write_bytes(data)
    print(f"Saved PDF to {pdf_path}", file=sys.stderr)
    return True


def _collapse(text: str | None) -> str:
    """Collapse arXiv's wrapped whitespace into a single-spaced string."""
    return " ".join(text.split()) if text else ""


def fetch_metadata(arxiv_id: str) -> dict[str, Any] | None:
    """Fetch structured metadata for a paper from the arXiv API."""
    query = urllib.parse.urlencode({"id_list": arxiv_id})
    xml = fetch(f"{ARXIV_API}?{query}")
    if xml is None:
        return None

    entry = ET.fromstring(xml).find("atom:entry", ATOM_NS)
    if entry is None:
        return None

    def text(tag: str) -> str:
        return _collapse(entry.findtext(tag, namespaces=ATOM_NS))

    primary = entry.find("arxiv:primary_category", ATOM_NS)
    pdf_url = ""
    for link in entry.findall("atom:link", ATOM_NS):
        if link.attrib.get("title") == "pdf":
            pdf_url = link.attrib.get("href", "")

    return {
        "title": text("atom:title"),
        "authors": [
            _collapse(a.findtext("atom:name", namespaces=ATOM_NS))
            for a in entry.findall("atom:author", ATOM_NS)
        ],
        "published": text("atom:published")[:10],
        "updated": text("atom:updated")[:10],
        "primary_category": primary.attrib.get("term", "") if primary is not None else "",
        "categories": [
            c.attrib.get("term", "")
            for c in entry.findall("atom:category", ATOM_NS)
        ],
        "doi": text("arxiv:doi"),
        "journal_ref": text("arxiv:journal_ref"),
        "comment": text("arxiv:comment"),
        "abs_url": text("atom:id"),
        "pdf_url": pdf_url,
        "abstract": text("atom:summary"),
    }


def _yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_front_matter(arxiv_id: str, meta: dict[str, Any]) -> str:
    """Render arXiv metadata as a YAML front-matter block."""
    lines = ["---", f"title: {_yaml_quote(meta['title'])}"]

    if meta["authors"]:
        lines.append("authors:")
        lines.extend(f"  - {_yaml_quote(name)}" for name in meta["authors"])

    lines.append(f"arxiv: {_yaml_quote(arxiv_id)}")

    for key in ("published", "updated", "primary_category"):
        if meta[key]:
            lines.append(f"{key}: {meta[key]}")

    if meta["categories"]:
        lines.append("categories: [" + ", ".join(meta["categories"]) + "]")

    for key in ("doi", "journal_ref", "comment", "abs_url", "pdf_url"):
        if meta[key]:
            lines.append(f"{key}: {_yaml_quote(meta[key])}")

    if meta["abstract"]:
        lines.append("abstract: >")
        lines.append(f"  {meta['abstract']}")

    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _display_author(authors: list[str]) -> str:
    if not authors:
        return "Unknown"
    last_name = authors[0].split()[-1]
    return f"{last_name} et al." if len(authors) > 1 else last_name


def update_index(meta: dict[str, Any], versioned_id: str) -> None:
    """Insert or refresh this paper's row in papers/index.md, sorted by year."""
    year = meta["published"][:4] if meta["published"] else ""
    author = _display_author(meta["authors"])
    title = meta["title"].replace("|", "\\|")
    row = (
        f"| {year} | {author} | {title} | "
        f"[{versioned_id}](https://arxiv.org/abs/{versioned_id}) |"
    )
    base_id = re.sub(r"v\d+$", "", versioned_id)

    prefix = INDEX_HEADER
    rows: list[str] = []
    if INDEX_PATH.exists():
        lines = INDEX_PATH.read_text(encoding="utf-8").splitlines()
        sep_idx = next(
            (
                i
                for i, line in enumerate(lines)
                if "|" in line and "-" in line and set(line.strip()) <= set("|-: ")
            ),
            None,
        )
        if sep_idx is not None:
            prefix = "\n".join(lines[: sep_idx + 1])
            rows = [ln for ln in lines[sep_idx + 1 :] if ln.strip().startswith("|")]

    rows = [r for r in rows if f"/abs/{base_id}" not in r]
    rows.append(row)

    def row_year(r: str) -> int:
        first = r.strip("| ").split("|", 1)[0].strip()
        return int(first) if first.isdigit() else 0

    rows.sort(key=row_year, reverse=True)
    INDEX_PATH.write_text(prefix + "\n" + "\n".join(rows) + "\n", encoding="utf-8")


def add_paper(arxiv_id: str) -> bool:
    """Download the PDF and write the Markdown + index row for one arXiv id."""
    base_id = re.sub(r"v\d+$", "", arxiv_id)

    print("Fetching metadata from arXiv API ...", file=sys.stderr)
    meta = fetch_metadata(base_id)
    if meta is None:
        print(f"No arXiv metadata found for {arxiv_id}; skipping.", file=sys.stderr)
        return False

    match = re.search(r"/abs/(\S+)$", meta["abs_url"])
    versioned_id = match.group(1) if match else base_id
    stem = build_stem(meta, versioned_id)

    pdf_ok = download_pdf(versioned_id, PDF_DIR / f"{stem}.pdf")
    if not pdf_ok:
        print("  PDF download failed; continuing with Markdown", file=sys.stderr)

    candidates = [
        f"https://arxiv.org/html/{versioned_id}",
        f"https://ar5iv.org/abs/{versioned_id}",
    ]

    html = None
    source_url = ""
    for candidate in candidates:
        print(f"Trying {candidate} ...", file=sys.stderr)
        html = fetch(candidate)
        if html is not None:
            print(f"Fetched from {candidate}", file=sys.stderr)
            source_url = candidate
            break

    if html is None:
        print(f"No HTML available for {versioned_id}", file=sys.stderr)
        return False

    markdown = build_front_matter(versioned_id, meta)
    article = absolutize_urls(strip_inline_graphics(extract_article(html)), source_url)
    markdown += display_math_to_dollars(html_to_markdown(article))

    md_path = MD_DIR / f"{stem}.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown, encoding="utf-8")
    print(f"Saved Markdown to {md_path}", file=sys.stderr)

    update_index(meta, versioned_id)
    print(f"Updated index {INDEX_PATH}", file=sys.stderr)
    return True


def read_index_ids() -> list[str]:
    """Return the arXiv ids linked in papers/index.md, in order, de-duplicated."""
    if not INDEX_PATH.exists():
        return []
    found = re.findall(
        r"/abs/([0-9]+\.[0-9]+(?:v[0-9]+)?)", INDEX_PATH.read_text(encoding="utf-8")
    )
    seen: set[str] = set()
    unique: list[str] = []
    for arxiv_id in found:
        if arxiv_id not in seen:
            seen.add(arxiv_id)
            unique.append(arxiv_id)
    return unique


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "arxiv_ids",
        nargs="*",
        help="arXiv ids to add. If omitted, every id in papers/index.md is processed.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=3.0,
        help="Seconds to wait between papers when processing several.",
    )
    args = parser.parse_args()

    ids = args.arxiv_ids or read_index_ids()
    if not ids:
        print(
            "No arXiv ids given and none found in papers/index.md.", file=sys.stderr
        )
        return 1

    failures: list[str] = []
    for n, arxiv_id in enumerate(ids, start=1):
        if n > 1:
            time.sleep(args.delay)
        print(f"[{n}/{len(ids)}] {arxiv_id}", file=sys.stderr)
        if not add_paper(arxiv_id):
            failures.append(arxiv_id)

    if failures:
        print(
            f"Done with {len(failures)} failure(s): {', '.join(failures)}",
            file=sys.stderr,
        )
        return 1
    print(f"Done. {len(ids)} paper(s) processed.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
