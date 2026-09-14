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

        In 1992, Ethan Bernstein and Umesh Vazirani set out to pin down the
        theoretical limits of quantum computation — the work that introduced the
        quantum Turing machine and the complexity class BQP. To make the
        power of a quantum computer concrete, they posed a deceptively simple
        guessing game, now known as the Bernstein-Vazirani algorithm.

        Building on Deutsch and Jozsa's result from the same year, it gave one of
        the first clean, provable separations between what quantum and classical
        machines need to solve the *same* problem. Alongside Simon's algorithm it
        became a stepping stone toward Shor's factoring algorithm, and it endures
        as a favorite first taste of quantum advantage — precisely because the
        speedup is so easy to state.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## The problem

        Suppose you are handed a black-box function $f_s\colon \{0,1\}^n \to \{0,1\}$
        that is guaranteed to be defined by $f_s(x) = s^T x \pmod 2$ for some
        undisclosed $s \in \{0,1\}^n$. Although you are allowed to execute $f_s$ on
        various inputs, you are not given the hidden string $s$ that defines $f_s$.
        You are instead tasked with the objective of identifying $s$ using as few
        queries to $f_s$ as possible.

        **Example 1.** Suppose $n = 3$ and $s = (1,0,1)^T$. Then you are given query
        access to the function
        \[
            f_s(x) = s^T x = (1,0,1) \begin{pmatrix}
                x_1 \\
                x_2 \\
                x_3
            \end{pmatrix} = 1 \cdot x_1 + 0 \cdot x_2 + 1 \cdot x_3
            = x_1 + x_3 \;\overset{\text{mod } 2}{=}\; x_1 \oplus x_3
        \]
        but do not know what $s$ or $f_s$ are. Your objective is to determine the
        undisclosed bit string $s = (1,0,1)^T$ by querying $f_s$ on various inputs.
        <div style="text-align:right">❖</div>

        **Example 2.** Suppose $n = 5$ and $s = (0,1,1,0,1)^T$. Then
        \[
            f_s(x) = s^T x = (0,1,1,0,1) \begin{pmatrix}
                x_1 \\
                x_2 \\
                x_3 \\
                x_4 \\
                x_5
            \end{pmatrix} = 0 \cdot x_1 + 1 \cdot x_2 + 1 \cdot x_3 + 0 \cdot x_4 +
            1 \cdot x_5 = x_2 + x_3 + x_5 \;\overset{\text{mod } 2}{=}\; x_2
            \oplus x_3 \oplus x_5
        \]
        with the same constraints as above.
        <div style="text-align:right">❖</div>

        Notice that in both cases, $f_s$ is simply the parity of the bitwise `AND` of
        $s$ and $x$. This holds in general, so $f_s$ may be rewritten as
        \[
            f_s(x) = s^T x \;\overset{\text{mod } 2}{=}\; \bigoplus_{i=1}^{n} s_i x_i.
        \]

        How would you approach this problem classically? One idea might be to query
        $f_s$ on inputs that have a single bit set to $1$ and all other bits set to $0$,
        thereby revealing each bit of the hidden string $s$ one by one. If you were to
        take this approach, you would then need $n$ queries to determine all $n$ bits of
        $s$.

        **Example 3.** Suppose that $n = 4$. If we were to query $f_s$ on the standard
        basis vectors of $\{0,1\}^4$ and obtain
        \[
            \begin{aligned}
                f_s(1, 0, 0, 0) &= \bigoplus_{i=1}^{n} s_i x_i = s_1 = 1, \\
                f_s(0, 1, 0, 0) &= \bigoplus_{i=1}^{n} s_i x_i = s_2 = 0, \\
                f_s(0, 0, 1, 0) &= \bigoplus_{i=1}^{n} s_i x_i = s_3 = 1, \quad
                    \text{and} \\
                f_s(0, 0, 0, 1) &= \bigoplus_{i=1}^{n} s_i x_i = s_4 = 0,
            \end{aligned}
        \]
        then we could identify the hidden bit string as $s = (1,0,1,0)^T$.
        <div style="text-align:right">❖</div>
        
        It turns out that this approach is in fact optimal on a classical machine.
        That is, if the hidden bit string has $n$ bits, then any conceivable
        classical algorithm will require $\Theta(n)$ queries to fully identify $s$.
        In contrast, however, a quantum machine can make use of the Bernstein-Vazirani
        algorithm to determine $s$ using just a single query. It does this by exploiting
        quantum superposition and interference to extract all bits of $s$
        simultaneously.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## The quantum approach

        Classically, you must learn $s$ one bit at a time as each query returns the
        single bit $s^T x$ for one chosen $x$. Instead of feeding $f_s$ a single
        input at a time, however, we may consider preparing a uniform superposition
        over all $2^n$ possible bit strings. A single oracle call to $f_s$ could then
        act on every possible $x$ at once. Crucially, note that this is distinct from
        simply parallelizing the $2^n$ classical queries, which would still require
        exponentially many queries to $f_s$.

        The Bernstein-Vazirani algorithm can be summarized as follows:

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
    secret_input = mo.ui.text(
        value="1011",
        label="Secret bit string $s$:",
        placeholder="e.g. 1011",
    ).form(submit_button_label="Apply")
    return (secret_input,)


