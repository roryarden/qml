---
arxiv_id: 2609.30195
version: v1
title: "Loan Portfolio Optimization with Variational Quantum Algorithms"
authors: [Balaganchi A. Bhargava, Kamlesh Kumar, Gouranga Dinda, Aniruddha Biswas, Vijay S. Rao, Debarag Banerjee, Arun Sehrawat]
primary_category: quant-ph
published: 2026-09-24
added: 2026-09-29
relevance: 4
tags: [finance, optimization, variational, encoding, hardware, qml-bottlenecks]
full_text: ../md/2026-bhargava-loan-portfolio-optimization-with-variational-quantum-algorit-arxiv2609.30195v1.md
---

## Problem
Select $K$ of $N$ borrowers to minimise credit risk (expected loss + loss variability + correlated defaults) — a large combinatorial problem. One-qubit-per-variable quantum formulations cap problem size on NISQ hardware.

## Method
Real microfinance data: 2012 borrowers, 26 monthly snapshots. Loss $=\text{EAD}\cdot\text{LGD}\cdot\text{PD}$ (LGD=1, PD from a fixed logistic credit-score mapping). QCBO objective $\alpha\mu^\top x+\beta x^\top\tilde\Sigma x$ with an ad-hoc signed-sqrt covariance $\tilde\Sigma$, relaxed to QUBO; cardinality enforced by top-$K$ post-processing. Solved by a VQA with **Pauli Correlation Encoding** ($\lceil\log_4(N+1)\rceil$ qubits; a three-subgroup variant needs only 3 measurement settings), EfficientSU2 + COBYLA with a $\gamma$-annealed tanh. Baseline: OR-Tools CP-SAT on a linearised model with matched time. Hardware: IBM superconducting device up to 1500 variables.

## Key results
- VQA portfolios are ~**40% worse** than OR-Tools at every size up to $N=1000$.
- Three-subgroup PCE matches full PCE quality with far fewer measurement settings.
- Hardware objective values within **10%** of simulation up to 1500 variables (≈9 qubits by the paper's formula).
- More layers/epochs help; authors explicitly claim feasibility, not advantage.

## Limitations / open problems
Simplified credit model (PD from score only, zero recovery, no CVaR or regulatory constraints). $\tilde\Sigma$ not a standard risk measure. Feasibility depends on classical top-$K$ repair. Trainability/BP and classical simulability of heavy PCE compression open. Summarizer notes: weak baseline (linearised CP-SAT with $N^2$ aux vars, no greedy/SA/QP solver), covariance from 26 time points is rank ≤25, single hardware runs without error bars.

## Why it matters to me
Directly in finance/credit risk on real lending data, and a candid snapshot of where NISQ optimisation stands (loses clearly to classical). PCE is a useful qubit-efficient encoding idea. Not machine learning, and no theory.
