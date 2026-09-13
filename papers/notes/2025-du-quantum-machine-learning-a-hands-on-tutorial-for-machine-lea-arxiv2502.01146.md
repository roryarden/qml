---
arxiv_id: 2502.01146
version: v1
title: "Quantum Machine Learning: A Hands-on Tutorial for Machine Learning Practitioners and Researchers"
authors: [Du et al.]
primary_category: quant-ph
published: 2025-02-03
added: 2026-09-10
relevance: 4
tags: [foundations, qml-bottlenecks, kernel-methods, quantum-neural-networks, quantum-transformers, theory]
full_text: ../md/2025-du-quantum-machine-learning-a-hands-on-tutorial-for-machine-lea-arxiv2502.01146v1.md
---

## Problem
A 260-page pedagogical tutorial (not a research result) to lower the entry barrier into QML for readers with a classical ML background, scoped primarily to the "Q-for-C" quadrant (quantum algorithms on classical data).

## Method
Textbook-style: quantum-computing basics (density matrices, block encoding/QSVT), then chapters each mirroring a classical model and its quantum extension — **quantum kernel methods**, **quantum neural networks** (VQCs, quantum GANs), **quantum transformers** (quantum self-attention, claimed quadratic inference speedup) — plus appendices on Haar measure and $t$-designs. Frames learnability along expressivity / trainability / generalization. Runnable code hosted externally.

## Key results
No new empirical claims; consolidates the theory of expressivity, generalization bounds, and trainability/barren plateaus across kernels and QNNs, and surveys FTQC (HHL, QPCA, QSVT) vs NISQ methods.

## Limitations / open problems
Per-chapter "challenges" note genuine quantum advantage "remains an ongoing challenge"; FTQC algorithms need tens of billions of qubits; NISQ noise limits practicality. Scope narrowed to the QC sector, circuit model, PAC framework.

## Why it matters to me
Reference anchor rather than a novel result — organizes the QML bottlenecks (trainability, encoding, noise, scalability) and statistical-learning framing I care about, is QML-on-classical-data focused, and covers kernels/VQCs/GANs/transformers. Useful to cross-reference the specialized papers in this library; finance is only a listed application.
