---
arxiv_id: 2608.29422
version: v1
title: "The ZZ feature map induces a signless Laplacian metric: a closed-form classical surrogate for quantum kernel regression"
authors: [Tekeli]
primary_category: quant-ph
published: 2026-08-29
added: 2026-09-10
relevance: 5
tags: [kernel-methods, theory, classical-data, qml-bottlenecks]
full_text: ../md/2026-tekeli-the-zz-feature-map-induces-a-signless-laplacian-metric-a-clo-arxiv2608.29422v1.md
---

> Note: the earlier HTML conversion captured only the abstract page; body-level
> details (proofs, tables) are from the abstract/metadata. Re-sync if full HTML
> becomes available.

## Problem
Quantum kernels lose their advantage once encoding bandwidth is tuned, resembling RBF kernels — but prior analysis covered only separable circuits. What classical kernel is an *entangling* ZZ feature map actually computing?

## Method
Analytical derivation (verified against simulation). Proves the small-bandwidth induced kernel is, to leading order, an anisotropic Gaussian kernel with metric $M=I+\pi^2 Q$ ($Q$ = signless Laplacian of the entanglement graph); structure persists at every depth as a Fubini–Study pullback. Empirical comparison on two near-infrared spectroscopy benchmarks.

## Key results
Derivation matches simulation to relative error $<10^{-3}$. Paired 95% bootstrap interval contains zero in 18/20 cells; typical relative test-error difference 2.7%; same preprocessing selected in 96% of splits. The quantum circuit can be removed without detectable predictive loss.

## Limitations / open problems
Leading-order small-bandwidth result; a failure regime exists (argued non-predictive). Only two spectroscopy datasets and the ZZ map. Anisotropy hinges on a phase convention.

## Why it matters to me
Dequantization-style result: a bandwidth-tuned entangling quantum kernel = a specific classical anisotropic Gaussian kernel — core to "when quantum doesn't help." Domain (spectroscopy) is off my payments focus, but the lesson transfers.
