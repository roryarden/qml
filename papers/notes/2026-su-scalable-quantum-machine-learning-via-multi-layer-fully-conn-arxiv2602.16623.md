---
arxiv_id: 2602.16623
version: v3
title: "Scalable Quantum Machine Learning via Multi-layer Fully-Connected Variational Quantum Circuits"
authors: [Howard Su, Chen-Yu Liu, Samuel Yen-Chi Chen, Kuan-Cheng Chen, Huan-Hsin Tseng]
primary_category: quant-ph
published: 2026-02-18
added: 2026-09-29
relevance: 4
tags: [variational, quantum-neural-networks, qml-bottlenecks, trainability, classical-data, finance]
full_text: ../md/2026-su-scalable-quantum-machine-learning-via-multi-layer-fully-conn-arxiv2602.16623v3.md
---

## Problem
VQCs face an expressivity–trainability dilemma and a width problem (one qubit per feature ⇒ $2^d$ simulation cost). Can VQC-only models compete on high-dimensional tasks without trainable classical encoders?

## Method
**FC-VQC:** small local VQC blocks (angle encoding + StronglyEntanglingLayers + Pauli-Z readout) linked across layers by measurement, parameter-free routing, and re-encoding; all trainable params are quantum. Mixing variants: fully connected ($q=\lceil\sqrt d\rceil$), sliding-window ($q=3$), parallel ($q=3$). Theory: error/finite-shot propagation bound (linear growth if layer Lipschitz ≤1 — not established), block-reach results, and a conditional-expectation approximation floor. Tasks: Concrete (regression), Red Wine (6-class), and Deep-BSDE PDEs (Black–Scholes, Burgers, oscillatory) at $d\in\{9,36,81,144\}$. Baselines: DNNs, FC-Angle-Linear, MPS, XGBoost, CatBoost. Noiseless simulation, 5 seeds.

## Key results
- Tabular: Concrete $R^2$ 0.893 vs DNN 0.849 vs monolithic VQC 0.677; Wine acc. 63.6% vs 58.4%.
- PDEs: DNNs win at $d=9$; at $d\in\{81,144\}$ an FC-VQC variant has lowest mean RelMAE in all six settings (e.g. Black–Scholes $d=144$: 0.0133 vs DNN 0.0230, MPS 0.0231). Burgers margin is tiny with high error for all.
- Monolithic VQC gradient spread collapses to ~$10^{-14}$; block models retain fluctuating gradients (authors: not BP immunity).
- Mild depolarizing noise changes $R^2$ by −0.020 to +0.004. FC-VQC is slower (739 s vs DNN 24 s) and uses more GPU memory.

## Limitations / open problems
Simulation only; simplified noise. Fixed-width SW/PL variants are classically simulable by construction; no advantage claimed. Hardware training would need sequential parameter-shift + input Jacobians per stage. PDE experiments train and evaluate on the same Monte Carlo paths; tabular lacks GBT and parameter-matched DNN baselines. Routing gains confounded with wider blocks.

## Why it matters to me
An honest scalability design that explicitly confronts the trainability-vs-simulability tension. The multi-asset Black–Scholes result is finance-relevant, though the separable exact solution may flatter block-local models (my inference). Not evidence that QML beats strong classical models on real tabular data.
