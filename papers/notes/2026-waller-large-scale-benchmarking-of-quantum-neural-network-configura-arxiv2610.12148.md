---
arxiv_id: 2610.12148
version: v1
title: "Large-Scale Benchmarking of Quantum Neural Network Configurations for Financial Time Series Forecasting"
authors: [Jack Waller, Xing Liang, Dimitrios Makris, Rajagopal Nilavalan]
primary_category: cs.LG
published: 2026-10-08
added: 2026-10-11
relevance: 4
tags: [quantum-neural-networks, variational, classical-data, finance, benchmark, qml-bottlenecks]
full_text: ../md/2026-waller-large-scale-benchmarking-of-quantum-neural-network-configura-arxiv2610.12148v1.md
---

> Note: the converted Markdown is **truncated** mid-§3.2 (encoding description). Methodology, results, discussion and references are missing; everything below rests on the abstract and introduction. Re-read from the PDF before relying on it.

## Problem
Systematic QNN component comparisons exist for classification, not regression. Which QNN design choices matter for financial time-series forecasting (GBP/USD spot rate)?

## Method
Grid over encodings (amplitude, angle, "circuit"), ansätze, qubit counts, depths and cost functions → 1,368 configurations, scored on accuracy, compute cost and convergence. Classical BiLSTM baseline. Selected configurations run on IQM Emerald. Data split, window, horizon, target transform, optimizer and shots not available in the converted text.

## Key results
(Abstract only.) Best QNN $R^2=0.985$, reported above BiLSTM. Gate selection/arrangement matter more than parameter count; entanglement is a whole-circuit property. On IQM Emerald, gate errors and decoherence are a significant barrier; gate choice and depth govern noise resilience.

## Limitations / open problems
Single FX pair; BiLSTM is the only named baseline. If the target is the price *level*, a naive persistence forecast typically scores $R^2\approx1$ — no persistence/random-walk baseline is visible, so the headline number may show no real skill. No hardware degradation numbers in available text.

## Why it matters to me
Finance + QML-on-classical-data + hardware-noise characterization, and the large configuration grid could inform VQC design. But the headline result needs a persistence check before it counts as evidence that QML "doesn't fail" here. Revisit with the full PDF.
