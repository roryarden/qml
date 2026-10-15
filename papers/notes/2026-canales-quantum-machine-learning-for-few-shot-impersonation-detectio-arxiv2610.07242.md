---
arxiv_id: 2610.07242
version: v1
title: "Quantum Machine Learning for Few-Shot Impersonation Detection in Digital Account Opening"
authors: [Javiera Canales, Jose Ortega, Maximiliano Araya]
primary_category: quant-ph
published: 2026-10-05
added: 2026-10-11
relevance: 5
tags: [fraud, finance, classical-data, qml-bottlenecks, hardware, benchmark]
full_text: ../md/2026-canales-quantum-machine-learning-for-few-shot-impersonation-detectio-arxiv2610.07242v1.md
---

## Problem
Identity-impersonation fraud in digital account opening surfaces only after activation, and confirmed cases are extremely rare (8 of 3,419 accounts, 0.23%). Imbalance remedies (SMOTE, cost-sensitive learning) break down below ~10 positives, and classical one-class detectors flag many legitimate accounts. Do quantum one-class classifiers do better on real bank data?

## Method
Proprietary BCI (Chile) cohorts: 2025 (3,419 accounts, 21 features) and an out-of-time 2026 cohort (5,143 accounts, 31 frauds). Training on normal accounts only. AQFM (genetic search over discrete gate layouts, sequential multi-feature loading per qubit) with an expectation-based anomaly score; VQC variants up to 23 qubits; baselines OCSVM, Isolation Forest, KNN, centroid, Z-score. GPU simulation (CUDA-Q); inference of the 2-qubit model on a SpinQ Triangulum II NMR device.

## Key results
- 2025 at 88% recall (7/8): AQFM precision 9.21% (69 FP) vs best classical KNN 3.0% (226 FP) — ~70% fewer false positives.
- 2026 with the 2025 threshold unchanged: AQFM 20/31 frauds (64.5% recall, 8.81% precision, AUC-PR 0.191) vs OCSVM 48.4% / 5.08% (AUC-PR 0.085).
- Wide CIs (2025 recall [47%, 99.7%]).
- 2 qubits best; 3–23 qubit configs much worse (precision 0.28–0.41%) — capacity must match data.
- NMR hardware: recall held at 88% but precision fell to **0.71%** (below all classical baselines); ~30 s/sample.

## Limitations / open problems
Only 8 2025 frauds; one bank and fraud type. Model choices appear selected on the same frauds (no separate validation). 2025 comparison not like-for-like (classical at label-chosen recall point). No deep one-class or ensemble baselines. Hardware erases the gain; no mitigation. Proprietary data, code on acceptance. Authors: "not evidence of general quantum advantage."

## Why it matters to me
Exactly my domain: real payment-sector fraud data, extreme imbalance, one-class setup, out-of-time validation. Also a bottleneck story (small circuits win; hardware noise and latency destroy the simulated edge). Treat as a case study and experimental template, not evidence that QML works for fraud — needs independent replication.
