---
arxiv_id: 2610.06176
version: v1
title: "What Does It Cost to Simulate a Quantum Sentence Classifier? An Energy and Compute Perspective on Near-Term QNLP"
authors: [Kishlay Kashyap, Sandipan Ganguly]
primary_category: quant-ph
published: 2026-10-05
added: 2026-10-11
relevance: 4
tags: [qml-bottlenecks, nlp, variational, classical-data, benchmark, trainability]
full_text: ../md/2026-kashyap-what-does-it-cost-to-simulate-a-quantum-sentence-classifier-arxiv2610.06176v1.md
---

## Problem
Near-term QNLP runs on classical simulators, but accuracy tables hide the compute cost. How much does simulating a VQC sentence classifier cost, and do VQC "wins" over a matched classical baseline survive multiple seeds?

## Method
SST-2 binary sentiment; balanced $N\in\{200,500,1000\}$; TF-IDF → PCA to 4/6/8 components (= qubits). PennyLane `AngleEmbedding` + `StronglyEntanglingLayers` (depth 1–3), fixed training protocol. Baselines: logistic regression on the same PCA features and on full TF-IDF. 27-config grid at seed 42; the 6 VQC wins rerun at two more seeds. Exact McNemar + Benjamini–Hochberg, paired bootstrap. Wall-clock primary cost; CodeCarbon secondary. One CPU.

## Key results
- VQC training 886–21,127× slower than matched classical (median 3,158×; ~2×10⁵ vs amortized per-fit times).
- Per-step time ≈ 0.053 + 0.0172×params s ($R^2=0.999$); 4→8 qubits only ~2× slower at this scale.
- Accuracy under PCA bottleneck: VQC 47.5–59.2% vs matched LR 49.3–59.5%; full TF-IDF LR reaches 70%.
- Training loss 0.93–1.01 (constant predictor = 1.0) — circuits barely fit.
- Of 6 seed-42 wins, only 1 survives the robustness rule, and it is not statistically established; 10 of 11 BH-significant comparisons favour classical.
- Energy estimates ≈ constant 41 W, adding nothing beyond runtime.

## Limitations / open problems
One dataset/representation/ansatz/simulator/CPU; exponential $2^n$ regime not reached. Software energy estimates. Partial, post-hoc seed coverage. Severe PCA compression keeps both arms near baseline. Not about DisCoCat/lambeq QNLP.

## Why it matters to me
Quantifies a practical bottleneck (simulation cost) and is a model negative result on real classical text data: matched baselines, multi-seed checks and corrected tests make apparent VQC wins disappear. The evaluation protocol is a template for my own experiments.
