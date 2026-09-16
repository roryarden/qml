---
arxiv_id: 2609.11637
version: v2
title: "Certifying Adversarial Robustness of Quantum Classifiers under Known-Readout Query Access"
authors: [Ji Guan, Mingyu Huang]
primary_category: quant-ph
published: 2026-09-10
added: 2026-09-16
relevance: 4
tags: [quantum-neural-networks, security, theory, classical-data, fraud, benchmark]
full_text: ../md/2026-guan-certifying-adversarial-robustness-of-quantum-classifiers-und-arxiv2609.11637v2.md
---

<!-- v2 (2026-09-16): exposition/theory refinement over v1 — tighter derivation of the
upper-bound quantity $p_k$ and a new §6.1 discussion of the attack-vs-witness tradeoff;
no new experiments. Worked Example 5.4: $\varepsilon_{\mathrm{RLB}}\approx7.21\times10^{-3}$
vs prior $2.55\times10^{-3}$, exact QCQP radius $1.20\times10^{-1}$ inside the sandwich
$[7.21\times10^{-3},\,3.68\times10^{-1}]$. -->

## Problem

The paper addresses **certified adversarial robustness of quantum classifiers** in a realistic deployment setting where the classifier is accessed remotely. Quantum classifiers are vulnerable to small input perturbations (in fidelity distance) that flip the predicted label. Prior robustness methods assume **white-box access** (unitary $U$, parameters, gradients), which the authors argue "rarely holds in practice" for proprietary/remote execution and cannot be reconstructed cheaply (process tomography is "generally prohibitive"). Core question: can one *formally certify* robustness of a deployed quantum classifier using only observable measurement statistics? They motivate it explicitly with **financial-transaction fraud detection**, where an adversarial flip from "fraudulent" to "legitimate" could evade review, or the reverse block a legitimate payment.

## Method

They define **known-readout query access (KRQA)**: the evaluator can prepare inputs, knows the readout POVM $\{M_k\}$, and observes finite-shot outcomes, but cannot inspect $U$, parameters, or gradients. A classifier is $\mathcal{Q}=(\mathcal{H},U,\{M_k\})$ predicting $\arg\max_k \mathrm{Tr}[M_k U|\psi\rangle\langle\psi|U^\dagger]$. The exact robustness radius $\varepsilon^*(\psi)$ is a nonconvex QCQP (NP-hard, white-box). Their framework produces a "**robustness sandwich**" $\varepsilon_{\mathrm{RLB}}\le\varepsilon^*\le\varepsilon_{\mathrm{RUB}}$:

- **Upper bound (attack witness):** define **POVM gap operators** $M_k-M_t=\Delta^+-\Delta^-$ and the **adversarial kernel space** $\mathcal{K}_{k\to t}=\mathrm{supp}(\Delta^+)$, intrinsic to the readout. Lemma 4.2 proves soundness/completeness. Bound $\varepsilon_{\mathrm{RUB}}=1-\max_k\sqrt{p_k}$ with $p_k$ estimated via a **binary projector measurement** (Algorithm 1). Attack-independent, always returns a witness.
- **Lower bound (safety certificate):** relax state-space search to an optimization **over outcome distributions** constrained by operator spectra. Using $F(\psi,\phi)\le\sum_j\sqrt{p_jq_j}$, optimize over a probability polytope with simplex constraint, adversarial condition $q_k\ge q_t$, and **spectral box constraints** $\lambda_{\min}(M_j)\le q_j\le\lambda_{\max}(M_j)$. Concave over a convex polytope; a scalar Lagrange dual (bisection) gives certified bounds (Algorithm 2). Dropping the spectral box recovers the prior probability-only bound of Guan et al. 2021, so this bound is provably **never weaker** and can be **strictly stronger**.

Both certificates have finite-shot guarantees ($N=O(\varepsilon^{-2}\log(C/\delta))$ shots), $O(Cd^3)$ one-time spectral preprocessing, $O(C^2L)$ per-input. Evaluation: variational QNNs on **MNIST (4-class), Fashion-MNIST (4-class), and a physics cluster-excitation classifier**, an untrained 30-qubit scalability run, vs a SciPy SLSQP white-box reference and random/FGSM/PGD attacks. A real-device PoC runs two 8-qubit binary QNNs on IBM Quantum hardware.

## Key results

- **Upper bound always non-trivial.** MNIST mean kernel upper bound 0.3166 (<1 on all 20 inputs). FGSM/PGD succeeded on only 75%/80% (MNIST), 30%/30% (Fashion-MNIST); on cluster-excitation **no attack found any witness**, yet the kernel bound stayed non-trivial — the certificate's value shows "when attacks fail."
- **Lower bound strictly improves prior work.** Under a spectral-box-active readout, mean proposed lower bound $6.16\times10^{-2}$ vs $6.05\times10^{-3}$ prior — **≈10.2× ratio**, strictly larger on all 20 inputs. On standard high-accuracy models the two coincide.
- **Tightness.** MNIST mean $\varepsilon_{\mathrm{RLB}}=0.0012$, white-box reference $0.0013$, $\varepsilon_{\mathrm{RUB}}=0.3166$; the reference lay between the two certificates on every input.
- **Scalability.** A 30-qubit QNN (MPS, 4096 shots) computed both certificates with correct ordering on all 20 samples.
- **Real hardware.** On `ibm_kingston`, two 8-qubit QNNs (MNIST 0-vs-1, Fashion-MNIST T-shirt-vs-Trouser), 40 circuits × 4096 shots, no mitigation. Accuracies 98.0%/90.5%; $\varepsilon_{\mathrm{RLB}}\le\varepsilon_{\mathrm{RUB}}$ on **every** tested input. A non-projective diagonal POVM implemented via classical post-processing ($\hat p=A\hat r$).

## Limitations / open problems

- **Certified readout must match deployed measurement.** Without trusted spectral info the box collapses to $[0,1]$ and only the weaker probability-only bound survives.
- **Upper bound is calibration-sensitive** when gap operators have near-zero eigenvalues; propagating calibration confidence regions is future work.
- **Access asymmetry:** the upper bound needs binary projector readouts; a label-only API supports only the lower bound.
- **Theory assumes unitary internal evolution** — does not certify arbitrary device noise or drift.
- **Hardware validation narrow:** one device, one calibration snapshot, binary tasks; intervals cover only sampling variability.
- Upper bound can be loose relative to successful attacks; statistics are conditional on retention and do not estimate population robustness rates.

## Why it matters to me

Strong fit. Sits at the intersection of **quantum classifiers**, **adversarial robustness/security**, and **rigorous theory** — the certificates come with soundness proofs, finite-sample guarantees, and a provable domination result over prior bounds. It directly and explicitly motivates the work with **payments/fraud detection**: an adversarial flip lets a fraudulent transaction "evade review or blocking," exactly my domain. It is genuinely **QML on classical data** (MNIST/Fashion-MNIST via PCA features) and touches a real **practicality bottleneck** — deployed quantum models are opaque/remote, so white-box verification is unrealistic — offering a query-access auditing primitive. The KRQA framing connects to the broader **security/data-privacy** angle I care about. Caveat: the finance motivation is illustrative rather than demonstrated (no financial dataset), and the method requires knowing the readout POVM, a non-trivial trust assumption for a third-party auditor.
