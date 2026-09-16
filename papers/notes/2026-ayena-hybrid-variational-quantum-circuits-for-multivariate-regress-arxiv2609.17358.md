---
arxiv_id: 2609.17358
version: v1
title: "Hybrid Variational Quantum Circuits for Multivariate Regression and High-Dimensional Data Reconstruction"
authors: [Koffi Ognandon Ayena, Frédéric Holweck, Serge Iovleff, Amah S d'Almeida]
primary_category: cs.LG
published: 2026-09-15
added: 2026-09-16
relevance: 4
tags: [variational, quantum-neural-networks, classical-data, encoding, benchmark, theory]
full_text: ../md/2026-ayena-hybrid-variational-quantum-circuits-for-multivariate-regress-arxiv2609.17358v1.md
---

> Note: the fetched Markdown for this paper (via ar5iv) captured only the arXiv
> abstract page — the full body (Introduction, methods, theorem statements, result
> tables, ablation) did not render. The summary below is grounded strictly in the
> abstract; quantitative margins and theorem details could not be verified.

## Problem

Standard variational quantum circuits (VQCs) produce **scalar** outputs, so extending
them to **vector-valued (multivariate) regression** naively requires one independent
circuit per output dimension — a "linear overhead" the paper aims to remove. The targets
are multivariate regression and high-dimensional data reconstruction under this
constraint.

## Method

A **Hybrid Variational Quantum Circuit (HVQC)** extends a VQC with a **classical affine
post-measurement layer**, enabling vector-valued regression "without the linear overhead
of independent scalar circuits." Theoretically, the abstract claims **elementary one- and
two-qubit circuits can approximate quadratic functions and products via data re-uploading
and entanglement**, providing "the foundations of the full architecture." Evaluation uses
two synthetic image-reconstruction datasets and the **Friedman1 benchmark (40,568 test
samples)**; baselines are **Gaussian Process Regression (GPR), XGBoost, and Random
Forest**. An ablation varies the quantum vs. classical components. (Exact circuit depths,
qubit counts, feature-map form, and training details are not present in the fetched text.)

## Key results

Per the abstract: on the synthetic reconstruction datasets and Friedman1 the HVQC
**matches GPR** and **outperforms XGBoost and Random Forest**. The **ablation confirms
both quantum and classical components are essential**, and the results "highlight the
central role of the feature map in hybrid quantum-classical models." No concrete error
metrics (R²/MSE) are recoverable from the fetched text beyond the 40,568-sample Friedman1
test set.

## Limitations / open problems

- Fetched text lacks the Limitations/Discussion section, so author-stated weaknesses
  cannot be reported faithfully.
- Results rest on **synthetic image data and one synthetic tabular benchmark (Friedman1)**
  rather than real-world data.
- HVQC only **matches** GPR (a strong classical baseline) rather than beating it — no
  demonstrated advantage over the best classical method tested.
- The theoretical claim is scoped to **quadratic functions and products on elementary
  one-/two-qubit circuits**; scaling behavior is left open.
- The classical affine layer raises the (abstract-unaddressed) question of how much the
  quantum component contributes beyond the ablation's qualitative "essential" claim.

## Why it matters to me

Reasonable but partial fit. It is squarely **QML-on-classical-data** (tabular/synthetic
regression) with **explicit head-to-head classical baselines (GPR, XGBoost, Random
Forest)** — the honest comparison relevant to "where does QML not fail." The finding that
HVQC only *matches* GPR while beating tree ensembles is itself a data point on **QML
practicality/bottlenecks**. The claimed **theory on approximating quadratic functions via
data re-uploading + entanglement** touches the rigorous-theory interest, and the emphasis
on the **feature map's central role** connects to encoding bottlenecks. Weaknesses for my
interests: no finance/fraud application, no real-world data, and no demonstrated advantage
over the strongest baseline. The full paper body should be re-fetched to verify the theory
and numbers.
