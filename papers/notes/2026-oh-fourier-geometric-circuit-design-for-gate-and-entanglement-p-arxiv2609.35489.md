---
arxiv_id: 2609.35489
version: v1
title: "Fourier-Geometric Circuit Design for Gate and Entanglement Placement in Quantum Neural Networks"
authors: [Seungcheol Oh, Chaemoon Im, Daeyeun Kim, Soohyun Park, Vaneet Aggarwal, Mohsen Heidari, Joongheon Kim]
primary_category: quant-ph
published: 2026-09-28
added: 2026-09-29
relevance: 4
tags: [theory, variational, quantum-neural-networks, encoding, qml-bottlenecks]
full_text: ../md/2026-oh-fourier-geometric-circuit-design-for-gate-and-entanglement-p-arxiv2609.35489v1.md
---

## Problem
Encoding gates fix which Fourier frequencies a PQC can output, but whether a coefficient is actually nonzero depends on how trainable and entangling gates are arranged. Prior Fourier analyses diagnose given circuits; none prescribe placement to make a target coefficient reachable.

## Method
Using the adjoint action of the encoding generator, operator space decomposes into 2-D invariant planes indexed by frequency (Props. 1–2); frequency-$\omega$ planes need ≥ $\omega$ active qubits. Each Fourier component is a bilinear product of projections of the effective state and observable onto those planes (Prop. 3). For commuting Ising-type entanglers, a three-stage **Expose → Spread → Align** placement rule; Corollary 1: all $\omega\le\deg(n)+1$ are generically reachable. Algorithm 1 is $O(|V|+|E|)$. Evaluated in simulation on PDEBench advection/Burgers (14 qubits), a physics-informed wave equation, a re-uploading variant, and noise/shot studies vs parameter-matched templates (Holm-corrected tests).

## Key results
- 14-qubit PDE regression, single upload: normalized MSE 0.107 (advection) / 0.195 (Burgers) with 126 params, 26 two-qubit gates; best template (circular HEA) 0.155 / 0.774 with 168 params, 69 gates. Six of eight templates failed to beat a constant predictor on advection.
- Placement ablation with identical gate counts: 225/225 nonzero Fourier pairs vs 3–122 for mis-ordered variants — all matching theory.
- Wave equation: 2 qubits, 20 params, rel. $L^2$ error $2.7\times10^{-5}$; 1-layer templates output zero.
- More noise-robust than HEA under depolarizing noise; finite-shot readout still needs >$10^4$ shots to beat the constant predictor.

## Limitations / open problems
Proofs restricted to one encoding layer, one entangling round per side, Pauli encodings/readouts and commuting entanglers. Reachable frequency capped by qubit degree (heavy-hex → $\omega\le4$). High-frequency planes are exactly the most noise-fragile. Reachability ≠ learnability; no trainability or generalization analysis. Simulation only; scientific-field targets, no tabular data.

## Why it matters to me
Turns Fourier-expressivity theory (cf. library papers by Novaes, Paul) into a constructive, provable design rule — gate *order* matters, not just count. Practical payoff: shallower, fewer-CNOT circuits. Weak fit to classical tabular/finance data; the DFT-to-target-frequency idea might transfer to periodic transaction signals (my speculation).
