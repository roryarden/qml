---
arxiv_id: 2609.36479
version: v1
title: "Quantum Computing for Network Security Classification: Near-Term Classification and Long-Term Memory Efficiency"
authors: [Yuqing Li, Poonam Bala Nehru, Yunpeng Zhang, Danindu Gammanpilage, Xin Jin, Zeguan Wu, Junyu Liu]
primary_category: quant-ph
published: 2026-09-29
added: 2026-10-11
relevance: 4
tags: [kernel-methods, classical-data, security, encoding, qml-bottlenecks, benchmark]
full_text: ../md/2026-li-quantum-computing-for-network-security-classification-near-t-arxiv2609.36479v1.md
---

## Problem
QML-for-network-security work typically reports one model on one dataset. How could quantum computing help network-security classification over two horizons: near-term accuracy against matched classical baselines, and long-term resource (memory) advantages?

## Method
Near-term: matched pipelines on KDD Cup 99, CICIDS2017 (one-class anomaly detection) and BoT-IoT (supervised DoS vs DDoS); TruncatedSVD to 10–12 dims, angle scaling; fidelity kernel ($R_y$ + nearest-neighbour phases) vs RBF; OCSVM/SVC; 8 seeds; kernel/qubit ablation. Long-term: quantum oracle sketching (QOS, Zhao et al.) memory-size proxy vs sparse/QRAM-style storage and a streaming proxy, across `min_df` feature filtering — an estimate, not a simulation. Statevector only.

## Key results
- KDD: classical RBF better on all metrics (AUC 0.928 vs 0.897).
- CICIDS2017: quantum better on all metrics (AUC 0.667 vs 0.621), with higher variance.
- BoT-IoT: both saturated (~0.998).
- Ablation: RBF is the strongest classical kernel; more qubits don't help monotonically; small-sample KDD result flips — sampling sensitivity.
- QOS proxy much smaller than sparse/QRAM storage at comparable accuracy, but not consistently smaller than a simple streaming proxy.
- Verdict: near-term kernels competitive but task-dependent; long-term value may be memory-efficient data access.

## Limitations / open problems
Noiseless simulation; single feature map; no bandwidth tuning; best-F1 threshold-optimized on evaluation data. QOS part only plugs sizes into a formula; inherits unchecked sparsity/conditioning assumptions. Dated IDS datasets; no tree-ensemble baselines; no theory.

## Why it matters to me
Matched quantum vs classical kernels on real tabular security data with a candid mixed result — CICIDS2017 is a lead (albeit weak) for "where QML doesn't fail". One-class OCSVM setup maps to payment fraud; the QOS framing touches the data-loading bottleneck but defers to Zhao et al. for rigor.
