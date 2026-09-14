---
description: "Scaffold a new browser-runnable marimo notebook that teaches one QML algorithm, following the notebooks authoring spec (Introduction, Math, Circuit/Model, Interactive demo, Why it works, Summary, Further reading)."
name: "New Notebook"
argument-hint: "Name the algorithm to scaffold (e.g. /new-notebook Deutsch-Jozsa)"
agent: "agent"
tools: [search, edit]
---

You scaffold a new learning notebook for this repository. The algorithm to build
is given by the user's argument (e.g. "Deutsch–Jozsa", "quantum kernel
estimation"). Work autonomously and produce a single new file
`notebooks/<snake_case_name>.py`.

## Inputs (read these first)

- **Content spec (source of truth):** [notebooks/AUTHORING.md](../../notebooks/AUTHORING.md)
- **Technical constraints & build:** [notebooks/README.md](../../notebooks/README.md)
- **Reference notebook to mirror:** [notebooks/bernstein_vazirani.py](../../notebooks/bernstein_vazirani.py)

Follow `AUTHORING.md` for the section structure and style. Do not restate it
here — read it and comply.

## Hard constraints

1. **Browser-runnable.** The notebook runs in Pyodide (WASM). Use only
   pure-Python wheels plus Pyodide's prebuilt scientific stack (NumPy, SciPy,
   scikit-learn, pandas, matplotlib). **Never** import PennyLane or Qiskit —
   they have no Pyodide wheel. Build the algorithm from scratch with NumPy.
2. **PEP 723 header.** Start the file with an inline script-metadata block
   pinning dependencies, matching the reference notebook's header.
3. **marimo format.** The file is a marimo notebook (plain Python). Reproduce the
   cell conventions from `bernstein_vazirani.py`: markdown cells for exposition,
   `mo-python` cells for interactive code, one import per cell at the bottom,
   `_`-prefixed cell-local throwaways.
4. **Cap problem sizes** so the computation stays small and responsive in WASM.

## Sections to produce (per the spec)

Introduction → Mathematical formulation → The model/circuit → Interactive demo
(control → compute → result + matplotlib figure) → Why it works → Summary →
Further reading → imports.

## After scaffolding

1. Register the notebook in the "Notebooks" list in
   [notebooks/README.md](../../notebooks/README.md) with a one-line description.
2. Tell the user how to preview it locally:
   `uvx marimo edit --sandbox notebooks/<name>.py`

## Note on live editing

If the target notebook is already open in VS Code with a running kernel, prefer
the marimo kernel tooling over direct file writes (see the marimo instructions).
For fresh scaffolding of a new file, writing the `.py` directly is correct.

## Guardrail

Only create the new notebook and update the README list. Do not run commands or
modify unrelated files.
