---
arxiv_id: 2606.10179
version: v3
title: "Trainability of IQP Quantum Circuit Born Machines Under Gaussian Initialization"
authors: [Gennaro De Luca, Vinayak Sharma, Aviral Shrivastava]
primary_category: quant-ph
published: 2026-06-08
added: 2026-09-29
relevance: 4
tags: [barren-plateaus, trainability, generative, theory, qml-bottlenecks, variational]
full_text: ../md/2026-luca-trainability-of-iqp-quantum-circuit-born-machines-under-gaus-arxiv2606.10179v3.md
---

## Problem
IQP QCBMs can be trained classically via an MMD loss ("train classically, deploy quantumly"), yet still face exponential concentration and barren plateaus. Prior analyses mostly assume uniform initialization; the lone Gaussian treatment uses loose global-depth assumptions.

## Method
Pure theory, no experiments. MMD² written as an expectation over Bernoulli observable masks with $p_\sigma$ set by kernel bandwidth $\sigma$. Key object: the **reverse light cone** $\Gamma(a)$ — generators overlapping observable $a$ an odd number of times. Tools: closed-form gradient, Stein's lemma covariance bound $\mathrm{Var}(\partial_kC)\ge\sigma_\theta^2(\mathbb E[\partial_l\partial_kC])^2$, Gaussian characteristic functions, and Gaussian Lipschitz concentration.

## Key results
- Thm 1: gradients are sparse — only observables overlapping $g_k$ contribute.
- Thm 2: variance lower bound governed by $|\Gamma(a)|$, not locality or total depth; can vanish via destructive interference or parity-symmetric targets.
- Cor. 1: concentration mitigated if $\sigma=\Omega(n)$, $\sigma_\theta^2=O(1/\max|\Gamma(a)|)$, $\mu_\theta=O(1/\sqrt{\max|\Gamma(a)|})$ — a quantum "Xavier" init with light-cone size as fan-in. Explains why Shen et al.'s $\sigma_\theta^2=c/D$ works but pushes toward identity/simulability.
- Thm 3: Lipschitz concentration of the gradient around its mean; BPs need both zero mean *and* concentrated variance.

## Limitations / open problems
No numerics at all. Avoiding concentration ≠ effective training or generalization; strategies are data-independent. Cor. 1 assumes no destructive interference; mean-scaling result proven only for non-overlapping generators. $L^2$ bound is loose. Summarizer flagged a possible tension (small $\sigma_\theta^2$ both helps and concentrates) and an apparent contradiction on bandwidth direction between §3.2 and §3.3.

## Why it matters to me
Rigorous, usable levers (init mean/variance, MMD bandwidth, generator sparsity) for a plausibly practical generative QML route. Stein/Gaussian-concentration machinery suits my stats background. No classical-data or finance experiments; synthetic transaction generation is my own speculation.
