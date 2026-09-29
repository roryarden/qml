---
arxiv_id: 2602.06699
version: v2
title: "Quantum Attention by Overlap Interference: Predicting Classical and Many-Body Quantum Sequences"
authors: [Alessio Pecilli, Matteo Rosati]
primary_category: quant-ph
published: 2026-02-06
added: 2026-09-29
relevance: 4
tags: [quantum-transformers, nlp, variational, encoding, theory, qml-bottlenecks]
full_text: ../md/2026-pecilli-quantum-attention-by-overlap-interference-predicting-classic-arxiv2602.06699v2.md
---

## Problem
Prior quantum attention/transformer proposals store predictions in amplitudes, requiring costly decoding into a classical loss, and leave the token embedding fixed and implicit — obstructing end-to-end training on near/mid-term hardware.

## Method
**Variational quantum self-attention (QSA):** amplitude-encoded tokens in superposition over time-steps; parameterised $V$ (values) and $W$ (queries/keys); attention weights from state overlaps $\langle\xi_j|W|\xi_i\rangle^p$; softmax replaced by a degree-$k$ kernel (mono-QSA $s^k$ or poly-QSA truncated $e^{\beta s}$ via LCU). Loss from just two all-zero projector expectations ($\mu$, $\zeta$). Constrained trainable embedding. No feedforward block. Statevector simulation ($T,d\le32$) on Penn Treebank next-token prediction and 4-qubit TFIM trajectories, vs softmax and polynomial-kernel classical "twins."

## Key results
- Thm 1: $\mathcal L_{\rm qsa}$ = Rényi-½ cross-entropy + norm-uniformity penalty (≡ −log fidelity of prediction and target superpositions).
- Thm 3: at fixed other params, phase alignment is the unique global min; all other critical points are strict saddles.
- Complexity: QSA $O(k^2Td\,C_{\rm ansatz}/(\epsilon^2\mu))$ vs classical polynomial-kernel twin $O(Td\,m_k)$, $m_k\sim d^k$; Thm 6 gives an advantage threshold on $\mu$.
- poly-QSA approaches softmax losses on classical text; mono-QSA lags. On quantum sequences both approach softmax as $k$ grows. Classical twins show a "favourable gap." Extrapolated advantage at $d\gtrsim119$.

## Limitations / open problems
No feedforward nonlinearity; softmax only approximated. Phase-landscape results assume fixed other params (joint training not covered). Advantage is conditional, extrapolated from $d\le32$, vs a narrow classical comparator, and excludes embedding cost. Simulation only; training-set loss only (no generalization); no BP analysis.

## Why it matters to me
Hits quantum transformers + quantum NLP with genuine proofs and addresses the readout/decoding bottleneck. The advantage story depends on amplitude-encoding cost and long sequences — ties back to the data-loading bottleneck. Weak evidence of QML success on classical data; no finance angle (transaction sequences would be a conceivable long-$T$ use case — my speculation).
