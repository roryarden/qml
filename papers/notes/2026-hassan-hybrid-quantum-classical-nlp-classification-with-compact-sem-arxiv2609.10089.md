---
arxiv_id: 2609.10089
version: v1
title: "Hybrid Quantum-Classical NLP Classification with Compact Semantic Representations: An Experimental Analysis of Representation Compression"
authors: [Hassan et al.]
primary_category: cs.LG
published: 2026-09-09
added: 2026-09-10
relevance: 5
tags: [nlp, encoding, classical-data, variational, qml-bottlenecks]
full_text: ../md/2026-hassan-hybrid-quantum-classical-nlp-classification-with-compact-sem-arxiv2609.10089v1.md
---

## Problem
Sentence embeddings are 768/384-dim but near-term QML circuits encode only a handful of features. How much semantic information can be compressed into a quantum-compatible representation before classification collapses — and how much is classical compression vs quantum contribution?

## Method
Hybrid pipeline: frozen `all-MiniLM-L6-v2` embeddings → reduction (PCA vs supervised NCA/LDA) → $R_y$ angle encoding → 5-qubit 2-layer VQC → classical softmax. Evaluated on TREC with a leakage-free cross-validation protocol.

## Key results
PCA shows a severe bottleneck (3/4/5/8 dims retain 8.2/10.2/11.9/16.4% variance, 50–63% accuracy). Supervised reduction is far more efficient: at **5 dims LDA 85.3%, NCA 83.1%**, matching the full 384-dim classical MLP baseline (85.1%). Explained variance is an unreliable proxy for accuracy.

## Limitations / open problems
"Preliminary"; critically **no matched quantum-vs-classical comparison on the *same* compressed features** — gains are attributable to classical reduction, not quantum expressibility. Simulation only, ≤8 qubits, linear reductions.

## Why it matters to me
QML encoding/data-loading bottleneck + QML-on-classical-data (real NLP text) + quantum+NLP, with honest methodology (refuses to claim quantum advantage). Caveat: the quantum-vs-classical head-to-head is deferred; no finance/fraud angle.
