---
layout: default
title: "Katherine Delno &#124; Statistician · Research & Quantitative Work"
nav_title: Home
permalink: /
description: "Katherine Delno is a statistician with an M.S. from the University of Washington. Explore selected research in statistical inference, causal analysis, and machine learning, alongside statistical services and private instruction."
---

{%- comment -%}
  Home page. Sections, in order: introduction, selected statistical work,
  statistical and quantitative services, private instruction, and a short
  closing note. The fuller account of each lives on its own page; this page
  only orders them.

  The <title> tag for this page is written in _includes/head.html. The
  front-matter title above exists for jekyll-seo-tag, which uses it for
  og:title, twitter:title, and the JSON-LD headline, so that those match the
  <title> tag. seo-tag runs titles through Markdown, where a bare pipe would
  be read as a table and dropped, hence &#124;. `nav_title` keeps the nav
  label as "Home".
{%- endcomment -%}

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;color:var(--ink);line-height:1.65}
  .pg p{max-width:66ch;margin:0}
  .pg p+p{margin-top:1rem}
  .pg h1,.pg h2,.pg h3{font-weight:700;color:var(--ink)}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 1.1rem}
  .pg a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}
  .hp-vh{position:absolute !important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}

  /* Introduction */
  .hp-intro{margin:3.4rem 0 0}
  .hp-intro h1{font-size:3.1rem;line-height:1.08;letter-spacing:-.028em;margin:0 0 1.8rem;max-width:15em}
  .hp-intro p{max-width:62ch}
  .pg .hp-lead{font-size:1.125rem;line-height:1.7}
  .pg .hp-sub{font-size:1.04rem;line-height:1.7;color:var(--muted);margin-top:1.15rem}

  /* Text links beneath a block: the intro, each section, the close */
  .pg .hp-links{display:flex;flex-wrap:wrap;gap:.7rem 2.2rem;margin-top:2.1rem;font-size:1rem}
  .pg .hp-links .hp-primary{font-weight:600}
  .pg .hp-more{margin-top:1.5rem;font-size:.97rem}

  /* Sections. One rule between them and the same generous interval throughout. */
  .hp-section{margin:3rem 0 0;padding-top:3rem;border-top:1px solid var(--line)}
  .hp-section.hp-first{margin-top:4.6rem;padding-top:3.4rem}
  .hp-section h2{font-size:1.95rem;line-height:1.18;letter-spacing:-.022em;margin:0 0 1.15rem}
  .hp-quiet h2{font-size:1.7rem}
  .hp-section .hp-intro-text{font-size:1.04rem}

  /* Research entries: a stacked list, ruled between entries */
  .hp-projects{margin:2.6rem 0 0}
  .hp-project{padding:2.1rem 0}
  .hp-project:first-child{padding-top:0}
  .hp-project+.hp-project{border-top:1px solid var(--line)}
  .hp-project h3{font-size:1.3rem;line-height:1.3;letter-spacing:-.012em;margin:0 0 .4rem}
  .pg .hp-meta{font-size:.86rem;color:var(--muted);letter-spacing:.01em;margin:0 0 .95rem;max-width:none}
  .hp-nw{white-space:nowrap}
  .pg .hp-project .hp-more{margin-top:.95rem;font-size:.95rem}
  .pg .hp-all{margin-top:.6rem;font-weight:600}

  /* Closing note */
  .hp-close{margin:3rem 0 1.6rem;padding-top:3rem;border-top:1px solid var(--line)}
  .hp-close h2{font-size:1.3rem;line-height:1.3;letter-spacing:-.01em;margin:0 0 .8rem}
  .hp-close p{color:var(--muted)}
  .pg .hp-close .hp-links{margin-top:1.3rem}

  @media (max-width:700px){
    .hp-intro{margin-top:1.4rem}
    .hp-intro h1{font-size:2.2rem;line-height:1.12;margin-bottom:1.3rem}
    .pg .hp-lead{font-size:1.06rem}
    .pg .hp-sub{font-size:1rem}
    .pg .hp-links{gap:.6rem 1.6rem;margin-top:1.7rem}
    .hp-section,.hp-close{margin-top:2rem;padding-top:2rem}
    .hp-section.hp-first{margin-top:2.6rem;padding-top:2.4rem}
    .hp-section h2{font-size:1.6rem}
    .hp-quiet h2{font-size:1.45rem}
    .hp-close h2{font-size:1.2rem}
    .hp-projects{margin-top:2rem}
    .hp-project{padding:1.7rem 0}
    .hp-project h3{font-size:1.16rem}
  }
</style>

