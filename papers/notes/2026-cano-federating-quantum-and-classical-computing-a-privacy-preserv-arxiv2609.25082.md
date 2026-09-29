---
arxiv_id: 2609.25082
version: v1
title: "Federating Quantum and Classical Computing: A Privacy-Preserving Hybrid Approach"
authors: [Carlos Cano, Daniel M. Jimenez-Gutierrez, Diego Sal, Georgios Kellaris, Joaquin del Rio, Oleksii Sliusarenko, Xabi Uribe-Etxebarria]
primary_category: cs.LG
published: 2026-09-18
added: 2026-09-29
relevance: 4
tags: [federated-learning, privacy, variational, encoding, benchmark]
full_text: ../md/2026-cano-federating-quantum-and-classical-computing-a-privacy-preserv-arxiv2609.25082v1.md
---

## Problem
Can two parties holding different features for the same samples (vertical FL) collaborate without centralising data when only one has a quantum model — and does the quantum model stay parameter-efficient? Prior vertical QFL needs quantum hardware at every party; prior mixed studies are horizontal and lack privacy mechanisms.

## Method
Vendor paper (all authors Sherpa.ai). Active party (features $x_1,x_2$ + labels) runs a hybrid 2-qubit model; passive party ($x_3,x_4$) runs a random forest. **Sherpa.ai Blind VFL (SBVFL):** passive party trains on synthetic targets ($Q$ per class) and is contacted twice; privacy analysis deferred to separate work. Synthetic **SMPP** benchmark: $y=\mathbb 1[\sin x_1\sin x_2+\sin x_3\sin x_4>0]$ with 5% label noise (ceiling 0.95), deliberately matched to $Z\otimes Z$ product-of-cosines structure. Baselines: ReLU MLPs (41–1201 params), 300-tree RF. Exact statevector, 10 seeds.

## Key results
- Local (active party only): hybrid 0.7227 (10 params) ≈ MLP 0.7223 (41 params); information-limited.
- SBVFL: hybrid **0.8757** (12 params) vs best MLP 0.8623 (1002 params) vs RF 0.8065.
- Centralised (non-private): hybrid 0.9216 (19 params) vs MLP 0.8663 vs RF 0.8462.
- $Q$ ablation non-monotonic; $Q=1$ best by 0.017.

## Limitations / open problems
Parameter-efficiency advantage holds for a target built to match the circuit's inductive bias; no general advantage claimed. Classically simulable 4-qubit circuit; no network/runtime measurements; no quantified privacy guarantee or privacy–utility curve. Federated gain confounded with platform components. One synthetic benchmark. Summarizer notes: no Fourier-feature classical baseline, and server/passive-party params excluded from the 12-param count.

## Why it matters to me
Vertical FL with quantum at only one party mirrors a realistic issuer/acquirer/merchant setting, and it's on my federated-learning + privacy interests. But synthetic data built to favour the quantum model, informal theory, and vendor self-evaluation — treat as a design pattern, not evidence.
