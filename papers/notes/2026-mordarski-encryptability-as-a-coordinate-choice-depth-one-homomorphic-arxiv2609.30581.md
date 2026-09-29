---
arxiv_id: 2609.30581
version: v1
title: "Encryptability As a Coordinate Choice: Depth-One Homomorphic Federated Learning of Quantum Neural Networks"
authors: [Marcel Mordarski, Nathan Mani, Arshad Patel, William Knottenbelt, Roberto Bondesan]
primary_category: quant-ph
published: 2026-09-24
added: 2026-09-29
relevance: 5
tags: [federated-learning, privacy, security, variational, theory, post-quantum]
full_text: ../md/2026-mordarski-encryptability-as-a-coordinate-choice-depth-one-homomorphic-arxiv2609.30581v1.md
---

## Problem
Homomorphic encryption (HE) needs low-degree server updates, but VQC weights are $\mathrm{SU}(2)$ rotations whose Euler-angle composition is transcendental. Existing QFL either sends plaintext updates (vulnerable to gradient inversion) or uses interactive blind delegation ($O(T)$ rounds) / Solovay–Kitaev compilation (>25k gates per rotation).

## Method
Represent each rotation as a unit quaternion: composition becomes the bilinear Hamilton product (degree 2, coefficients in $\{-1,0,+1\}$). Prop. 1: encrypted rotation update = 1 multiplicative level; weighted FedAvg = 0 levels; no bootstrapping (extends to any $\mathrm{Spin}(n)$ layer). One-exchange-per-round protocol: clients train in plaintext, sign-align and encrypt quaternions; server does a depth-0 blind sum; clients decrypt and recover angles. Quaternion one-time pad for rotations + Pauli one-time pad for Cliffords. Lemmas on mask placement, a chordal-vs-angle averaging bias bound ($-\tfrac1{24}\sum w_k\delta_k^3$), and exact entangler compilation. Experiments: 6-qubit, 6-layer VQC + classical head on California Housing and Wine Quality; LWE multi-key and CKKS backends; single-qubit round trip on IBM `ibm_fez`.

## Key results
- Aggregation error 0.0 rad (multi-key) and $-2\times10^{-12}$ rad (CKKS).
- Zero measurable utility tax: $\Delta=+9\times10^{-6}$ MSE, $p=0.92$ (paired, 5 seeds); 8-bit noise ablation shows encryption noise does **not** regularise.
- Averaging-bias bound tracks empirics (corr ≥0.999); at operating dispersion bias is 47× below the encryption noise floor.
- Hardware round-trip fidelity 0.9918 vs 0.99957 control (gap ≈ readout error).
- 1 exchange/round vs 37–73 for interactive baselines; scales to 20 clients.

## Limitations / open problems
Reported runs use a structural-verification lattice profile (not a security claim). Shared decryption keys among clients; poisoning undetectable under honest-but-curious model. Heavy bandwidth (22.67 MB/client/round) and encryption time (~167 s vs ~76 s training); loses to interactive protocols below ~100 Mbps. Encrypted CNOT ~1.5 h/gate. Small simulated models; a pure-quantum model failed to converge. No classical baselines, no advantage claim.

## Why it matters to me
Directly on quantum federated learning + privacy with genuine proofs, and a reusable principle (the group law decides encryption cost). Maps well to bank-consortium settings (server-blind aggregation of fraud signals) and touches post-quantum assumptions (LWE). Doesn't address QML performance bottlenecks and uses generic regression data.
