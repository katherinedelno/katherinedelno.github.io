---
layout: page
title: Projects
permalink: /projects/
---
**RandomForestSpecCheck: A Permutation-Based Random Forest Diagnostic for LMMs** 03/2025 

Linear mixed models (LMMs) are a cornerstone of modern statistical analysis, but they can yield misleading inferences when key structure is omitted or misspecified. To address this, I developed a novel nonparametric diagnostic tool, RandomForestSpecCheck, which fits a random forest to the residuals of an LMM and uses within‐cluster permutation tests to assess leftover mean‐structure. In 5400 simulated datasets spanning 54 misspecification scenarios, the method controlled type I error below 3% and delivered over 90% power to detect both fixed‐effect and random‐slope violations. When applied to real-world data, it correctly confirmed well‐specified models and flagged a time‐omitted candidate, demonstrating its practical utility. Packaged as an R function, RandomForestSpecCheck returns both the observed statistic and permutation distribution alongside clear decision criteria, empowering analysts to rigorously validate and refine their mixed‐model fits. Additional details on the way. 
<br><br>

**A Conformal Prediction Framework for Multi-Label Movie Genre Classification** 03/2025 

Led development of a multi-label movie genre classifier by fine-tuning a lightweight transformer and integrating conformal prediction to produce calibrated sets of genre tags, striking an effective balance between capturing all relevant labels and avoiding spurious ones. Additional details on the way. 
<br><br>

**Fine-Tuning BERT Models for Recipe Classification: An Evaluation of Transformer-Based NLP Approaches** 02/2025 

Fine-tuned transformer-based NLP architectures to classify recipes by dietary category, leveraging transfer learning to capture rich culinary semantics and implementing an end-to-end ML workflow while embedding-driven feature engineering, hyperparameter optimization, and rigorous cross-validation to deliver a robust, generalizable classifier. Additional details on the way. 
<br><br>

**More projects to be added...**
