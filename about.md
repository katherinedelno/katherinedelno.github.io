---
layout: page
title: About
permalink: /about/
description: "About Katherine Delno, a statistician and mathematics instructor with graduate training in statistics, university teaching experience, and an independent private practice."
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
      <p>I am a statistician and mathematics instructor. I run a small independent teaching practice and also accept selected statistical and quantitative projects.</p>
      <p>I did not begin as a student who found mathematics easy. I struggled with it for years in school, and that experience still shapes the way I think about teaching. I remember what it is like for notation to feel arbitrary, for a method to seem like a sequence of rules, and for an explanation to move past the point where understanding actually stopped.</p>
    </div>
    <img src="/assets/img/headshot.jpg" alt="Katherine Delno" class="headshot" width="230" height="250" loading="lazy" decoding="async">
  </div>

  <div class="about-section">
    <p class="label">Background</p>
    <h2>From mathematics to statistics</h2>
    <p>What eventually held my attention was the structure underneath those procedures, the reasons an argument works, the assumptions a method depends on, and the way one idea connects to another. That interest led me first to mathematics and later to statistics.</p>
    <p style="margin-top:.9rem;">I earned a B.S. in Mathematics at the University of Nevada, Reno and an M.S. in Statistics at the University of Washington. Graduate study let me work more closely with statistical inference, modeling, causal questions, statistical learning, and computation, without leaving behind the mathematical structure that drew me to the subject in the first place.</p>
  </div>

  <div class="about-section">
    <p class="label">Teaching</p>
    <h2>A small teaching practice</h2>
    <p>My teaching began at the University of Nevada, Reno, where I taught undergraduate statistics as a graduate teaching assistant. Later, at the University of Washington, I designed and led a one-on-one directed reading course in statistical learning through the Statistics and Probability Association. I started my independent practice in 2025 and now work closely with a small number of students in mathematics and statistics.</p>
    <p style="margin-top:.9rem;">Working one-on-one suits the way I like to teach. Over time it becomes possible to see more than whether a student can produce a correct answer. I can pay attention to how a problem is being organized, where the reasoning becomes uncertain, which errors recur, and whether an idea remains available when the form of the problem changes.</p>
    <p style="margin-top:.9rem;">That continuity is one reason I keep the practice deliberately small.</p>
    <p style="margin-top:1.2rem;"><a href="/private-instruction/">More about private instruction &rarr;</a></p>
  </div>

  <div class="about-section" id="training">
    <p class="label">Education</p>
    <h2>Academic training</h2>

    <h3>M.S. Statistics</h3>
    <p class="deg-meta">University of Washington &middot; 2025</p>
    <p>Graduate training in statistical inference, regression for independent and correlated data, experimental design, categorical data analysis, causal inference, biostatistics, statistical learning, and statistical computing. The core was a theoretical inference sequence in which estimators, tests, and confidence intervals were derived rather than applied, alongside applied analysis in R and Python.</p>

    <h3 style="margin-top:2.2rem;">B.S. Mathematics</h3>
    <p class="deg-meta">University of Nevada, Reno &middot; 2021 &middot; Specialization in Statistics</p>
    <p>Proof-based training that included the calculus sequence, linear algebra, differential equations, two semesters of real analysis, numerical methods, and mathematical modeling, along with probability, mathematical statistics, and regression. In real analysis, the ideas of calculus are rebuilt from rigorous definitions and proofs. This is the mathematical foundation for the graduate work in statistics that followed.</p>
  </div>

  <div class="about-section" id="statistical-work">
    <p class="label">Research</p>
    <h2>Statistical work</h2>
    <p>My graduate work included independent methodological research and applied projects in statistical modeling, causal inference, statistical learning, and uncertainty quantification. My principal independent project, RandomForestSpecCheck, developed and evaluated a permutation-based diagnostic for misspecification in linear mixed models.</p>
    <p style="margin-top:1.2rem;"><a href="/statistical-work/">View Selected Statistical Work &rarr;</a></p>
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
