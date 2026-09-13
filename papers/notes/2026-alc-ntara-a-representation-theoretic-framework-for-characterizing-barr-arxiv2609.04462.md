---
arxiv_id: 2609.04462
version: v1
title: "A Representation-Theoretic Framework for Characterizing Barren Plateaus"
authors: [Alcántara et al.]
primary_category: quant-ph
published: 2026-09-03
added: 2026-09-10
relevance: 5
tags: [barren-plateaus, trainability, theory, variational]
full_text: ../md/2026-alc-ntara-a-representation-theoretic-framework-for-characterizing-barr-arxiv2609.04462v1.md
---

## Problem
DLA-based barren-plateau theory only applies when the initial state or observable lives inside the circuit's dynamical Lie algebra — excluding many physical cases. Is that restriction intrinsic or an artifact of the math?

## Method
Recasts trainability as harmonic analysis on compact Lie groups. Under a unitary 2-design assumption, decomposes operator space into irreducible-representation channels; Schur orthogonality splits the second moment into non-negative per-irrep terms, giving exact variance + bounds for arbitrary states/observables. Validated on the 1D ANNNI model across three ansätze.

## Key results
$\mathrm{Var}[\ell]=\sum_{\zeta\neq\tau}\mathcal C_\zeta$; prior DLA theory recovered as a special case. Fully expressive $\mathfrak{su}(2^n)$ → exponential suppression; local $\mathfrak{su}(2)^n$ → extensive (linear) variance; commuting $\mathfrak{u}(1)^{2n-1}$ → size-independent lower bound $\ge 1/2^6$. A single-irrep certificate proves nonvanishing variance cheaply.

## Limitations / open problems
Rests entirely on the 2-design assumption (asymptotic deep regime); finite-depth corrections open. Applying the theorem needs the explicit irrep decomposition. One benchmark Hamiltonian.

## Why it matters to me
Proof-driven barren-plateau theory that unifies prior work and yields an actionable design principle (symmetry-restrict the ansatz) plus a practical lower-bound certificate. Physics observable, not classical-data/finance; 2-design limits shallow-circuit use.
