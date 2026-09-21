---
arxiv_id: 2609.21916
version: v1
title: "Asymptotics for Frequency Redundancies in Quantum Machine Learning Models"
authors: [Felix Paul, Bhilahari Jeevanesan, Peter Jung]
primary_category: quant-ph
published: 2026-09-18
added: 2026-09-21
relevance: 4
tags: [theory, encoding, trainability, qml-bottlenecks, variational, foundations]
full_text: ../md/2026-paul-asymptotics-for-frequency-redundancies-in-quantum-machine-le-arxiv2609.21916v1.md
---

## Problem

In Quantum Fourier Models (QFMs) — parametrized / data-reuploading circuits whose
output is a truncated Fourier series $f(x;\theta)=\sum_{\omega\in\Omega}c_\omega(\theta)e^{i\omega x}$ —
the *frequency redundancy* $r_\omega$ (the number of eigenvalue-difference
combinations producing a given frequency $\omega$) shapes both expressivity and
trainability. Prior work showed low-redundancy Fourier coefficients can vanish
exponentially in qubit count and that gradient magnitudes correlate with
redundancy. The paper asks: how is the redundancy profile $r_\omega$ determined by
the choice of eigenvalues of the data-encoding Hamiltonians, and what shape does
it take as the number of re-uploading layers $L$ grows?

## Method

Purely analytical (no experiments or datasets). The authors introduce a
generating-function formalism: encode the eigenvalue multiset $\Lambda^{(\ell)}$
of layer $\ell$ as $f^{(\ell)}(z)=\sum_{\lambda}z^{\lambda}$, so that
$\prod_\ell f^{(\ell)}(z)f^{(\ell)}(1/z)=\sum_\omega r_\omega z^\omega$ (Eq. 15–16).
Redundancies are recovered by contour integration around the unit circle via
Cauchy's formula, $r_\omega=\frac{1}{2\pi}\int_{-\pi}^{\pi} f(e^{i\theta})e^{-i\omega\theta}\,d\theta$
(Eq. 17). They apply this to (i) arithmetic-progression eigenvalues
$H=\mathrm{diag}(1,\dots,d)$, (ii) single-qubit Pauli-$Z$ encodings with
coefficients $a_k=2^{k-1}$, and (iii) the general case of an arbitrary but
layer-identical integer-eigenvalue Hamiltonian, using Laplace's method for the
large-$L$ asymptotics. Analysis is restricted to integer eigenvalues (with a
brief real-valued extension).

## Key results

- Arithmetic eigenvalues give an exact Dirichlet-kernel integral (Eq. 20); its
  large-$L$ limit is Gaussian,
  $r_\omega\sim d^{2L}\sqrt{\tfrac{3}{\pi L(d^2-1)}}\exp\!\big(-\tfrac{3\omega^2}{L(d^2-1)}\big)$
  (Eq. 23), with width scaling as $\sqrt{L}$. For $L=1$ the exact profile is a
  triangle function $r_\omega=d-|\omega|$ (Eq. 25).
- The single-qubit encoding with $a_k=2^{k-1}$ reduces to the *same*
  Dirichlet-kernel form (Eq. 33), because those eigenvalues are equidistant —
  again triangle at $L=1$, Gaussian for large $L$.
- **Central result (Eq. 38):** for *any* layer-identical integer-eigenvalue
  Hamiltonian, $r_\omega\sim\frac{d^{2L}}{\sqrt{4\pi L s^2}}\exp\!\big(-\tfrac{\omega^2}{4Ls^2}\big)$,
  where $s^2$ is the variance of the eigenvalue distribution. The Gaussian width
  is set solely by that eigenvalue variance and is independent of Hilbert-space
  dimension $d$.
- Random-walk interpretation: $h(\theta)^L$ is the characteristic function of an
  $L$-step i.i.d. walk over the eigenvalue set, so $r_\omega/d^{2L}$ is the walk's
  landing probability at $\omega$; the Gaussian follows from the central limit
  theorem. Implication: generic / unstructured encodings inherently bias the
  model toward low frequencies (which carry high redundancy) rather than treating
  all frequencies equally.

## Limitations / open problems

Results assume identical encoding Hamiltonians in every layer and integer
eigenvalues (with GCD of differences equal to 1 — argued WLOG via rescaling). The
expressivity/trainability link relies on prior-work assumptions (variational
blocks forming independent 2-designs) rather than being re-derived here. The work
is entirely analytic with no numerical or hardware validation of the downstream
training claims. The authors explicitly leave the **inverse design problem**
open: given a target (e.g. flat / unbiased) redundancy profile, find encoding
eigenvalues realizing it — related to the "turnpike problem." Whether a truly
unbiased QFM is achievable is stated as future work.

## Why it matters to me

Strong fit on the *rigorous theory* and *QML bottlenecks / encoding* axes. It
gives closed-form, CLT-grounded proofs that encoding choice mechanically induces a
low-frequency spectral bias — a concrete, actionable statement about why "generic"
data-loading hurts QFM expressivity and trainability, directly relevant to the
encoding-cost bottleneck. The generating-function / random-walk framing is a clean
statistical-learning-flavored tool for reasoning about model bias. Fit is weaker on
my applied interests: there is no classical-data experiment, no finance/fraud
angle, and no generalization-bound or sample-complexity result — it is foundational
theory about model construction rather than demonstrated advantage.
