---
arxiv_id: 2609.21243
version: v1
title: "From Trainability Diagnostics to Optimization Claims: Boundaries and Controls in Variational Quantum Optimization"
authors: [Pilsung Kang]
primary_category: quant-ph
published: 2026-09-18
added: 2026-09-21
relevance: 4
tags: [trainability, barren-plateaus, optimization, variational, qml-bottlenecks, theory]
full_text: ../md/2026-kang-from-trainability-diagnostics-to-optimization-claims-boundar-arxiv2609.21243v1.md
---

## Problem

Barren-plateau (BP) diagnostics tell you whether informative gradient signal
*survives* as a variational quantum circuit scales, but surviving signal is not
the same as successful optimization. The paper targets this
"trainability–optimization gap": whether interventions and diagnostics that look
favorable on gradient-structure grounds actually convert into better optimization
(lower energy), or whether they merely change update geometry without any real
optimization benefit.

## Method

For a variational energy $E(\theta)=\langle H\rangle$ with a Pauli decomposition
$H=\sum_\alpha c_\alpha P_\alpha$, the author treats each coefficient-weighted
Hamiltonian-term gradient $\mathbf{g}_\alpha$ as a "task-like" component
(borrowing PCGrad gradient surgery from multi-task learning, but explicitly *not*
claiming VQA is literally multi-task). Step-level diagnostics
($S_{\mathrm{step}}, N_{\mathrm{eff}}^{\mathrm{step}}, U_{\mathrm{step}}, Q_{\mathrm{step}}$)
are defined along the actual update direction, yielding the exact bridge
$\mathbf{g}^{\top}\mathbf{u}=U_{\mathrm{step}}\sqrt{Q_{\mathrm{step}}}$. This is
then resolved into standard first-order geometry
($\sqrt{Q_{\mathrm{step}}}=G\nu A$, $U_{\mathrm{step}}A=G\cos\theta$), leaving a
single residual "term-space composition" coordinate $C=\log(|U_{\mathrm{step}}|/A)$.
Three update rules (vanilla gradient descent, blind deterministic Hamiltonian-term
PCGrad, and probe-gated LSO-PCGrad) plus three matched controls (norm-matched
PCGrad, grid-based LSO, norm-matched vanilla line search) are compared.
Experiments use exact statevector simulation of transverse-field Ising model
(TFIM, $h=1.0$) instances with a hardware-efficient ansatz (HEA) and a Hamiltonian
variational ansatz (HVA), across 4 system sizes ($n\le 10$), 3 depths, 30 seeds
(360 seed–condition cases), 100 steps, $\eta=0.05$. A prespecified adjudication
design fixes materiality / reproducibility criteria and estimability screening in
advance, using partial Spearman correlations of realized descent against
$(\nu,\cos\theta,C)$.

## Key results

- *Fixed-norm boundary (theory):* By Cauchy–Schwarz, at fixed state and matched
  update norm the raw gradient already maximizes first-order descent of the summed
  objective; no termwise reorganization can beat it at first order. So
  $U_{\mathrm{step}}$ and $A$ are not independent optimization axes.
- *Diagnostic–optimization mismatch:* Blind PCGrad substantially raises the
  signal-survival diagnostic $B_{\mathrm{eff}}$ (mean $\Delta B_{\mathrm{eff}}=+0.451$
  HEA, $+0.697$ HVA) while worsening final energy — worse in 7/12 HEA conditions
  and all 12/12 HVA conditions (mean $\Delta E_{\mathrm{final}}=+1.377$ HVA). So
  $\Delta B_{\mathrm{eff}}>0 \not\Rightarrow \Delta E_{\mathrm{final}}<0$.
- *LSO-PCGrad* improves energy (HEA $-0.626$, wins 242/360; HVA $-0.037$, wins
  263/360) *without* raising final-step $B_{\mathrm{eff}}$.
- *Association analysis:* After conditioning on standard first-order geometry, the
  residual composition coordinate $C$ shows no reproducible material incremental
  association with realized descent (0/12 material cells for most rule–ansatz
  combinations). The optimizer-relative norm $\nu$ shows positive material
  associations in some settings (18/18 material cells positive) but fails the
  prespecified cross-regime reproducibility bar (best case 8/12).
- *Matched controls:* Norm-matched PCGrad does not rescue final energy (worse than
  vanilla in 11/12 HEA, 12/12 HVA). In the matched-budget line-search comparison,
  vanilla-direction line search beats projected-direction LSO on energy —
  "practical separation" in HEA (+0.267, wins 267/360) and same direction but
  unresolved size in HVA (+0.034, wins 308/360). Conclusion: LSO-PCGrad's
  advantage comes from probe-based search and step-norm adaptation, **not**
  Hamiltonian-term projection.

## Limitations / open problems

Exact statevector only, $n\le 10$, fixed learning rate, no sampling / hardware
noise, so no asymptotic-scaling or noise-robustness claims. Results are specific to
the deterministic (order-dependent) Hamiltonian-term PCGrad variant and the capped
five-candidate probe design; they do not transfer to randomized PCGrad or general
line search. Projected updates depend on the chosen term decomposition. The role of
update norm is non-uniform across ansatz / size (no single mechanism). The
time-controlled post hoc analysis was estimable in only a minority of cells, so
within-trajectory association could not be cleanly separated from optimization
drift; the variation-budget observation ($\bar\rho_\nu$ correlating with $s_\nu$,
$r=0.739$) is descriptive only.

## Why it matters to me

Strong fit to "QML bottlenecks & practicality" and "rigorous theory." This is a
careful, proof-backed dissection of a trainability bottleneck — it directly warns
that BP / gradient-survival diagnostics (a big theme in QML) should not be read as
evidence of optimization benefit, and it demonstrates a rigorous methodology
(fixed-norm boundary, matched-norm and matched-budget controls, prespecified
estimability / reproducibility criteria) for evaluating new VQA optimizers
honestly. The negative result — that a plausible gradient-surgery intervention
gives no real benefit once you control for norm and search budget — is exactly the
kind of "don't fool yourself" rigor useful when judging QML advantage claims.
Weaker on the classical-data / finance / fraud axis: this is Ising-model VQE
optimization, no classical dataset or application angle.
