---
arxiv_id: 2607.02626
version: v4
title: "Krylov-Lie Algebras for Variational Quantum Algorithms: Geometric, Depth-Aware Insights into Expressivity and Trainability"
authors: [Anžej Margeta-Cacace]
primary_category: quant-ph
published: 2026-07-02
added: 2026-09-29
relevance: 4
tags: [barren-plateaus, trainability, variational, theory, qml-bottlenecks]
full_text: ../md/2026-margeta-cacace-krylov-lie-algebras-for-variational-quantum-algorithms-geome-arxiv2607.02626v4.md
---

## Problem
Standard VQA landscape theory (DLA variance formulas of Ragone et al., Anschuetz's JAWS, $t$-designs) assumes Haar/near-Haar sampling over the full dynamical Lie group, ignoring finite-depth geometry — ill-suited to the shallow regime where training is feasible (cf. "cragged terrains" in shallow QAOA).

## Method
159-page mathematics thesis, purely theoretical. Defines **Krylov-Lie algebras/groups**: project generators onto a grade-$k$ Krylov subspace built from seed states and take the generated (reductive) Lie algebra; its closure gives a compact depth-aware proxy for the reachable manifold. Develops dimension theory (generic maximal dimension, Witt-formula bounds), approximation theory (pushforward absolute continuity, canonical comparison map), exact weighted moment formulas under arbitrary sampling laws $\nu=q\mu_K$, and an "observable Kawada–Itô" ergodic theorem. Worked example: cycle-graph QAOA on MaxCut.

## Key results
- Factorial approximation error bounds (e.g. $\le 2B_C^{k+1}/(k+1)!$ for prefix KLAs).
- Concentration transport via log-Sobolev on the compact KLG.
- Weighted variance formula reducing to Ragone et al. at $q\equiv1$; non-Haar gap $\le 3\|q-1\|_{L^1}\|O\|_\infty^2$.
- Counterexample: in cycle-graph QAOA some parameter distributions never converge to Haar; author argues Ragone et al.'s Lemma 6 / Thm 2 need extra hypotheses. Convergence iff "observably adapted and strictly aperiodic."
- Polynomially many parameters ⇒ Haar-type expressivity alone gives only polynomial decay of the reduced-loss variance; non-Haar densities could *increase* variance.

## Limitations / open problems
Noiseless unitary circuits only; results concern the *reduced* loss; needs $O$ or $\rho$ in the algebra and seed certificates. Transferring polynomial-variance conclusions to the real circuit requires approximation error below variance scale — not established. No numerics; the claimed flaw in Ragone et al. is not independently confirmed. Many open questions (attainable dimensions, classical simulability, practical reweighting schemes).

## Why it matters to me
Strong fit on trainability theory with real proofs, and a potentially important challenge to the standard BP narrative ("VQAs may be more trainable than posited"). The init-distribution reweighting idea is a concrete mitigation lead. Mathematically heavy; nothing on classical data or finance.
