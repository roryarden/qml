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
    uv run scripts/add_from_arxiv.py 2412.07626
    uv run scripts/add_from_arxiv.py 1706.03762
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

USER_AGENT = "roryarden/qml/0.1 (https://arxiv.org; contact: local script)"

PDF_DIR = Path("papers/pdfs")
MD_DIR = Path("papers/md")
LUA_FILTER = Path(__file__).parent / "clean.lua"

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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "arxiv_id",
        help="arXiv id, optionally with a version suffix (e.g. 2412.07626v2).",
    )
    args = parser.parse_args()

    base_id = re.sub(r"v\d+$", "", args.arxiv_id)

    print("Fetching metadata from arXiv API ...", file=sys.stderr)
    meta = fetch_metadata(base_id)
    if meta is None:
        print(
            f"No arXiv metadata found for {args.arxiv_id}; aborting without writing.",
            file=sys.stderr,
        )
        return 1

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
    for url in candidates:
        print(f"Trying {url} ...", file=sys.stderr)
        html = fetch(url)
        if html is not None:
            print(f"Fetched from {url}", file=sys.stderr)
            break

    if html is None:
        print(f"No HTML available for {versioned_id}", file=sys.stderr)
        return 1

    markdown = build_front_matter(versioned_id, meta)
    markdown += html_to_markdown(extract_article(html))

    md_path = MD_DIR / f"{stem}.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown, encoding="utf-8")
    print(f"Saved Markdown to {md_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
