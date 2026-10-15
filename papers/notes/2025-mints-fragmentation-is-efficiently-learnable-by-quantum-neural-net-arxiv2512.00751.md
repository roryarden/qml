---
arxiv_id: 2512.00751
version: v4
title: "Fragmentation is Efficiently Learnable by Quantum Neural Networks"
authors: [Mikhail Mints, Eric R. Anschuetz]
primary_category: quant-ph
published: 2025-11-30
added: 2026-10-11
relevance: 4
tags: [barren-plateaus, trainability, quantum-neural-networks, theory, variational, chemistry-physics]
full_text: ../md/2025-mints-fragmentation-is-efficiently-learnable-by-quantum-neural-net-arxiv2512.00751v4.md
---

## Problem
QNNs that provably avoid barren plateaus usually rely on symmetry structure that also enables classical simulation (dequantization). Is there a physically motivated task that is provably trainable on a QNN with no known dequantization? Candidate: **fragment classification** — identify which dynamically disconnected Krylov subspace (under Hilbert-space fragmentation) a state belongs to.

## Method
Learner gets only local generators of the algebra; bicommutant decomposition defines sectors. Ansatz built from exponentials of algebra elements interleaved with random-time evolutions under a Hamiltonian satisfying full ETH within each Krylov subspace. Proof chain: replace evolutions by Haar block unitaries → Gaussian matrices → semi-isotropic operator (JAWS framework); Hessian rank for overparameterization; Kac–Rice on a perturbed loss for spurious minima. Small qutip numerics on Temperley–Lieb (4 and 6 qubits).

## Key results
- Training one example per $(\lambda,q_\lambda)$ generalizes across all exponentially many multiplicity labels.
- No barren plateaus: gradient variance $\Omega(1/\mathrm{poly}(L))$.
- Overparameterized with $\mathrm{poly}(L)$ parameters; expected spurious local minima → 0.
- Known Lie/Jordan-algebraic simulators need structure constants, which require nested commutators that can blow up — argued as evidence of classical hardness.
- Numerics: final-loss distribution peaks at zero once overparameterized.

## Limitations / open problems
Classical hardness conjectured, not proven (invites attempts at classical simulators). Relies on full ETH; Haar-replacement step justified physically, not rigorously. Requires poly-dim relevant subspace and Schur-basis training states. Numerics on a classically simulable model, tiny scale. Application only sketched.

## Why it matters to me
Rigorous trainability theory (no barren plateaus, no bad minima) aimed squarely at the "trainable ⇒ simulable" tension — a template for where non-dequantizable practical QML might come from. Quantum-data task; no classical-data or finance angle.
