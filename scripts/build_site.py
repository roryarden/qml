"""Build the browser-runnable QML notebook website.

Exports every marimo notebook under ``notebooks/`` to a self-contained
WebAssembly HTML app (Python runs in the visitor's browser via Pyodide) and
generates an ``index.html`` gallery that links to each one. The resulting
``site/`` directory is what gets published to GitHub Pages.

Usage:
    uv run --group site python scripts/build_site.py
    uv run --group site python scripts/build_site.py --mode edit
"""

from __future__ import annotations

import argparse
import html
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
DEFAULT_OUTPUT = REPO_ROOT / "site"


def find_notebooks(directory: Path) -> list[Path]:
    """Return notebook files in `directory`, skipping private/underscore files."""
    return sorted(p for p in directory.glob("*.py") if not p.name.startswith("_"))


def title_for(notebook: Path) -> str:
    """Turn a file stem like ``bernstein_vazirani`` into ``Bernstein Vazirani``."""
    return notebook.stem.replace("_", " ").title()


def export_notebook(notebook: Path, out_dir: Path, mode: str) -> None:
    """Export a single notebook to a WASM HTML app under `out_dir`."""
    subprocess.run(
        [
            sys.executable,
            "-m",
            "marimo",
            "export",
            "html-wasm",
            str(notebook),
            "-o",
            str(out_dir),
            "--mode",
            mode,
            "--no-sandbox",
            "--show-code",
        ],
        check=True,
    )


def render_index(notebooks: list[Path]) -> str:
    """Render the gallery landing page linking to each exported notebook."""
    cards = "\n".join(
        f'      <li><a href="./{n.stem}/">{html.escape(title_for(n))}</a></li>'
        for n in notebooks
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>QML Notebooks</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 42rem; margin: 4rem auto;
           padding: 0 1rem; line-height: 1.6; color: #1a1a1a; }}
    h1 {{ margin-bottom: 0.25rem; }}
    p.lede {{ color: #555; margin-top: 0; }}
    ul {{ list-style: none; padding: 0; }}
    li {{ margin: 0.5rem 0; }}
    a {{ color: #2a9d8f; text-decoration: none; font-weight: 600; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>Quantum Machine Learning Notebooks</h1>
  <p class="lede">Interactive marimo notebooks that run entirely in your browser.</p>
  <nav>
    <ul>
{cards}
    </ul>
  </nav>
</body>
</html>
"""


def build(output: Path, mode: str) -> int:
    """Export all notebooks and write the gallery. Returns a process exit code."""
    notebooks = find_notebooks(NOTEBOOKS_DIR)
    if not notebooks:
        print(f"No notebooks found in {NOTEBOOKS_DIR}", file=sys.stderr)
        return 1

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    for notebook in notebooks:
        print(f"Exporting {notebook.name} -> {output / notebook.stem}")
        export_notebook(notebook, output / notebook.stem, mode)

    (output / "index.html").write_text(render_index(notebooks), encoding="utf-8")
    print(f"Wrote {output / 'index.html'} ({len(notebooks)} notebooks)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Directory to write the built site into (default: ./site).",
    )
    parser.add_argument(
        "--mode",
        choices=("edit", "run"),
        default="run",
        help="'run' ships a read-only app (default); 'edit' is editable.",
    )
    args = parser.parse_args()
    return build(args.output, args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
