---
arxiv_id: 2609.28229
version: v1
title: "Distilling Datasets into Shallow Circuits for Quantum Machine Learning"
authors: [Guang Lin, Qibin Zhao]
primary_category: quant-ph
published: 2026-09-23
added: 2026-09-29
relevance: 5
tags: [qml-bottlenecks, encoding, classical-data, variational, quantum-neural-networks]
full_text: ../md/2026-lin-distilling-datasets-into-shallow-circuits-for-quantum-machin-arxiv2609.28229v1.md
---

## Problem
Every training sample must be reloaded by a state-preparation circuit on every shot of every step, so training cost scales with (#samples × loading cost). Prior work either cheapens per-sample loading (approximate amplitude encoding, TN compilation) or shrinks the dataset and then encodes separately — the latter can leave distilled samples expensive to load or lossy once compiled.

## Method
**Quantum Dataset Distillation (QDD):** each synthetic sample *is* a staircase loading circuit ($R_y$ layer + $L$ nearest-neighbour blocks, exactly $2(n-1)L$ CNOTs; an MPS/QTT state with bond dim ≤ $2^L$). Loss = distribution matching over random untrained downstream circuits + $\alpha$·class-mean density-matrix Frobenius term ($\alpha=0.3$). Optimised fully classically with exact gradients. MNIST / Fashion-MNIST at 16×16 → 8-qubit amplitude states (plus a 10-qubit 32×32 study). Downstream: 336-angle brickwork classifier. Baselines: random, herding, forgetting, coreset, k-center, k-means (all compiled to the same 42-CNOT loader) and a distill-then-compress control. Inference on three IBM devices (no mitigation).

## Key results
- Best in 5/6 settings vs selection baselines; IPC 10 (≈0.0017× dataset): 81.62% MNIST, 69.67% Fashion-MNIST. Largest margin at IPC 1 MNIST (+5.71 pts); ~1–2 pts at larger IPC.
- Joint optimisation beats distill-then-compress most at tight budgets (+9.25 pts at 14 CNOTs, IPC 10), but not uniformly (loses slightly at 28/42 CNOTs for some IPCs).
- Finite-shot: QDD-10 hits 95% of full-data accuracy with 134–576× fewer cumulative shots vs **full-batch** full-data training — but only ~2× vs matched mini-batch training.
- Hardware: QDD-10 78.9–83.6% vs full data 78.1–83.6%; exact (uniformly-controlled) preparation of the same states collapses to **6–24%** on hardware despite 85% noiseless.

## Limitations / open problems
Distillation and training are classically simulated at 8–10 qubits; hardware used only for inference on 128 images, no error bars; 3 seeds. Absolute accuracies are well below classical baselines (none reported). Headline shot savings are inflated by the full-batch comparison. No theoretical guarantees. Scaling to larger systems, regression and generative tasks left open.

## Why it matters to me
A concrete, practical attack on the data-loading bottleneck — budgeting both sample count and CNOTs-per-sample is a clean cost framing. The hardware finding (deep exact encodings collapse; shallow approximate loaders survive) is strong evidence about what makes QML practical. No tabular/finance data and no advantage claim; would need QTT-style loaders adapted to transaction features.
