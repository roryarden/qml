---
arxiv_id: 2610.00649
version: v1
title: "On Evaluating Quantum Kernel Robustness for Low-Resource Cross-Corpus Audio Deepfake Detection"
authors: [Lisan Al Amin, Lei Zhang, Vandana P. Janeja]
primary_category: cs.SD
published: 2026-09-30
added: 2026-10-11
relevance: 4
tags: [kernel-methods, classical-data, security, benchmark, encoding, fraud]
full_text: ../md/2026-amin-on-evaluating-quantum-kernel-robustness-for-low-resource-cro-arxiv2610.00649v1.md
---

## Problem
Audio-deepfake detectors degrade with scarce labels and cross-corpus shift ("cold start": a few hundred verified examples of a new attack). With the front-end fixed, does a quantum-kernel SVM behave differently from classical back-ends under shift?

## Method
Frozen wav2vec 2.0 embeddings → standardize → PCA to 4 dims (56% variance), fit on source only. Back-ends: QSVM (depth-1 full-entanglement ZZ fidelity kernel, exact statevector), RBF-SVM, MLP, plus LR/RF/GB/k-NN. $N=200$ balanced samples, 5 folds. Corpora: ASVspoof 2019, ASVspoof 5, ADD 2023, In-the-Wild; full 3×3 transfer matrix, no target adaptation. Metrics incl. EER, TPR@5%FPR, ECE.

## Key results
- In-corpus: QSVM best mean on most benchmarks (ASV5 EER 8.0% vs LR 12.5%).
- Severe shift ASV19→ADD: MLP random (AUC 50%), RBF inverted (37%), QSVM AUC 76.0% / EER 27% — but accuracy at training threshold only 49%.
- Near-domain ASV19→ASV5: classical better (MLP AUC 89 vs QSVM 77).
- Transfer matrix: QSVM best AUC on 3/9 pairs; trained on ADD it falls below chance on two targets.
- TPR@5%FPR advantage mostly doesn't survive; QSVM worse calibrated (ECE 0.154).
- Explicitly no quantum advantage (4-qubit kernel exactly simulable); bounded oscillatory kernel shape offered as hypothesis.

## Limitations / open problems
Everything at 4-d PCA — no full-768-d classical comparison. Simulator only. Advantage inconsistent and direction-dependent. Poor calibration. No SOTA detectors; one budget; no significance tests; kernel-shape hypothesis untested (e.g. classical periodic kernel ablation).

## Why it matters to me
Honest QSVM benchmark on real classical data in a few-label security setting close to voice-spoofing/account-takeover fraud; reports the full transfer matrix and operating-point metrics. Practical lesson: good AUC can coexist with a broken deployed threshold under drift.
