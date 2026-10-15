---
arxiv_id: 2609.00475
version: v2
title: "Fractal dimension predicts quantum kernel collapse in angle-encoded data"
authors: [Ana Paula Appel]
primary_category: quant-ph
published: 2026-08-31
added: 2026-09-10
relevance: 5
tags: [kernel-methods, kernel-concentration, encoding, classical-data, qml-bottlenecks, hardware]
full_text: ../md/2026-appel-fractal-dimension-predicts-quantum-kernel-collapse-in-angle-arxiv2609.00475v2.md
---

## Problem
Angle-encoded fidelity kernels on tabular data collapse toward the identity as the circuit widens; the usual PCA-95% or all-columns width can silently hand a QSVM a dead kernel. Is there an a-priori, classically computable qubit budget — and does fractal column selection beat PCA/random columns under the same quantum map?

## Method
Budget $q^*=\lceil D_2\rceil$ (correlation fractal dimension, box-counting on ≤4000 rows); FD-ASE forward-greedy column selection (stop at gain <0.15). "Alive" rule: near ≥0.25, near/far ≥2, $\bar K$ ≥0.03; knee = last alive $q$. Nine datasets, one-layer ZZ default plus two-layer ZZ, Z, IQP, dense-angle, re-uploading; bandwidth sweep $c\in\{0.25,0.5,1,2\}$; RBF control; IBM `ibm_fez` (256 shots, no mitigation). **New in v2:** Haar-rotated $k$-cubes, n=128 downstream scores, effective-rank comparison.

## Key results
- $\lceil D_2\rceil$ near the knee on clean cases (breast 3 vs knee 3; PCA-95% asks 10). RBF never collapses → collapse is a property of the quantum map.
- Self-reported failures: OneBig lives past the ceiling; wine/diabetes die early (knees 4–5 even at n=128).
- Rotated subspaces (v2): $D_2$ overshoots, FD-ASE kernels die, PCA-95% is right — method needs axis-aligned geometry.
- Map/bandwidth: two-layer ZZ never alive; Z/IQP live past the ceiling; smaller $c$ delays collapse.
- Hardware: MAE 0.021 vs statevector at q=3; at n=16 only FD-ASE preserves near>far (ratio 2.1).
- Effective rank rises smoothly with no corner at the knee.

## Limitations / open problems
Box-count $D_2$ is sample-hungry and unreliable when $E\gg\log N$. Alive rule is an operational threshold, not a test. Budget tight only for one-layer ZZ at $c=1$ — quoting $\lceil D_2\rceil$ without map and bandwidth overclaims. Dead kernels don't always hurt downstream scores. Tiny kernel samples and hardware runs; no theorem linking $D_2$ to concentration; no quantum-vs-classical advantage claim.

## Why it matters to me
A cheap pre-circuit check against the kernel-concentration bottleneck for wide tabular data — exactly the shape of payments/fraud tables. v2 makes the method more honest (rotated-axes failure, map/bandwidth caveats), so the practical rule becomes: profile intrinsic dimension *and* check axis alignment before choosing width. Evidence is about avoiding failure, not finding advantage.
