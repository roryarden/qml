---
arxiv_id: 2610.09798
version: v2
title: "Quantum Optimization of the Color-of-Money Problem on IBM Quantum Hardware: A Proof-of-Concept Study"
authors: [Rahul Rana, Suman Kumar Roy, M Girish Chandra]
primary_category: quant-ph
published: 2026-10-07
added: 2026-10-11
relevance: 4
tags: [finance, optimization, variational, encoding, hardware]
full_text: ../md/2026-rana-quantum-optimization-of-the-color-of-money-problem-on-ibm-qu-arxiv2610.09798v2.md
---

## Problem
The Color-of-Money (CoM) treasury problem: allocate and route funds across accounts, currencies and periods subject to fund-eligibility rules, balance conservation and invoice deadlines ("Invoice Funding and Liquidity Transfer"). Treasury problems are under-studied in quantum finance; goal is correctness/feasibility on hardware, not advantage.

## Method
MILP (binary assignment + continuous transfers/payments/balances) → QUBO via squared-penalty constraints (Verma–Lewis weights) and binary expansion of continuous variables. Pauli Correlation Encoding (PCE) compresses qubits to $O(\sqrt\eta)$ using same-axis two-qubit correlators with a $\tanh$ relaxation. Parameters trained on a noiseless simulator; final evaluation on ibm-aachen with zero-noise extrapolation. One instance (3 assets, 3 invoices, 2 periods) vs SCIP.

## Key results
SCIP: objective 151.00 in 0.02 s. VQA-PCE on IBM hardware: objective 151.00 (optimum recovered) in 31.00 s. Validates the MILP → QUBO → PCE pipeline; no computational advantage.

## Limitations / open problems
Single tiny instance; slower than SCIP. Missing: variable/qubit counts, penalties, ansatz, optimizer, shots, ZNE settings, repeat runs/variance. Training fully on a noiseless simulator, so hardware only confirms a pre-found solution. Unexplained $[-1,1]$ vs $\{0,1\}$ mapping and a seemingly shared slack variable. No QAOA/annealing comparison.

## Why it matters to me
Directly a payments/treasury problem (invoice funding, liquidity routing, fund-use eligibility) — close to my day job. Value is the end-to-end formulation template and PCE qubit compression, not evidence of practicality. Optimization, not learning.
