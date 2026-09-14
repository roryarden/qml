# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo==0.24.2",
#     "numpy==2.5.3",
#     "matplotlib==3.11.2",
# ]
# ///
"""Deutsch–Jozsa, simulated from scratch with NumPy.

Runs both locally (`marimo edit notebooks/deutsch_jozsa.py`) and in the
browser, since it depends only on NumPy and matplotlib.
"""

import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Deutsch–Jozsa

    You are handed a black-box function $f:\{0,1\}^n \to \{0,1\}$ with a
    **promise**: it is either **constant** (the same output on every input)
    or **balanced** (output $0$ on exactly half of the inputs and $1$ on the
    other half). The task is only to decide *which*.

    A **classical** deterministic algorithm can, in the worst case, need
    $2^{n-1} + 1$ queries: after seeing $2^{n-1}$ identical answers you still
    cannot rule out a balanced function. **Deutsch–Jozsa** decides with a
    **single** quantum query.

    This notebook builds the full state vector by hand with NumPy, so every
    step is explicit and it runs entirely in your browser.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## The problem

    Let $f:\{0,1\}^n \to \{0,1\}$ satisfy the promise

    $$f \text{ is constant} \quad\text{or}\quad
      \big|\{x : f(x) = 0\}\big| = \big|\{x : f(x) = 1\}\big| = 2^{n-1}.$$

    We access $f$ only through a reversible **oracle**
    $$U_f : |x\rangle|y\rangle \mapsto |x\rangle|y \oplus f(x)\rangle,$$
    where $x \in \{0,1\}^n$ indexes the input register and $y \in \{0,1\}$ is
    a single output qubit. The goal is to output `constant` or `balanced`.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## The circuit

    1. Prepare $n$ input qubits in $|0\rangle$ and one output qubit in $|1\rangle$.
    2. Apply a Hadamard to every qubit. The output qubit becomes $|-\rangle$,
       which turns the oracle into a **phase kickback**.
    3. Apply the oracle $|x\rangle|y\rangle \mapsto |x\rangle|y \oplus f(x)\rangle$.
    4. Apply a Hadamard to the $n$ input qubits.
    5. Measure the input register. Outcome $0^n$ ⇒ **constant**; any other
       outcome ⇒ **balanced**.
    """
    )
    return


@app.cell
def _(mo):
    n_slider = mo.ui.slider(1, 6, value=3, label="Number of input qubits $n$")
    kind_dropdown = mo.ui.dropdown(
        options=[
            "Constant (0)",
            "Constant (1)",
            "Balanced (parity)",
            "Balanced (first bit)",
        ],
        value="Balanced (parity)",
        label="Hidden function $f$",
    )
    mo.vstack([n_slider, kind_dropdown])
    return kind_dropdown, n_slider


@app.cell
def _(np):
    def make_truth_table(kind, n):
        """Return the length-2^n array of f(x) values for the chosen function."""
        size = 2**n
        if kind == "Constant (0)":
            return np.zeros(size, dtype=int)
        if kind == "Constant (1)":
            return np.ones(size, dtype=int)
        if kind == "Balanced (parity)":
            # f(x) = parity of x — flips on exactly half the inputs.
            return np.array([bin(x).count("1") & 1 for x in range(size)], dtype=int)
        # "Balanced (first bit)": f(x) = most-significant bit of x.
        return np.array([(x >> (n - 1)) & 1 for x in range(size)], dtype=int)

    return (make_truth_table,)


@app.cell
def _(kind_dropdown, make_truth_table, mo, n_slider):
    n = n_slider.value
    f_table = make_truth_table(kind_dropdown.value, n)
    _promise = "constant" if kind_dropdown.value.startswith("Constant") else "balanced"
    mo.md(
        f"Using **{kind_dropdown.value}** on **{n} qubits** — a *{_promise}* "
        f"function over ${2**n}$ inputs."
    )
    return f_table, n


@app.cell
def _(np):
    def deutsch_jozsa(f_table):
        """Return (verdict, input_probabilities) for the oracle `f_table`."""
        n = int(round(np.log2(len(f_table))))
        dim = 2 ** (n + 1)
        # Basis index encodes the n input qubits in the high bits and the single
        # output qubit in the lowest bit: index = (x << 1) | y.
        state = np.zeros(dim, dtype=complex)
        state[1] = 1.0  # input |0...0>, output |1>

        hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
        identity = np.eye(2, dtype=complex)

        # Step 2: Hadamard on all n + 1 qubits.
        all_h = np.array([[1.0 + 0j]])
        for _ in range(n + 1):
            all_h = np.kron(all_h, hadamard)
        state = all_h @ state

        # Step 3: oracle |x>|y> -> |x>|y XOR f(x)>.
        oracle = np.zeros((dim, dim), dtype=complex)
        for basis in range(dim):
            x = basis >> 1
            y = basis & 1
            fx = int(f_table[x]) & 1
            oracle[(x << 1) | (y ^ fx), basis] = 1.0
        state = oracle @ state

        # Step 4: Hadamard on the n input qubits, identity on the output qubit.
        input_h = np.array([[1.0 + 0j]])
        for _ in range(n):
            input_h = np.kron(input_h, hadamard)
        input_h = np.kron(input_h, identity)
        state = input_h @ state

        # Step 5: marginal measurement probabilities over the input register.
        amplitudes = state.reshape(2**n, 2)
        input_probs = np.sum(np.abs(amplitudes) ** 2, axis=1)

        verdict = "constant" if input_probs[0] > 0.5 else "balanced"
        return verdict, input_probs

    return (deutsch_jozsa,)


@app.cell
def _(deutsch_jozsa, f_table):
    verdict, input_probs = deutsch_jozsa(f_table)
    return input_probs, verdict


@app.cell
def _(input_probs, kind_dropdown, mo, n, verdict):
    _promise = "constant" if kind_dropdown.value.startswith("Constant") else "balanced"
    _ok = "✅" if verdict == _promise else "❌"
    _classical = 2 ** (n - 1) + 1
    mo.md(
        f"""
    ## Result

    - Hidden function is **{_promise}**; measured $P(0^n) = {input_probs[0]:.3f}$.
    - Verdict from **one** quantum query: **{verdict}** {_ok}
    - Classical worst case: **{_classical}** queries &nbsp;·&nbsp; quantum
      queries: **1**
    """
    )
    return


@app.cell
def _(input_probs, np, plt):
    _fig, _ax = plt.subplots(figsize=(8, 3))
    _xs = np.arange(len(input_probs))
    _ax.bar(_xs, input_probs, color="#c7c7c7")
    _ax.bar([0], [input_probs[0]], color="#2a9d8f")
    _ax.set_xlabel("input register value $z$")
    _ax.set_ylabel("probability")
    _ax.set_title("Measurement distribution of the input register")
    _ax.set_ylim(0, 1.05)
    _fig
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Why it works

    After the first layer of Hadamards the input register is a uniform
    superposition and the output qubit is $|-\rangle$:

    $$\frac{1}{\sqrt{2^n}} \sum_{x} |x\rangle \otimes |-\rangle.$$

    The oracle acts by **phase kickback**,
    $|x\rangle|-\rangle \mapsto (-1)^{f(x)} |x\rangle|-\rangle$, so the input
    register becomes

    $$\frac{1}{\sqrt{2^n}} \sum_{x} (-1)^{f(x)} |x\rangle.$$

    Applying Hadamards again, with
    $H^{\otimes n}|x\rangle = \frac{1}{\sqrt{2^n}} \sum_{z} (-1)^{x \cdot z} |z\rangle$,
    gives

    $$\frac{1}{2^n} \sum_{z} \Big( \sum_{x} (-1)^{f(x) + x \cdot z} \Big) |z\rangle.$$

    The amplitude of $|0\rangle^{\otimes n}$ is
    $\frac{1}{2^n} \sum_{x} (-1)^{f(x)}$, whose magnitude is **$1$ if $f$ is
    constant** and **$0$ if $f$ is balanced** (the $+1$ and $-1$ terms cancel).
    So measuring all zeros certifies *constant* and any other outcome certifies
    *balanced* — decided from a single query.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Summary

    - Deutsch–Jozsa separates *constant* from *balanced* with **one** quantum
      query, versus up to $2^{n-1} + 1$ classical queries — an exponential gap
      for exact, deterministic decision.
    - The mechanism is **interference**: phase kickback stamps each $|x\rangle$
      with $(-1)^{f(x)}$, and the final Hadamards make those phases add up at
      $|0^n\rangle$ (constant) or cancel there (balanced).
    - The speedup relies on the promise; without it, no such exponential
      deterministic advantage holds.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Further reading

    - D. Deutsch and R. Jozsa, *Rapid solution of problems by quantum
      computation*, Proc. R. Soc. Lond. A **439** (1992) 553–558.
      [doi:10.1098/rspa.1992.0167](https://doi.org/10.1098/rspa.1992.0167)
    - M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum
      Information*, §1.4.3–1.4.4 (the Deutsch and Deutsch–Jozsa algorithms).
    - IBM Quantum, *Quantum query algorithms* tutorial —
      [https://quantum.cloud.ibm.com/learning](https://quantum.cloud.ibm.com/learning)
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


if __name__ == "__main__":
    app.run()
