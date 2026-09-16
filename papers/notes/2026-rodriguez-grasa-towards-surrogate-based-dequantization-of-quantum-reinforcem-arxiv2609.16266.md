---
arxiv_id: 2609.16266
version: v1
title: "Towards Surrogate Based Dequantization of Quantum Reinforcement Learning"
authors: [Pablo Rodriguez-Grasa, Sofiene Jerbi, Mikel Sanz, Ryan Sweke]
primary_category: quant-ph
published: 2026-09-14
added: 2026-09-16
relevance: 5
tags: [theory, qml-bottlenecks, kernel-methods, encoding, statistical-learning, generalization]
full_text: ../md/2026-rodriguez-grasa-towards-surrogate-based-dequantization-of-quantum-reinforcem-arxiv2609.16266v1.md
---

## Problem

Whether PQC-based **quantum Q-learning** (a parameterized quantum circuit replacing
the neural network as the action-value approximator in deep Q-learning) offers a
genuine, provable advantage over classical methods on problems of practical
relevance is unresolved. Prior **surrogate-based dequantization** — constructing
efficient classical algorithms that match a variational quantum model's best
achievable performance — had only been established for supervised learning and
generative modelling. The paper asks whether that program extends to reinforcement
learning.

## Method

The authors work in a deliberately simplified RL setting: access to a **uniform
generative model** (Assumption 5.1) yielding i.i.d. state-action samples from
$U(\mathcal{S}\times\mathcal{A})$, idealizing sampling from a large experience-replay
buffer after sufficient exploration. They use the known fact that a Hamiltonian-encoded
PQC value model $f_\theta(s,a)=\langle 0|U^\dagger(s,\theta)V^\dagger(a)OV(a)U(s,\theta)|0\rangle$
is a **linear model in a finite Fourier feature map** $\phi_{\mathcal D}$ determined
solely by the data-encoding strategy $\mathcal{D}$. Hence the whole PQC model class
lies inside the RKHS $\mathcal{H}_{(\mathcal{D},w)}$ of a "PQC-inspired" reweighted kernel
$K_{(\mathcal{D},w)}(z,z')=\tfrac{1}{\|w\|_2^2}\sum_i w_i^2\cos\langle\omega_i, z-z'\rangle$.
The classical surrogate (Algorithm 1) is **kernelized Fitted Q-Iteration**: each
iteration forms Bellman targets $y_i=r_i+\gamma\max_a\hat Q_k(s_i',a)$ and solves an
$\ell_2$-regularized kernel ridge regression in $\mathcal{H}_{(\mathcal{D},w)}$, with
clipping to $[-V_{\max},V_{\max}]$. Efficient kernel evaluation is guaranteed by drawing
$w$ from a symmetric MPS of polynomial bond dimension, avoiding the exponential feature
dimension $M$.

## Key results

The dequantization notion is **relative-to-best** (Def. 2.2): match the best hypothesis
in the PQC model class — an agnostic-learning benchmark that upper-bounds any achievable
quantum advantage without characterizing the quantum optimizer. The main result,
**Theorem 7.8**, gives sufficient conditions under which Algorithm 1 is an efficient
PAC learner: with $m=\tilde{\mathcal{O}}(\mathrm{poly}(d_{\mathcal S},|\mathcal A|,1/\epsilon,1/\delta))$
samples and $K=\mathcal{O}(\log(1/\epsilon))$ iterations it returns, w.p. $\ge 1-\delta$,
a policy with $\mathcal{L}(Q^{\pi_K})\le\mathcal{L}(Q^*_{(\mathcal{D},w)})+\epsilon$. The
conditions are: uniform sampling (5.1); Bellman closure (7.1/Eq. 7.2), implying
$Q^*\in\mathcal{H}_{(\mathcal{D},w)}$ and $\mathcal{L}(Q^*_{(\mathcal{D},w)})=0$
(Cor. 7.3); bounded transition density $p_{\max}=\mathrm{poly}$ controlling the
concentrability coefficient $\phi_{U,U}\le\sqrt{|\mathcal A|\,p_{\max}}$ (7.4);
inverse-polynomial decay of ordered kernel weights $w_i^2/\|w\|_2^2\le C(i+1)^{-p}$,
$p>1$, forcing sublinear maximum information gain $\Gamma(m)=\mathcal{O}((m\log^{p-1}m)^{1/p})$
(7.5); encoding norms $N_{\max},\lambda_{\max}=2^{O(\mathrm{poly})}$ bounding the frequency
norm $L_{\mathcal D}$; and a problem-dependent **alignment** condition
$G_K=\max_k\|T\hat Q_{k-1}\|_{\mathcal{H}_{(\mathcal{D},w)}}=\mathcal{O}(\mathrm{poly})$.
Because $\mathcal{F}_{\Theta,\mathcal{D},O}\subset\mathcal{H}_{(\mathcal{D},w)}$ implies
$\mathcal{L}(Q^*_{(\mathcal{D},w)})\le\mathcal{L}(Q_{\theta^*})$, Theorem 7.8 yields
relative-to-best dequantization: whenever the conditions hold, **no exponential quantum
advantage is possible via quantum Q-learning in this setting**. The finite-sample
FQI-with-PQC-kernel bound is also offered as a standalone classical contribution.

## Limitations / open problems

- Results hold only under the **uniform generative-model idealization** (Assumption 5.1),
  not the standard RL setting with temporally correlated trajectory samples; presented as
  groundwork and heuristic motivation, not a full dequantization of RL.
- The **Bellman closure / realizability** assumption (7.1) is "somewhat restrictive" and
  generally fails for finite-dimensional PQC-RKHS; Appendix H sketches a relaxation at the
  cost of an extra approximation-error term.
- The **alignment condition** on $G_K$ is the most problem-dependent and **cannot be
  verified a priori** (knowing the optimal regression functions ≈ having solved the
  problem), and must hold **uniformly across all $K$ iterations** — strictly stronger than
  the single-target supervised analog (Remark 8.2). There is explicit tension between
  polynomial eigenvalue decay (7.5) and alignment, both defined through $w$.
- Excludes some general PQC models: trainable data-encoding, incompatible action
  observables with different spectra, and directly trainable output scaling.
- **No numerical experiments** — purely theoretical.

## Why it matters to me

A rigorous **theory-with-proofs** contribution squarely on **QML bottlenecks /
practicality**: it sharpens *where* variational QML (here quantum Q-learning) cannot beat
classical methods, operationalizing the payoff as concrete conditions on data encoding,
kernel-spectrum decay, and problem-structure alignment. The agnostic-learning /
relative-to-best framing, the RKHS-and-Mercer-eigenvalue machinery, and the finite-sample
PAC-style bounds tie QML directly to **classical statistical learning theory** — exactly
my interest in when quantum genuinely helps versus when a classical surrogate suffices.
Caveats for my angle: it is RL-focused (not finance/fraud or tabular classification) and
confined to an idealized sampling model, so direct payments relevance is weak — but the
dequantization methodology and the "alignment vs. spectrum decay" insight generalize to
the broader hunt for regimes where QML does not collapse to a classical kernel method.
