---
arxiv_id: 2609.09407
version: v1
title: "Balancing Expressivity and Overfitting in Quantum Gaussian Process Regression"
authors: [Joshi et al.]
primary_category: quant-ph
published: 2026-09-08
added: 2026-09-10
relevance: 4
tags: [kernel-methods, kernel-concentration, generalization, qml-bottlenecks, classical-data]
full_text: ../md/2026-joshi-balancing-expressivity-and-overfitting-in-quantum-gaussian-p-arxiv2609.09407v1.md
---

## Problem
How does a quantum fidelity kernel behave as the GPR covariance inside an active-learning loop, and how sensitive is it to regularization? Claim: beyond large-scale exponential concentration, overfitting can collapse GPR even at *small* scale.

## Method
Active-learning loop with quantum GPR surrogating $f(x)=x\sin(x)$. Fidelity kernel with "Simple" and "Chebyshev" feature maps, $N=2$–4 qubits. Sweeps signal variance $\tau^2$ and noise variance $\lambda^2$ over 25 combos; SPSA on negative log marginal likelihood, Qiskit AerSimulator into scikit-learn GPR.

## Key results
Four regimes: overfitting ($\tau^2>\lambda^2$, covariance goes diagonal, MSE blows up to 155–10466); limited expressivity (Simple at $N=2$, fixed by $N=4$); underfitting ($\tau^2<\lambda^2$, locks to global mean); balanced (best MSE ~0.003–0.01). MSE alone can't distinguish failure modes — the kernel matrix must be inspected.

## Limitations / open problems
Small/low-dim (1D target, $N=2$–4 qubits), explicitly not the quantum-advantage regime; hyperparameters must balance against covariance magnitude; simulator only; no theorem — qualitative study on one synthetic task.

## Why it matters to me
QML-bottlenecks axis — quantum-kernel concentration/overfitting framed through classical statistical-learning tools, with a concrete diagnostic (inspect the kernel matrix, not just MSE). No finance/fraud, no formal theory — intuition/diagnostic more than rigorous result.
