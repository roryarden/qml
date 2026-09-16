---
arxiv_id: 2609.14131
version: v1
title: "Operator Learning with Variational Quantum Circuits"
authors: [Jorgen Wu, Masoud Barati, Peyman Givi]
primary_category: quant-ph
published: 2026-09-12
added: 2026-09-15
relevance: 4
tags: [variational, trainability, barren-plateaus, theory, generalization, qml-bottlenecks]
full_text: ../md/2026-wu-operator-learning-with-variational-quantum-circuits-arxiv2609.14131v1.md
---

> Note: the converted Markdown for this paper captured only the arXiv abstract page (title, authors, comment, abstract), not the full 67-page body / 22 figures. The summary below is grounded in that abstract; quantitative details (specific equations, bound constants, error values) are unavailable in the source and are flagged as such.

## Problem

The paper addresses how to make **variational quantum circuits (VQCs) learn solution operators to differential equations** — both linear and non-linear. The stated gap is bringing QML to **operator learning** (mapping input functions to solution functions of DEs) with favorable error/parameter scaling and without the trainability failures (barren plateaus) that commonly afflict QML.

## Method

- The authors **extend the DeepONet framework** by **replacing its branch and trunk neural networks with variational quantum circuits**.
- The construction leverages the **quantum universal approximation theorem** to justify VQCs as function approximators for the branch/trunk roles.
- A **theoretical framework of explicit error bounds** decomposes the total operator approximation error into **truncation, branch circuit, and trunk circuit** contributions.
- Bounds are derived in the $L^2$, $L^p$, $C^0$, and Sobolev $H^k$ norms, with a **classical–quantum comparative analysis** (Supplemental Materials).
- The method is **tested on several differential equations** (specific equations not present in the captured text).

## Key results

- The model achieves **low approximation and generalization errors even with shallow circuit depths** (specific values not in the available text).
- It **does not encounter barren plateaus during training** (abstract claim).
- It shows **improved error and parameter scaling relative to the classical DeepONet**.
- Claimed reason: the approximation error **depends on the dimension of the input function space rather than the number of sensor locations** — an intrinsic property distinguishing it from the classical DeepONet.
- Explicit error bounds quantify truncation, branch, and trunk contributions across the four norms.
- (Quantitative tables and the 22 figures referenced in metadata are **not present** in the supplied Markdown.)

## Limitations / open problems

- The abstract states no explicit limitations; failure-mode / noise / hardware sections are **not present in the available file**, so the authors' stated weaknesses cannot be reported.
- The barren-plateau-free claim and scaling advantages are asserted in the abstract but the supporting derivations/experiments cannot be verified from this file.
- The universal-approximation and error-bound arguments appear **theoretical / possibly simulation-based**; robustness on real quantum hardware under noise is not addressed in the available text.

## Why it matters to me

Two of my priority signals. First, it directly targets **QML bottlenecks / trainability** by claiming a VQC construction that **avoids barren plateaus** and offers **improved parameter scaling** — the core "what makes QML practical" question I care about. Second, it is **rigorous-theory-heavy**: explicit **error bounds decomposed by source and derived across $L^2$, $L^p$, $C^0$, $H^k$ norms**, plus a classical–quantum comparison, aligning with my interest in proofs and error/generalization bounds. The **generalization-error** claim at shallow depth is relevant to my sample-complexity / when-does-quantum-help interest. The fit to **finance/fraud/payments** and **classical-tabular-data** is **weak**: this is operator learning for differential equations (a scientific-computing / PDE-surrogate domain), not financial or classical-tabular classification. Value to me is mainly the **trainability and rigorous-bounds methodology**, which could transfer conceptually. Worth re-fetching the full text (the current `papers/md/` copy is abstract-only) to verify the barren-plateau-free and scaling claims.
