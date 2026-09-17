---
arxiv_id: 2609.17991
version: v1
title: "Fourier Analysis of Parametrized Interactive Quantum Classifiers"
authors: [Fábio Novaes, Fernando M. de Paula Neto, João V. M. Cardoso]
primary_category: quant-ph
published: 2026-09-16
added: 2026-09-17
relevance: 4
tags: [theory, encoding, variational, classical-data, generalization, qml-bottlenecks]
full_text: ../md/2026-novaes-fourier-analysis-of-parametrized-interactive-quantum-classif-arxiv2609.17991v1.md
---

## Problem
Interactive Quantum Classifiers (IQCs) are open-system-inspired QML models where a target qubit interacts with an ancillary "environment" via a Hamiltonian, and the classical input is encoded into the environment's Hamiltonian eigenvalues. Prior work introduced alternative Hamiltonian parameterizations and showed empirically that they help, but the role of these parameters "remains poorly understood." The paper connects two research lines — the Fourier/spectral characterization of parameterized quantum circuits (Schuld et al. 2021) and open-system quantum learning — by characterizing how an input-dependent environmental Hamiltonian and the target-Hamiltonian spectrum jointly set the classifier's Fourier structure.

## Method
- **Analytical derivation**: for a single target qubit and a diagonal environment Hamiltonian $H_e(W,\boldsymbol{x})=\operatorname{diag}(W\boldsymbol{x})$, tracing out the environment gives a closed-form reduced channel. The joint evolution decomposes into an environment-controlled multiplexor of target-qubit rotations; via Rodrigues' formula the prediction becomes an explicit finite Fourier series $f=\sum_l[A_l\cos(2\kappa\boldsymbol{w}_l^T\boldsymbol{x})+B_l\sin(2\kappa\boldsymbol{w}_l^T\boldsymbol{x})]+C$. Rows of $W$ set the accessible frequencies; the target Hamiltonian direction, initial state, measurement, and environment probabilities set the coefficients.
- **Generalized model (IQC-Multi)**: a unified formulation recovering prior IQCs as special cases. Its novelty: environment dimension $N_e$ becomes an independent architectural knob, and each eigenvalue depends on a linear combination $\boldsymbol{w}_l^T\boldsymbol{x}$ of features, producing **non-separable, multidimensional** Fourier frequencies. IQC-AIL (amplitude-encoded input) is shown to reduce to a homogeneous quadratic decision boundary.
- **Experiments**: six variants (IQC, IQC-AIL, IQC-α, IQC-Multi-2/4/8) on 7 synthetic (Blobs, Circles, Moons, Stripes, XOR) and 4 real-world (Iris, Wine, Pima Diabetes, Caesarian) benchmarks; one-vs-rest multiclass. All **classical numerical simulation** (NumPy/JAX), MSE loss, 10 repeated 80/20 splits, Adam + particle-swarm, Friedman + Wilcoxon (Holm) testing.
- **Expressibility**: Sim et al. (2019) fidelity/KL-to-Haar measure plus an idle-normalized "relative expressibility" to compare across Hilbert-space dimensions.

## Key results
- **Aggregate (mean over 11 datasets)**: IQC-Multi-8 best on all four metrics (accuracy 0.863, F1 0.833, precision 0.860, recall 0.852); Multi-4 and Multi-2 follow; IQC-α, IQC-AIL, plain IQC lower.
- **Hard nonlinear datasets show the gain**: on XOR, IQC-Multi-4 reaches 0.996 accuracy while non-multidimensional variants stay near chance; on Moons, IQC-Multi-8 gets 0.929. Blobs are near-saturated for all.
- **No universal ordering**: on Wine IQC-AIL is best; on Pima IQC-Multi-2 leads. Friedman significant on 7/11 datasets; in F1 post-hoc IQC-Multi-8 had 10 wins / 0 losses but most comparisons were "no difference" — advantage is not statistically universal.
- **Expressibility ≠ performance**: IQC-Multi-8 has the smallest KL to Haar, yet the paper explicitly concludes global state-ensemble expressibility "does not directly predict classification performance," separating global expressibility from task-relevant Fourier expressivity.
- **Interpretation**: IQC-α mainly tunes Fourier *coefficients* (separable spectrum preserved); IQC-Multi adds *spectral-structure* control (non-separable frequencies), confirmed by richer decision boundaries. A simpler four-parameter extension often matches performance with far fewer trainable parameters.

## Limitations / open problems
- **Single target qubit only**; extending the analytic result to multiple target qubits is future work.
- **Parameter redundancy**: target-Hamiltonian scale $\kappa$ rescales frequencies while its direction sets coefficients — the roles are entangled, with substantial parameter sharing; a reparametrization is suggested.
- **Expressibility metric mismatch**: computed on the *global* target+environment state, but the classifier uses only the *reduced* target state.
- **No quantum-advantage or classical-baseline claim**; all classical simulation on small standard datasets, no noise/hardware, no trainability/barren-plateau analysis. Appropriate $N_e$ is dataset-dependent.

## Why it matters to me
Strong fit on **rigorous theory** and **QML-on-classical-data**: a clean, honest closed-form derivation (Rodrigues rotation → finite Fourier series) linking an encoding Hamiltonian to the exact function class a quantum classifier can represent — exactly the expressivity analysis I value. It also hits a **QML-bottleneck** theme by empirically debunking the "higher Haar expressibility ⇒ better classification" intuition and flagging coefficient-controllability (not just accessible frequencies) as the real constraint. Practical relevance is moderate: generic UCI/sklearn benchmarks, no finance/fraud data, no hardware, no classical baseline — so it grounds quantum-classifier theory rather than proving applied advantage.
