---
arxiv_id: 2608.24631
version: v2
title: "When Similarity Is Interaction-Driven: Quantum Kernels for Regime-Sensitive Learning"
authors: [Hanqiu Peng, Jianlong Lu, Ying Chen]
primary_category: quant-ph
published: 2026-08-25
added: 2026-09-10
relevance: 5
tags: [kernel-methods, fraud, finance, classical-data, encoding, hardware]
full_text: ../md/2026-peng-when-similarity-is-interaction-driven-quantum-kernels-for-re-arxiv2608.24631v2.md
---

## Problem
In fraud/anomaly detection, similarity is often driven by sparse high-order variable interactions, not distance — two transactions can be close yet in different risk regimes. Distance kernels smooth across these boundaries; generic polynomial kernels bury the 5 relevant monomials among ~10k. When does an interaction-aligned quantum kernel win?

## Method
"Thin-slab" model: $d=Bk$ features in $B$ blocks, regime bit $r_b=\mathrm{sign}(\prod_j x_{b,j})$; one small-coordinate flip changes the regime at distance $2\delta$. Feature map: per-block Hadamards, one-body phases, and a $k$-body Pauli-string phase. Fidelity kernel proven PSD with an exact per-block closed form (classically $O(Bk)$ per entry). Kernel ridge regression vs linear/RBF/Laplacian/poly-2..8 and **InterFea** (ridge given the true planted products), 10 seeds. Real data: FDB Credit Card Fraud (chronological split, 75 test frauds) and IEEE-CIS. **New in v2:** IBM `ibm_kingston` (156-qubit Heron r2) run on $(d,k,B)=(20,4,5)$ at $\beta=0$, 512 shots + readout symmetrization, 27,312 circuits.

## Key results
- Synthetic: best in all 8 balanced and 8 imbalanced configs; scaling $(80,8)$ F1 0.395 vs InterFea 0.320 ($p=0.004$).
- Credit Card Fraud: best F1 0.472±0.075 vs Poly2 0.348, beats Poly2 in 10/10 runs. IEEE-CIS: **second** to Laplacian (F1 0.239 vs 0.267).
- **Hardware (v2):** within 0.003–0.007 of the noise-free simulator (e.g. bal. acc. 0.749 vs 0.753), still above InterFea in all four configs; noise mainly shrinks $Y$-type expectations ~14% (corr. 0.974–0.990).
- Performance tracks feature-map–target alignment, not Hilbert-space dimension.

## Limitations / open problems
Advantage is representational, not computational: the block-factorized kernel is exactly classically computable. Synthetic generator is matched to the map; real-data blocks fixed by ordering/correlation. Only 75 test frauds; fixed splits. Hardware only at $\beta=0$, one synthetic setting, no real-data hardware run. No concentration analysis as $B$ grows; tuning grids unpublished, code on request.

## Why it matters to me
QML-on-classical-data + fraud on real FDB benchmarks, with a clean thesis about *when* quantum kernels help (inductive-bias alignment). v2's hardware run shows the shallow block circuits survive real noise, but the honest takeaway for payments is "interaction-aligned kernel design" — quantum or quantum-inspired — since the gain is classically reproducible. InterFea control + paired tests are good evaluation practice to copy.
