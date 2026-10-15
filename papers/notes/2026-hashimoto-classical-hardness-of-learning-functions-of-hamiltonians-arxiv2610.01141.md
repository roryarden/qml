---
arxiv_id: 2610.01141
version: v1
title: "Classical Hardness of Learning Functions of Hamiltonians"
authors: [Sota Hashimoto, Akinori Kawachi]
primary_category: quant-ph
published: 2026-10-01
added: 2026-10-11
relevance: 4
tags: [theory, statistical-learning, foundations, security]
full_text: ../md/2026-hashimoto-classical-hardness-of-learning-functions-of-hamiltonians-arxiv2610.01141v1.md
---

## Problem
Morohoshi et al. proposed "Hamiltonian function learning" (HFL): predict $\mathrm{Tr}[f(H)\rho]$ from classical descriptions of $H$ and $\rho$ with unknown $f$, gave an efficient quantum learner, but left average-case classical hardness unproven.

## Method
Kearns–Valiant-style cryptographic reduction under average-case hardness of factoring random RSA moduli. Hard instances: a projector Hamiltonian $H=U^\dagger\Pi_{\rm acc}U$ from a coherent amplified Shor circuit that accepts iff $b$ is the $j$-th bit of $\min\{p,q\}$; since $H$ is a projector, $\cos(\pi H)$ and $e^{-\beta H}$ are affine in the acceptance probability. Training data generated classically from known factors; a classical learner with small expected squared loss would reveal factor bits.

## Key results
- Theorem 3.1: for $f=\cos(\pi\lambda)$ and $f=e^{-\beta\lambda}$ (any fixed rational $\beta>0$), an efficient classical learner with classically evaluable hypotheses ⇒ classical factoring of random RSA moduli.
- Needs only small expected squared loss (vs pointwise), uniform average-case hardness, explicit samplable distribution; hardness holds even when $f$ is known.
- Generalizes to any problem with classically samplable instance–witness pairs, quantum-recoverable witnesses and average-case classical hardness.

## Limitations / open problems
Hard Hamiltonians are non-local circuit-defined projectors, not physical local Hamiltonians (open). Instances are cryptographic constructions. Requires classically evaluable hypotheses. Quantum side needs fault-tolerant Shor-scale circuits. No experiments. LLM assistance disclosed.

## Why it matters to me
A clean, complete separation proof in a regression/statistical-learning setting, and a reminder that "practical" QML advantages often borrow their hardness from Shor/RSA — useful for judging which advantage claims are informative. Loose Q-Day link; no data or finance relevance.
