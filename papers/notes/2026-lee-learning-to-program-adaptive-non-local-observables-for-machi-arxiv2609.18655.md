---
arxiv_id: 2609.18655
version: v1
title: "Learning to Program Adaptive Non-Local Observables for Machine Learning"
authors: [Yu-Ting Lee, Samuel Yen-Chi Chen, Huan-Hsin Tseng]
primary_category: cs.LG
published: 2026-09-16
added: 2026-09-17
relevance: 4
tags: [qml-bottlenecks, variational, quantum-neural-networks, classical-data, benchmark]
full_text: ../md/2026-lee-learning-to-program-adaptive-non-local-observables-for-machi-arxiv2609.18655v1.md
---

## Problem
Quantum neural networks (QNNs) built from variational quantum circuits (VQCs) are constrained by **local measurements**, a stated bottleneck limiting how complex a data distribution they can learn. Adaptive non-local observables (ANO) make the measurement a trainable multi-qubit Hermitian operator, but existing ANO-based QNNs learn a **single static observable per task** that is fixed across all inputs. The paper asks whether the non-local observable can be made **input-conditioned** to improve QNN performance.

## Method
- **QFWP-ANO**: a hybrid model where a **classical hypernetwork** (encoder–decoder) reads each input and dynamically programs the VQC rotation angles $\theta$, the ANO observable parameters $\phi$, or both. A shared MLP encoder produces a latent $z$; a linear decoder emits $\theta$ and a two-layer MLP decoder emits $\phi$. Unlike the QFWP it builds on, it carries **no accumulated temporal state** — each input maps independently.
- **Circuit**: data re-uploading VQC (Hadamard init, then $D$ layers of $R_z, R_y$ rotations, circular CNOTs, $R_y, R_z$ re-uploading). A $k$-local observable $H(\phi)$ (a $2^k\times2^k$ Hermitian) is measured over all $\binom{n}{k}$ qubit subsets.
- **Variants**: QFWP-ANO-R (angles only), -O (observable only), -RO (both).
- **Tasks/data**: (1) multivariate time-series forecasting on four **ETT** datasets (7 variates, lookback 16, horizons 1–48), MSE/MAE, $n=7$ qubits, sweeping $D\in\{1,3\}$, $k\in\{1..7\}$; (2) **A3C reinforcement learning** on Acrobot and MiniGrid-SimpleCrossingS9N1, $n=4$ qubits, $D=4$, $k=3$. All averaged over 10 seeds. Baselines: MTSF-ANO, QuLTSF, QFWP, and linear DLinear/NLinear/Linear.

## Key results
- **Forecasting**: lowest MSE in **16 of 20** settings, second-lowest in the other 4; beats the static ANO baseline in **17 of 20**. Largest gains on ETTm1 (up to **6.6%**), growing with horizon. Programming the **observable** (O/RO) beats programming only angles (R) — the paper's central claim that input-conditioned *measurement* is the key lever.
- **RL**: all three variants clearly beat the ANO-VQC baseline on Acrobot (~episodes 1000–4000), with O/RO peaking earlier (better sample efficiency); QFWP-ANO-RO leads throughout on SimpleCrossingS9N1.
- **Ablation**: MSE minimized at **moderate non-locality $k\in\{2,3\}$** and rises sharply at $k=7$ (combinatorial scheme collapses to a single expectation); **shallower circuits ($D=1$) match or beat $D=3$** in most settings.

## Limitations / open problems
- **No theoretical analysis** — expressivity, generalization, and trainability (barren plateaus) are asserted informally, not proven.
- **Simulation-only**, no hardware, no noise study; scalability capped at 7 qubits.
- A **heavy classical hypernetwork** does much of the "programming," leaving open how much benefit is genuinely quantum vs classical.
- The **$k=7$ collapse** is a structural weakness of the combinatorial measurement scheme.
- Toy RL environments; ETT is sensor data, not financial/anomaly data.

## Why it matters to me
Moderate–good fit. It directly engages a **QML bottleneck** (measurement locality limiting VQC expressivity) and is **QML on classical data** (real multivariate time-series). Author affiliation (Wells Fargo, with disclaimer) is finance-adjacent, but the datasets are electricity-transformer sensors — no payments/fraud/anomaly angle — and the work is empirical/architectural with no rigorous theory and only modest edge over strong classical linear baselines. Speaks to practicality-engineering more than the theory or finance priorities I weight highest.
