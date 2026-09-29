---
arxiv_id: 2608.29422
version: v2
title: "The ZZ feature map induces a signless Laplacian metric: a closed-form classical surrogate for quantum kernel regression"
authors: [Erkut Tekeli]
primary_category: quant-ph
published: 2026-08-29
added: 2026-09-10
relevance: 5
tags: [kernel-methods, encoding, theory, qml-bottlenecks, classical-data, statistical-learning]
full_text: ../md/2026-tekeli-the-zz-feature-map-induces-a-signless-laplacian-metric-a-clo-arxiv2608.29422v2.md
---

> Note: both the v1 and v2 conversions captured only the arXiv abstract page;
> body-level details (proofs, tables, dataset names) are from the
> abstract/metadata. Re-sync if full HTML becomes available.
>
> **v2 (2026-09-26) vs v1:** 30 → 25 pages; the abstract's claims are softened
> and made more precise — "the induced kernel *is* an anisotropic Gaussian"
> became "has the anisotropic *Mahalanobis geometry* $M$ and *admits* a
> parameter-free Gaussian surrogate matching it *through second order*";
> "every circuit depth" → "any fixed depth"; dropped the claim that the
> failure regime begins at the same bandwidth on both datasets; dropped the
> closing line "the quantum circuit can thus be removed without detectable
> predictive loss". All numbers unchanged.

## Problem
Bandwidth-tuned quantum kernels lose their advantage and resemble RBF kernels, but the analytical support covered only separable encodings. What classical kernel is the *entangling* ZZ feature map actually computing?

## Method
Small-bandwidth expansion of the ZZ feature-map kernel, linking leading-order geometry to the signless Laplacian $Q$ of the entanglement graph; quadratic structure at any fixed depth as a Fubini–Study pullback; shifted vs unshifted phase conventions compared. Verified against direct simulation (path, cycle, complete graphs). Kernel regression on two NIR spectroscopy benchmarks: 4 targets × 5 preprocessing pipelines × 100 resampled splits, paired bootstrap intervals.

## Key results
- Proved: leading-order anisotropic Mahalanobis geometry $M=I+\pi^2Q$ with a parameter-free Gaussian surrogate matching through second order.
- Anisotropy depends entirely on phase convention — unshifted gives $M=I$ regardless of entanglement, explaining the prior isotropic RBF resemblance.
- Theory vs simulation: relative error $<10^{-3}$.
- Empirics: bootstrap CI contains zero in 18/20 cells; typical relative test-error difference 2.7%; same preprocessing chosen in 96% of splits. Restricting to the classical regime improves mean test error by 3.8% (a random restriction does not).

## Limitations / open problems
ZZ map and small-bandwidth regime only; surrogate exact only to second order. Regression on two spectroscopy datasets; 2/20 cells unexplained in the abstract. Nothing on hardware/shot noise or scaling. v2 explicitly narrows the claims (surrogate, fixed depth) and no longer asserts the circuit can be dropped outright.

## Why it matters to me
Proof-based dequantization: a bandwidth-tuned entangling quantum kernel reduces to a specific classical anisotropic Gaussian — core to "when QML doesn't help." The phase-convention trap is a practical warning. The surrogate is a cheap classical baseline to run before trying ZZ-map kernels on financial tabular data.
