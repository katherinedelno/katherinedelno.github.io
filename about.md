---
layout: page
title: About
permalink: /about/
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;color:var(--ink);line-height:1.65}
  .pg p{max-width:70ch}
  .pg h1,.pg h2,.pg h3{font-weight:700}
  .pg b,.pg strong{font-weight:600}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .6rem}

  .about-grid{display:grid;grid-template-columns:minmax(0,1fr) 230px;column-gap:40px;align-items:center;margin:1rem 0 0}
  .about-grid h1{font-size:2.1rem;line-height:1.12;margin:0 0 .9rem;letter-spacing:-.02em}
  .headshot{width:230px;height:250px;border-radius:16px;object-fit:cover;border:1px solid var(--line)}

  .about-section{margin:2.8rem 0 0;padding-top:2.2rem;border-top:1px solid var(--line)}
  .about-section h2{font-size:1.35rem;margin:0 0 1rem;letter-spacing:-.01em}
  .about-section h3{font-size:1.08rem;margin:1.6rem 0 .1rem}
  .about-section .meta{font-size:.9rem;color:var(--muted);margin:0 0 .8rem;font-weight:600;letter-spacing:.02em}
  .pg-sub{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:1.2rem 0 .2rem}
  .pg-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:.7rem;max-width:74ch}
  .pg-tags span{font-size:.82rem;background:var(--accent-soft);color:var(--accent);padding:6px 12px;border-radius:999px}
  .pg-callout{margin-top:1.3rem;padding:18px 22px;border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;background:var(--card);max-width:74ch}
  .pg-callout p{margin:0;font-size:.95rem}

  .pg-timeline{margin-top:1.4rem;border-left:2px solid var(--line);padding-left:26px}
  .pg-entry{position:relative;padding-bottom:2rem}
  .pg-entry:last-child{padding-bottom:0}
  .pg-entry::before{content:"";position:absolute;left:-33px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px #fff}
  .pg-entry .date{font-size:.76rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
  .pg-entry h3{margin:.25rem 0 .1rem;font-size:1.12rem}
  .pg-entry .org{font-size:.92rem;color:var(--muted);margin:0 0 .6rem}
  .pg-entry p{margin:0;font-size:.95rem}
  .pg-entry.current::before{background:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
  .pg-entry.current h3 .badge{font-size:.68rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:var(--accent);padding:3px 9px;border-radius:999px;margin-left:10px;vertical-align:middle}

  .lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);align-items:center;justify-content:center;padding:24px;z-index:9999}
  .lightbox:target{display:flex}
  .lightbox img{max-width:min(720px,90vw);max-height:75vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.35);pointer-events:none}
  .lb-close{position:absolute;inset:0;cursor:zoom-out}
  .lb-x{position:absolute;top:14px;right:16px;z-index:2;width:44px;height:44px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:2rem;line-height:1;text-decoration:none}

  @media (max-width:700px){
    .about-grid{grid-template-columns:1fr;row-gap:20px}
    .about-grid h1{font-size:1.8rem}
    .headshot{width:180px;height:196px;justify-self:start}
  }
</style>

