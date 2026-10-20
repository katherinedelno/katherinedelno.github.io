---
layout: page
title: "About Katherine Delno &#124; Statistics, Research & Teaching"
seo_title: "About Katherine Delno | Statistics, Research & Teaching"
nav_title: About
permalink: /about/
description: "Learn about Katherine Delno's background in mathematics and statistics, graduate research at the University of Washington, and interests in statistical inference, machine learning, and artificial intelligence."
---

{%- comment -%}
  Titles. `seo_title` is the <title> tag. `title` exists for jekyll-seo-tag,
  which uses it for og:title, twitter:title, and the JSON-LD headline; seo-tag
  runs titles through Markdown, where a bare pipe would be read as a table and
  dropped, hence &#124;. `nav_title` keeps the nav label as "About".

  The page is written as one essay in sections, so it carries no section
  labels. Statistical Work and Current Interests share a single rule: they are
  separate sections that belong together.

  Body type follows the rest of the site: paragraphs inherit minima's 16px
  base with the 1.65 leading every principal page sets on .pg, and the
  introduction uses the 1.06rem / 1.6 setting of the page introductions on
  Selected Statistical Work and Statistical Services. Paragraphs within a
  section are 15px apart, as elsewhere.
{%- endcomment -%}

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;color:var(--ink);line-height:1.65}
  .pg p{max-width:68ch;margin:0}
  .pg p+p{margin-top:.94rem}
  .pg h1,.pg h2,.pg h3{font-weight:700;color:var(--ink)}
  .pg b,.pg strong{font-weight:600}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 1rem}
  .pg a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}

  /* Introduction, with the portrait beside it */
  .ab-intro{display:grid;grid-template-columns:minmax(0,1fr) 200px;column-gap:44px;align-items:center;margin:2.6rem 0 0}
  .ab-intro h1{font-size:2.75rem;line-height:1.08;letter-spacing:-.026em;margin:0 0 1.4rem}
  .pg .ab-intro p:not(.label){font-size:1.06rem;line-height:1.6}
  .pg .ab-intro .ab-sub{color:var(--muted)}
  .headshot{width:200px;height:218px;border-radius:14px;object-fit:cover;border:1px solid var(--line);display:block}

  /* Sections: one rule and the same interval between each */
  .ab-section{margin:3rem 0 0;padding-top:3rem;border-top:1px solid var(--line);scroll-margin-top:24px}
  .ab-section h2{font-size:1.65rem;line-height:1.2;letter-spacing:-.018em;margin:0 0 1.2rem}
  .ab-section.ab-first{margin-top:3.8rem;padding-top:3.2rem}
  .ab-section.ab-near{margin-top:3rem;padding-top:0;border-top:none}
  .pg .ab-more{margin-top:1.4rem;font-size:.97rem}

  /* Degrees: two entries, ruled between */
  .ab-degrees{margin-top:1.8rem}
  .ab-degree{padding:2rem 0}
  .ab-degree:first-child{padding-top:0}
  .ab-degree:last-child{padding-bottom:0}
  .ab-degree+.ab-degree{border-top:1px solid var(--line)}
  .ab-degree h3{font-size:1.2rem;line-height:1.3;letter-spacing:-.01em;margin:0 0 .25rem}
  .pg .ab-meta{font-size:.86rem;color:var(--muted);letter-spacing:.01em;margin:0 0 .9rem}

  /* The personal close: a smaller heading and quieter text */
  .ab-section.ab-close{margin-bottom:1.6rem}
  .ab-close h2{font-size:1.3rem;letter-spacing:-.01em;margin-bottom:.8rem}
  .ab-close p{color:var(--muted)}

  .lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);align-items:center;justify-content:center;padding:24px;z-index:9999}
  .lightbox:target{display:flex}
  .lightbox img{max-width:min(720px,90vw);max-height:75vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.35);pointer-events:none}
  .lb-close{position:absolute;inset:0;cursor:zoom-out}
  .lb-x{position:absolute;top:14px;right:16px;z-index:2;width:44px;height:44px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:2rem;line-height:1;text-decoration:none}

  @media (max-width:700px){
    .ab-intro{grid-template-columns:1fr;row-gap:26px;margin-top:1.3rem}
    .ab-intro h1{font-size:2.15rem;margin-bottom:1.1rem}
    .headshot{width:170px;height:185px}
    .ab-section{margin-top:2rem;padding-top:2rem}
    .ab-section.ab-first{margin-top:2.4rem;padding-top:2.2rem}
    .ab-section.ab-near{margin-top:2.2rem;padding-top:0}
    .ab-section h2{font-size:1.4rem}
    .ab-close h2{font-size:1.2rem}
    .ab-degree{padding:1.4rem 0}
  }
