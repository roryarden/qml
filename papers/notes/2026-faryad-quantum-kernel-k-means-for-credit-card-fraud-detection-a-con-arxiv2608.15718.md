---
arxiv_id: 2608.15718
version: v1
title: "Quantum Kernel k-Means for Credit-Card Fraud Detection: A Controlled Benchmark on Real Transaction Data"
authors: [Faryad]
primary_category: quant-ph
published: 2026-08-16
added: 2026-09-10
relevance: 5
tags: [kernel-methods, fraud, finance, classical-data, benchmark, kernel-concentration]
full_text: ../md/2026-faryad-quantum-kernel-k-means-for-credit-card-fraud-detection-a-con-arxiv2608.15718v1.md
---

## Problem
Does a quantum fidelity kernel genuinely help credit-card fraud detection, or do "advantages" come from flawed benchmarking (weak baselines, select-and-report on same data, single splits)?

## Method
Quantum kernel $k$-means on the real ULB dataset (0.173% fraud); 2/4/8/12 qubits; budget-matched held-out protocol (dev vs 30 disjoint report seeds), paired $t$-tests + CIs. Quantum search over 264 feature-map configs vs classical 105. Qiskit Aer exact statevectors + finite-shot repeat.

## Key results
No robust advantage — sign flips with register size; all effect sizes $<0.013$ ARI. The 8-qubit "advantage" is a search-budget artefact (20 vs 264 configs → quantum leads only 34%). A single classical bandwidth moves performance ~14× more. More qubits hurt via kernel concentration. Anomaly-scoring survives but quantum still no edge over classical.

## Limitations / open problems
Single dataset (PCA features may suit classical kernels); no trainable feature maps; noiseless sim (called conservative); ignores asymptotic kernel-eval speedup.

## Why it matters to me
QML-on-classical-data on finance/fraud, fundamentally about QML bottlenecks (kernel concentration, bandwidth dominance). Its search-budget ablation converting a "significant" advantage into an artefact is a superb cautionary template for vetting quantum fraud classifiers — the "why apparent wins are illusory" analysis I value.
