---
arxiv_id: 2207.01848
version: v6
title: "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second"
authors: [Hollmann, Müller, Eggensperger, Hutter]
primary_category: cs.LG
published: 2022-07-05
added: 2026-09-29
relevance: 3
tags: [classical-data, benchmark, statistical-learning, generalization]
full_text: ../md/2022-hollmann-tabpfn-a-transformer-that-solves-small-tabular-classificatio-arxiv2207.01848v6.md
---

## Problem
GBDTs still lead on tabular classification, but reaching top accuracy takes costly per-dataset tuning or AutoML. The paper asks whether one pretrained Transformer can take the training set as input and predict test labels in a single forward pass, with no per-dataset fitting. The target is small, clean data: **≤1,000 training samples, ≤100 purely numerical features with no missing values, ≤10 classes**.

## Method
- **Prior-Data Fitted Network (PFN)** (Müller et al. 2022):
  - Trained offline to minimise cross-entropy on held-out points of synthetic datasets $D\sim p(D)$.
  - This approximates the Bayesian posterior predictive $p(y\mid x,D)\propto\int p(y\mid x,\phi)\,p(D\mid\phi)\,p(\phi)\,d\phi$.
  - Inference is pure in-context learning, with no gradient steps on the real data.
- **Prior:** a 50/50 mixture of structural causal models (SCMs) and Bayesian neural networks (BNNs).
  - Nearly all prior hyperparameters are themselves distributions, so the model marginalises over architectures.
  - Occam bias: graphs with few nodes and few parameters are more likely.
  - SCM graphs are MLP-shaped DAGs with dropped edges. Activations come from {Tanh, LeakyReLU, ELU, Identity}. Features and target are randomly chosen nodes.
  - Class labels come from cutting a continuous target at $N_c-1$ random bounds, which gives imbalanced multiclass tasks. Class order is then shuffled.
  - Refinements:
    - blockwise-correlated features
    - feature-importance weights and sparsification to make functions irregular
    - non-Gaussian inputs
    - 20% probability of categorical features
    - **no NaN handling: NaNs are replaced by 0**
- **Model:**
  - 12-layer Transformer (emb 512, FFN 1024, 4 heads), **25.82M params**.
  - Trained for **18,000 steps × 512 datasets** of size 1,024 in **20 h on 8× RTX 2080 Ti**.
  - Test tokens attend only to training tokens, so cost is $n^2+nm$ instead of $(n+m)^2$.
  - Fewer than 100 features are zero-padded and rescaled.
  - At inference, features are z-scored and Yeo–Johnson transformed.
  - The full TabPFN ensembles **32 passes** over feature/class-index rotations and power transform on/off.
- **Evaluation:**
  - Main set: the **18** purely numerical OpenML-CC18 datasets without missing values. The other 12 small CC18 datasets are in the appendix.
  - Protocol: 5 seeds, 50/50 splits, ROC AUC (OVO).
  - Baselines: KNN, LogReg, XGBoost, LightGBM and CatBoost (random search, 5-fold CV), plus AutoGluon and Auto-sklearn 2.0. Budgets from 30 s to 1 h.

## Key results
- **Table 1 (18 numerical datasets, 60-min budget), mean ROC AUC:**

  | Method | Mean ROC AUC |
  |---|---|
  | TabPFN | **0.934** |
  | TabPFN n.e. | 0.932 |
  | AutoGluon | 0.930 |
  | ASKL2.0 | 0.929 |
  | CatBoost | 0.924 |
  | XGBoost | 0.924 |
  | LightGBM | 0.920 |

  - Std is about 0.009.
  - Mean AUC rank: TabPFN 2.94 vs AutoGluon 4.0.
  - AutoGluon is slightly better on accuracy (0.881 vs 0.879) and cross-entropy (0.714 vs 0.716).
- **Speed:**
  - TabPFN without ensembling: **1.30 s CPU / 0.05 s GPU**. The 32-pass ensemble: 0.62 s GPU (37.6 s CPU).
  - Baselines use about 3,100–3,700 s.
  - The **230× (CPU) / 5,700× (GPU)** speedups compare against baselines at a 5-minute budget.
  - The 20 h pretraining cost is excluded.
