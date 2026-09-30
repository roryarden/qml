---
arxiv_id: 2207.08815
version: v1
title: "Why do tree-based models still outperform deep learning on tabular data?"
authors: [Grinsztajn, Oyallon, Varoquaux]
primary_category: cs.LG
published: 2022-07-18
added: 2026-09-29
relevance: 4
tags: [benchmark, classical-data, statistical-learning, encoding, generalization]
full_text: ../md/2022-grinsztajn-why-do-tree-based-models-still-outperform-deep-learning-on-t-arxiv2207.08815v1.md
---

## Problem
Tree ensembles like XGBoost are still the default for tabular data. Many new tabular NN papers claim to match or beat them, but those claims don't reproduce well, and there's no standard benchmark. The paper builds a reproducible benchmark that accounts for tuning cost, then asks *which inductive biases* make tabular data suit trees and not NNs.

## Method
- **Datasets:** 45 OpenML datasets.
- **Selection filters:**
  - heterogeneous columns
  - $d/n<1/10$
  - I.I.D. data
  - real-world data
  - at least 3k samples and at least 4 features
  - "not too easy": dropped if logistic regression is within 5% of both a default ResNet and a default HGBT
  - non-deterministic targets
- **Side issues removed:** train set capped at 10k (a 50k "large" regime is in the appendix), no missing data, balanced binary classes, categoricals with at most 20 levels.
- **Models:** RF, GBT/HGBT and XGBoost vs. MLP, ResNet, FT-Transformer and SAINT.
- **Tuning:** about 400 random-search iterations per model per dataset, starting from defaults. Test score of the best-on-validation configuration is reported as a function of budget, bootstrapped over 15 shuffles of the search order. Scores are aggregated with ADTM-style normalization (0 = 10%/50% error quantile, 1 = best). About 20k compute-hours; all raw search results are released.
- **Three probes** (numerical classification only):
  1. Gaussian-kernel smoothing of the training target
  2. Removing low-importance features, or adding Gaussian noise features
  3. Random rotations of the features

## Key results
- **Trees win at every search budget.** The gap stays wide after heavy tuning and grows when measured in wall-clock time. Categorical features explain only part of it.
- **Finding 1: NNs are biased toward smooth functions** (spectral bias). Smoothing the target clearly hurts trees and barely affects NNs, so the NNs weren't capturing the irregular part anyway. Example on *electricity*: RF 85% vs. MLP 80%.
- **Finding 2: tabular data has many uninformative features.** A GBT barely changes with up to 50% of features removed. Adding noise features widens the MLP/ResNet gap; removing them narrows it.
- **Finding 3: the column basis matters.** Ng (2004): a rotationally invariant learner's worst-case sample complexity grows at least linearly in the number of irrelevant features. Under random rotations only ResNet is unaffected, and the ranking **reverses** (NNs above trees).
- At 50k samples the gap seems to narrow; the authors call this preliminary.

## Limitations / open problems
- **Stated by the authors:** very small and very large data are unexplored, as are missing values and high-cardinality categoricals. Timing comparisons are rough.
- **My observations:**
  - Aggregate results are shown only as figures, with no significance tests.
  - Feature importance comes from an RF and is then evaluated with a GBT (mild pro-tree circularity).
  - The curation (balanced classes, no missing values, I.I.D.) excludes traits typical of payments data.

## Why it matters to me
No quantum content, but it effectively defines a credible classical baseline for any QML-on-tabular claim: **tuned** XGBoost/RF, matched tuning budgets, and results shown as budget curves.

My QML inferences (not claims made by the paper):
- **Rotation invariance and encodings:**
  - The amplitude-encoding fidelity kernel is exactly rotation-invariant, which the paper argues is the wrong bias for tabular data.
  - Per-feature angle/ZZ encodings keep the column axes.
  - PCA-before-encoding is exactly the rotation that erased the tree advantage, so trees should also be reported on raw features.
- **Smoothness of VQCs:** few-re-upload VQCs are band-limited Fourier series, arguably even smoother than MLPs. Running the paper's smoothing probe on a VQC or quantum kernel is a cheap diagnostic.
- **Feature selection:** selecting features (inside CV) before one-qubit-per-feature encoding saves qubits and may improve accuracy.
- **Fraud data:** imbalance, drift, and high-cardinality categoricals mean this protocol needs extending before it can benchmark quantum fraud models.
