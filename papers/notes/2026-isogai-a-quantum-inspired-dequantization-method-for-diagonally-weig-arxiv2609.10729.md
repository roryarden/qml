---
arxiv_id: 2609.10729
version: v1
title: "A Quantum-Inspired Dequantization Method for Diagonally Weighted Matrix Functions: Application to Learning with Optimized Random Features"
authors: [Natsuto Isogai, Mio Murao, Hayata Yamasaki]
primary_category: quant-ph
published: 2026-09-09
added: 2026-09-15
relevance: 4
tags: [theory, kernel-methods, classical-data, statistical-learning, qml-bottlenecks]
full_text: ../md/2026-isogai-a-quantum-inspired-dequantization-method-for-diagonally-weig-arxiv2609.10729v1.md
---

## Problem

The paper asks whether a specific QML routine proposed as a *quantum-advantage candidate* can be simulated efficiently classically. The routine is the QSVT-based sampler for **learning with optimized random features** of Yamasaki et al., which claimed an exponential (superpolynomial in input dimension $D$) speedup "without sparsity and low-rank assumptions." Its core step applies the regularized inverse $\boldsymbol{\Sigma}_{\epsilon}^{-1}=(\epsilon\boldsymbol{I}+\sqrt{\hat{\boldsymbol{q}}^{(\rho)}}\,\boldsymbol{k}\,\sqrt{\hat{\boldsymbol{q}}^{(\rho)}})^{-1}$ on a space with $G^{D}$ basis states. Existing dequantization frameworks do **not** cover this case, because the classical input model does not supply sampling-and-query (SQ) access to the composite matrix that must be inverted — only to the diagonal factor $\sqrt{\hat{\boldsymbol{q}}^{(\rho)}}$, plus entry access to the kernel. Neither sampling-based (Tang-style) nor sparse-matrix (Gharibian–Le Gall) methods apply.

## Method

A general dequantization method for **diagonally weighted matrix functions** $f(\gamma\boldsymbol{I}+\boldsymbol{D}\boldsymbol{A}\boldsymbol{D})$, where $\boldsymbol{D}\ge 0$ is available through SQ access and $\boldsymbol{A}$ is Hermitian (possibly dense, full-rank) available only through entry queries.

The **diagonal-truncation** scheme: (1) draw $R=\lceil \frac{\|\boldsymbol{D}\|_{\mathrm F}^2}{\epsilon_D^2}\log(\cdots)\rceil$ samples from $\mathrm{SQ}(\boldsymbol{D})$ to recover, w.h.p., all "heavy" coordinates $H_{\epsilon_D}=\{i:d_i\ge\epsilon_D\}$ (count $\le\|\boldsymbol{D}\|_{\mathrm F}^2/\epsilon_D^2$); (2) form truncated $\widetilde{\boldsymbol{D}}$ on the recovered set $S$; (3) query $\boldsymbol{A}$ only on the $S\times S$ principal block, build $\widetilde{\boldsymbol{M}}_S=\gamma\boldsymbol{I}+\widetilde{\boldsymbol{D}}\widetilde{\boldsymbol{A}}\widetilde{\boldsymbol{D}}$, and compute $\boldsymbol{B}=f(\widetilde{\boldsymbol{M}}_S)$ by exact diagonalization; (4) output a sparse representation $\boldsymbol{N}$ equal to $\boldsymbol{B}$ on $S$ and $f(\gamma)$ elsewhere. Key structural fact: $\gamma\boldsymbol{I}+\widetilde{\boldsymbol{D}}\boldsymbol{A}\widetilde{\boldsymbol{D}}$ differs from $\gamma\boldsymbol{I}$ only on that block. Error analysis uses operator-norm perturbation + an operator-Lipschitz estimate (Aleksandrov–Peller) giving a $\log(1+s)$ factor.

Applied to optimized random features: $\boldsymbol{D}=\sqrt{\hat{\boldsymbol{q}}^{(\rho)}}$, $\boldsymbol{A}=\boldsymbol{k}$, $f(x)=x^{-1}$. The kernel is diagonalized by the DFT so each entry is estimable even though $\boldsymbol{k}$ is not directly queryable. Crucially, since $\hat q^{(\rho)}$ is a normalized probability distribution, $\|\sqrt{\hat{\boldsymbol{q}}^{(\rho)}}\|_{\mathrm F}=1$, so no dependence on $|\mathcal X|=G^D$ is introduced.

## Key results

- **Theorem 1 (diagonal-truncation approximation):** outputs $\boldsymbol{N}$ with retained block size $s\le \|\boldsymbol{D}\|_{\mathrm F}^2/\epsilon_D^2$ and, w.h.p., $\|f(\boldsymbol{M})-\boldsymbol{N}\|_{\mathrm{op}}\le C[1+\log(1+s)]L\nu$. Runtime scales as $\widetilde{O}[(\|\boldsymbol{D}\|_{\mathrm F}/\epsilon_D)^6\log(1/\delta_D)]$ times per-access costs.
- **Theorem 2 (classical optimized-feature sampler):** under matched oracle access and the $\boldsymbol{k}(0,0)=\Omega(1)$ assumption, a randomized classical algorithm produces one sample from $\mathcal D'$ with $d_{\mathrm{TV}}(\mathcal D_\epsilon,\mathcal D')\le\delta$, per-sample runtime $O[D\,\mathrm{polylog}\,G+\cdots]\times \widetilde O[(Q_{\max}^{(\tau)}/\epsilon)^{18}\delta^{-6}]$.
- **Consequence:** when $Q_{\max}^{(\tau)}/\epsilon=\mathrm{poly}(D)$ and $1/\delta=\mathrm{poly}(D)$, the classical sampler runs in time polynomial in $D$ and $\log G$. Since feature sampling was the only quantum component (coefficient fitting is already classical), **the proposed superpolynomial separation in $D$ disappears**.

## Limitations / open problems

- The quantum (linear) and classical (power-18 in $Q_{\max}^{(\tau)}/\epsilon$, power-6 in $1/\delta$) parameter dependences **do not match**, and the classical powers "are not claimed to be optimal."
- $\delta$ is the TV error of a *single* feature sample and "does not by itself determine the end-to-end statistical cost."
- Explicitly an **oracle-level dequantization**, not a new statistical learning method; guarantees hold under the matched oracle-access model.
- Assumptions carried over from Yamasaki et al. ($\boldsymbol{k}(0,0)=\Omega(1)$, the polynomial regimes) are required.
- Open direction: characterizing **more general factor-level access conditions** under which block-encoded composite matrices can be dequantized.

## Why it matters to me

Strong fit for **rigorous QML theory** and **QML-on-classical-data where an advantage gets dequantized away**. Learning with optimized random features was a headline example of a *provable exponential QML speedup without sparsity/low-rank assumptions* on a classical kernel-learning task — and this paper gives a proof-backed classical algorithm (operator-norm guarantees, explicit sample complexity) that removes the superpolynomial separation in input dimension. That directly informs the "which QML advantages survive under matched data-access?" question central to my thinking about QML practicality and bottlenecks. The technique — exploit the *factorization structure* ($\boldsymbol{D}\boldsymbol{A}\boldsymbol{D}$ with a normalized probability diagonal) rather than needing SQ access to the whole matrix — sharpens my intuition about when kernel/random-feature methods on classical data are genuinely quantum-hard vs classically tractable. The fit to **finance/fraud** is weak: random features and KRR are used in finance, but this is pure algorithm theory with no financial application, datasets, or empirical evaluation.