- **All 30 CC18 datasets (with categoricals and missing values):** the edge disappears.
  - Mean AUC: TabPFN 0.894, AutoGluon 0.895.
  - AutoGluon vs TabPFN on AUC: 13/4/13 (win/tie/loss).
  - AutoGluon wins 20 of 30 on cross-entropy.
- **Statistical tests** (Wilcoxon, Holm correction):
  - Numerical data, fast regime (≤30 s): TabPFN significantly beats all baselines.
  - 1 h tuned regime: TabPFN is not significantly better than the AutoML systems after correction.
- **Ensembling:** TabPFN's per-dataset errors correlate weakly with GBDTs, so averaging it with AutoGluon gives the best ranks (AUC rank 2.67).
- **Length extrapolation:** trained only on ≤1,024 samples, it keeps improving up to 5,000 training samples. This is shown only as a figure.
- **Prior ablation (Table 4, smaller compute):**

  | Prior | Mean ROC AUC |
  |---|---|
  | BNN | 0.865 |
  | SCM | 0.881 |
  | SCM + BNN | 0.883 |

  The SCM prior is the main driver.
- **Grinsztajn et al. probes (App. B.3)**, run against untuned LightGBM and an sklearn MLP:
  1. **Irregular functions:** TabPFN fits fairly smooth functions because the prior prefers simple SCMs. It fits more complex ones as the number of samples grows.
  2. **Uninformative features:** adding shuffled copies hurts **TabPFN and the MLP**, while LightGBM stays flat. The worst case is *collins* (~0.98 vs ~1.0), which recovers to 1.0 using only the top 5 features.
  3. **Rotations:** only the MLP is invariant. GBDTs are very sensitive. TabPFN is less sensitive but still does better unrotated. The authors link its weakness with junk features to this partial rotation invariance (Ng 2004).

## Limitations / open problems
- **Stated by the authors:**
  - Attention is quadratic in the number of samples.
  - Hard limit of 100 features and 10 classes.
  - Weaker with categoricals, missing values and uninformative features.
  - Pure predict time is often slower than the baselines' predict step.
  - Results are aggregates, and some numerical datasets are poor (e.g. *pm10*).
  - Future work: scaling up, regression, out-of-distribution robustness, fairness, adversarial robustness, explainability.
- **My observations:**
  - Prior hyperparameters were chosen by looking at the same ~150 meta-validation datasets later reported as extra evidence (App. B.5), so those results aren't independent.
  - The headline margins are 0.002–0.014 AUC on 18 datasets, with std about 0.009.
  - Heavy class imbalance is never tested, and there is no PR-AUC.
  - Timing compares GPU TabPFN with single-CPU baselines, so the 230× CPU figure is the fairer one.
  - §6 says "0.4 s" while Table 1 says 0.62 s.
  - The abstract's "67 additional datasets" isn't clearly reconciled with the 149 validation datasets in the body.

## Why it matters to me
No quantum content. It sets the **classical bar for small tabular data**, which is exactly the regime most QML classifier and kernel papers test in.

My QML inferences (not claims made by the paper):
- **Baseline requirement:** a QML advantage shown only against untuned SVMs, MLPs or default XGBoost is weak evidence. TabPFN runs in under a second, so there's no excuse to leave it out next to tuned GBDTs and AutoGluon.
- **Inductive-bias checklist:** the Grinsztajn/B.3 probes (smoothness, junk features, rotations) are a cheap way to characterise angle-encoded VQCs and quantum kernels. Low error correlation with strong baselines, as TabPFN shows, is a realistic target for hybrid ensembles even without an outright win.
- **Amortised learning for QML:** prior-fitting moves training cost offline and does it once. Meta-training a circuit or quantum-attention model on synthetic SCM tasks, or using PFN-style priors to warm-start VQCs, might sidestep per-dataset barren-plateau and shot costs. This is speculative and untested here.
- **Payments/fraud:** heavy categoricals, missing values, many weak features, extreme imbalance and scale are all TabPFN's documented or untested weak spots. It is at most a quick baseline on small curated feature subsets. The credit datasets fit this picture: credit-g 0.789 vs AutoGluon 0.794, and credit-approval 0.932 vs 0.942.
