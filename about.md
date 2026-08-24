---
layout: page
title: About
permalink: /about/
description: "The academic training, teaching experience, and statistical research behind Katherine Delno's practice. M.S. Statistics, University of Washington, and B.S. Mathematics."
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
  .deg-meta{font-size:.9rem;color:var(--muted);margin:0 0 .8rem;font-weight:600;letter-spacing:.02em}
  .about-section .meta{font-size:.9rem;color:var(--muted);margin:0 0 .8rem;font-weight:600;letter-spacing:.02em}

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
    </div>
    <img src="/assets/img/headshot.jpg" alt="Katherine Delno" class="headshot" width="230" height="250" loading="lazy" decoding="async">
  </div>

  <div class="about-section" id="training">
    <p class="label">Education</p>
    <h2>Academic training</h2>

    <h3>M.S. Statistics</h3>
    <p class="deg-meta">University of Washington &middot; 2025</p>
    <p>Graduate training in statistical inference, regression for independent and correlated data, experimental design, categorical data analysis, causal inference, biostatistics, statistical learning, and statistical computing. The core was a theoretical inference sequence in which estimators, tests, and confidence intervals were derived rather than applied, alongside applied analysis in R and Python and independent methodological research in diagnostics for linear mixed models.</p>

    <h3 style="margin-top:2.2rem;">B.S. Mathematics</h3>
    <p class="deg-meta">University of Nevada, Reno &middot; 2021 &middot; Specialization in Statistics</p>
    <p>Proof-based training in mathematics, including the calculus sequence, linear algebra, differential equations, two semesters of real analysis, numerical methods, and mathematical modeling, together with probability, mathematical statistics, and regression. In real analysis, the ideas of calculus are rebuilt from rigorous definitions and proofs. This is the mathematical foundation for the graduate work in statistics that followed.</p>
  </div>

  <div class="about-section" id="statistical-work">
    <p class="label">Research</p>
    <h2>Statistical work</h2>
    <p>My graduate work included independent methodological research along with applied projects in statistical modeling, causal inference, statistical learning, and uncertainty quantification. The principal independent project, RandomForestSpecCheck, developed and evaluated a permutation-based diagnostic for detecting misspecification in linear mixed models.</p>
    <p style="margin-top:1.2rem;"><a href="/statistical-work/">View Selected Statistical Work &rarr;</a></p>
  </div>

  <div class="about-section">
    <p class="label">Professional</p>
    <h2>Experience</h2>

    <div class="pg-timeline">

      <div class="pg-entry current">
        <p class="date">2025 &ndash; Present</p>
        <h3>Private Mathematics &amp; Statistics Instructor <span class="badge">Current</span></h3>
        <p class="org">Independent Practice &middot; Remote</p>
        <p>I run an independent private practice providing one-on-one instruction in mathematics and statistics to high school and college students. I also write the curriculum, problems, worked solutions, and supporting materials the practice runs on.</p>
      </div>

      <div class="pg-entry">
        <p class="date">2024</p>
        <h3>Directed Reading Program Mentor</h3>
        <p class="org">Statistics &amp; Probability Association, University of Washington</p>
        <p>I designed and led a one-on-one directed reading course in statistical learning covering regression, classification, resampling methods, and regularization. I wrote the course materials and led weekly discussions on the statistical foundations and interpretation of the methods studied.</p>
      </div>

      <div class="pg-entry">
        <p class="date">2022</p>
        <h3>Graduate Teaching Assistant</h3>
        <p class="org">Department of Mathematics &amp; Statistics, University of Nevada, Reno</p>
        <p>I led discussion sections for an undergraduate statistics course, developed instructional materials, and evaluated coursework with attention to statistical reasoning and interpretation.</p>
      </div>

    </div>
  </div>

  <div class="about-section">
    <p>My current practice centers on private mathematics and statistics instruction, and I also accept selected statistical and quantitative projects. Details are available under <a href="/private-instruction/">Private Instruction</a> and <a href="/statistical-services/">Statistical Services</a>. I can be reached at <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>.</p>
  </div>

  <div class="about-section">
    <p class="label">Personal</p>
    <h2>Outside the classroom</h2>
    <p>I live in Seattle. Away from the whiteboard, I am usually baking, fussing over my espresso setup, adding to a slowly growing ceramics collection, or spending time with my cat, <a href="#blue-photo">Blue</a>.</p>
  </div>

  <div id="blue-photo" class="lightbox" aria-hidden="true">
    <a href="#" class="lb-close" aria-label="Close"></a>
    <a href="#" class="lb-x" aria-label="Close">&times;</a>
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
