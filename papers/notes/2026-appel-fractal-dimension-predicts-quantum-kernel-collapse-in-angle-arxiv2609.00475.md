---
arxiv_id: 2609.00475
version: v1
title: "Fractal dimension predicts quantum kernel collapse in angle-encoded data"
authors: [Appel]
primary_category: quant-ph
published: 2026-08-31
added: 2026-09-10
relevance: 5
tags: [kernel-methods, kernel-concentration, encoding, classical-data, qml-bottlenecks]
full_text: ../md/2026-appel-fractal-dimension-predicts-quantum-kernel-collapse-in-angle-arxiv2609.00475v1.md
---

## Problem
Angle-encoded quantum fidelity kernels on tabular data suffer exponential concentration — as qubits grow, the kernel collapses to the identity. The usual PCA-95% recipe can feed a *dead* kernel. Is there an a-priori, classically computable qubit budget before collapse?

## Method
Proposes the correlation fractal dimension $D_2$ as the qubit ceiling $q^*=\lceil D_2\rceil$ and FD-ASE to pick which columns to encode. Collapse judged by kernel diagnostics (near/far/mean-off-diagonal) with an explicit "alive rule." Nine datasets, statevector sim, RBF control, map/bandwidth ablations, IBM hardware.

## Key results
$\lceil D_2\rceil$ sits at/next to the empirical knee on clean cases (breast $D_2{=}3$ = knee 3 vs PCA-95% asking 10). Classical RBF stays alive → collapse is a quantum-map property. Budget is map/bandwidth-dependent. Hardware reproduces the live kernel at fractal width (MAE 0.012–0.021), diagonal past it.

## Limitations / open problems
Box-count $D_2$ needs enough samples/scales; unreliable when $E\gg\log N$. FD-ASE selects original columns (misses oblique signal). Alive rule is operational, not a hypothesis test. Ceiling tight only for one-layer ZZ at $c=1$. Single hardware backend.

## Why it matters to me
Targets the kernel-concentration bottleneck with a classically-cheap a-priori mitigation; squarely QML-on-classical-tabular-data, blending classical statistical learning (intrinsic dimension) with quantum kernels. Method transfers to any tabular fraud/anomaly QSVM pipeline.
