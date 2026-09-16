---
arxiv_id: 2503.21336
version: v4
title: "Few-sample regression with an adaptively grown variational quantum Kolmogorov--Arnold network"
authors: [Hikaru Wakaura, Rahmat Mulyawan, Andriyan B. Suksmono]
primary_category: quant-ph
published: 2025-03-27
added: 2026-09-15
relevance: 4
tags: [variational, quantum-neural-networks, kernel-methods, generalization, statistical-learning, benchmark]
full_text: ../md/2025-wakaura-few-sample-regression-with-an-adaptively-grown-variational-q-arxiv2503.21336v4.md
---

## Problem

The paper asks whether quantum Kolmogorov–Arnold networks (KANs) — architectures placing learnable one-dimensional functions on network edges — offer any *practical* benefit over classical or standard quantum baselines. The authors argue prior quantum-KAN claims are unreliable because they rest on "single optimisation runs, on quantum-neural-network baselines whose initialisation and depth were not tuned, on classical baselines without regularisation, and on test sets that were also used to pick the best epoch." The goal is a rigorous, leak-free, partly pre-registered evaluation of an Adaptive Variational Quantum KAN establishing "the resources and limits" of the approach.

## Method

- **Model:** An Adaptive VQKAN mapping $\mathbf{x}\in[0,1]^d$ to a scalar expectation $h(\mathbf{x};\boldsymbol\theta)=\langle\Psi|\hat H|\Psi\rangle$ on $N_q=\max(4,d)$ qubits. Angle-encoded inputs ($R_y$); a KAN layer applies $\exp(-i\pi\phi_p(\mathbf{z})P_p)$ where each edge function $\phi_p$ is a quadratic B-spline with $N_g=8$ learnable control values (8 params per operator).
- **Adaptive growth:** Starting from a single $X_1$ operator, every $T_g$ steps the pool of one- and two-body Pauli strings is scanned and the operator most lowering the *training* cost is adopted (ADAPT-VQE rule, cost replacing energy). Derivative-free COBYLA.
- **Baselines:** untuned + tuned QNN arms; classical regressors as a test-knowledge "oracle"; and regularised classical models tuned on training points only — ridge, **kernel ridge regression (RBF) with leave-one-out CV**, and a Gaussian process.
- **Targets:** five four-qubit synthetic regressions, plus a difficulty-controlled standardised family $\tilde f_d$ at $d=12,16,18$. Only $N=10$ training points, 50 test points.
- **Protocol:** seed-paired comparisons, model selection using only training cost (test set evaluated once), Wilcoxon signed-rank tests. The scaling claim was a **pre-registered confirmatory study** (four hypotheses, seeds 30–49, Holm correction, frozen analysis script committed before runs). Robustness via finite shots (256/1024/4096), depolarising noise, and execution on the 156-qubit IBM Heron `ibm_marrakesh`.

## Key results

- **Four qubits — no benefit:** on the main target the Adaptive VQKAN reaches $11.5\pm4.2$, indistinguishable from the equal-size QNN ($10.7\pm1.7$; $p\geq0.77$) and beaten by linear regression ($7.7\pm1.8$) and an MLP ($7.9\pm1.6$). On the exponential target it is worse than a constant predictor.
- **Pre-registered scaling — a real few-sample effect:** with 10 points, the 32-parameter model beats the classical oracle at $d=12$ (Holm $p=0.017$) and $d=16$ (Holm $p=0.004$), and beats the tuned QNN at $d=12$ on all 20 seeds. It **fails at $d=18$** ($p=1.0$).
- **But classically reproducible:** a cross-validated kernel ridge regressor matches it — $p=0.96$ at $d=12$; $13.7\pm3.2$ at $d=16$. Ridge, CV classical KAN, and the GP do not match.
- **Mechanism = implicit regularisation, not expressivity:** in a sample-size sweep at $d=12$, quantum error is nearly flat (11.3→9.5 as points go 10→100) while kernel ridge falls to $3.2$; the advantage vanishes by 20 points. Growth reliably adopts four operators (dominated by $XX$, $XY$), always ending at 32 parameters.
- **Robustness:** 256 shots do not degrade it; depolarising noise up to $p_2=0.03$ leaves trained-model error unchanged (shallow circuits, 2–6 $CZ$ gates). On IBM hardware, test errors differ from exact by ≤0.28; twelve-qubit runs claimed as the first hardware evaluation of a quantum KAN at that size.

## Limitations / open problems

- The benefit is **only implicit regularisation of a deliberately low-capacity model**, not a quantum expressivity/feature-space advantage.
- It is **absent at four qubits, gone with 20+ training points, and fails at $d=18$** (capacity ceiling).
- **Large circuit-evaluation budget:** 25,000–110,000 statevector preparations per run vs 10,000 for the QNN; ~$10^7$ shots per training run on hardware.
- **Fails at classification** (Appendix A): error rate equals majority voting while a QNN and SVM reach ~15%.
- Adding a second KAN layer *hurts* at four qubits. Whether a different encoding/readout or a genuinely KAN-suited target could beat the RBF kernel is left open.

## Why it matters to me

Strong fit. Squarely a **QML-on-classical-data** and **QML-practicality/bottleneck** paper that honestly hunts for the regime where a quantum model does *not* lose — and finds a narrow one (few-sample, moderate-dimension regression) while showing it is matched by a cheap cross-validated **kernel method**. That is exactly the "when does quantum actually help vs classical" question grounded in **statistical learning** (capacity, implicit regularisation, sample-size scaling) that I value, and the pre-registered, leak-free, tuned-baseline protocol is a model for skeptical QML benchmarking; the connection to the Schuld "quantum models are kernel methods" framing is directly relevant. Weaknesses for my purposes: **no finance/fraud/payments application** and synthetic targets, so the commercial angle is absent — but the methodological lesson (regularised classical baselines will often erase apparent quantum advantage) transfers directly to any payments-data QML claim I would scrutinize.