<div class="pg" markdown="0">

  <section class="hp-intro" aria-labelledby="hp-title">
    <p class="label">Katherine Delno &middot; Statistician</p>
    <h1 id="hp-title">Statistical research and quantitative reasoning.</h1>
    <p class="hp-lead">I am a statistician with an M.S. in Statistics from the University of Washington and a B.S. in Mathematics from the University of Nevada, Reno. My graduate work encompassed statistical inference, modeling, causal inference, and statistical learning, with extensive computational work in R and Python.</p>
    <p class="hp-sub">My interests lie in the foundations of statistical methods: the assumptions on which they depend, how they behave in practice, and what their conclusions can reasonably establish. Since completing my graduate studies in 2025, I have maintained an independent mathematics and statistics teaching practice. I also accept selected statistical and quantitative projects.</p>
    <p class="hp-links">
      <a href="/statistical-work/" class="hp-primary">Selected Statistical Work <span aria-hidden="true">&rarr;</span></a>
      <a href="/about/">Academic Background <span aria-hidden="true">&rarr;</span></a>
    </p>
  </section>

  <section class="hp-section hp-first" aria-labelledby="hp-research">
    <p class="label">Research</p>
    <h2 id="hp-research">Selected Statistical Work</h2>
    <p class="hp-intro-text">My graduate work included independent methodological research and applied projects in causal inference and machine learning. The selections below reflect an interest in statistical methods as objects of study in their own right, including the assumptions they require, the circumstances in which they perform well, and the limits of their interpretation.</p>

    <div class="hp-projects">

      <article class="hp-project" aria-labelledby="hp-rfsc">
        <h3 id="hp-rfsc">RandomForestSpecCheck</h3>
        <p class="hp-meta">Independent methodological research &middot; Sole author &middot; University of Washington, 2025</p>
        <p>Developed a permutation-based random forest diagnostic for detecting <span class="hp-nw">mean-structure</span> misspecification in linear mixed models. The procedure was evaluated through simulation across varying data structures and applied to the Framingham Heart Study, with particular attention to its operating characteristics and limitations.</p>
        <p class="hp-more"><a href="/projects/random-forest-spec-check/">Read project<span class="hp-vh">: RandomForestSpecCheck</span> <span aria-hidden="true">&rarr;</span></a></p>
      </article>

      <article class="hp-project" aria-labelledby="hp-nhanes">
        <h3 id="hp-nhanes">Causal Analysis of Food Insecurity and Type&nbsp;2&nbsp;Diabetes</h3>
        <p class="hp-meta">Collaborative research &middot; University of Washington, 2024</p>
        <p>Examined the relationship between food insecurity and type 2 diabetes using pooled national survey data, augmented inverse probability weighting, and <span class="hp-nw">g-computation</span>. The analysis emphasized causal identification, the assumptions required for estimation, and the limitations of observational data.</p>
        <p class="hp-more"><a href="/projects/causal-inference-nhanes/">Read project<span class="hp-vh">: Causal Analysis of Food Insecurity and Type 2 Diabetes</span> <span aria-hidden="true">&rarr;</span></a></p>
      </article>

      <article class="hp-project" aria-labelledby="hp-conformal">
        <h3 id="hp-conformal">Conformal Prediction for Multi-Label Classification</h3>
        <p class="hp-meta">Applied machine learning &middot; Project lead &middot; 2025</p>
        <p>Fine-tuned a DistilBERT model for multi-label movie genre classification and applied conformal prediction to construct prediction sets. The study examined empirical coverage, <span class="hp-nw">prediction-set</span> size, and the practical limitations of uncertainty quantification in multi-label classification.</p>
        <p class="hp-more"><a href="/projects/conformal-prediction-genre/">Read project<span class="hp-vh">: Conformal Prediction for Multi-Label Classification</span> <span aria-hidden="true">&rarr;</span></a></p>
      </article>

    </div>

    <p class="hp-more hp-all"><a href="/statistical-work/">View all selected work <span aria-hidden="true">&rarr;</span></a></p>
  </section>

  <section class="hp-section hp-quiet" aria-labelledby="hp-services">
    <p class="label">Professional Work</p>
    <h2 id="hp-services">Statistical and Quantitative Services</h2>
    <p>I accept a limited number of projects involving statistical analysis, methodological review, research support, and quantitative content. My approach begins with the structure of the problem: the research question, the available evidence, and the assumptions necessary to connect one to the other.</p>
    <p>I place particular importance on reproducible analysis, transparent methodological choices, and interpretations that remain within the limits of the data.</p>
    <p class="hp-more"><a href="/statistical-services/">Statistical Services <span aria-hidden="true">&rarr;</span></a></p>
  </section>

  <section class="hp-section hp-quiet" aria-labelledby="hp-teaching">
    <p class="label">Teaching</p>
    <h2 id="hp-teaching">Private Mathematics and Statistics Instruction</h2>
    <p>I maintain a small independent teaching practice in AP&nbsp;Statistics, AP&nbsp;Calculus AB/BC, and AP&nbsp;Precalculus. Instruction is individual and typically extends across an academic course, allowing for close attention to a student's reasoning, developing understanding, and recurring difficulties.</p>
    <p>My approach to teaching is informed by the same interests that shape my statistical work: the structure behind a method, the assumptions that justify its use, and the distinction between carrying out a procedure and understanding why it works.</p>
    <p class="hp-more"><a href="/private-instruction/">Private Instruction, Courses &amp; Rates <span aria-hidden="true">&rarr;</span></a></p>
  </section>

  <section class="hp-close" aria-labelledby="hp-background">
    <h2 id="hp-background">Background &amp; Inquiries</h2>
    <p>Further details of my academic training, research interests, and teaching history are available on the About page. For inquiries concerning statistical projects or private instruction, I can be reached by email.</p>
    <p class="hp-links">
      <a href="/about/">About <span aria-hidden="true">&rarr;</span></a>
      <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>
    </p>
  </section>

</div>
