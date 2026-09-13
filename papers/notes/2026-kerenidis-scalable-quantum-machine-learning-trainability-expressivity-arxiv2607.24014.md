---
arxiv_id: 2607.24014
version: v2
title: "Scalable Quantum Machine Learning: Trainability, Expressivity and Efficiency"
authors: [Kerenidis]
primary_category: quant-ph
published: 2026-07-27
added: 2026-09-10
relevance: 5
tags: [qml-bottlenecks, barren-plateaus, trainability, theory, generalization, finance]
full_text: ../md/2026-kerenidis-scalable-quantum-machine-learning-trainability-expressivity-arxiv2607.24014v2.md
---

## Problem
Frames three simultaneous obstacles to a *scalable* PQC architecture: barren plateaus, no guarantee the learned class is classically hard, and prohibitive ($O(n^2)$) circuit evaluations per gradient step. Claims to resolve all; leaves practical usefulness explicitly open.

## Method
Theory only. Two particle-number-preserving fermionic architectures (unitary **brick-wall** and **butterfly**) from RBS gates + single-qubit $R_z$ phases that lift the DLA from $\mathfrak{so}(n)$ to $\mathfrak{u}(n)$. Non-Gaussian magic-state data loading; particle number $k$ is a dial trading classical hardness vs training cost. Key contribution: a multi-layer parallel parameter-shift rule.

## Key results
Two-body correlator gradient variance $\Theta(k^3/n^5)$ (no exponential barren plateaus). All gradients in $4kn$ / $4k\log n$ evaluations — factor $n/k$ reduction ($17\times$ at $n{=}1024,k{=}60$). Hardness ladder in $k$ up to average-case Fermion Sampling at $k=\Theta(n)$. Generalization scales with parameter count, not Hilbert-space dimension.

## Limitations / open problems
No experiments. Butterfly's sharp rate is conditional on an unproven 2-design conjecture. Average-case hardness proven only at $k=\Theta(n)$, not the $k{=}60$ operating point. Fixed-body expectations are classically tractable at any $k$ — a v1 hard-readout claim was refuted (Amidi) and removed.

## Why it matters to me
The flagship "QML bottlenecks + rigorous theory" paper — trainability, gradient cost, and the trainability-vs-hardness tension. Names portfolio construction/execution as targets (payments-adjacent), though fraud-specific application is absent and it's entirely theoretical.
