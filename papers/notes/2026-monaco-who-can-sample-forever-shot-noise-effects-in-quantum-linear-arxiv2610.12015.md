---
arxiv_id: 2610.12015
version: v1
title: "Who can sample forever? Shot noise effects in quantum linear regression"
authors: [Gabriele Lo Monaco, Salvatore Lorenzo, Alessandro Ferraro, Mauro Paternostro, G. Massimo Palma, Luca Innocenti]
primary_category: quant-ph
published: 2026-10-08
added: 2026-10-11
relevance: 5
tags: [qml-bottlenecks, theory, statistical-learning, generalization, kernel-methods]
full_text: ../md/2026-monaco-who-can-sample-forever-shot-noise-effects-in-quantum-linear-arxiv2610.12015v1.md
---

## Problem
Fidelity kernels, quantum extreme learning machines (QELMs) and reservoirs share one architecture: fixed quantum features + a classically trained linear model ("quantum linear regression"). They dodge barren plateaus, but features must be estimated from finite shots. How do shots per state $N$, training states $n_{\rm tr}$ and test shots $M$ jointly set prediction error?

## Method
Unregularized pseudoinverse QELM on multinomial frequency matrices. Key observation: ideal features have rank $d^2$, but shot noise makes the estimate full rank, so $\|\hat P_N^+\|\gtrsim\sqrt N$. Three tools: block perturbative expansion of the pseudoinverse, a Gaussian (Wishart) reference model, and a rigorous bias + fluctuation + remainder decomposition (proved in supplement). Label noise added to model state-prep error. Simulations: Haar states, MUB measurements, $d=2..7$.

## Key results
- Ill-conditioning is unavoidable, but with exact targets the divergent block drops out of predictions.
- MSE $\approx b_N^2/N^2+V_N/(Nn_{\rm tr})$: a bias floor $\propto N^{-2}$ that more data cannot remove, and a variance term once $N\gtrsim n_{\rm tr}$.
- Bias = quantum errors-in-variables attenuation; $N^{-1}\Sigma$ acts as implicit Tikhonov regularization.
- Closed-form 2-design coefficients $\mathbb E[b^2],\mathbb E[V]\sim d^2$, matched by simulation.
- With noisy labels, "quantum overfitting": test error has a minimum in $N$ then grows linearly (ridgeless-like factor $(n_{\rm out}-d^2)/(n_{\rm tr}-n_{\rm out}-1)$).
- Budget should be a joint allocation between dataset size and shots per state. Code public.

## Limitations / open problems
Only the unregularized estimator; ridge/truncation left open. Analysis centred on QELMs (kernel extension stated as future work). Perturbative/Gaussian results not rigorous to all orders; rigorous result asymptotic in $n_{\rm tr}$. Simulation only, quantum-state inputs, achievable targets. Companion paper on sampling-driven double descent.

## Why it matters to me
Identifies shot-noise ill-conditioning as a structural cost of the non-variational models often pitched as the escape from barren plateaus — a genuine bottleneck result with real statistical-learning machinery (errors-in-variables, ridgeless regression). The "more data won't fix shot bias" lesson applies to any quantum-kernel pipeline on transaction data, even though no classical dataset is used here.
