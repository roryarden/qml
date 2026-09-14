# Authoring notebooks

This is the **content spec** for notebooks in this directory. It's the single
source of truth for how a notebook is structured and written. For the
*technical* side — dependencies, the Pyodide/WASM constraint, and how the site
is built — see [README.md](README.md).

## Purpose

Each notebook teaches **one** quantum (machine-learning) algorithm by building it
from scratch and letting the reader poke at it. The goals, in order:

1. **Explain** the idea clearly, from motivation through the math to the mechanism.
2. **Show** it working with an interactive demo that runs entirely in the browser.
3. **Ground** it in references the reader can follow to go deeper.

Notebooks are plain Python files (marimo), git-friendly, and must run in the
browser via Pyodide — so keep them on NumPy/SciPy and friends (see the
browser-runnable constraint in [README.md](README.md)).

## Structure

Author the sections in this order. Markdown sections carry the exposition;
`mo-python` cells carry the interactive parts. Keep imports in their own cells at
the **bottom** of the file (marimo resolves the dependency graph, so ordering is
about reading flow, not execution).

### 1. Introduction (markdown)

- A `#` H1 title — the algorithm's name.
- One short paragraph: what problem this solves, why it matters, and the
  classical-vs-quantum framing (e.g. "classical needs $n$ queries; this needs
  one").
- A closing sentence noting it's built from scratch and runs in your browser.

### 2. Mathematical formulation (markdown)

- State the problem precisely in math, using KaTeX (`$...$` inline, `$$...$$`
  block).
- Define all notation once, here. Don't introduce symbols in later sections
  without defining them.

### 3. The model / circuit (markdown)

- Describe the algorithm as a numbered list of steps (for circuits) or a clear
  procedural description (for ML models).
- This is the "what happens", not yet the "why" — save the derivation for §5.

### 4. Interactive demo (`mo-python`)

The heart of the notebook. Structure it as a small pipeline of cells:

- **Control cell(s):** one or more `mo.ui` widgets (`mo.ui.text`, `mo.ui.slider`,
  …) that expose the interesting knobs. Echo the interpreted input back with
  `mo.md(...)`.
- **Compute cell:** a pure function that takes the inputs and returns results.
  Keep it self-contained and readable — this is the code the reader studies.
- **Result cell(s):** a `mo.md` summary of the outcome and at least one
  matplotlib figure visualizing it.

Guardrails:

- **Cap problem sizes** so the state vector / computation stays small and the
  WASM app stays responsive (e.g. BV caps the secret at 10 qubits).
- Sanitize widget input (strip, validate, fall back to a sensible default).
- Prefix cell-local throwaway variables with `_` so marimo doesn't treat them as
  shared globals.

### 5. Why it works (markdown)

- The derivation that ties the demo back to the math in §2.
- This is where the insight lives — connect the mechanism (phase kickback,
  interference, a kernel, …) to the result the reader just saw. Don't skip it.

### 6. Summary (markdown)

- 2–3 takeaways.
- A crisp complexity / performance comparison where it applies (classical vs.
  quantum queries, gates, samples, …).

### 7. Further reading (markdown)

- A short bibliography as a linked list: original paper(s), a good textbook
  treatment, and any tutorial the reader can jump to.
- Prefer stable links (arXiv, DOI, canonical docs).

### Imports (`mo-python`, at the bottom)

- One import per cell, e.g. `import marimo as mo`, `import numpy as np`,
  `import matplotlib.pyplot as plt`.

## Style

- **Tone:** explain to a curious reader who knows linear algebra but not this
  algorithm. Motivate before you formalize.
- **Math:** KaTeX everywhere; define notation before using it.
- **Code:** favor explicitness over cleverness — the reader is here to learn.
  A short docstring on the main compute function is welcome; skip narrating
  obvious lines.
- **Figures:** label axes and title every plot; highlight the meaningful result
  (e.g. color the winning bar).

## Reference example

[bernstein_vazirani.py](bernstein_vazirani.py) follows this spec end to end —
use it as the template.
