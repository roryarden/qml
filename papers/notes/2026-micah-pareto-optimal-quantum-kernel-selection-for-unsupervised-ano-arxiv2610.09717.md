---
arxiv_id: 2610.09717
version: v1
title: "Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing data"
authors: [Boaz Micah, Nadia Milazzo, Maissa Beji, Borja Aizpurua, Llorenç Espinosa-Portalés, Esteban Payares, Ghada Ben Slama, Luc Andrea, Michel Kurek, Thomas Cope, Olivier Salomon]
primary_category: quant-ph
published: 2026-10-07
added: 2026-10-11
relevance: 5
tags: [kernel-methods, classical-data, qml-bottlenecks, security, benchmark, hardware]
full_text: ../md/2026-micah-pareto-optimal-quantum-kernel-selection-for-unsupervised-ano-arxiv2610.09717v1.md
---

## Problem
Judging quantum-kernel potential needs both task performance and how far the kernel's geometry departs from classical alternatives — usually reported separately. In unsupervised anomaly detection there are no labels to tune on. Can both be optimized jointly, label-free, on real cybersecurity data?

## Method
One-class SVM with fidelity or projected (PQK) quantum kernels over four generic encodings (Z, IQP-style, CNOT ladder, Hamiltonian evolution). Two objectives: normalised pseudo-discrepancy (NPD, label-free quality proxy) and geometric difference (GD) to a tuned classical RBF reference. NSGA-II Pareto search with knee-point selection, plus single-objective TPE runs. Data: Stratosphere normal + CTU-13 botnet beaconing flows, 6 unsupervised-selected features, 200 normal training flows. Statevector, IQM noisy sim, IQM 20-qubit Garnet QPU.

## Key results
- Classical baseline AUC 0.765. Best overall: NPD-selected fidelity kernel AUC **0.840**, but GD 4.30 < $\sqrt N=14.1$ — gain can't be certified as quantum.
- Projected kernels reach GD up to 272, but Pareto knee only AUC 0.782 (GD 88.6).
- Huge GD arises when large bandwidth pushes $K_Q\to I$ (memorisation regime) — reproducible by a re-tuned RBF. No systematic GD–AUC trend.
- Noisy sim: Pareto fidelity kernel most robust (0.798); deep IQP knee collapses to 0.647.
- Garnet QPU: AUC 0.532 (fidelity) / 0.612 (projected, $\nu$ tuned on test) — below classical.
- Conclusion: no kernel both departs clearly from classical and beats what classical could plausibly reach.

## Limitations / open problems
One dataset, $N=200$, 6 features ($O(N^2)$ circuit cost). Pareto fronts not converged. GD measured against one classical family. Generic encodings not designed for traffic. NPD weakly tracks AUC within a family. Basic mitigation, small shadows.

## Why it matters to me
Careful QML on real classical data with an unsupervised, rare-label setup structurally close to fraud detection; the NPD + GD Pareto protocol could transfer straight to transaction anomaly detection. The warning that large GD can be manufactured by bandwidth (kernel → identity) is a key bottleneck lesson for interpreting advantage claims.
