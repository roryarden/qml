---
arxiv_id: 2609.38720
version: v1
title: "Does the Readout Bypass Leak the Input? A Feature-Visibility Audit of Hybrid Quantum-Classical Models"
authors: [Guilin Zhang, Kai Zhao, Xiquan Cui, Henry Heng, Xu Chu, Aletta Johanna Blanken]
primary_category: quant-ph
published: 2026-09-30
added: 2026-10-11
relevance: 4
tags: [federated-learning, privacy, security, classical-data, variational, qml-bottlenecks]
full_text: ../md/2026-zhang-does-the-readout-bypass-leak-the-input-a-feature-visibility-arxiv2609.38720v1.md
---

## Problem
"Readout-side residual" hybrids concatenate raw inputs with measured quantum features to work around the measurement bottleneck, and were pitched for federated learning with a privacy claim based on membership-inference AUC ≈ 0.5. Can an FL server reconstruct the record from a client's gradient?

## Method
Honest-but-curious server sees single-example gradients. Analytic first-layer inversion ($z^\top=g_{W,j}/g_{b,j}$, known result) and iterative cosine gradient matching with iDLG label inference. Visibility-conditioned metrics: PSNR/MSE/cosine over the full record and over the 6 coordinates every model sees. Wine and Breast Cancer; 6-qubit circuit encoding the first 6 features; four heads (pure quantum, $Q(x)$-MLP, input-only MLP, residual bypass). 15 attacked records per dataset × architecture; loss-threshold MIA as diagnostic. Noiseless simulation. Workshop poster.

## Key results
- Residual and input-only heads: median full-record PSNR 73–96 dB (near-exact recovery).
- Quantum-only heads: 8–11 dB on full record but 54–96 dB on the 6 encoded coordinates — "protection" is just unseen features.
- Labels recovered in 120/120 attacks; MIA AUC stays 0.48–0.54 even when records are reconstructed.
- Input-only classical head matches or beats the residual on accuracy.

## Limitations / open problems
Two small datasets, one split, 15 attacks, noiseless. Single-example gradients only — no claim for aggregation, batches, multi-step FedAvg. Analytic baseline's empirical success not measured. No classical 6-in/6-out control; encoding choice may differ from the original. Defenses (DP-SGD, secure aggregation) not evaluated.

## Why it matters to me
A clear caution for federated QML in payments: quantum encoding is not privacy for gradients, and MIA ≈ 0.5 is not a privacy certificate. Reporting rules (which coordinates each update touches, what aggregation precedes the server) transfer directly to cross-institution fraud models.
