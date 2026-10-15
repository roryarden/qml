---
arxiv_id: 2610.02636
version: v1
title: "Where Quantum Fourier Sampling Stops Short: A Three-Gate Audit Protocol for Delay-PUF Security Models"
authors: [Owen Friedewald, Ali Shiri Sichani, Chi-Ren Shyu]
primary_category: quant-ph
published: 2026-10-02
added: 2026-10-11
relevance: 4
tags: [qml-bottlenecks, kernel-methods, kernel-concentration, security, theory, benchmark]
full_text: ../md/2026-friedewald-where-quantum-fourier-sampling-stops-short-a-three-gate-audi-arxiv2610.02636v1.md
---

## Problem
Can quantum Fourier sampling (QFS) help audit the learnability of delay-based PUFs (arbiter and XOR-arbiter), given XOR-PUFs are low-degree concentrated? Does the promise survive access matching, a strong classical comparator (Kushilevitz–Mansour), and real oracle-synthesis cost — and does a quantum-kernel route fare better?

## Method
Pre-registered "Three-Gate Quantum Audit Protocol". Structure gate: Fourier tail bound for XOR halfspace products (proof avoiding an invalid clipping argument) + numerics $n=10..18$. Algorithmic gate: ideal QFS vs KM on 45 tasks; quantum kernel (parity-aligned Havlíček-style map) vs structured classical kernels via trace-normalized geometric difference $g_{CQ}$ and label complexity $s_K$, with permutation null. Implementation gate: fixed-point QFT-adder phase oracle, transpiled to FakeSherbrooke; Clifford+T estimates.

## Key results
- No useful sparsity at reachable $n$: 4-XOR $n=14$ degree ≤9 admits 91% of characters; 90%-mass set is a third of the spectrum.
- KM recovers heavy characters but exhausts the domain; no 4-XOR ideal-QFS case reaches 90% mass within $2^n$ calls.
- Kernel: $g_{CQ}$ rises to 2.151 at $N=512$, but quantum Gram ≈ identity so $g^2\approx1/\lambda_{\min}(K_C)$ (corr. 0.991); 4-XOR $s_C/s_Q$ ratio not above permutation null ($p=0.930$).
- Oracle: line-QFT cuts depth 18.9%, but certified precisions take 1.18–1.55× median $T_2$; ~7×10⁴ T gates per call.
- No end-to-end advantage in the evaluated regime.

## Limitations / open problems
Simulated PUF models only; small $n$, few kernel pools/instances; KM's asymptotic savings unshown; static backend snapshot, no QPU. Not an impossibility result; dual-use caveat noted.

## Why it matters to me
The most transferable lesson: geometric difference can grow purely from classical Gram ill-conditioning while the quantum kernel is near-identity — any kernel-advantage claim (incl. on fraud data) should report $\lambda_{\min}(K_C)$, ridge sensitivity and a label-permutation control. The three-gate checklist is reusable for vetting vendor claims.
