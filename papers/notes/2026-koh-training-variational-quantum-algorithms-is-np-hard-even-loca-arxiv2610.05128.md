---
arxiv_id: 2610.05128
version: v1
title: "Training Variational Quantum Algorithms Is NP-Hard, Even Locally"
authors: [Dax Enshan Koh, Triscia Mundo, Iosif Sakos, Antonios Varvitsiotis]
primary_category: quant-ph
published: 2026-10-04
added: 2026-10-11
relevance: 5
tags: [qml-bottlenecks, trainability, variational, optimization, theory]
full_text: ../md/2026-koh-training-variational-quantum-algorithms-is-np-hard-even-loca-arxiv2610.05128v1.md
---

## Problem
Global minimization of VQA objectives is known to be NP-hard (Bittel & Kliesch), but practice only seeks local minima, and global hardness doesn't imply local hardness. Does settling for a local minimizer — or a point near one — escape the computational barrier? (Separate from shot cost and barren plateaus.)

## Method
Reduction chain from Stable Set: a copositivity-based quadratic $q(x)=x^\top Mx$ on $[0,1]^n$ whose local minimizers are all at 0 iff $\alpha(G)<k$; composition with the open surjection $T(\theta)=(1-\cos\theta)/2$ preserves local minimizers and yields a degree-≤2 Hermitian trigonometric polynomial; an explicit $2n$-qubit circuit (shared-parameter $R_x$ pairs, diagonal 2-local observable) reproduces it exactly. Purely theoretical.

## Key results
- Finding a local minimizer of an efficiently represented VQA objective is **strongly NP-hard**.
- So is finding any point within $\ell_p$-distance $<\pi/2$ of some local minimizer, for every $p\ge1$.
- Holds even when the objective is efficiently classically evaluable — shot noise isn't the cause.
- Hard instances are simple: single-qubit rotations, commuting diagonal 2-local Hamiltonian, $2n$ gates.

## Limitations / open problems
Worst-case only; known tractable families (level-1 QAOA, overparameterized VQEs, Gaussian-process QNN limit) are unaffected. Hard instances are artificial graph encodings with no data/loss-over-samples structure. Open: which architectural/observable restrictions separate tractable from hard.

## Why it matters to me
A rigorous third obstacle to trainability alongside barren plateaus and traps: switching to local optimization doesn't remove worst-case hardness, so general training guarantees can't exist and progress must come from structured ansätze. Short, self-contained proof with reusable tools. Says nothing directly about data-driven VQC classifiers.
