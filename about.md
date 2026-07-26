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
      <p>I teach mathematics and statistics one-on-one, mostly AP Statistics, AP Calculus, and AP Precalculus. Before this was a practice, it was the part of every job I liked best: sitting next to someone, watching how they think through a problem, and figuring out what would actually help. I eventually decided to make that the whole job.</p>
      <p>What I care about in teaching is the distance between following an explanation and producing the reasoning yourself. Most of my students are capable people who understand things in class and then get stuck alone at the desk. Closing that gap, patiently and without drama, is the work.</p>
    </div>
    <img src="/assets/img/headshot.jpeg" alt="Katherine Delno" class="headshot" width="230" height="250" loading="lazy" decoding="async">
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
    <p>Graduate and undergraduate degrees in statistics and mathematics, with coursework spanning everything my students study and a great deal beyond it. The coursework matters less than the judgment it builds: seeing the structure underneath a problem, tracing an error to its source, and explaining a topic a second way when the first doesn't land.</p>

    <h3>M.S. Statistics: Advanced Methods &amp; Data Analysis</h3>
    <p class="deg-meta">University of Washington &middot; 2025 &middot; Statistics ranked #6 nationally, UW #3 among U.S. public universities (U.S. News, 2026)</p>
    <p>Rigorous graduate training in statistical theory, methodology, and computation. The core was the full theoretical inference sequence, where the estimators, tests, and intervals of applied statistics are derived and proved rather than taken on faith, alongside regression for independent and correlated data, the design and analysis of experiments, categorical data analysis, and statistical computing, with applied biostatistics and a capstone in applied statistics carried out in R and Python.</p>
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
    <p>A deeply proof-based mathematics core: the full calculus sequence, linear algebra, differential equations, and numerical methods, together with two semesters of real analysis, where calculus itself is rebuilt from rigorous foundations, and formal training in proof writing. This was paired with statistics coursework in probability, statistical theory, regression, and computing. I began university in engineering, which left me with a broad foundation across the physical sciences as well; it helps me meet students wherever their coursework sits.</p>
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
    <p>My teaching is grounded in years of one-on-one and university-level instruction. My current work, and full focus, is the private instruction practice.</p>

    <div class="pg-timeline">

      <div class="pg-entry current">
        <p class="date">2025 &ndash; Present</p>
        <h3>Private Mathematics &amp; Statistics Instructor <span class="badge">Current</span></h3>
        <p class="org">Independent &middot; Remote</p>
        <p>I run a private instruction practice teaching mathematics and statistics to high school and college students, with a focus on AP coursework. Each session is built around how the student actually reasons: I watch closely as they work, diagnose whether a difficulty is conceptual, procedural, or a matter of execution, and adjust the teaching to what I see. I assess not only whether a student reaches the correct answer but how they get there, using recurring patterns in their work to shape pacing, explanation, and practice over time. A complete curriculum I write myself and detailed written and verbal feedback sit behind the work, so each session builds on the last.</p>
      </div>

      <div class="pg-entry">
        <p class="date">2024</p>
        <h3>Mentor, Directed Reading Program</h3>
        <p class="org">Statistics &amp; Probability Association, University of Washington &middot; Seattle, WA</p>
        <p>Designed and led a one-on-one short course on statistical learning, covering linear regression, classification methods, resampling techniques, and regularization. Created all course materials and lectures, guided weekly discussions, and provided ongoing feedback to deepen the student's understanding throughout the quarter.</p>
      </div>

      <div class="pg-entry">
        <p class="date">2022</p>
        <h3>Graduate Teaching Assistant</h3>
        <p class="org">Department of Mathematics &amp; Statistics, University of Nevada, Reno &middot; Reno, NV</p>
        <p>Led discussion sections for an undergraduate statistics course, designed and delivered lecture materials, and provided one-on-one and group tutoring to help students understand complex statistical concepts. Graded exams and quizzes with detailed feedback, and mentored undergraduates with academic support and guidance throughout the course.</p>
      </div>

    </div>
  </div>

  <div class="about-section" id="work">
    <style>
      .work-item{margin-top:1.7rem;max-width:74ch}
      .work-item h3{font-size:1.05rem;margin:0 0 .1rem}
      .work-item .deg-meta{margin:0 0 .5rem}
      .work-item p{margin:0;font-size:.95rem}
    </style>
    <p class="label">Research</p>
    <h2>Statistical work</h2>
    <p>Alongside teaching, my graduate work included independent methodological research and applied projects in statistics and machine learning. It is the depth behind the instruction, particularly in AP Statistics.</p>

    <div class="work-item">
      <h3>A permutation-based random forest diagnostic for linear mixed models</h3>
      <p class="deg-meta">Independent research &middot; Sole author &middot; 2025</p>
      <p>A nonparametric diagnostic I designed for detecting misspecification in linear mixed models, where standard residual plots and information criteria often miss subtle violations. A random forest measures leftover structure in the model's residuals, and a permutation test that respects the clustered design supplies the null distribution, without assuming normality. Across 5,400 simulated datasets spanning 54 misspecification scenarios, the method held false-positive rates near 1&ndash;3% at a 5% level while reaching 80&ndash;100% power against large mean-structure departures, and it correctly cleared well-specified models fit to the Framingham Heart Study. Packaged as an R function.</p>
    </div>

    <div class="work-item">
      <h3>Conformal prediction for multi-label genre classification</h3>
      <p class="deg-meta">Project lead &middot; 2025</p>
      <p>Paired a fine-tuned DistilBERT with conformal prediction to assign calibrated sets of genre labels to films, targeting at least 90% coverage on held-out data. The framework generalizes to other multi-label problems, such as medical tagging and document classification.</p>
    </div>

    <div class="work-item">
      <h3>Fine-tuning BERT models for recipe classification</h3>
      <p class="deg-meta">Project lead &middot; 2025</p>
      <p>Compared fine-tuned BERT Base, BERT Large, and RoBERTa on a specialized text-classification task across more than 20,000 recipes, tuning each for generalization; the smallest model held up best on unseen data.</p>
    </div>

    <div class="work-item">
      <h3>Causal analysis of food insecurity and type 2 diabetes</h3>
      <p class="deg-meta">Project lead &middot; 2024</p>
      <p>Estimated the effect of food insecurity on type 2 diabetes across three NHANES cycles using augmented inverse probability weighting, a doubly robust estimator. The substantive finding was null; the contribution is a careful account of what cross-sectional survey data can and cannot support causally.</p>
    </div>
  </div>

  <div class="about-section">
    <p class="label">Personal</p>
    <h2>Outside the classroom</h2>
    <p>I live in Seattle. Away from the whiteboard I'm usually baking, fussing over my espresso setup, adding to a slowly growing ceramics collection, or spending time with my cat, <a href="#blue-photo">Blue</a>.</p>
  </div>

  <div class="about-section">
    <p>If you're curious whether I'd be a good fit for your student, the <a href="/private-instruction/">private instruction page</a> has the full picture, or just email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>.</p>
  </div>

  <div id="blue-photo" class="lightbox" aria-hidden="true">
    <a href="#" class="lb-close" aria-label="Close"></a>
    <a href="#" class="lb-x" aria-label="Close">&times;</a>
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
