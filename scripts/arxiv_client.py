"""Shared arXiv HTTP + Atom helpers used by the digest and library scripts.

Centralizes the polite fetch layer (User-Agent, ~3s request spacing, and HTTP
429 backoff) plus the Atom namespace map, so both scripts talk to arXiv the same
way.
"""

from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request

USER_AGENT = "roryarden/qml/0.1 (https://arxiv.org; contact: local script)"
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# arXiv asks callers to space requests ~3s apart and rate-limits per IP.
REQUEST_DELAY = 3.0
MAX_RETRIES = 4
BACKOFF_BASE = 3.0


def collapse(text: str | None) -> str:
    """Collapse whitespace runs in an Atom text field to single spaces."""
    return " ".join(text.split()) if text else ""


def _open_with_retry(url: str, timeout: int):
    """Open a URL, backing off and retrying when arXiv returns HTTP 429."""
    for attempt in range(MAX_RETRIES):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            return urllib.request.urlopen(request, timeout=timeout)
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == MAX_RETRIES - 1:
                raise
            retry_after = exc.headers.get("Retry-After", "")
            delay = (
                float(retry_after)
                if retry_after.isdigit()
                else BACKOFF_BASE * (2**attempt)
            )
            print(f"  {url} -> HTTP 429; retrying in {delay:.0f}s", file=sys.stderr)
            time.sleep(delay)
    raise urllib.error.URLError("retry limit exceeded")


def fetch(url: str) -> str | None:
    """Return the page body if the URL responds 200, else None."""
    try:
        with _open_with_retry(url, timeout=30) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        print(f"  {url} -> HTTP {exc.code}", file=sys.stderr)
    except urllib.error.URLError as exc:
        print(f"  {url} -> {exc.reason}", file=sys.stderr)
    return None


def fetch_bytes(url: str) -> bytes | None:
    """Return the raw response body if the URL responds 200, else None."""
    try:
        with _open_with_retry(url, timeout=60) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        print(f"  {url} -> HTTP {exc.code}", file=sys.stderr)
    except urllib.error.URLError as exc:
        print(f"  {url} -> {exc.reason}", file=sys.stderr)
    return None
