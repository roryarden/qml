---
arxiv_id: 2609.20594
version: v1
title: "Recursive Quantum Long Short-Term Memory for Stable Short-Horizon Temperature Forecasting"
authors: [Mu-En Lee, Yen-Ku Liu, Samuel Yen-Chi Chen, Yun-Cheng Tsai]
primary_category: cs.LG
published: 2026-09-17
added: 2026-09-21
relevance: 4
tags: [quantum-neural-networks, variational, trainability, classical-data, generalization, benchmark]
full_text: ../md/2026-lee-recursive-quantum-long-short-term-memory-for-stable-short-ho-arxiv2609.20594v1.md
---

## Problem

QLSTM models (LSTMs with variational quantum circuits replacing some gate
transformations) are expressive but their optimization is unstable — sensitive to
random initialization, circuit depth, expressibility, barren-plateau effects, and
the amount of temporal context. The paper asks whether a *recursive* QLSTM variant
yields more stable convergence, lower error, and better generalization than
standard QLSTM on a concrete short-horizon time-series task.

## Method

Empirical head-to-head comparison of standard QLSTM (Chen et al. 2022) vs.
Recursive QLSTM (the `MetaCore_Single_NN` configuration from Chen et al. 2026,
which reuses intermediate quantum feature representations across the recurrent
update). Task: one-step-ahead prediction of next-day min/max temperature from a
single Toronto weather station (1 May 2024 – 30 Apr 2026), 80/20 chronological
train/test split. Inputs are 8 continuous features (day-of-year sine/cosine, year,
mean/min/max temperature, heating/cooling degree days) scaled with training-set
statistics only. Shared config: QNN depth 1, hidden size 3, input projection 3, 6
qubits, window lengths $L\in\{8,16,32\}$, 60 epochs, batch size 8, learning rate
$5\times10^{-4}$, 20 seeds. Metrics: MAE, RMSE, P95 absolute error, $R^2$, absolute
bias, generalization gap (test − train loss), best-epoch, and $t_{95}$ (first epoch
reaching 95% of a run's total improvement). All circuits are simulated.

## Key results

- Recursive QLSTM reaches 95% of its eventual test-loss improvement in fewer epochs
  across all three windows (faster *early* convergence), though the epoch of the
  single minimum test loss is broadly comparable between models — no consistent
  best-epoch advantage.
- Accuracy (mean ± SD over 20 seeds, °C): at $L=8$, MAE 3.73±0.18 vs 4.08±0.24,
  RMSE 4.66 vs 5.15, $R^2$ 0.69 vs 0.625; at $L=16$, MAE 3.79 vs 4.14, $R^2$ 0.685
  vs 0.616; at $L=32$, MAE 3.84 vs 4.17, $R^2$ 0.681 vs 0.617.
- Recursive QLSTM keeps MAE below 3.9 °C at every window (vs ~4.1–4.2 °C) and has
  lower P95 tail error and absolute bias for both min and max targets.
- The generalization gap is smaller by roughly one-quarter to one-third at both best
  and final epochs, with narrower error bars (more repeatable across seeds),
  especially at $L=16$ and $L=32$.

## Limitations / open problems

Authors explicitly state results do **not** demonstrate a general quantum
advantage. Constraints: a single urban weather station, one forecasting horizon
(one-step), shallow *simulated* circuits (no noise/hardware), fixed
hyperparameters, and no strong classical baseline (a classical LSTM is not
benchmarked despite being the natural comparison). Longer windows may add
redundant/noisy seasonal information. Suggested future work: more stations, longer
horizons, noisy/missing-data settings, broader hyperparameter sweeps, stronger
classical baselines, NARMA-style benchmarks, and noisy quantum hardware.

## Why it matters to me

Direct hit on **QML-on-classical-data** and **trainability/practicality
bottlenecks** of VQC-based models — the paper's whole framing is stability across
seeds and generalization gap, which is exactly the "when does QML not fall over"
question. The 20-seed protocol and explicit generalization-gap reporting is
methodologically honest. Fit weaknesses: no finance/fraud angle (weather, not
payments — though the same authors' cited work touches fintech trading), no
rigorous theory or proofs (purely empirical, no barren-plateau analysis despite
citing it), and critically **no classical baseline**, so it cannot speak to genuine
quantum advantage. Useful as a data point on QLSTM stability engineering, not as
evidence of separation.
