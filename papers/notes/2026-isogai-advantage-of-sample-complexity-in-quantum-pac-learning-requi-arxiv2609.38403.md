---
arxiv_id: 2609.38403
version: v1
title: "Advantage of Sample Complexity in Quantum PAC Learning Requires Inverse Access to State-Preparation Unitaries"
authors: [Natsuto Isogai, Satoshi Yoshida, Mio Murao]
primary_category: quant-ph
published: 2026-09-29
added: 2026-10-11
relevance: 5
tags: [theory, statistical-learning, generalization, encoding, qml-bottlenecks, classical-data]
full_text: ../md/2026-isogai-advantage-of-sample-complexity-in-quantum-pac-learning-requi-arxiv2609.38403v1.md
---

## Problem
In quantum PAC learning, copies of the quantum example state give no asymptotic sample advantage over classical PAC learning, while access to the state-preparation unitary $U$ *and* $U^\dagger$ improves realizable accuracy dependence to ~$1/\sqrt\varepsilon$ (Salmon et al.). Does forward-only access to $U$ help?

## Method
Worst case over compatible unitaries and ambient dimension $N$. Reduction theorem: for $|\psi\rangle$ in a known $r$-dim subspace with a Haar-random completion of $U$, the averaged output of any adaptive $q$-query forward-only algorithm is approximated by a channel on $q$ copies, error ≤ $q(r-1)/(N-1)$. Proof via block decomposition of $U$, phase averaging, SWAP-in of fresh copies and a "monitored experiment" bound. Padding $N$ transfers known copy lower bounds to forward-query learners. Purely theoretical.

## Key results
- Realizable forward-only query complexity $\Theta((d+\log(1/\delta))/\varepsilon)$; agnostic $\Theta((d+\log(1/\delta))/\varepsilon^2)$, $d$ = VC dimension.
- Achieved by just measuring $U|0\rangle$ and running a classical learner → no asymptotic advantage over classical samples or copies.
- Inverse access is therefore essential for the known realizable improvement.
- New reduction uses only $q$ copies (vs $O(q^2/\eta)$ in Tang–Wright–Zhandry), enabling lossless transfer of lower bounds.

## Limitations / open problems
Relies on worst case over $N$; for fixed low dimension, forward-only tomography can beat $1/\varepsilon$ at worse $d$-dependence. Optimal agnostic complexity with inverse access open. Query counts only, not runtime; adversarial Haar completions.

## Why it matters to me
Tight VC-dimension sample-complexity results — squarely statistical learning theory for QML. Practical reading: loading classical data through a forward state-prep circuit buys no sample efficiency over measuring and learning classically; any data-efficiency advantage needs coherent inverse access, which is costly. A useful caution against "quantum data advantage" claims.
