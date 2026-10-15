---
arxiv_id: 2610.00841
version: v1
title: "Neural Fourier Surrogates for Data Reuploading Quantum Neural Networks"
authors: [Oliver Knitter, Jonathan Mei, Sang Hyub Kim, Chi Chen, Masako Yamada, Martin Roetteler]
primary_category: quant-ph
published: 2026-09-30
added: 2026-10-11
relevance: 5
tags: [quantum-neural-networks, variational, encoding, classical-data, benchmark, qml-bottlenecks]
full_text: ../md/2026-knitter-neural-fourier-surrogates-for-data-reuploading-quantum-neura-arxiv2610.00841v1.md
---

## Problem
Comparing QNNs to MLPs/SVMs/tree ensembles says little about the classical–quantum boundary because the function classes differ. A data-reuploading QNN computes a finite Fourier series with frequency support set by the encoding and reupload count $L$. Can a classical model learn over that same support, giving a same-function-class baseline?

## Method
Neural Fourier Surrogates (NFS): learn $\omega\mapsto f_\theta(\omega)$ over the QNN's frequency set, evaluated stochastically as $\|f\|_1\mathbb E_{\omega\sim|f|}[e^{i(\phi(\omega)+\omega\cdot x)}]$. Autoregressive transformer modulus network (exact sampling), odd phase network, log-derivative gradients, importance-sampled reuse, Gaussian frequency prior. Compared with a PennyLane angle-encoded reuploading QNN (width 10), MLP/SVM/RF/XGBoost/LightGBM and Random Fourier Features on 15 OpenML/UCI tabular datasets (5 seeds), plus synthetic targets from random QNNs.

## Key results
- NFS broadly competitive but never best (e.g. Wine 0.983 vs SVM 0.989; Letter 0.822 vs LightGBM 0.961; Glass 0.567 vs RF 0.791); drops on higher-dimensional data.
- Accuracy vs training size: NFS ≈ QNN ≈ RFF qualitatively; NFS generally ahead of the QNN (attributed to fixed QNN observable).
- Varying encoded dimension 4–12: QNN generally ahead of NFS; both insensitive — the linear dimension reduction is the bottleneck.
- Learned spectra vs data-generating QNN: bimodal correlation (near 1 or 0).
- $L=1$ best; Gaussian prior helps; low learning rates collapse.

## Limitations / open problems
NFS is strictly more expressive than a fixed-observable QNN; no parameter-matched comparison. Higher training cost (unquantified). Order-dependent autoregression; biased gradient estimator. Noiseless small-scale single-ansatz QNNs only. No theory. AI-assisted code/ideation disclosed.

## Why it matters to me
Gives a principled classical comparator for reuploading VQCs on tabular data — exactly what's needed to tell whether a QNN result on a fraud or tabular dataset is genuinely quantum or matched by a Fourier model. Fits the dequantization/surrogate line. Light theory, no finance data.
