---
arxiv_id: 2608.24229
version: v1
title: "A Theory of Finite-Noise Optima and Generalization in Quantum Machine Learning"
authors: [Zhang et al.]
primary_category: quant-ph
published: 2026-08-25
added: 2026-09-10
relevance: 5
tags: [qml-bottlenecks, generalization, statistical-learning, theory, classical-data]
full_text: ../md/2026-zhang-a-theory-of-finite-noise-optima-and-generalization-in-quantu-arxiv2608.24229v1.md
---

## Problem
Moderate quantum noise sometimes *reduces* test error — a non-monotonic effect unexplained by weak- or strong-noise analyses. What sets the optimal noise level and why does the benefit vanish?

## Method
Statistical learning theory via a noise-order surrogate (binomial ensemble over predictors grouped by number of noise events). Central quantity: noise-order purity $s_2\approx e^{-2\beta g}I_0(2\beta g)$ controlling effective complexity and the generalization gap. Tested on a 4-qubit re-uploading regressor (diabetes) and 8–9-qubit QGNNs (molecular property) across four noise channels.

## Key results
Across channels, training loss rises monotonically but **test loss dips below noiseless then rises** — a finite-noise optimum; gap follows $s_2$, $d_{\rm eff}\propto s_2$. Benefit precedes trainability collapse. Optimum $s^\star=\mathrm{SNR}/(\mathrm{SNR}+d_{\rm eff}^{(0)}/n_{\rm train})$; more data shifts it toward zero noise.

## Limitations / open problems
Assumes independent gate-level noise; surrogate + local linearization, not the physical model; small scale (4–9 qubits); noise programming can only add effective noise.

## Why it matters to me
QML-bottleneck (noise/generalization) with rigorous statistical-learning framing and a closed-form optimum, reframing noise as a tunable regularizer. On classical data (clinical/molecular); no finance/fraud angle.
