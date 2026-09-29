---
arxiv_id: 2609.25641
version: v1
title: "When Quantum Meets AI: Quantum Methods for Machine Learning and Machine Learning Methods for Quantum Systems"
authors: [Tak Hur]
primary_category: quant-ph
published: 2026-09-22
added: 2026-09-29
relevance: 4
tags: [encoding, generalization, theory, quantum-neural-networks, statistical-learning]
full_text: ../md/2026-hur-when-quantum-meets-ai-quantum-methods-for-machine-learning-a-arxiv2609.25641v1.md
---

> Note: the conversion (ar5iv fallback) captured only the abstract page of this
> 171-page thesis; everything below is from the abstract. Re-sync if full HTML
> becomes available, or read the PDF.

## Problem
Two directions: (1) quantum methods for ML — learning embeddings that make quantum classifiers work (incl. noisy hardware and DQC1), and what actually predicts QNN generalization; (2) ML for quantum systems — surface-code decoding and neural-quantum-state optimisation.

## Method
- **Neural Quantum Embedding (NQE):** learn a representation maximising trace distance between embedded class ensembles, lowering an embedding-dependent empirical-risk bound.
- **DQC1 extension:** Hilbert–Schmidt-based objective, demonstrated on an NMR processor.
- **Margin-based generalization analysis** linking QNN performance to quantum state discrimination.
- Also: a Mamba-based surface-code decoder; stochastic reconfiguration reinterpreted as tangent-space ridge regression with a multi-shift variant.

## Key results
(Abstract-level, no numbers available.) NQE improves classification on noisy hardware; DQC1 variant runs on NMR. Margin distributions predict generalization better than parameter-count metrics "in the studied benchmarks." Mamba decoder matches a Transformer baseline with quadratic (vs quartic) inference scaling in code distance. Multi-shift SR lowers validation residuals and update variance at extra cost.

## Limitations / open problems
Hedged claims in the abstract ("in the studied benchmarks", explicit noise model for the decoder, extra SR cost). Datasets, bound tightness, scaling and failure modes cannot be assessed from the captured text.

## Why it matters to me
The QML half is squarely on my interests: learned embeddings attack the encoding bottleneck, and margin/state-discrimination generalization is the statistical-learning framing I want. Worth pulling the full PDF to check NQE datasets (tabular?) and the actual bounds. Decoder/NQS chapters are lower priority.
