---
layout: page
title: Projects
permalink: /projects/
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&display=swap');
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1a1a1a;--muted:#5b6168;--line:#e7e7e3;--accent:#959386;--accent-soft:#cac9c3;--accent-ink:#57554C;--card:#fbfbfa;color:var(--ink);line-height:1.6}
  .pg p{max-width:74ch}
  .pg h1,.pg h2,.pg h3,.pg h4,.pg b{font-weight:700}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent-ink);margin:0 0 .5rem}
  .pg-hero{margin:0 0 2.4rem}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .6rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero .tagline{font-size:1.12rem;color:var(--muted);max-width:64ch;margin:0}

  /* Featured project */
  .pg-feature{position:relative;border:1.5px solid var(--accent);border-radius:16px;padding:30px 30px 28px;background:#fff;box-shadow:0 6px 22px rgba(31,42,68,.08);margin-top:20px}
  .pg-feature .pill{position:absolute;top:-12px;left:28px;background:var(--accent);color:var(--ink);font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:5px 11px;border-radius:999px}
  .pg-feature .date{font-size:.74rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent-ink)}
  .pg-feature h3{margin:.35rem 0 .2rem;font-size:1.28rem;line-height:1.25;letter-spacing:-.01em}
  .pg-feature .author{font-size:.9rem;color:var(--muted);margin:0 0 .9rem}
  .pg-feature p{font-size:.96rem}
  .pg-breakdown{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:1.4rem 0 .4rem;padding:1.3rem 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
  .pg-breakdown h4{font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;color:var(--accent-ink);margin:0 0 .35rem}
  .pg-breakdown p{font-size:.88rem;color:var(--muted);margin:0;max-width:none}

  /* Standard project cards */
  .pg-project{border:1px solid var(--line);border-radius:14px;padding:24px 26px;background:var(--card);margin-top:18px}
  .pg-project .date{font-size:.74rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent-ink)}
  .pg-project h3{margin:.3rem 0 .15rem;font-size:1.14rem;line-height:1.3;letter-spacing:-.01em}
  .pg-project .author{font-size:.88rem;color:var(--muted);margin:0 0 .7rem}
  .pg-project p{margin:0;font-size:.95rem}
  .pg-result{display:inline-block;margin-top:.9rem;font-size:.88rem;background:var(--accent-soft);color:var(--accent-ink);padding:6px 12px;border-radius:8px;font-weight:600}

  .pg-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:1rem}
  .pg-tags span{font-size:.78rem;background:#fff;border:1px solid var(--line);color:var(--accent-ink);padding:5px 11px;border-radius:999px}
  .pg-feature .pg-tags span{background:var(--accent-soft);border-color:transparent}

  @media (max-width:720px){.pg-hero h1{font-size:1.7rem}.pg-feature,.pg-project{padding:22px}.pg-breakdown{grid-template-columns:1fr;gap:14px}}
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Projects</p>
    <h1>Statistical work</h1>
    <p class="tagline">Alongside teaching, my graduate training included substantial applied and methodological work in statistics and machine learning. These projects reflect the depth of training that informs my instruction, particularly in AP Statistics.</p>
  </div>

  <div class="pg-feature">
    <span class="pill">Featured &middot; Independent research</span>
    <p class="date">2025</p>
    <h3>RandomForestSpecCheck: A Permutation-Based Random Forest Diagnostic for Linear Mixed Models</h3>
    <p class="author">Sole author</p>
    <p>My primary independent research: a novel, nonparametric diagnostic I designed and developed for detecting misspecification in linear mixed models (LMMs). The method combines a machine-learning measure of leftover structure with a permutation test that respects clustered data, and is packaged as an R function that returns the observed statistic, the full permutation distribution, and a clear decision.</p>
    <div class="pg-breakdown">
      <div>
        <h4>The problem</h4>
        <p>Linear mixed models are easy to misspecify, and standard diagnostics such as residual plots, Q&ndash;Q plots, and AIC/BIC often miss subtle nonlinear or random-effects violations.</p>
      </div>
      <div>
        <h4>The method</h4>
        <p>Fit a random forest to the model's residuals and measure leftover structure with an out-of-bag R&sup2;. A null distribution is built by permuting residuals within clusters, preserving the design without assuming normality. A dual-criteria rule flags a model only when the statistic exceeds both the 97.5th percentile of the null and a practical effect-size threshold.</p>
      </div>
      <div>
        <h4>Validation</h4>
        <p>Across 5,400 simulated datasets spanning 54 misspecification scenarios, it held false-positive rates near 1&ndash;3% at a 5% level and reached 80&ndash;100% power for large mean-structure departures. Applied to the Framingham Heart Study, it correctly cleared well-specified models.</p>
      </div>
    </div>
    <div class="pg-tags"><span>R</span><span>Random Forests</span><span>Linear Mixed Models</span><span>Permutation Testing</span><span>Out-of-Bag R&sup2;</span><span>Novel Method</span></div>
  </div>

  <div class="pg-project">
    <p class="date">March 2025</p>
    <h3>A Conformal Prediction Framework for Multi-Label Movie Genre Classification</h3>
    <p>Led a project pairing a fine-tuned transformer with conformal prediction to assign calibrated sets of genre tags to films, an approach that generalizes to other multi-label problems such as medical tagging and document classification.</p>
    <div class="pg-breakdown">
      <div>
        <h4>The problem</h4>
        <p>Movies span multiple genres, so the task is multi-label: a model must capture all relevant genres while avoiding spurious ones, and standard classifiers give point predictions with no reliability guarantee.</p>
      </div>
      <div>
        <h4>The method</h4>
        <p>Fine-tune DistilBERT end-to-end on the combined title, overview, and tagline, then wrap it in global conformal prediction with a sum-based non-conformity score, calibrated on held-out data to target at least 90% coverage.</p>
      </div>
      <div>
        <h4>Results</h4>
        <p>Produced calibrated genre sets that balance coverage against set size, capturing nearly all true genres while controlling overprediction.</p>
      </div>
    </div>
    <div class="pg-tags"><span>Python</span><span>PyTorch</span><span>Hugging Face</span><span>DistilBERT</span><span>Conformal Prediction</span><span>NLP</span></div>
  </div>

  <div class="pg-project">
    <p class="date">February 2025</p>
    <h3>Fine-Tuning BERT Models for Recipe Classification</h3>
    <p>Led a study evaluating transformer-based NLP models on a specialized text-classification task, comparing architectures and tuning them for the best generalization to unseen data.</p>
    <div class="pg-breakdown">
      <div>
        <h4>The problem</h4>
        <p>Classify recipes as vegetarian from free text, where meaning hinges on subtle domain language, for example "vegetable broth" signals vegetarian while "chicken stock" does not.</p>
      </div>
      <div>
        <h4>The method</h4>
        <p>Fine-tune and compare BERT Base, BERT Large, and RoBERTa on combined description and ingredient text, with hyperparameter tuning over learning rate, weight decay, sequence length, and batch size, plus early stopping.</p>
      </div>
      <div>
        <h4>Results</h4>
        <p>BERT Base generalized best across more than 20,000 recipes, outperforming the larger variants on held-out test data.</p>
      </div>
    </div>
    <div class="pg-tags"><span>Python</span><span>PyTorch</span><span>Hugging Face</span><span>BERT</span><span>RoBERTa</span><span>NLP</span></div>
  </div>

  <div class="pg-project">
    <p class="date">May 2024</p>
    <h3>Causal Analysis of Food Insecurity and Type 2 Diabetes Using NHANES</h3>
    <p>Led a causal inference study on a national health dataset, applying a doubly robust estimator and examining the limits of what cross-sectional survey data can support.</p>
    <div class="pg-breakdown">
      <div>
        <h4>The problem</h4>
        <p>Does food insecurity causally raise the risk of developing type 2 diabetes? Observational health data makes this difficult, with confounding and no clear time ordering between exposure and outcome.</p>
      </div>
      <div>
        <h4>The method</h4>
        <p>Apply augmented inverse probability weighting (AIPW), a doubly robust estimator, to estimate the average treatment effect across three NHANES cycles (2013&ndash;2018), adjusting for sociodemographic confounders.</p>
      </div>
      <div>
        <h4>Results</h4>
        <p>No statistically significant effect was found. The core contribution is a careful account of why cross-sectional survey data limits causal inference, making the case for longitudinal follow-up.</p>
      </div>
    </div>
    <div class="pg-tags"><span>R</span><span>Causal Inference</span><span>AIPW</span><span>Survey Data</span><span>NHANES</span></div>
  </div>

</div>
