---
layout: page
title: Projects
permalink: /projects/
---
**RandomForestSpecCheck: A Permutation-Based Random Forest Diagnostic for LMMs** 03/2025 

Linear mixed models (LMMs) are a cornerstone of modern statistical analysis, but they can yield misleading inferences when key structure is omitted or misspecified. To address this, I developed a novel nonparametric diagnostic tool, RandomForestSpecCheck, which fits a random forest to the residuals of an LMM and uses within‐cluster permutation tests to assess leftover mean‐structure. In 5400 simulated datasets spanning 54 misspecification scenarios, the method controlled type I error below 3% and delivered over 90% power to detect both fixed‐effect and random‐slope violations. When applied to real-world data, it correctly confirmed well‐specified models and flagged a time‐omitted candidate, demonstrating its practical utility. Packaged as an R function, RandomForestSpecCheck returns both the observed statistic and permutation distribution alongside clear decision criteria, empowering analysts to rigorously validate and refine their mixed‐model fits. Additional details on the way. 
<br><br>

**A Conformal Prediction Framework for Multi-Label Movie Genre Classification** 03/2025 

Led development of a multi-label movie genre classifier by fine-tuning a lightweight transformer and integrating conformal prediction to produce calibrated sets of genre tags, striking an effective balance between capturing all relevant labels and avoiding spurious ones. Leveraging DistilBERT for efficient contextual representation of movie text (title, overview, tagline), we fine-tuned the model end-to-end to maximize performance. To produce reliable genre predictions, we apply global conformal prediction using a sum-based non-conformity score, allowing us to generate prediction sets that maintain high empirical coverage (≥90%), ensuring that nearly all true genres are captured while controlling overprediction. This approach combined modern natural language processing (NLP) techniques with principled uncertainty quantification. The model is trained using PyTorch and Hugging Face Transformers, with predictions calibrated through a held-out validation set to determine a conformal threshold. This project highlighted the tradeoff between coverage and set size. This methodology is broadly applicable to other multi-label problems where prediction confidence is a priority, such as medical tagging, multi-topic document classification, or emotion recognition.
<br><br>

**Fine-Tuning BERT Models for Recipe Classification** 02/2025 

Fine-tuned transformer-based NLP architectures to classify recipes by dietary category, leveraging transfer learning to capture rich culinary semantics and implementing an end-to-end ML workflow while embedding-driven feature engineering, hyperparameter optimization, and rigorous cross-validation to deliver a robust, generalizable classifier. Our solution integrated pre-processing, model training, evaluation, and prediction using the Hugging Face Transformers and PyTorch libraries. A custom class efficiently tokenizes combined recipe descriptions and ingredient lists, ensuring consistent input formatting for BERT. The core training loop includes early stopping, validation performance tracking, and model checkpointing, all implemented from scratch. We also built a lightweight inference pipeline to batch-process unseen data, demonstrating an end-to-end deployment-ready workflow. This shows how pre-trained transformer models can be adapted for domain-specific binary classification tasks through thoughtful engineering. Rather than relying on out-of-the-box tools, we implemented robust data loaders, model evaluation routines, and checkpoint management to enable reproducible training and experimentation. The modular and scalable structure of the code allows for easy adaptation to other text classification problems, highlighting best practices in applied NLP development.
<br><br>

**More projects to be added...**
