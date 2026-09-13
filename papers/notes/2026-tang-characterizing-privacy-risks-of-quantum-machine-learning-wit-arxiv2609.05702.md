---
arxiv_id: 2609.05702
version: v2
title: "Characterizing Privacy Risks of Quantum Machine Learning with Emergent Quantum-Native Access"
authors: [Tang et al.]
primary_category: quant-ph
published: 2026-09-04
added: 2026-09-10
relevance: 4
tags: [privacy, security, theory, quantum-neural-networks, classical-data]
full_text: ../md/2026-tang-characterizing-privacy-risks-of-quantum-machine-learning-wit-arxiv2609.05702v2.md
---

## Problem
Membership-inference-attack studies against QML assume a purely *classical* adversary receiving classical outputs. In a quantum-native world (programmable measurements or pre-measurement state access), does a quantum-capable adversary gain a privacy-attack advantage?

## Method
Formalizes MIAs against QNNs as a LiRA-style membership game across three access regimes — classical outcome-only (C), programmable Pauli measurement (M), full state (Q) — each with a $k$-shot budget. Uses quantum hypothesis testing (TV distance, Helstrom) to derive optimal advantages. Empirics: 4-qubit QNN on MNIST 0-vs-1 / 3-vs-8.

## Key results
(Thm III.1) under classicalized output a quantum adversary gains **no** advantage. (Thm III.2) strict leakage hierarchy $L_C\le L_M\le L_Q$ — more quantum access ⇒ more leakage. (Thm III.3) finite-resource gap bounded by $\sqrt{2d^k/K}$. Experiments confirm the hierarchy.

## Limitations / open problems
Small-scale (4-qubit), noiseless sim; MIA susceptibility is model-dependent; the bound is non-tight; the strongest Q regime depends on immature quantum networking; defenses discussed but not implemented.

## Why it matters to me
Rigorous proof-driven QML privacy theory (Helstrom/TV hypothesis testing, leakage hierarchy) in my "rigorous theory" and "data privacy / implications of quantum" areas; relevant to payments where training-data confidentiality matters. Caveat: a privacy characterization, not a fraud application; toy-scale.
