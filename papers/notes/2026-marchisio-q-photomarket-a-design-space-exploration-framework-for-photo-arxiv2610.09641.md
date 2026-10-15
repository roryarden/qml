---
arxiv_id: 2610.09641
version: v1
title: "Q-PhotoMarket: A Design Space Exploration Framework for Photonic Hybrid Quantum Neural Networks in Financial Market Prediction"
authors: [Alberto Marchisio, Hanzalah Mohamed Siraj, Muhammad Kashif, Nouhaila Innan, Muhammad Shafique]
primary_category: quant-ph
published: 2026-10-07
added: 2026-10-11
relevance: 4
tags: [finance, classical-data, quantum-neural-networks, variational, benchmark]
full_text: ../md/2026-marchisio-q-photomarket-a-design-space-exploration-framework-for-photo-arxiv2610.09641v1.md
---

## Problem
Photonic QML studies usually test one hand-designed architecture; nobody has mapped how photonic design choices affect financial prediction. Predict the direction of next-day returns across markets.

## Method
Binary target $\mathbf 1(r_{t\to t+1}>\tau)$, $\tau\in\{0,0.5\%,1\%\}$. Daily OHLCV 2018–2025 for S&P 500, NIFTY 50, crypto; 16 leakage-safe price features; 5-fold expanding walk-forward. Merlin photonic `QuantumLayer` (17 modes) + classical MLP head. Design space: input photon state × circuit (Simple, Ring, Clements, Phase-only, Permuted Ring) × entangler (MZI, Bell) × measurement (Fock, unbunched, dual-rail, expectations, correlations) → ~5,400 runs; Optuna TPE refinement. Class weights, threshold calibration, prediction-collapse diagnostics. Baselines: majority, logistic regression, shallow MLP. Simulation only.

## Key results
- Median AUC ≈ 0.5; mean AUC rises with $\tau$ (S&P 0.500 → 0.528).
- Circuit and measurement matter most (Clements best on average; Fock good on equities, correlations competitive on crypto); input state/entangler matter little.
- Best configs: S&P AUC 0.528±0.019, NIFTY 0.514±0.028; best single runs ~0.57–0.58.
- Many top-AUC rows have MCC 0 / balanced accuracy 0.5 (decision collapse); max MCC ~0.063.
- "Competitive" with LR/MLP on accuracy only; modest gains over MLP.

## Limitations / open problems
Weak signal, single seed, thousands of configs, no significance tests — winner's-curse risk. Accuracy-only baseline comparison; no quantum-layer ablation. Unexplained Fock-measurement mode limit and inconsistent config counts. Short training. No hardware, no theory.

## Why it matters to me
Finance + QML on real market data with a leakage-safe protocol; the threshold-calibration and collapse diagnostics carry over to rare-positive fraud problems. As evidence, it's honest-negative-leaning: mostly chance-level, no demonstrated edge over a shallow MLP.