@app.cell
def _(mo, secret_input):
    _raw = "1011" if secret_input.value is None else secret_input.value.strip()

    _error = None
    if _raw == "" or any(ch not in "01" for ch in _raw):
        _error = "$s$ must be a bit string of $0$s and $1$s."
    elif len(_raw) > 10:
        _error = (
            "Woah there! Let's keep the secret to at most $10$ bits (remember "
            "that the state vector grows as $2^n$)."
        )
    # Wrap the form itself in a callout: red while invalid, green once accepted.
    mo.stop(
        _error is not None,
        mo.callout(mo.vstack([secret_input, mo.md(_error or "")]), kind="danger"),
    )

    secret = [int(ch) for ch in _raw]
    n = len(secret)
    mo.callout(secret_input, kind="success")
    return n, secret


@app.cell
def _(mo, np, plt, secret):
    def draw_bv_circuit(secret):
        from matplotlib.patches import Circle, Rectangle

        n = len(secret)
        set_bits = [i for i, b in enumerate(secret) if b]

        dx = 2.4  # horizontal spacing between stages (room for the captions)
        x_flip = dx
        x_h1 = 2 * dx
        oracle_xs = [3 * dx + k for k in range(max(1, len(set_bits)))]
        x_h2 = oracle_xs[-1] + dx
        x_meas = x_h2 + dx
        x_end = x_meas + 0.9

        y_in = [-i for i in range(n)]  # input qubits, top to bottom
        y_anc = -n  # output (ancilla) qubit at the bottom

        # Match the figure aspect to the drawing so the circuit sits centered.
        x_lo, x_hi = -1.6, x_end + 0.3
        y_lo, y_hi = y_anc - 1.9, 1.6
        fig, ax = plt.subplots(figsize=(0.55 * (x_hi - x_lo), 0.55 * (y_hi - y_lo)))

        def gate(x, y, label, fc="#e8f0fe"):
            ax.add_patch(
                Rectangle(
                    (x - 0.28, y - 0.28),
                    0.56,
                    0.56,
                    facecolor=fc,
                    edgecolor="#333",
                    zorder=3,
                )
            )
            ax.text(x, y, label, ha="center", va="center", fontsize=12, zorder=4)

        def cnot(x, y_ctrl, y_tgt):
            ax.plot([x, x], [y_ctrl, y_tgt], color="#2a9d8f", lw=1.8, zorder=2)
            ax.plot([x], [y_ctrl], "o", ms=8, color="#2a9d8f", zorder=4)
            ax.add_patch(
                Circle(
                    (x, y_tgt), 0.17, fill=False, edgecolor="#2a9d8f", lw=1.8, zorder=4
                )
            )
            ax.plot(
                [x - 0.17, x + 0.17], [y_tgt, y_tgt], color="#2a9d8f", lw=1.6, zorder=4
            )
            ax.plot(
                [x, x], [y_tgt - 0.17, y_tgt + 0.17], color="#2a9d8f", lw=1.6, zorder=4
            )

        def meter(x, y):
            ax.add_patch(
                Rectangle(
                    (x - 0.28, y - 0.28),
                    0.56,
                    0.56,
                    facecolor="#eeeeee",
                    edgecolor="#333",
                    zorder=3,
                )
            )
            _t = np.linspace(np.deg2rad(15), np.deg2rad(165), 30)
            ax.plot(
                x + 0.19 * np.cos(_t),
                y - 0.08 + 0.19 * np.sin(_t),
                color="#333",
                lw=1.2,
                zorder=4,
            )
            ax.plot([x, x + 0.15], [y - 0.08, y + 0.14], color="#333", lw=1.2, zorder=4)

        def step_marker(x, num, y):
            ax.add_patch(
                Circle((x, y), 0.2, facecolor="#2a9d8f", edgecolor="none", zorder=5)
            )
            ax.text(
                x,
                y,
                str(num),
                ha="center",
                va="center",
                color="white",
                fontsize=10,
                fontweight="bold",
                zorder=6,
            )

        for y in y_in + [y_anc]:
            ax.plot([-0.9, x_end], [y, y], color="#333", lw=1, zorder=1)
            ax.text(-1.0, y, r"$|0\rangle$", ha="right", va="center", fontsize=12)

        # Dashed barriers separating the circuit blocks.
        _bt, _bb = 0.55, y_anc - 0.55
        for _bx in (
            (x_flip + x_h1) / 2,
            (x_h1 + oracle_xs[0]) / 2,
            (oracle_xs[-1] + x_h2) / 2,
            (x_h2 + x_meas) / 2,
        ):
            ax.plot([_bx, _bx], [_bt, _bb], color="#bbb", ls="--", lw=1, zorder=1.5)

        gate(x_flip, y_anc, "X", fc="#fde8e8")  # step 1: output -> |1>
        for y in y_in + [y_anc]:  # step 2: Hadamard everywhere
            gate(x_h1, y, "H")
        for k, i in enumerate(set_bits):  # step 3: oracle U_f = CNOT where s_i = 1
            cnot(oracle_xs[k], y_in[i], y_anc)
        ax.add_patch(
            Rectangle(
                (oracle_xs[0] - 0.5, y_anc - 0.5),
                (oracle_xs[-1] - oracle_xs[0]) + 1.0,
                n + 1.0,
                fill=False,
                edgecolor="#2a9d8f",
                ls="--",
                zorder=2,
            )
        )
        ax.text(
            (oracle_xs[0] + oracle_xs[-1]) / 2,
            0.72,
            r"$U_f$",
            ha="center",
            va="center",
            fontsize=13,
            color="#2a9d8f",
        )
        for y in y_in:  # step 4: Hadamard on the input register
            gate(x_h2, y, "H")
        for y in y_in:  # step 5: measure the input register
            meter(x_meas, y)

        # Numbered markers tying each stage to the steps in "The algorithm".
        _yt = 1.15
        step_marker(x_flip, 1, _yt)
        step_marker(x_h1, 2, _yt)
        step_marker((oracle_xs[0] + oracle_xs[-1]) / 2, 3, _yt)
        step_marker(x_h2, 4, _yt)
        step_marker(x_meas, 5, _yt)

        _yl = y_anc - 0.85
        _cap = {"ha": "center", "va": "top", "fontsize": 8.5, "color": "#555"}
        ax.text(x_h1, _yl, "uniform\nsuperposition", **_cap)
        ax.text(
            (oracle_xs[0] + oracle_xs[-1]) / 2,
            _yl,
            "kickback\n$(-1)^{s\\cdot x}$",
            **_cap,
        )
        ax.text(x_h2, _yl, "inverse\n$H^{\\otimes n}$", **_cap)
        ax.text(x_meas, _yl, "outcome\n$= s$", **_cap)

        _s = "".join(str(b) for b in secret)
        ax.set_title(rf"Bernstein–Vazirani circuit for the secret $s = {_s}$")
        ax.set_xlim(x_lo, x_hi)
        ax.set_ylim(y_lo, y_hi)
        ax.set_aspect("equal")
        ax.axis("off")
        return fig

    mo.center(draw_bv_circuit(secret))
    return


