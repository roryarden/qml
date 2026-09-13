---
arxiv_id: 2609.03220
version: v1
title: "Discretization-Aware Fine-Tuning for Quantum Machine Learning with Chemical Foundation Models"
authors: [Matsuura, Johri]
primary_category: quant-ph
published: 2026-09-02
added: 2026-09-10
relevance: 5
tags: [encoding, qml-bottlenecks, classical-data, nlp, benchmark]
full_text: ../md/2026-matsuura-discretization-aware-fine-tuning-for-quantum-machine-learnin-arxiv2609.03220v1.md
---

## Problem
Bit-bit (basis) encoding compresses features into short binary strings, causing cross-class collisions (different-label samples → same bit-string) that are provably unclassifiable. How does upstream representation, not circuit design, govern QML competitiveness?

## Method
DAFT — adapts a pretrained ChemBERTa-77M with a differentiable soft collision loss penalizing opposite-class pairs sharing a quantization bin. Bit-bit pipeline into a bipartite entangling classifier at $n_q\in\{4..10\}$. Info-controlled protocol vs logistic regression on the *identical* bit-string, on BBBP (scaffold split, 5 seeds).

## Key results
At $n_q=4$, collisions drop 11,544 → ≈1 and QML accuracy +11–13 pp. Headline at $n_q=10$: **without DAFT classical lr-bit beats QML 0.821 vs 0.761**; **with DAFT reversed**, QML 0.883 vs 0.855 (+2.8 pp, $p=0.026$), driven by a differential DAFT gain (+12.2 pp QML vs +3.4 pp classical).

## Limitations / open problems
5 seeds; main advantage rests on $n=4$ after one seed excluded; modest (+2.8 pp) vs a *linear* baseline; ideal statevector sim; one dataset/foundation model; commercial framework.

## Why it matters to me
Targets the encoding/data-loading bottleneck with a rigorous info-controlled protocol isolating representation from quantum processing — "when does QML actually beat classical?" On real classical data; transformer-embedding-into-register touches quantum+NLP. The "align continuous representation to the discrete register" principle transfers to financial pipelines.
