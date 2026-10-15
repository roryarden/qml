---
arxiv_id: 2610.11360
version: v2
title: "When Does Interference Help Learning? Kernel Geometry as a Pre-Experimental Test for Photonic Reservoir Computing"
authors: [Oishik Kar, Aswath Babu H]
primary_category: quant-ph
published: 2026-10-08
added: 2026-10-11
relevance: 4
tags: [kernel-methods, classical-data, qml-bottlenecks, theory, statistical-learning, kernel-concentration]
full_text: ../md/2026-kar-when-does-interference-help-learning-kernel-geometry-as-a-pr-arxiv2610.11360v2.md
---

## Problem
Photonic reservoir experiments report advantage, null and train-only effects from multi-photon interference — on incomparable tasks and platforms. Is there a task-independent characterization of the interference resource, and a rule that says in advance whether a task can use it?

## Method
Boson-sampling reservoir features (indistinguishable $|\mathrm{Per}|^2$ vs distinguishable $\mathrm{Per}|\cdot|^2$, partial distinguishability via HOM visibility $V$) with ridge readout → kernel machines. Compare $K_Q$, $K_C$ via spectra, geometric difference $g$, retention $R(V)$ and kernel–target alignment. Adversarial (Yin et al.) and natural tasks, UCI digits, random-label control, RFF baseline. Exact-permanent simulation; shot noise modelled. Pre-registered 13-family battery; held-out prediction of Joly et al. Two short proofs for $N=2$.

## Key results
- Interference spreads variance: 61 vs 33 effective dimensions; $g=10.3\pm1.1$.
- $g-1$ linear in $V$ at small $V$ (proved for $N=2$); ~80% retained at $V=0.864$, ~96% at $V=0.972$.
- $g$ is conditioning-dependent ($g\cdot\lambda_{\min}(K_C)\approx$ const).
- Designed task advantage +0.22; natural tasks ~10× smaller (≤0.04); digits +0.036±0.054; no growth with photon number.
- Held-out Joly et al. prediction matches (+0.015 vs published +0.014).
- Convexity in $V$ rules out kernel-geometry interior optima.
- Four-step pre-experimental protocol (compute $g$ and alignments on ~100 unlabeled inputs).

## Limitations / open problems
Numerics only, simulable sizes; synthetic/simple natural tasks. Pre-registered battery mostly failed (alignment-gap vs advantage $\rho=0.027$). Post-hoc weighted score. Protocol needs #P-hard permanents at scale. Reconciliation with past experiments is retrospective.

## Why it matters to me
A rigorous, honest answer to *when* a quantum feature map helps on classical inputs: geometric separation shows *some* task benefits; alignment decides whether *yours* does — and on natural tasks the gain was small. The cheap alignment check is transferable to candidate fraud datasets before spending hardware time; also reinforces the "$g$ tracks classical conditioning" caveat.
