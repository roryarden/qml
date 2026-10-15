---
arxiv_id: 2610.04190
version: v1
title: "Reduced Cost Quantum Kernel Training"
authors: [Daniel R. Germain, Benjamin Goldweber, Kayla J. Rodriguez, Kristen Rhinehardt]
primary_category: quant-ph
published: 2026-10-03
added: 2026-10-11
relevance: 5
tags: [kernel-methods, kernel-concentration, qml-bottlenecks, fraud, classical-data, benchmark]
full_text: ../md/2026-germain-reduced-cost-quantum-kernel-training-arxiv2610.04190v1.md
---

## Problem
Non-variational quantum kernels are expensive: $O(N^2)$ Gram evaluations on hardware, huge shot counts if kernels concentrate, and no rule for picking feature maps. Is one-class (nominal-only) anomaly detection a regime where these costs become manageable?

## Method
ULB Credit Card Fraud dataset, PCA to 1–20 qubits; fixed 2,000-sample test set (5% anomalies); nominal-only training sets of 500–4k drawn via K-means strata, 12 seeds. Fidelity kernels: angle encoding (AE, classically closed-form control), modified ZZ, ZZ with random re-uploading layers (ZZ-R); classical RBF baseline. Detectors: OC-SVM and per-feature reconstruction QSVR. Power-law fits $\mathrm{AP}(N)=A-B/N^\alpha$, concentration statistics, Nyström approximation with 5–350 landmarks. Noiseless GPU simulation.

## Key results
- Diminishing returns: 500-sample models keep 89.8–93.2% of fitted asymptotic AP; all $0<\alpha<1$.
- At 20 qubits/4k: AE-OC-SVM best (AP 0.849), RBF-OC-SVM 0.842, ZZ-R-OC-SVM 0.841 — classical/classically-simulable kernels win.
- No severe concentration up to 20 qubits (ZZ median 0.112; ZZ-R less concentrated than ZZ despite more depth).
- Nyström with 5 landmarks: QSVR keeps 94–97% of exact AP; OC-SVM degrades unpredictably.
- ZZ-QSVR: kernel evaluations 7.998M → 2,485 (>3,200×) for AP 0.812 → 0.737; illustrative IonQ cost \$1.34B → \$417k.

## Limitations / open problems
Noiseless only. Saturation thresholds extrapolated below 500 samples. Concentration explanation untested; input-scaling $\eta$ and SVM hyperparameters unreported (could drive low concentration). Landmark selection unspecified; inference cost ignored; single dataset. No advantage claimed.

## Why it matters to me
QML on the canonical credit-card fraud benchmark with a concrete recipe (small one-class training set + Nyström) attacking the quadratic-Gram and dollar-cost bottleneck. Also honest evidence that, here, classical RBF and classically computable kernels match or beat the quantum ones — useful calibration for "where QML doesn't fail."
