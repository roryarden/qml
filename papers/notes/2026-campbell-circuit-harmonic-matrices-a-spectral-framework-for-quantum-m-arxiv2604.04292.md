---
arxiv_id: 2604.04292
version: v2
title: "Circuit Harmonic Matrices: A Spectral Framework for Quantum Machine Learning"
authors: [Kyle James Stuart Campbell, Luigi Del Debbio, Petros Wallden]
primary_category: quant-ph
published: 2026-04-05
added: 2026-10-11
relevance: 4
tags: [theory, trainability, encoding, variational, qml-bottlenecks]
full_text: ../md/2026-campbell-circuit-harmonic-matrices-a-spectral-framework-for-quantum-m-arxiv2604.04292v2.md
---

## Problem
The encoder fixes allowed input frequencies, but not which coefficients actually vary, how they co-vary over parameters, or how easily training moves them. How does the whole circuit constrain representable functions and learning — and do coefficient variance, covariance and the QNTK predict learning?

## Method
Circuit harmonic matrix $C$ with $a(\theta)=C\psi(\theta)$ (rows: input frequencies; columns: parameter harmonics), built by Pauli propagation. Derives mean coefficients, covariance $\Sigma$, pointwise and averaged QNTK, and an optimizer-independent fitting-error lower bound from the affine span. Two-copy propagation computes $\Sigma$ and averaged QNTK exactly without building $C$. 400 configurations (8 circuit families, $R_X/R_Y$ encoding, 2–6 qubits, depth 1–5) on noiseless 1D Fourier targets; frozen-QNTK forecast test. Appendices not fully read by summarizer.

## Key results
- Two-copy method matches explicit CHM to ~$10^{-16}$.
- Support grows with depth (family-dependent); variance shrinks with qubits and depth; profiles approach redundancy-proportional shape.
- Depth decorrelates coefficients; qubit count mostly doesn't.
- Strong spectral bias: variance correlates with early learning ($\rho=0.977$) and final MSE ($-0.987$), but adds little once circuit/frequency controlled.
- Deeper circuits learn faster and better despite lower variance (90/96 conditions); more qubits slows early learning.
- No robust benefit from covariance alignment; QNTK effective rank ≤0.305.
- Frozen QNTK forecasts small-step GD loss within ~1% (one setting).

## Limitations / open problems
Exact algorithm only for Clifford + single-use independent uniform rotations, commuting encoders; worst-case exponential; pruning uncertified. ≤6 qubits, 1D synthetic noiseless targets. Associational statistics on a fixed bank. Open: held-out prediction of learning, reachable-set geometry, lazy training.

## Why it matters to me
Rigorous linear-algebraic theory tying circuit design to trainability and representational limits, with a nuanced practical finding (depth can help even as variance shrinks). No real-data or finance content.
