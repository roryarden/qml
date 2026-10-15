---
arxiv_id: 2610.08131
version: v1
title: "Mu-DisCoCat: A Variational Pipeline for Compositional Generalization on Quantum Processors"
authors: [Mina Abbaszadeh, Matilda Karabina Moore, Raem Haq, Martha Lewis, Mehrnoosh Sadrzadeh]
primary_category: cs.LG
published: 2026-10-06
added: 2026-10-11
relevance: 4
tags: [nlp, variational, quantum-neural-networks, encoding, generalization, hardware]
full_text: ../md/2026-abbaszadeh-mu-discocat-a-variational-pipeline-for-compositional-general-arxiv2610.08131v1.md
---

## Problem
Compositional concept generalization (recombining known primitives, e.g. shapes in new spatial relations) is hard for vision-language models like CLIP. DisCoCat suits compositionality but its tensors are expensive classically; prior VQC versions were text-only or simulation-only with post-selection. Can a multimodal DisCoCat run on current noisy hardware?

## Method
Pregroup grammar → Hilbert-space functor; relations as $V^*\otimes W\otimes V^*$ tensors. Sim4 text / IQP image ansätze. Two-stage training: learn nouns from single-object image–caption pairs (contrastive), freeze, then learn relations. Image encodings: one-/multi-hot, CLIP embeddings (amplitude or PCA+angle), "collage". Hardware tweaks: 4-qubit images, partial trace instead of post-selection, Uhlmann fidelity via destructive SWAP test. CoBi2 (synthetic CLEVR) with OOD splits, 5 seeds. Classical CLIP-text baseline. Aer, fake backends, IBM Marrakesh.

## Key results
- Single-object OOD: one-hot 93.3% (168 params) vs CLIP baseline 91.0% (63.4M params).
- Relational OOD: multi-hot 85.9%; collage+angle 72.3%; CLIP-angle multistage 55.3%; CLIP baseline at chance (50%).
- 4-qubit hardware model (sim): 93.0% / 72.7%.
- Real Marrakesh: Pearson with simulated fidelities 0.949 (stage 1) and 0.732 (stage 2, depth ~365); cluster separation shrinks.

## Limitations / open problems
No advantage claimed; comparison not parameter-matched. Only text is compositional. Training simulated; hardware used for evaluation only, reported as correlation not accuracy. Synthetic small data. CLIP-feature quantum models weak; best results use hand-built encodings. Some table oddities (CLIP baseline OOD val 11%).

## Why it matters to me
Strong quantum + NLP/linguistics fit (DisCoCat/pregroups) with concrete hardware-bottleneck engineering (removing post-selection, compressing embeddings, depth/noise scaling). Weak evidence for "classical data where QML doesn't fail" given synthetic data and an at-chance baseline.