<div class="pg" markdown="0">

  <div class="about-grid">
    <div>
      <p class="label">About</p>
      <h1>Hi, I'm Katherine</h1>
      <p>I teach mathematics and statistics one-on-one, primarily in AP Statistics, AP Calculus, and AP Precalculus.</p>
      <p>I did not begin as a student who found mathematics easy. I struggled with it for years in school, and I remember very clearly what it feels like to sit in front of a problem and have no idea how to begin. I eventually went on to earn a degree in mathematics and a graduate degree in statistics. That experience still shapes how I teach.</p>
      <p>Difficulty is useful information. A student may feel as though they do not understand an entire topic when the actual problem began several steps earlier. I try to find that point precisely. Then we rebuild from there until the student can carry the reasoning independently.</p>
    </div>
    <img src="/assets/img/headshot.jpg" alt="Katherine Delno" class="headshot" width="230" height="250" loading="lazy" decoding="async">
  </div>

  <div class="about-section" id="training">
    <style>
      .cw-details{margin-top:.9rem;max-width:74ch}
      .cw-details summary{cursor:pointer;font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);list-style:none;display:flex;align-items:center;gap:8px}
      .cw-details summary::-webkit-details-marker{display:none}
      .cw-details summary::after{content:"+";font-size:1rem;font-weight:400;color:var(--muted)}
      .cw-details[open] summary::after{content:"\2212"}
      .cw-details .pg-tags{margin-top:.8rem}
      .deg-meta{font-size:.9rem;color:var(--muted);margin:0 0 .8rem;font-weight:600;letter-spacing:.02em}
    </style>
    <p class="label">Education</p>
    <h2>Academic training</h2>
    <p>My training in mathematics and statistics is rigorous and strongly theoretical. It includes the full sequence of topics my students encounter, along with proof-based mathematics, statistical theory, advanced regression, inference, computation, and applied research.</p>
    <p>That background matters in my teaching. It helps me see the structure underneath a problem, trace an error to its source, and explain the same idea in more than one way when needed.</p>

    <h3>M.S. Statistics</h3>
    <p class="deg-meta">University of Washington &middot; 2025 &middot; Statistics ranked #6 nationally, UW #3 among U.S. public universities (U.S. News, 2026)</p>
    <p>My graduate work focused on statistical theory, methodology, and computation. The core included a full theoretical inference sequence in which estimators, tests, and confidence intervals were derived rather than simply applied. I also studied regression for independent and correlated data, experimental design, categorical data analysis, statistical computing, biostatistics, causal inference, and applied statistics in R and Python.</p>
    <details class="cw-details">
      <summary>Graduate coursework</summary>
      <div class="pg-tags">
        <span>Statistical Inference I &amp; II</span>
        <span>Regression Methods for Independent &amp; Dependent Data</span>
        <span>Applied Regression</span>
        <span>Design &amp; Analysis of Experiments</span>
        <span>Categorical Data Analysis</span>
        <span>Statistical Computing</span>
        <span>Applied Biostatistics I &amp; II</span>
        <span>Causal Inference in Biomedical Studies</span>
        <span>Applied Statistics Capstone</span>
        <span>Independent Research</span>
      </div>
    </details>

    <h3 style="margin-top:2.2rem;">B.S. Mathematics</h3>
    <p class="deg-meta">University of Nevada, Reno &middot; 2021 &middot; Specialization in Statistics &middot; Minor in Civil Engineering</p>
    <p>My undergraduate mathematics training was heavily proof-based. It included the full calculus sequence, linear algebra, differential equations, numerical methods, proof writing, and two semesters of real analysis. In real analysis, the ideas of calculus are rebuilt from rigorous definitions and proofs.</p>
    <p>I also completed substantial coursework in probability, statistical theory, regression, computing, engineering, and the physical sciences. I began university in engineering before moving fully into mathematics and statistics, so that broader technical background remains part of how I approach quantitative problems.</p>
    <details class="cw-details">
      <summary>Undergraduate coursework</summary>
      <div class="pg-tags">
        <span>Calculus I, II &amp; III</span>
        <span>Differential Equations</span>
        <span>Partial Differential Equations</span>
        <span>Linear Algebra</span>
        <span>Real Analysis I &amp; II</span>
        <span>Proof Writing for Mathematics &amp; Statistics</span>
        <span>Numerical Methods</span>
        <span>Mathematical Modeling</span>
        <span>Probability</span>
        <span>Statistical Theory</span>
        <span>Regression &amp; Linear Models</span>
        <span>Categorical Data Analysis</span>
        <span>Statistical Computing</span>
        <span>Computer Science I &amp; II</span>
        <span>General Chemistry I &amp; II</span>
        <span>Organic Chemistry</span>
        <span>Calculus-Based Physics I &amp; II</span>
        <span>General Biology</span>
        <span>Engineering Statics</span>
        <span>Fluid Dynamics</span>
      </div>
    </details>
  </div>

  <div class="about-section">
    <p class="label">Experience</p>
    <h2>Teaching experience</h2>
    <p>My teaching experience includes private instruction, university statistics courses, and one-on-one academic mentoring. My current work and primary focus are the private instruction practice.</p>

    <div class="pg-timeline">

      <div class="pg-entry current">
        <p class="date">2025 &ndash; Present</p>
        <h3>Private Mathematics &amp; Statistics Instructor <span class="badge">Current</span></h3>
        <p class="org">Independent &middot; Remote</p>
        <p>I teach mathematics and statistics privately to high school and college students, with a focus on AP coursework. Sessions are built around the student's reasoning. I watch how they set up a problem, where they hesitate, which errors repeat, and how much of the work they can reproduce independently.</p>
        <p style="margin-top:.7rem;">I use those patterns to shape the pacing, explanation, and practice over time. I also write the curriculum and supporting materials used in sessions and keep detailed notes so that each meeting builds on the last.</p>
      </div>

      <div class="pg-entry">
        <p class="date">2024</p>
        <h3>Mentor, Directed Reading Program</h3>
        <p class="org">Statistics &amp; Probability Association, University of Washington &middot; Seattle, WA</p>
        <p>I designed and led a one-on-one short course in statistical learning. Topics included linear regression, classification, resampling methods, and regularization. I created the course materials, led weekly discussions, and provided ongoing feedback throughout the quarter.</p>
      </div>

      <div class="pg-entry">
        <p class="date">2022</p>
        <h3>Graduate Teaching Assistant</h3>
        <p class="org">Department of Mathematics &amp; Statistics, University of Nevada, Reno &middot; Reno, NV</p>
        <p>I led discussion sections for an undergraduate statistics course and developed instructional materials for weekly meetings. I also provided individual and group support, graded exams and quizzes with written feedback, and worked with students on statistical reasoning and communication.</p>
      </div>

    </div>
  </div>

  <div class="about-section" id="statistical-work">
    <p class="label">Research</p>
    <h2>Statistical work</h2>

    <div class="pj-work">

      <p class="pj-work__intro">My graduate work also included independent methodological research and applied projects in statistics and machine learning. These projects reflect the depth of statistical training behind my teaching, particularly in AP Statistics. Each project below has a full write-up.</p>

      <!-- One grid, as on /resources/: the featured entry spans two of the
           three columns and the three applied projects follow. -->
      <div class="pj-work__grid">

      <a class="pj-feature" href="{{ '/projects/random-forest-spec-check/' | relative_url }}">

        <p class="pj-feature__kicker">
          <span class="pj-feature__tag">Independent research</span>
          <span>Sole author</span>
          <span>2025</span>
        </p>

        <h3 class="pj-feature__title">RandomForestSpecCheck: A permutation-based random forest diagnostic for linear mixed models</h3>

        <p class="pj-feature__blurb">I designed a nonparametric diagnostic for detecting misspecification in linear mixed models. A random forest measures remaining structure in the model residuals, while a permutation test that preserves the clustered design supplies the null distribution.</p>

        <div class="pj-stats">
          <div class="pj-stat">
            <div class="pj-stat__value">5,400</div>
            <div class="pj-stat__label">simulated datasets across 54 scenarios</div>
          </div>
          <div class="pj-stat">
            <div class="pj-stat__value">1&ndash;3%</div>
            <div class="pj-stat__label">false-positive rate at a 5% level</div>
          </div>
          <div class="pj-stat">
            <div class="pj-stat__value">80&ndash;100%</div>
            <div class="pj-stat__label">power against large departures</div>
          </div>
        </div>

        <span class="pj-feature__more">Read the full account &rarr;</span>
      </a>


        <a class="pj-card" href="{{ '/projects/conformal-prediction-genre/' | relative_url }}">
          <p class="pj-card__kicker">Machine learning &middot; 2025</p>
          <h3 class="pj-card__title">Conformal prediction for multi-label genre classification</h3>
          <p class="pj-card__blurb">A fine-tuned DistilBERT model paired with conformal prediction to return calibrated sets of genre labels with at least 90% coverage. The target coverage was achieved. The write-up focuses on the tradeoffs required to obtain it.</p>
          <span class="pj-card__more">Read &rarr;</span>
        </a>

        <a class="pj-card" href="{{ '/projects/bert-recipe-classification/' | relative_url }}">
          <p class="pj-card__kicker">Machine learning &middot; 2025</p>
          <h3 class="pj-card__title">Fine-tuning BERT models for recipe classification</h3>
          <p class="pj-card__blurb">Twenty-two configurations of BERT Base, BERT Large, and RoBERTa were compared across 20,000 recipes. The smallest model performed best, while validation accuracy proved to be an unreliable guide to the final result.</p>
          <span class="pj-card__more">Read &rarr;</span>
        </a>

        <a class="pj-card" href="{{ '/projects/causal-inference-nhanes/' | relative_url }}">
          <p class="pj-card__kicker">Causal inference &middot; 2024</p>
          <h3 class="pj-card__title">Causal analysis of food insecurity and type 2 diabetes</h3>
          <p class="pj-card__blurb">A doubly robust estimate of the effect of food insecurity on type 2 diabetes across three NHANES cycles. The estimated effect was null. The project focuses on what can and cannot be supported by observational survey data.</p>
          <span class="pj-card__more">Read &rarr;</span>
        </a>

      </div>

    </div>
  </div>

  <div class="about-section">
    <p class="label">Personal</p>
    <h2>Outside the classroom</h2>
    <p>I live in Seattle. Away from the whiteboard, I am usually baking, fussing over my espresso setup, adding to a slowly growing ceramics collection, or spending time with my cat, <a href="#blue-photo">Blue</a>.</p>
  </div>

  <div class="about-section">
    <p>If you are curious whether I would be a good fit for your student, the <a href="/private-instruction/">private instruction page</a> has the full picture. You can also email me at <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>.</p>
  </div>

  <div id="blue-photo" class="lightbox" aria-hidden="true">
    <a href="#" class="lb-close" aria-label="Close"></a>
    <a href="#" class="lb-x" aria-label="Close">&times;</a>
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
