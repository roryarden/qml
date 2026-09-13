---
arxiv_id: 2608.24631
version: v1
title: "When Similarity Is Interaction-Driven: Quantum Kernels for Regime-Sensitive Learning"
authors: [Peng et al.]
primary_category: quant-ph
published: 2026-08-25
added: 2026-09-10
relevance: 5
tags: [kernel-methods, fraud, finance, classical-data, theory]
full_text: ../md/2026-peng-when-similarity-is-interaction-driven-quantum-kernels-for-re-arxiv2608.24631v1.md
---

## Problem
In fraud/anomaly detection, similarity is often driven by sparse high-order variable interactions, not distance — two transactions can be close yet in different risk regimes. Distance-based kernels are misaligned. Can an interaction-aligned quantum kernel do better?

## Method
A controlled "thin-slab" synthetic model plus an interaction-driven quantum kernel from entangled Pauli-string feature maps encoding block products. Fidelity kernel proven PSD, block-factorized closed form. Baselines incl. an InterFea control given the planted products. Kernel ridge regression on synthetic (3rd–8th order) and two real FDB fraud benchmarks. Exact classical simulation.

## Key results
Best across synthetic. Real data: Credit Card Fraud best F1 0.472 vs Poly2 0.348 (~36% gain), beating Poly2 in all 10 runs; IEEE-CIS **second** behind Laplacian. Performance depends on feature-map–target *alignment*, not Hilbert-space dimension; advantage is representational (classically reproducible), not computational.

## Limitations / open problems
Synthetic generator matched to the feature map (blocks known a priori). Credit Card test split has only 75 fraud cases. Exact simulation only. No computational advantage claimed; IEEE-CIS knocks it to second.

## Why it matters to me
QML-on-classical-data + finance/fraud on real FDB benchmarks, engaging *when* quantum kernels help via inductive-bias alignment with statistical rigor. Honest for "where QML doesn't fail": gains are real but representational and partly matched by a classical engineered-feature baseline.
