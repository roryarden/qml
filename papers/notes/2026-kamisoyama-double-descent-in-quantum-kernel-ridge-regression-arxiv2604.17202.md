---
arxiv_id: 2604.17202
version: v2
title: "Double Descent in Quantum Kernel Ridge Regression"
authors: [Kamisoyama et al.]
primary_category: quant-ph
published: 2026-04-19
added: 2026-09-10
relevance: 5
tags: [kernel-methods, generalization, statistical-learning, theory, kernel-concentration]
full_text: ../md/2026-kamisoyama-double-descent-in-quantum-kernel-ridge-regression-arxiv2604.17202v2.md
---

## Problem
Double descent is well studied classically but underexplored in QML; prior quantum work lacked an explicit predictive test-risk formula. Can one rigorously derive the test risk of quantum kernel *ridge* regression (QKRR, $\lambda>0$) and quantify how regularization suppresses the peak?

## Method
Maps QKRR to classical ridge regression in the normalized Pauli basis; defines an effective feature map of dimension $p=\mathrm{rank}(\Sigma)$ and applies deterministic equivalents from random matrix theory. Validated by statevector simulation (HEA, TPA) on synthetic teacher–student and Fashion-MNIST binary.

## Key results
Explicit test-risk DE with effective regularization $\kappa_\lambda$ and effective DoF $\eta_\lambda$; peak is a variance divergence at $\eta_\lambda\to1$. As $\lambda\downarrow0$ variance grows $\lambda^{-1/2}$; explicit $\lambda>0$ suppresses it; ridgeless $\kappa_0>0$ acts as implicit regularization. DE matches empirical MSE.

## Limitations / open problems
Pointwise at fixed $\lambda>0$; benign-overfitting regime uncovered. Assumes noise-free kernel matrix — ignores shot noise and kernel concentration, so many-qubit scalability unaddressed. Notes Haar-like circuits give flat spectra (no inductive bias).

## Why it matters to me
Rigorous statistical-learning theory (RMT, bias–variance, effective DoF) on a QML bottleneck (kernel generalization), candid about kernel concentration and when quantum kernels can help. Classical data (Fashion-MNIST); no finance/fraud.
