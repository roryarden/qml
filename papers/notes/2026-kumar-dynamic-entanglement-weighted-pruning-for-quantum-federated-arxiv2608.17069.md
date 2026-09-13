---
arxiv_id: 2608.17069
version: v1
title: "Dynamic Entanglement-Weighted Pruning for Quantum Federated Unlearning in Supply-Chain Risk Prediction"
authors: [Kumar, Chongder]
primary_category: quant-ph
published: 2026-08-17
added: 2026-09-10
relevance: 5
tags: [federated-learning, privacy, finance, variational, qml-bottlenecks]
full_text: ../md/2026-kumar-dynamic-entanglement-weighted-pruning-for-quantum-federated-arxiv2608.17069v1.md
---

## Problem
Federated variational quantum classifiers must honor GDPR right-to-erasure, but full retraining is wasteful and it's unclear which circuit parameters carry a client's influence (entanglement spreads it non-locally).

## Method
Entanglement-Weighted Pruning (EWP): score each parameter by the product of its diagonal quantum Fisher information on the forgetting client (parameter-shift) and a structural entanglement weight; prune below threshold, then short fine-tune on retained clients. 4-qubit/3-layer data-re-uploading ansatz, FedAvg over 5 non-IID supply-chain clients, noiseless sim, 3 seeds.

## Key results
EWP reaches accuracy 0.837/AUROC 0.907, statistically indistinguishable from the retrain oracle ($p=0.28$), with better forgetting/membership scores, at a $16.4\times$ speed-up. Random/Fisher-only/entanglement-only pruning all collapse → both signals jointly necessary.

## Limitations / open problems
Only diagonal QFIM; noiseless, 4-qubit/24-param/3-seed scale; membership result attacker-specific, not a certified guarantee; synthetic data; headline depends heavily on the fine-tuning recovery pass (Table 7 shows 0.344 pre-fine-tune).

## Why it matters to me
Quantum federated learning on a finance/commerce-adjacent tabular task (supply-chain risk), foregrounding privacy/GDPR (payments-relevant), engaging QML bottlenecks via quantum Fisher information. A mechanism demonstration, not evidence QML wins (no classical unlearning baseline, tiny scale).
