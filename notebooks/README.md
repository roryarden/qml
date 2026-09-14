# Notebooks

Interactive [marimo](https://marimo.io) notebooks of QML algorithms, written for
learning. Each notebook is a plain Python file (git-friendly, no JSON diffs) and
is designed to run **entirely in the browser** once published, so the site needs
no backend.

## Notebooks

- [`bernstein_vazirani.py`](bernstein_vazirani.py) — the Bernstein–Vazirani
  algorithm, simulated from scratch with NumPy.
- [`deutsch_jozsa.py`](deutsch_jozsa.py) — the Deutsch–Jozsa algorithm: decide
  constant vs. balanced in a single quantum query, built from scratch with NumPy.

## Authoring locally

Each notebook is self-contained: its runtime dependencies are pinned inline via
PEP 723 script metadata, so edit it in a sandbox marimo builds from that header —
the same declaration the browser build uses:

```sh
uvx marimo edit --sandbox notebooks/bernstein_vazirani.py
```

## Browser-runnable constraint (important)

The site runs Python in the browser via **Pyodide** (WebAssembly). Only packages
with pure-Python wheels — plus the scientific packages Pyodide pre-builds
(NumPy, SciPy, scikit-learn, pandas, matplotlib) — can be imported.

Notably, **PennyLane and Qiskit do _not_ run in the browser**: both pull in
compiled dependencies (`pennylane-lightning`, `rustworkx`, Qiskit's Rust core)
that have no Pyodide wheel. Keep the browser-facing notebooks on NumPy/SciPy.

Each notebook declares its dependencies inline via
[PEP 723](https://peps.python.org/pep-0723/) script metadata at the top of the
file. If a notebook ever needs a native-only package, exclude it from WASM with a
platform marker so it still runs locally:

```python
# /// script
# dependencies = [
#     "numpy",
#     "some-native-pkg; sys_platform != 'emscripten'",
# ]
# ///
```

## Building the site

```sh
uv run --no-default-groups --group site python scripts/build_site.py   # outputs ./site/
```

Each notebook is exported to a self-contained WASM app under `site/<name>/`, and
a gallery `site/index.html` links to them. On push to `main`, the
[deploy-notebooks workflow](../.github/workflows/deploy-notebooks.yml) rebuilds
`site/` and publishes it to GitHub Pages.
