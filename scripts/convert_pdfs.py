"""Convert every PDF under papers/pdfs to Markdown under papers/md.

The subfolder layout (e.g. transformers/) is mirrored, and files are skipped
when an up-to-date Markdown version already exists.

Conversion uses marker-pdf, which keeps LaTeX equations and tables. On an
NVIDIA GPU it runs in `balanced` mode; on CPU/Apple Silicon it falls back to
marker's `fast` mode. CUDA is detected at runtime, so the same script works on
the Mac (no CUDA -> fast) and the PC (CUDA -> balanced).

Usage:
    uv run scripts/convert_pdfs.py                 # new/changed only
    uv run scripts/convert_pdfs.py --force         # reconvert everything
    uv run scripts/convert_pdfs.py --mode balanced
    uv run scripts/convert_pdfs.py --use-llm       # marker + LLM refinement
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PDF_DIR = Path("papers/pdfs")
MD_DIR = Path("papers/md")


def detect_device() -> str:
    """Return 'cuda', 'mps', or 'cpu' based on what torch can see."""
    try:
        import torch
    except ImportError:
        return "cpu"
    try:
        if torch.cuda.is_available():
            return "cuda"
        if torch.backends.mps.is_available():
            return "mps"
    except Exception:
        pass
    return "cpu"


def marker_available() -> bool:
    return shutil.which("marker_single") is not None


def convert_with_marker(
    pdf_path: Path, md_path: Path, mode: str, use_llm: bool
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            "marker_single",
            str(pdf_path),
            "--output_dir",
            tmp,
            "--output_format",
            "markdown",
            "--mode",
            mode,
        ]
        if use_llm:
            cmd.append("--use_llm")
        subprocess.run(cmd, check=True)

        produced = next(Path(tmp).rglob("*.md"), None)
        if produced is None:
            raise RuntimeError(f"marker produced no Markdown for {pdf_path}")
        md_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(produced, md_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("balanced", "fast"),
        default=None,
        help="marker mode. Default: balanced on CUDA, fast otherwise.",
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Pass --use_llm to marker for higher-accuracy math/tables.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reconvert even when the Markdown file is newer than the PDF.",
    )
    args = parser.parse_args()

    if not PDF_DIR.exists():
        print(f"No PDF directory found at {PDF_DIR}", file=sys.stderr)
        return 1

    if not marker_available():
        print(
            "'marker_single' is not on PATH. Install it with: uv add marker-pdf",
            file=sys.stderr,
        )
        return 1

    device = detect_device()
    mode = args.mode or ("balanced" if device == "cuda" else "fast")
    print(f"Engine: marker ({mode} mode) | device: {device}")

    converted = 0
    skipped = 0

    for pdf_path in sorted(PDF_DIR.rglob("*.pdf")):
        md_path = MD_DIR / pdf_path.relative_to(PDF_DIR).with_suffix(".md")

        up_to_date = (
            md_path.exists()
            and md_path.stat().st_mtime >= pdf_path.stat().st_mtime
        )
        if up_to_date and not args.force:
            skipped += 1
            continue

        print(f"Converting {pdf_path} -> {md_path}")
        convert_with_marker(pdf_path, md_path, mode, args.use_llm)
        converted += 1

    print(f"Done. {converted} converted, {skipped} up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
