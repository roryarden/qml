---
arxiv_id: 2610.09947
version: v1
title: "On the Expressive Power and Capacity of Quantum Data Reuploaders"
authors: [Lord Sen, Shyamapada Mukherjee]
primary_category: quant-ph
published: 2026-10-07
added: 2026-10-11
relevance: 4
tags: [theory, encoding, quantum-neural-networks, variational, generalization, classical-data]
full_text: ../md/2026-sen-on-the-expressive-power-and-capacity-of-quantum-data-reuploa-arxiv2610.09947v1.md
---

## Problem
Data-reuploading circuits compute trigonometric polynomials (Schuld et al.). Exactly which frequencies are reachable at finite depth $R$ for general multivariate encodings, how does the set grow, what does it imply for capacity — and how do small reuploaders compare with parameter-matched classical models?

## Method
Assuming integer encoding eigenvalues: $K_R=T^{(R)}=\{k\in\mathcal L:\ell_T(k)\le R\}$, the radius-$R$ word-metric ball in the lattice spanned by $T=S-S$ (counterexample for irrational spectra). Rademacher bound $B\sqrt{|K_R|/n}$. Experiments with single-qubit QDRs ($3(R+1)$ params, input scale $\sigma$) vs tanh MLPs with ≤ same params: 8 univariate targets, $\tanh(x^3)$ sweep, 27 Feynman equations ($d=2..9$), XOR/blobs/spiral.

## Key results
- Spectrum *directions* fixed at $R=1$ (rank-deficient lattice ⇒ model sees only a projection of $x$ at every depth); max frequency grows linearly, $|K_R|=\Theta(R^m)$; never saturates.
- For $m\ge2$, $|K_R|$ outgrows parameters; for one qubit, parameters exceed frequencies.
- FFT of simulated models matches theory exactly.
- QDR beats MLP on 4/8 smooth/periodic univariate targets; loses on ReLU/sigmoid/step (wrap-around), fixed largely by $\sigma=0.5$.
- Input scale matters more than depth (~10× error change).
- Feynman: QDR wins only on $d\le3$ equations; median RMSE 0.149 vs MLP 0.090; failures are underfitting.

## Limitations / open problems
Theory described by authors as elementary sumset consequences. Spectrum ≠ reachable coefficients (open). Capacity bound ignores parameters and isn't tight. Tiny single-qubit experiments, limited tuning, $\sigma$ grid hit its edge, no noise/hardware.

## Why it matters to me
Clean expressivity theory plus a Rademacher bound, and practical encoding warnings for VQCs on classical data: encoding choice fixes representable directions; input scaling is first-order; single-qubit reuploading underfits for $d\ge4$ — relevant before trying VQCs on wide fraud features.
