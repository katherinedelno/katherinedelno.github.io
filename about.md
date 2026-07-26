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
  .lightbox img{max-width:720px;max-height:85vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.35)}
  .lb-close{position:absolute;inset:0;cursor:zoom-out}

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

  <div class="about-section">
    <p class="label">Education</p>
    <h2>Academic training</h2>
    <p>The foundation of how I teach: graduate and undergraduate degrees in statistics and mathematics, with coursework spanning the full range of topics my students encounter and extending well beyond them. What matters isn't the coursework itself but the judgment it builds: seeing the structure underneath a problem, tracing an error to its real source, and explaining a topic more than one way when the first explanation doesn't land.</p>

    <h3>M.S. Statistics: Advanced Methods &amp; Data Analysis</h3>
    <p class="meta">University of Washington &middot; 2025</p>
    <p>Rigorous graduate training in modern statistical methodology, theory, and computation. My coursework covered the full theoretical inference sequence, regression methods for both independent and dependent (correlated) data, the design and analysis of experiments, categorical data analysis, and statistical computing, alongside an applied biostatistics sequence and a capstone in applied statistics. This is the foundation behind the predictive modeling, simulation, and uncertainty quantification in my research, carried out in R and Python.</p>
    <div class="pg-callout">
      <p>The University of Washington ranks <b>#3 among U.S. public universities</b>, with its Department of Statistics ranking <b>#6 in the nation</b> (U.S. News, 2026).</p>
    </div>
    <p class="pg-sub">Selected coursework</p>
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

    <h3 style="margin-top:2.2rem;">B.S. Mathematics</h3>
    <p class="meta">University of Nevada, Reno &middot; 2021 &middot; Specialization in Statistics &middot; Minor in Civil Engineering</p>
    <p>A mathematics degree with a specialization in statistics, built on a deeply proof-based core: the full calculus sequence, linear algebra, differential equations, real analysis, numerical methods, and proof writing, paired with statistics coursework in probability, statistical theory, regression and linear models, categorical data analysis, and statistical computing.</p>
    <p class="pg-sub">Mathematics &amp; statistics</p>
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
    </div>
    <p class="pg-sub">Sciences &amp; engineering</p>
    <div class="pg-tags">
      <span>General Chemistry I &amp; II</span>
      <span>Organic Chemistry</span>
      <span>Calculus-Based Physics I &amp; II</span>
      <span>General Biology</span>
      <span>Engineering Statics</span>
      <span>Fluid Dynamics</span>
    </div>
    <div class="pg-callout">
      <p>I began university as an engineering major, which gave me a broad STEM foundation across the physical and life sciences and engineering, in addition to my mathematics and statistics core. That range helps me connect ideas across subjects and meet students wherever their coursework sits.</p>
    </div>
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

    <p style="margin-top:1.6rem;">A selection of my statistical work is under <a href="/projects/">projects</a>.</p>
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
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
