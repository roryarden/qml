---
arxiv_id: 2609.22822
version: v1
title: "From IceCube to IT-Sphere: A Hybrid Quantum-Classical GNN for Banking IT Root Cause Analysis"
authors: [Antonio Greco, Riccardo Paoletti, Roberto Cappuccio, Mario Onorato]
primary_category: quant-ph
published: 2026-09-19
added: 2026-09-29
relevance: 4
tags: [finance, classical-data, variational, quantum-neural-networks, hardware, trainability]
full_text: ../md/2026-greco-from-icecube-to-it-sphere-a-hybrid-quantum-classical-gnn-for-arxiv2609.22822v1.md
---

## Problem
Banking IT ops face streams of alarms; event-correlation tools cluster but don't trace causal chains, so root-cause analysis (RCA) is manual. Framed as graph reconstruction by analogy with IceCube neutrino events. Can a hybrid quantum–classical GNN do this and run on NISQ hardware?

## Method
Short QCE26 poster extended abstract. HQ-RCA: Union–Find alarm clustering + PCA → DynEdge GNN backbone (1031-dim node embedding) → linear+tanh → 4-qubit VQC (HEE2 encoding + RandomLayers, 12 params) → $\langle Z_0\rangle$ → softmax. Data: 13 months, ~13k alarm clusters from a major European bank; weak heuristic labels. Baselines: RF, XGBoost, standalone DynEdge, parameter-matched classical head. Dimensional Expressivity Analysis (Jacobian rank), readout comparison, layout-seed sweep, noise/shot sweeps, IBM Heron r2 (`ibm_fez`) without mitigation.

## Key results
- 2k subset: $F_1$ 0.931, AP 0.953, AUC 0.974; full 13k: $F_1$ 0.915 ± 0.017.
- Deployed readout is **rank-1** — optimisation collapses to a single angle; a 1-D grid scan reaches $F_1$ 0.925.
- Richer readouts raise rank (10) but not $F_1$; across 21 layouts rank (0–9) is uncorrelated with $F_1$ ($r=-0.08$).
- Parameter-matched classical head: $F_1$ 0.907 after recalibration (below VQC) but better AP/AUC (0.961/0.986). Standalone DynEdge matches on $F_1$ and leads on ranking.
- Hardware: $F_1$ 0.587 at τ=0.5, recovered to 0.915 by threshold recalibration; AP/AUC mostly preserved.

## Limitations / open problems
Weak labels, single-root-cause assumption, single split/seed. No advantage: classical models lead on ranking metrics. Quantum part is a thin 12-param head on a large classical backbone, effectively one parameter when deployed. Extended-abstract brevity; baseline numbers only in figures.

## Why it matters to me
Rare QML study on real bank data, with an honest "feasible, not advantageous" verdict. Illustrates the "thin quantum head on a classical model" pattern and how DEA exposes how little the quantum layer contributes. Hardware noise mainly shifts the decision threshold — a practical deployment lesson. Planned extension to mainframe transactions could edge toward payments.
