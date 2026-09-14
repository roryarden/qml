# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo==0.24.2",
#     "numpy==2.5.3",
#     "matplotlib==3.11.2",
# ]
# ///
"""Bernstein-Vazirani algorithm, simulated from scratch with NumPy.

Runs both locally (`marimo edit notebooks/bernstein_vazirani.py`) and in the
browser once exported to WebAssembly, since it depends only on NumPy and
matplotlib -- both available in Pyodide.
"""

import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Bernstein–Vazirani

        Given a hidden bit string $s \in \{0,1\}^n$ and a black-box function

        $$f(x) = s \cdot x \pmod 2 = \bigoplus_{i} s_i x_i,$$

        the goal is to recover $s$. A **classical** algorithm must query $f$ once
        per bit — probing with $x = 100\ldots0$, $010\ldots0$, and so on — for a
        total of $n$ queries. **Bernstein–Vazirani** recovers all of $s$ with a
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
        ## The circuit

        1. Prepare $n$ input qubits in $|0\rangle$ and one output qubit in $|1\rangle$.
        2. Apply a Hadamard to every qubit. The output qubit becomes $|-\rangle$,
           which turns the oracle into a **phase kickback**.
        3. Apply the oracle $|x\rangle|y\rangle \mapsto |x\rangle|y \oplus f(x)\rangle$.
        4. Apply a Hadamard to the $n$ input qubits.
        5. Measure the input register — the outcome is exactly $s$.
        """
    )
    return


@app.cell
def _(mo):
    secret_input = mo.ui.text(value="1011", label="Secret string $s$ (bits)")
    secret_input
    return (secret_input,)


@app.cell
def _(mo, secret_input):
    _raw = secret_input.value.strip()
    _cleaned = "".join(ch for ch in _raw if ch in "01") or "1011"
    _cleaned = _cleaned[:10]  # cap at 10 qubits to keep the state vector small
    secret = [int(ch) for ch in _cleaned]
    n = len(secret)
    mo.md(f"Interpreting the secret as **`{_cleaned}`** ({n} qubits).")
    return n, secret


@app.cell
def _(np):
    def bernstein_vazirani(secret):
        """Return (recovered_bits, input_probabilities) for the hidden `secret`."""
        n = len(secret)
        s_int = 0
        for i, bit in enumerate(secret):
            s_int |= (bit & 1) << (n - 1 - i)

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

        # Step 3: oracle |x>|y> -> |x>|y XOR f(x)>, f(x) = parity(s AND x).
        oracle = np.zeros((dim, dim), dtype=complex)
        for basis in range(dim):
            x = basis >> 1
            y = basis & 1
            fx = bin(s_int & x).count("1") & 1
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

        recovered_int = int(np.argmax(input_probs))
        recovered_bits = [(recovered_int >> (n - 1 - i)) & 1 for i in range(n)]
        return recovered_bits, input_probs

    return (bernstein_vazirani,)


@app.cell
def _(bernstein_vazirani, secret):
    recovered, input_probs = bernstein_vazirani(secret)
    return input_probs, recovered


@app.cell
def _(mo, n, recovered, secret):
    _recovered_str = "".join(str(b) for b in recovered)
    _secret_str = "".join(str(b) for b in secret)
    _ok = "✅" if recovered == secret else "❌"
    mo.md(
        f"""
        ## Result

        - Secret string: `{_secret_str}`
        - Recovered in **one** quantum query: `{_recovered_str}` {_ok}
        - Classical queries required: **{n}** &nbsp;·&nbsp; quantum queries: **1**
        """
    )
    return


@app.cell
def _(input_probs, np, plt):
    _fig, _ax = plt.subplots(figsize=(8, 3))
    _xs = np.arange(len(input_probs))
    _ax.bar(_xs, input_probs, color="#c7c7c7")
    _peak = int(np.argmax(input_probs))
    _ax.bar([_peak], [input_probs[_peak]], color="#2a9d8f")
    _ax.set_xlabel("input register value $x$")
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
        superposition and the output qubit is $|-\rangle$. The oracle stamps each
        basis state $|x\rangle$ with a phase $(-1)^{s \cdot x}$ (phase kickback).
        The state of the input register becomes

        $$\frac{1}{\sqrt{2^n}} \sum_{x} (-1)^{s \cdot x} |x\rangle,$$

        which is exactly the Hadamard transform of $|s\rangle$. Applying Hadamards
        again inverts the transform and collapses the register onto $|s\rangle$ with
        certainty — recovering all $n$ bits from a single query.
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
