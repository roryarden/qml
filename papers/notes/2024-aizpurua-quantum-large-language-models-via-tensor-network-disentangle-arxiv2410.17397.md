---
arxiv_id: 2410.17397
version: v2
title: "Quantum Large Language Models via Tensor Network Disentanglers"
authors: [Aizpurua et al.]
primary_category: quant-ph
published: 2024-10-22
added: 2026-09-10
relevance: 5
tags: [quantum-transformers, nlp, encoding, qml-bottlenecks, hardware]
full_text: ../md/2024-aizpurua-quantum-large-language-models-via-tensor-network-disentangle-arxiv2410.17397v2.md
---

## Problem
How to inject quantum resources into a *pretrained* LLM without degrading accuracy? Classical tensor-network compression has a bond-dimension ceiling; prior quantum-language work handled only simple models.

## Method
Replace each weight matrix in attention/MLP layers with VQC + MPO + VQC. Tensorize $W$ to an MPO, compute two disentangling circuits (MERA-style) that push entanglement into the circuits, truncate the residual MPO. Circuits initialized to leave the layer unchanged (hybrid exactly reproduces baseline); a trainable Cayley adapter is fine-tuned to surpass it. Demonstrated by replacing SmolLM2's 10th-layer attention weight; perplexity on WikiText; partial IBM Heron execution.

## Key results
Disentangling alone changes PPL ≤0.003%. Residual MPO to bond dim 1 = **~36 params** (vs 110,592) at +0.26% PPL; undisentangled truncation costs +9.7%. Cayley adapter lowers PPL up to ~1.6% below baseline. Hardware proof-of-concept answers "9×6" on IBM Heron.

## Limitations / open problems
Only a single layer replaced. Memory saving realized only if circuits run on a QPU (disentanglers carry ≥ as many params as $W$). Hardware limited to 2-qubit gates. Disclaims any inference-speed quantum advantage.

## Why it matters to me
Quantum + NLP / quantum transformers, targeting the parameter-loading bottleneck with a construction guaranteeing the hybrid never underperforms the classical baseline. Weaker on finance/fraud (no financial data) and formal theory (constructive, not a proven separation).
