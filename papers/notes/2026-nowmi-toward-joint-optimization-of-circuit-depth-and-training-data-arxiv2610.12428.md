---
arxiv_id: 2610.12428
version: v1
title: "Toward Joint Optimization of Circuit Depth and Training Data Size in Adaptively Grown Quantum Classifiers"
authors: [Saeefa Rubaiyet Nowmi, Md Mahmuduzzaman Kamol, Mohammad Saidur Rahman]
primary_category: quant-ph
published: 2026-10-08
added: 2026-10-11
relevance: 4
tags: [generalization, statistical-learning, variational, classical-data, qml-bottlenecks, theory]
full_text: ../md/2026-nowmi-toward-joint-optimization-of-circuit-depth-and-training-data-arxiv2610.12428v1.md
---

## Problem
Caro et al.'s generalization bound ($O(\sqrt{K\log(MT)/N})$ with $K$ active gates) and Q-FLAIR's gate-by-gate circuit growth suggest a predictable scaling law between circuit size and training-set size. Does Q-FLAIR's stopping rule pick circuit size by data budget, and does the generalization gap track the bound?

## Method
Faithful Q-FLAIR reimplementation (5-qubit ring, analytic sinusoid reconstruction, bounded scalar minimizer, stop at $\Delta L<10^{-3}$), then a new joint Adam fine-tune to measure $K$ (weights moving >0.05). Full Caro Theorem 3 bound reported. MNIST 3-vs-5 on raw 784 pixels, $N\in\{2k..10k\}$, 3 seeds, statevector simulation. Short workshop paper.

## Key results
- No trend with $N$: circuit size ~16–23 gates, seed SD up to ±9; test accuracy 0.84–0.89 non-monotone; gaps 0.0045–0.0141.
- Bound never violated in the 14 applicable runs (15th excluded, $K=0$), but correlation with the gap only $r=0.12$ (raw $T$: 0.05).
- Hypothesis: with 784 candidate features some gate always clears the fixed threshold, decoupling stopping from $N$; suggests $N$- and pool-size-aware thresholds.

## Limitations / open problems
One task, 3 seeds, 5 qubits, noiseless; fine-tune hyperparameters fixed once; no classical baseline; dimensionality explanation untested. Open: why a valid bound has so little predictive power.

## Why it matters to me
A direct test of rigorous QML generalization theory against a real adaptive pipeline on raw classical data: the bound is valid but not useful for model-size selection — a practical gap between theory and design. Small-scale and no finance angle, but a good template for checking bounds against practice.