</style>

<div class="pg" markdown="0">

  <section class="ab-intro" aria-labelledby="ab-title">
    <div>
      <p class="label">Katherine Delno</p>
      <h1 id="ab-title">About</h1>
      <p>I am a statistician with an M.S. in Statistics from the University of Washington and a B.S. in Mathematics from the University of Nevada, Reno. My academic work has ranged from mathematical statistics and statistical inference to methodological research, causal inference, and statistical learning, with extensive computational work in R and Python.</p>
      <p class="ab-sub">Since completing my graduate studies in 2025, I have maintained an independent mathematics and statistics teaching practice. I also accept selected statistical and quantitative projects.</p>
    </div>
    <img src="/assets/img/headshot.jpg" alt="Katherine Delno" class="headshot" width="200" height="218" loading="lazy" decoding="async">
  </section>

  <section class="ab-section ab-first" id="background" aria-labelledby="ab-background">
    <h2 id="ab-background">From Mathematics to Statistics</h2>
    <p>Mathematics did not come easily to me in school. For years, its notation and methods felt arbitrary, as though the task were to follow rules whose underlying reasons remained obscure.</p>
    <p>What eventually held my attention was the structure beneath those procedures: why an argument works, which assumptions a method depends on, and how seemingly different ideas relate to one another. That interest led me first to mathematics and later to statistics.</p>
    <p>Statistics introduced a different set of questions. What can be inferred from incomplete observations? Under what assumptions are those inferences justified? How can we distinguish a result that is statistically detectable from one that is substantively meaningful? I became particularly interested in the theoretical foundations of statistical methods and the relationship between their mathematical properties and their behavior in practice.</p>
  </section>

  <section class="ab-section" id="training" aria-labelledby="ab-training">
    <h2 id="ab-training">Academic Training</h2>

    <div class="ab-degrees">
      <div class="ab-degree">
        <h3>M.S. Statistics</h3>
        <p class="ab-meta">University of Washington &middot; 2025</p>
        <p>Graduate study at the University of Washington brought together the mathematical theory of statistical inference and methods for analyzing complex data. The theoretical inference sequence involved deriving estimators, hypothesis tests, and confidence procedures, studying their statistical properties, and examining the conditions under which their conclusions are justified. Particular emphasis was placed on likelihood-based inference, large-sample approximations, and the mathematical foundations of estimation and uncertainty quantification.</p>
        <p>My coursework also encompassed regression and generalized linear models, longitudinal and correlated data, experimental design, categorical data analysis, causal inference, biostatistics, statistical learning, and statistical computing. These subjects introduced related questions of model specification, dependence, identification, and the interpretation of statistical evidence. Bayesian methods, simulation, resampling, and computational model evaluation provided additional approaches to studying statistical procedures and their behavior.</p>
        <p>Programming in R and Python was integral to my graduate work, from simulation studies and statistical modeling to applied machine learning. My independent methodological research allowed me to pursue a statistical problem beyond the application of established procedures, developing and evaluating a diagnostic method through computational experimentation and analysis of its operating characteristics.</p>
      </div>

      <div class="ab-degree">
        <h3>B.S. Mathematics</h3>
        <p class="ab-meta">University of Nevada, Reno &middot; 2022 &middot; Specialization&nbsp;in&nbsp;Statistics</p>
        <p>My undergraduate studies established a mathematical foundation through proof-based coursework in real analysis, linear algebra, differential equations, probability, mathematical statistics, numerical methods, and mathematical modeling.</p>
        <p>Two semesters of real analysis were particularly formative. The subject develops the foundations of calculus through precise definitions and proofs, including the study of convergence, continuity, differentiation, and integration. It requires close attention to the logical structure of an argument and to the conditions under which a mathematical result holds.</p>
        <p>My specialization in statistics extended that mathematical training toward probability, estimation, and statistical modeling, providing the foundation for the more advanced theoretical and computational work I later pursued at the University of Washington.</p>
      </div>
    </div>
  </section>

  <section class="ab-section" id="statistical-work" aria-labelledby="ab-work">
    <h2 id="ab-work">Statistical Work</h2>
    <p>My graduate research included independent methodological development and applied projects in causal inference, statistical learning, and uncertainty quantification.</p>
    <p>My principal independent project, RandomForestSpecCheck, involved developing and evaluating a permutation-based diagnostic for mean-structure misspecification in linear mixed models. The work combined statistical modeling, random forests, simulation-based evaluation, and an examination of the conditions under which the proposed method was informative.</p>
    <p>Other projects examined causal identification and estimation in observational data, as well as transformer-based classification and conformal prediction.</p>
    <p class="ab-more"><a href="/statistical-work/">View Selected Statistical Work <span aria-hidden="true">&rarr;</span></a></p>
  </section>

  <section class="ab-section ab-near" id="interests" aria-labelledby="ab-interests">
    <h2 id="ab-interests">Current Interests</h2>
    <p>My current interests increasingly concern the theoretical foundations of artificial intelligence, particularly large language models and their behavior. I am interested in how these systems develop internal representations, how reasoning-like capabilities emerge or become observable, and how reliably those capabilities generalize across tasks and contexts.</p>
    <p>These questions invite a statistical perspective. Evaluating the behavior of a language model requires decisions about what is being measured, how evidence is collected, and which conclusions the observations can support. I am particularly interested in the methodological problems involved in distinguishing apparent competence from reliable generalization, and in understanding what behavioral evaluations can reveal about the mechanisms underlying model performance.</p>
    <p>I am beginning to pursue these questions as an independent research direction, starting with the theoretical foundations of modern machine learning and the literature on language-model behavior, evaluation, and interpretability. My aim is to develop a rigorous understanding of these systems and the methods available for investigating them before narrowing toward more specific research questions.</p>
    <p>My interests also extend to the philosophy of artificial intelligence, particularly the relationship between statistical learning, knowledge, reasoning, and understanding. The question of what it means for a computational system to exhibit intelligent behavior, and what evidence would justify attributing particular capacities to it, is one I find especially compelling.</p>
  </section>

  <section class="ab-section" id="teaching" aria-labelledby="ab-teaching">
    <h2 id="ab-teaching">Teaching</h2>
    <p>I began teaching statistics at the University of Nevada, Reno, where I served as a teaching assistant for undergraduate statistics. Later, as a mentor in the Statistics &amp; Probability Directed Reading Program at the University of Washington, I designed and led an individualized course in statistical learning.</p>
    <p>I established my independent teaching practice in 2025 and now work with a small number of students in mathematics and statistics.</p>
    <p>Working individually with students allows me to observe how their reasoning develops: how they approach an unfamiliar problem, where uncertainty enters, and whether an idea remains understood when the form of a problem changes. My teaching emphasizes conceptual structure and mathematical justification alongside procedural proficiency.</p>
    <p class="ab-more"><a href="/private-instruction/">More About Private Instruction <span aria-hidden="true">&rarr;</span></a></p>
  </section>

  <section class="ab-section ab-close" id="personal" aria-labelledby="ab-personal">
    <h2 id="ab-personal">Outside the Classroom</h2>
    <p>I live in Seattle. Away from mathematics and statistics, I enjoy baking, making espresso, collecting ceramics, reading, and spending time with my cat, <a href="#blue-photo">Blue</a>.</p>
  </section>

  <div id="blue-photo" class="lightbox" aria-hidden="true">
    <a href="#" class="lb-close" aria-label="Close"></a>
    <a href="#" class="lb-x" aria-label="Close">&times;</a>
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
