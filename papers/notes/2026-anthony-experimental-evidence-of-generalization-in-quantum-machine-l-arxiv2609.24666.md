---
arxiv_id: 2609.24666
version: v1
title: "Experimental evidence of generalization in quantum machine learning in small-data regime"
authors: [Leena Anthony, Artemiy Burov, Nicolas Piro, Matteo Dal Peraro, Clément Javerzac]
primary_category: quant-ph
published: 2026-09-21
added: 2026-09-29
relevance: 4
tags: [generalization, encoding, qml-bottlenecks, classical-data, quantum-neural-networks, statistical-learning]
full_text: ../md/2026-anthony-experimental-evidence-of-generalization-in-quantum-machine-l-arxiv2609.24666v1.md
---

## Problem
Caro et al.'s bounds ($O(\sqrt{T\log T/N})$) suggest QCNNs, with $O(\log n)$ parameters, can learn from few samples — but were shown on quantum data. Does a hardware-compatible QCNN generalize from few *classical* images, what blocks scaling, and is parameter-efficient learning an advantage? (No advantage claimed.)

## Method
Cong–Choi–Lukin QCNN as a Qiskit dynamic circuit (shared two-qubit conv kernels, mid-circuit-measurement pooling with feed-forward, final $SU(4)$); 45 params / 6 qubits (8×8) and 57 / 10 qubits (28×28). Amplitude (QPIE) encoding. Datasets: sklearn digits 0 vs 1 ($N=2$–80, FakeKyiv noise, 4,000 shots, finite-difference gradients) and BreastMNIST ($N=20$–294, exact statevector). Baselines: parameter-matched CNN, 25,666-param CNN, LR, SVMs, kNN, PCA+LR, MLP. Transpilation study of amplitude vs angle encoding from 2×2 to 512×512 on FakeKyiv.

## Key results
- Digits: ~0.94 test acc. at $N=10$, plateau ~0.95; generalization gap $4\times10^{-2}\to10^{-3}$ at $N=80$.
- Parameter-matched classical CNN stays at chance on both tasks; QCNN learns.
- But strong classical models win everywhere: RBF-SVM >0.98 by $N=5$; on BreastMNIST all standard classical models beat the QCNN (QCNN balanced acc. 58.6–62.0% vs large CNN ~74% at $N=294$).
- 512×512: amplitude encoding 18 qubits but depth $1.9\times10^6$; angle encoding depth ~6,143 but 262,144 qubits. **Encoding, not optimisation, is the scaling barrier.**

## Limitations / open problems
All simulated ("Experimental" = numerical). Only $N$ varied — doesn't test the $\sqrt T$ / $\log M$ dependence of the bounds. Easy datasets; only win is parameter efficiency at matched architecture. QCNN classical-simulability results cited. Encoding bottleneck measured, not solved (patch/hybrid encodings proposed).

## Why it matters to me
Honest, quantified evidence that data loading is the bottleneck, with proper classical baselines — useful negative evidence for "datasets where QML doesn't fail." Small-sample regime loosely echoes rare-fraud settings (not claimed). Good statistical-learning framing, no new proofs.
