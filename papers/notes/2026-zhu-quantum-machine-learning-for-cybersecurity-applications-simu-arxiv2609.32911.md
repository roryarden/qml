---
arxiv_id: 2609.32911
version: v1
title: "Quantum Machine Learning for Cybersecurity Applications: Simulation and Hardware Validation"
authors: [Zirui Zhu, Zisheng Chen, Xiangyang Li]
primary_category: quant-ph
published: 2026-09-26
added: 2026-09-29
relevance: 4
tags: [kernel-methods, variational, classical-data, security, hardware, benchmark]
full_text: ../md/2026-zhu-quantum-machine-learning-for-cybersecurity-applications-simu-arxiv2609.32911v1.md
---

## Problem
Budget-constrained threat detection degrades near the decision boundary. Prior QML intrusion-detection work confounds attribution (different pipelines/sizes) and rarely measures the sim-to-hardware gap. RQs: do quantum heads change near-boundary margins; can the hardware gap be bounded; how robust is the quantum head to evasion?

## Method
Shared classical front end (preprocessing + small MLP → $q$-dim unit embedding); only the head varies: linear/logistic baseline, QSVM (ZZFeatureMap fidelity kernel, double-centered), or VQC (data re-uploading + TwoLocal). 2×2 grid ($q\in\{2,4\}$ × head). NSL-KDD (tabular intrusion) and Ling-Spam (TF–IDF spam). Qiskit Aer with depolarizing noise, 1,024 shots. 4-qubit QSVM run on an unnamed IBM backend (M3 + XY8 DD) on 100 stratified test samples. Robustness tests (magic words, char perturbation, FGSM/PGD, combined) on Ling-Spam QSVM.

## Key results
- NSL-KDD (noisy sim): QSVM $q=4$ acc. 0.921 / macro-F1 0.910 vs MLP+Linear 0.691 / 0.661; VQC $q=4$ drops to 0.807 acc. despite AUROC 0.937.
- Ling-Spam: all hybrids ≥0.955 macro-F1; QSVM $q=4$ near ceiling.
- Hardware ($n=100$): NSL-KDD acc. 0.84 (down from 0.92), Ling-Spam 0.99.
- Combined attack costs −0.037 acc., −0.066 spam-F1; others ~−0.034 to −0.054 F1.

## Limitations / open problems
Only baseline is a **linear** head — no classical RBF-SVM on the same embedding, so gains can't be attributed to anything quantum. RQ1/RQ2 not answered with data (no margin analyses); abstract's "dominated by device noise" conflicts with the stated inability to isolate noise sources. No seeds/error bars; 100-sample hardware test; several hyperparameters and backend unspecified. Robustness tested only on QSVM, with attacks on classical features. No theory.

## Why it matters to me
Intrusion detection is a close cousin of fraud detection (imbalanced tabular data, FP/FN trade-offs, macro-F1/AUPRC); the encoder→small-quantum-kernel-head pattern is directly reusable for payments. But as evidence it's weak — a good cautionary example of why a classical nonlinear-kernel baseline is mandatory.
