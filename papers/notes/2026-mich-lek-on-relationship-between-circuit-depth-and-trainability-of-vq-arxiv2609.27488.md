---
arxiv_id: 2609.27488
version: v1
title: "On Relationship Between Circuit Depth and Trainability of VQAs"
authors: [Jan Michálek, Martin Friák, Petr Vašík]
primary_category: quant-ph
published: 2026-09-23
added: 2026-09-29
relevance: 4
tags: [trainability, qml-bottlenecks, variational, theory, chemistry-physics]
full_text: ../md/2026-mich-lek-on-relationship-between-circuit-depth-and-trainability-of-vq-arxiv2609.27488v1.md
---

## Problem
How many independent parameters $p$ does a VQA need so that local minima approximate the global one? Anschuetz (2022) found a local-minima phase transition only as $p\to\infty$; does it hold at finite sizes, and what can be done about the exponential growth of the problem's degrees of freedom $m$?

## Method
Model the VQE cost as a Wishart Hypertoroidal Random Field; $m=\|H-\lambda_1I\|_*^2/\|H-\bar\lambda I\|_F^2$ (a spectral SNR), overparameterisation ratio $\gamma=p/2m$. Derive a discrete Kac–Rice formula for the expected number of local minima at a given energy; Monte Carlo estimate of the conditioned-Hessian determinant. Benchmarks: toy $m=8$ and 1D Fermi–Hubbard (2–7 sites). Symmetry reduction (particle number, spatial parity, spin flip) to lower $m$.

## Key results
- Finite-size transition at $p=2m-2$: below it minima sit at sub-optimal energies; above it they concentrate at the global minimum.
- Thresholds: toy 14; 2-site FH 38 / 62; 3-site 288; 4-site 1496.
- The transition stems from the analytic prefactor exponent $\alpha=m-p/2-1$; Monte Carlo mainly scales.
- $m$ grows exponentially (32 → 27,700 from 2 to 6 sites); symmetry reduction cuts it sharply (6 sites: 27,700 → 729) but stays exponential.

## Limitations / open problems
No VQA is actually trained — only the random-field surrogate. Threshold is largely baked into the formula. WHRF validity for symmetry-restricted ansätze asserted, not proven. Trade-off with barren plateaus unquantified. Exact $m$ needs full diagonalisation. Hardware runs mentioned without data. Physics Hamiltonian only; no data-driven losses.

## Why it matters to me
Gives a clean a-priori rule of thumb ($p\gtrsim2m$) and explains why hardware-efficient ansätze are hopelessly underparameterised; the remedy is problem structure/symmetry. Rigor largely inherited from Anschuetz. Extending the $m$/$\gamma$ analysis to supervised VQC losses (e.g. fraud classifiers) is an open question.
