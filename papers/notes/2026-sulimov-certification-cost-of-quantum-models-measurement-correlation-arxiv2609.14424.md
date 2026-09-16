---
arxiv_id: 2609.14424
version: v1
title: "Certification cost of quantum models: measurement correlation, not parameter count"
authors: [Pavel Sulimov, Claude Lehmann]
primary_category: quant-ph
published: 2026-09-13
added: 2026-09-15
relevance: 4
tags: [qml-bottlenecks, theory, trainability, variational, statistical-learning, hardware]
full_text: ../md/2026-sulimov-certification-cost-of-quantum-models-measurement-correlation-arxiv2609.14424v1.md
---

## Problem

The paper addresses an accounting gap in variational quantum machine learning: researchers routinely report the Fisher-information geometry of a trained variational quantum model, but never quote the *shot budget* (number of circuit executions) needed to certify that geometry to a stated precision. Without that budget, "a reported geometry cannot be audited." The authors ask three ordered questions: (1) what does a stated geometry cost in shots at matched estimation quality; (2) is the widely-quoted cubic ($p^3$, where $p$ is parameter count) cost scaling a genuine law; and (3) if not, what physically decides which cost regime a device is in. They motivate urgency with a concrete number: budgeting $p^3$ instead of the measured $p^{1.966}$ on their product family overestimates the 256-qubit endpoint by a factor of ~600.

## Method

- **Object certified:** the empirical Fisher matrix $F=\tfrac{1}{B}\sum_i g_i g_i^{\mathsf T}$ of a layered hardware-efficient ansatz ($R_X$ encoding, then depth layers of $R_X(\theta)$ plus an entangler), observable the uniform mean $f=\tfrac1n\sum_q\langle Z_q\rangle$. Gradients via the two-term $\pm\pi/2$ parameter-shift rule.
- **Theory (Theorem 1, the certification cost law):** to certify $\mathbb E\lVert\hat F-F\rVert_F\le\varepsilon\lVert F\rVert_F$ under coordinate-wise parameter shift costs $B_Q=\Theta(Bp^2 V/(\varepsilon^2 G))$ executions, where $V=n^{-2}\sum_{q,q'}\mathrm{Cov}(Z_q,Z_{q'})$ is the *measured* readout variance (the full covariance sum, where entanglement enters) and $G=\lVert\nabla_\theta f\rVert^2$ the squared gradient norm. Uniform shot allocation is proven optimal within the coordinate-wise parameter-shift class (constructive upper bound + matching lower bound).
- **Accounting identity:** the fitted cost exponent equals $2+\tfrac{\mathrm d\log(nV)}{\mathrm d\log n}-\tfrac{\mathrm d\log(nG)}{\mathrm d\log n}+\mathrm{bias}$, i.e. the exponent is forced by how total readout variance and total signal scale with register size.
- **Circuit families:** product (no entangler), chain, ring, brickwork (light cone $2d+1$), and blocked (cone width exactly $L$ by construction).
- **Simulation:** exact state vectors to $n\approx24$, then a bounded-$\chi$ MPS backend (validated to $\sim1.5\times10^{-16}$). **Hardware:** mirror circuits (ideal output 1, zero ideal variance) on IBM Heron devices ibm_marrakesh, ibm_fez, ibm_kingston, in a $3\times3$ factorial over $(n,\text{depth})$ with six seeds.
- **Discipline:** 14 pre-registered checks (dated commits before data), interval-containment tests, no $P$-values; failures reported openly.

## Key results

- **One constant covers two families:** dividing out $pV/(\varepsilon^2 G)$ leaves a constant of 0.338 (entangling) vs 0.349 (product), a 3% difference; pooled CV drops from 1.466 (raw shots) to 0.283. Reproduces families whose $B_Q$ exponents differ by a full power of $p$: 2.856 vs 1.990.
- **Cubic is falsified:** the product family certified to $n=256$ gives an executions exponent of 1.966 (95% CI 1.934–1.997) vs prediction 1.990 ($R^2=0.996$); the value 3 lies far outside. The brickwork entangler falls from 2.853 (<10 qubits) to 1.715 (>64 qubits).
- **Cone mechanism:** the blocked entangler gives 1.984 at fixed cone width vs 3.034 at proportional cone. The accounting identity holds family-by-family to within 0.001 across 624 MPS cells. Conclusion: the cubic exponent is a *finite-size cone window*, not a law; a fixed device coupling map fixes the cone, so a cubic budget extrapolated from a small simulation overestimates a large machine.
- **Positional attenuation:** along a chain the count of parameters that measurably move the output saturates; median $|\partial_j f|$ collapses from $5.1\times10^{-4}$ ($n=16$) to the double-precision floor by $n=128$.
- **Hardware multiplier:** $\overline{1/\alpha^2}$ = 2.07× / 2.38× / 1.91× on the three devices. **Readout-weight optimization** (closed-form generalised eigenvector) cuts the measured shot budget by 2.67× on hardware over $n=4$–12.
- **Leakage angle:** because the bound "does not read intentions," $V/G$ is framed as a leakage-resistance parameter — any party with parameter-shift query access pays the same cost — though stressed this is *not* a model-extraction result.

## Limitations / open problems

- **Optimality is class-restricted:** Theorem 1's $\Theta$ holds only within coordinate-wise parameter-shift designs; a matched lower bound against joint single-copy / multi-copy strategies (e.g. classical shadows) is not established.
- **Simulator + 1D only:** scale results are MPS on one-dimensional families at depth 2; a 2D coupling map is not covered. The blocked family is classically easy (though the claim concerns measurement cost).
- **Thin hardware leg:** nine design points on one device with six-seed replication on a second; wide cluster-robust intervals.
- **14 registered checks did not all clear** (reported openly): the entangling $V=\Theta(1)$ prediction failed; the $\varepsilon$-exponent came out $-1.92$ vs $-2$; a "size-dependent noise floor" claim was retracted; deployable control variates and a readout-weight training speedup were falsified.
- The ring family above $n\approx80$ produces floating-point-noise gradients and is excluded.

## Why it matters to me

Strong fit for the **QML bottlenecks / practicality** and **rigorous theory** parts of my profile. It reframes a real practicality bottleneck — the *measurement / shot budget* — as the binding constraint, with a closed-form provable cost law (Theorem 1) plus matching lower bound. The deflationary message ("report $nV$ and $nG$ scalings separately, not a fitted cost exponent"; the cubic law is only a finite-size cone window) is exactly the statistical-learning-style accounting of quantum models I value, and the Fisher-geometry framing connects to sample-complexity thinking. The leakage-resistance angle ($V/G$, parameter-shift query access to a *deployed* model) has a security/privacy flavor relevant to payments, though the authors are careful it is not model extraction. Caveats: **no finance/fraud dataset and no direct classical-data advantage result** — the closest is Appendix A, where a quantum-inspired classical baseline wins on every target tested (used only to justify costing measurement rather than accuracy). Practicality/theory relevance high; finance and QML-advantage relevance weak.
