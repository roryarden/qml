---
arxiv_id: 2603.06473
version: v2
title: "A Mixture-of-Experts Framework for Practical Hybrid-Quantum Models in Credit Card Fraud Detection"
authors: [Chaves et al.]
primary_category: quant-ph
published: 2026-03-06
added: 2026-09-10
relevance: 5
tags: [fraud, finance, classical-data, variational, qml-bottlenecks, encoding]
full_text: ../md/2026-chaves-a-mixture-of-experts-framework-for-practical-hybrid-quantum-arxiv2603.06473v2.md
---

## Problem
Can hybrid quantum–classical ML deliver *practical* improvements in credit-card fraud detection under extreme class imbalance, non-stationarity, and hard real-time latency? Core obstacle: quantum clock speeds make fully-quantum inference infeasible for authorization windows.

## Method
(1) An improved Guided Quantum Compressor (GQC) — autoencoder (trained only on non-fraud) → angle-encoded 6-qubit VQC (ALA, Pauli-Z cost to mitigate barren plateaus) → classical head + calibration. (2) A mixture-of-experts where an XGBoost router sends a transaction to the quantum expert only when predicted to fix an XGBoost misclassification. Evaluated on Kaggle ULB (~0.172% fraud), 3× 5-fold CV; hardware timing on OQC Toshiko.

## Key results
At 0.6 router threshold, AP $0.793\pm0.085$ vs XGBoost $0.770\pm0.096$ — marginal. Precision rose but recall dropped ($0.913$ vs $0.934$) — a precision/recall trade-off. GQC inference ~542× / ~1387× faster than prior quantum baselines; routing sent only ~1–3% of points to hardware (7–21 min vs ~12 h fully-quantum).

## Limitations / open problems
Gains over XGBoost marginal, with reduced recall (fewer frauds caught). Router latency benchmark used only 180 samples. No claim of genuine quantum advantage. Explicitly leaves open **data-complexity measures that predict where quantum models succeed** (to drive routing).

## Why it matters to me
Directly QML-for-fraud on real classical financial data (OQC + Mastercard authors), targeting deployment bottlenecks (hardware latency, barren plateaus, encoding). Honest marginal-gains + precision/recall trade-off is useful evidence on when QML helps; its open "data-complexity-driven routing" question is squarely the "datasets where QML doesn't fail" theme.
