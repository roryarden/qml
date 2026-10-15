---
arxiv_id: 2509.16410
version: v2
title: "Does Data Complexity Predict Quantum Advantage? A framework, a pre-specified test, and an attribution of the measured edge"
authors: [Christophe Pere]
primary_category: quant-ph
published: 2025-09-19
added: 2026-10-11
relevance: 5
tags: [qml-bottlenecks, classical-data, benchmark, barren-plateaus, encoding, statistical-learning]
full_text: ../md/2025-pere-does-data-complexity-predict-quantum-advantage-a-framework-a-arxiv2509.16410v2.md
---

## Problem
Can a dataset's "data complexity" (entropy, correlation order, compressibility, topology) predict, before any training, whether a quantum model will beat classical ones? v1 claimed a composite score would rank the quantum edge, control barren-plateau onset and govern generalization; v2 corrects that framework and tests it under a pre-registered protocol.

## Method
Composite score withdrawn (unidentifiable weights; one component carried all variance) and replaced by a rank-normalized complexity vector plus an embedding-dependent interaction vector; corrected barren-plateau law; rebuilt topology estimator. Six pre-specified hypotheses — central H5: LODO $R^2\ge0.4$ on the budget-matched edge. 27 binary datasets (incl. credit default, breast cancer, Higgs, parity, spin glasses) × 10 encodings × 6 ansätze × 5 seeds = 8,100 cells, 8-qubit noiseless simulation. Primary comparator logistic regression; sensitivity vs an untuned best-of-six classical library. Parity-probe control.

## Key results
- **H5 fails:** pooled LODO $R^2=-0.32$ (GP), $-0.58$ (GBM); corrected topology doesn't rescue it.
- Edge tracks the baseline: vs LR $R^2=+0.13$ and quantum wins 17% of cells; vs best-of-six $R^2=-0.94$, win rate 1.1% (0% on parity).
- Quantum accuracy $0.481\pm0.069$, at chance in 81.5% of cells; ~82% of edge variance is the classical term; encodings/ansätze explain ~0.5% each.
- Preprocessing leaves ~0 nonlinear headroom (GBM ≈ linear probe).
- Gradient variance decays as $n^{-2.15}$ (power law, not exponential) up to 14 qubits.
- Designed parity control: +0.42 edge with a structure-aware measurement; generic ansätze stay at chance.

## Limitations / open problems
Narrow regime: one model family, $Z_0$ readout, noiseless, ≤14 qubits, 27 non-random datasets. Best-of-six is untuned and trains on raw features. Interaction vector effectively untested; no QRAM/quantum-native cells. The parity control is not a matched separation. Open: label–observable locality as a better axis; quantum-native data.

## Why it matters to me
A careful pre-registered null on real tabular data (incl. credit default) that shows how a weak LR baseline or classical preprocessing manufactures apparent quantum edges. Directly answers "where does QML not fail?" in the negative for standard tabular benchmarks. Adopt its habits: sweep classical baselines, decompose the gap into preprocessing vs residual, check the target actually varies.