@app.cell
def _(mo, secret):
    _n = len(secret)
    _bits = "".join(str(b) for b in secret)
    _set = [i for i, b in enumerate(secret) if b]

    _qk_oracle = "\n".join(f"qc.cx({i}, n)" for i in _set) or "# f is constant"
    _pl_oracle = (
        "\n    ".join(f"qml.CNOT(wires=[{i}, n])" for i in _set)
        or "pass  # f is constant — no CNOTs"
    )

    _qiskit = f"""from qiskit import QuantumCircuit

secret = {secret}          # hidden string s = {_bits}
n = {_n}

qc = QuantumCircuit(n + 1, n)
qc.x(n)                    # output qubit -> |1>
qc.h(range(n + 1))         # Hadamard on every qubit
{_qk_oracle}
qc.h(range(n))             # Hadamard on the input register
qc.measure(range(n), range(n))
# one shot returns s = {_bits}
"""

    _pennylane = f"""import pennylane as qml

secret = {secret}          # hidden string s = {_bits}
n = {_n}
dev = qml.device("default.qubit", wires=n + 1)

@qml.qnode(dev)
def bernstein_vazirani():
    qml.PauliX(wires=n)                 # output qubit -> |1>
    for w in range(n + 1):
        qml.Hadamard(wires=w)
    {_pl_oracle}
    for w in range(n):
        qml.Hadamard(wires=w)
    return qml.probs(wires=range(n))    # peak sits at s = {_bits}
"""

    _numpy = f"""import numpy as np

secret = {secret}          # hidden string s = {_bits}
n = {_n}

# Represent all n + 1 qubits as one 2^(n+1) state vector and apply
# each layer as a matrix. (Full engine in the cell below.)
state = np.zeros(2 ** (n + 1), dtype=complex)
state[1] = 1.0                          # input |0...0>, output |1>

H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
state = kron(*[H] * (n + 1)) @ state    # Hadamard on every qubit
state = oracle(secret) @ state          # U_f: |x,y> -> |x, y XOR s.x>
state = kron(*[H] * n, I) @ state       # Hadamard on the input register

probs = (np.abs(state.reshape(2 ** n, 2)) ** 2).sum(axis=1)
"""

    mo.ui.tabs(
        {
            "Qiskit": mo.md(f"```python\n{_qiskit}```"),
            "PennyLane": mo.md(f"```python\n{_pennylane}```"),
            "NumPy": mo.md(f"```python\n{_numpy}```"),
        }
    )
    return


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
def _(mo):
    mo.md(
        r"""
        ## Summary

        - Bernstein–Vazirani recovers an $n$-bit secret with **one** quantum
          query, versus **$n$** classical queries — a linear-to-constant
          collapse in query complexity.
        - The mechanism is **phase kickback plus interference**: the oracle
          encodes $s$ in the phases $(-1)^{s \cdot x}$, and a second layer of
          Hadamards inverts the Hadamard transform to read $s$ out directly.
        - It is the single-shot cousin of Deutsch–Jozsa: the same circuit, but
          the promise here pins down an entire string rather than one
          constant-vs-balanced bit.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Further reading

        - E. Bernstein and U. Vazirani, *Quantum complexity theory*, SIAM J.
          Comput. **26** (1997) 1411–1473.
          [doi:10.1137/S0097539796300921](https://doi.org/10.1137/S0097539796300921)
        - M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum
          Information*, §1.4.4.
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
