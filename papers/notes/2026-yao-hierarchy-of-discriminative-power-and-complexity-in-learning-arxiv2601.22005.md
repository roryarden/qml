---
arxiv_id: 2601.22005
version: v2
title: "Hierarchy of discriminative power and complexity in learning quantum ensembles"
authors: [Jian Yao, Pengtao Li, Xiaohui Chen, Quntao Zhuang]
primary_category: quant-ph
published: 2026-01-29
added: 2026-10-11
relevance: 4
tags: [theory, statistical-learning, generative, kernel-methods, qml-bottlenecks]
full_text: ../md/2026-yao-hierarchy-of-discriminative-power-and-complexity-in-learning-arxiv2601.22005v2.md
---

> Note: the conversion fell back to ar5iv and captured **only the arXiv abstract page**. Everything below is from the abstract; read the PDF for proofs and QDDPM experiments.

## Problem
Distance metrics are central to ML, but distances between ensembles of quantum states are poorly understood under measurement constraints. What is the trade-off between a metric's discriminative power and the samples needed to estimate it?

## Method
Defines MMD-$k$, a hierarchy of integral probability metrics generalizing maximum mean discrepancy to quantum ensembles with moment order $k$. Proves sample-complexity bounds for MMD-$k$, for any stable metric with full discriminative power, and for the quantum Wasserstein distance. Illustrated by training quantum denoising diffusion probabilistic models (QDDPMs).

## Key results
- Strict power–efficiency trade-off as $k$ grows.
- Pure-state ensembles of size $N$, constant $k$: estimating MMD-$k$ needs $\Theta(N^{1-1/k})$ samples under any measurement scheme.
- Any stable full-power metric: $O(N\log N)$ upper and $\Omega(N)$ instance-gap lower bounds.
- Quantum Wasserstein (large fixed dimension): nearly linear lower bound, $O(N\log N)$ upper bound.
- Claimed to guide loss design in QML (QDDPM demonstration).

## Limitations / open problems
From the abstract: tight bound only for pure states and constant $k$; Wasserstein bound "nearly" linear and needs large dimension; full-power metrics lack matching bounds. Experimental details unavailable in the converted file.

## Why it matters to me
Matched upper/lower sample-complexity bounds and an MMD/kernel view of quantum data — rigorous statistical learning theory bearing on a practical bottleneck (choosing losses for generative QML under measurement budgets). Quantum-data setting; no classical-data or finance angle.
