---
layout: default
title: Home
permalink: /
---

<style>
  .page-heading{display:none}
  .pg{--ink:#1a1a1a;--muted:#5b6168;--line:#e7e7e3;--accent:#1f2a44;--accent-soft:#eef1f6;--card:#fbfbfa;color:var(--ink);line-height:1.6}
  .pg p{max-width:74ch}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .5rem}

  .hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 210px;column-gap:32px;align-items:center;margin-bottom:.5rem}
  .hero-grid h1{font-size:2.2rem;line-height:1.12;margin:0 0 .5rem;letter-spacing:-.01em}
  .hero-grid .tagline{font-size:1.12rem;color:var(--muted);margin:0 0 1rem;max-width:60ch}
  .hero-grid p{margin:0 0 .85rem}
  .headshot{width:210px;height:210px;border-radius:50%;object-fit:cover;opacity:1 !important;filter:none !important;-webkit-filter:none !important;mix-blend-mode:normal !important}

  .pg-btn{display:inline-block;background:var(--accent);color:#fff !important;padding:12px 24px;border-radius:10px;text-decoration:none;font-weight:600;border:1px solid var(--accent);margin-top:.4rem}
  .pg-btn:hover{opacity:.9}

  .pg-section{margin:2.6rem 0;padding-top:2.2rem;border-top:1px solid var(--line)}
  .pg-section h2{font-size:1.3rem;margin:0 0 1rem;letter-spacing:-.01em}
  .pg-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:1.1rem}
  .pg-card{border:1px solid var(--line);border-radius:14px;padding:20px;background:var(--card)}
  .pg-card h3{margin:0 0 .35rem;font-size:1.05rem}
  .pg-card p{margin:0;font-size:.94rem;color:var(--muted)}
  .pg-links{font-size:.96rem}
  .pg-personal{margin-top:2.4rem;padding-top:1.6rem;border-top:1px solid var(--line);color:var(--muted);font-size:.95rem}

  .lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);align-items:center;justify-content:center;padding:24px;z-index:9999}
  .lightbox:target{display:flex}
  .lightbox img{max-width:720px;max-height:85vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.35)}
  .lb-close{position:absolute;inset:0;cursor:zoom-out}

  @media (max-width:700px){
    .hero-grid{grid-template-columns:1fr;row-gap:18px}
    .hero-grid h1{font-size:1.8rem}
    .headshot{width:160px;height:160px;justify-self:start}
    .pg-cards{grid-template-columns:1fr}
  }
</style>

<div class="pg" markdown="0">

  <div class="hero-grid">
    <div>
      <p class="label">Private Instruction</p>
      <h1>Hi, I'm Katherine.</h1>
      <p class="tagline">I provide private, one-on-one instruction in AP Statistics, AP Calculus, and Precalculus.</p>
      <p>I run a private instruction practice focused entirely on one-on-one teaching for high school and early college students. Each session is structured and instructor-led, built around clear teaching, guided practice, and custom materials I write myself.</p>
      <p>I'm a statistician and mathematician by training, with an M.S. in Statistics from the University of Washington and a B.S. in Mathematics from the University of Nevada, Reno. That foundation lets me teach these subjects with both rigor and clarity.</p>
      <a href="/ap-stats/" class="pg-btn">Explore private instruction</a>
    </div>
    <img src="/assets/img/headshot.jpeg" alt="Katherine Delno" class="headshot" width="210" height="210" loading="lazy" decoding="async">
  </div>

  <div class="pg-section">
    <p class="label">Courses</p>
    <h2>What I teach</h2>
    <div class="pg-cards">
      <div class="pg-card"><h3>AP Statistics</h3><p>Procedure selection, condition checks, inference, and rubric-aligned statistical writing.</p></div>
      <div class="pg-card"><h3>AP Calculus (AB/BC)</h3><p>Limits, derivatives, integrals, and applications, with precise notation and AP justification.</p></div>
      <div class="pg-card"><h3>Precalculus</h3><p>Functions, trigonometry, and the analytic foundations for success in AP Calculus.</p></div>
    </div>
  </div>

  <div class="pg-section">
    <p class="label">The practice</p>
    <h2>A focused, individualized approach</h2>
    <p>This practice is my full focus. I take a limited number of students each academic year so that every session is well-prepared and individualized, and so each family receives consistent attention throughout the year. You can read more about my approach, structure, and rates on the <a href="/ap-stats/">private instruction page</a>.</p>
  </div>

  <div class="pg-section">
    <p class="label">Background</p>
    <h2>Training and experience</h2>
    <p class="pg-links">Learn more about my <a href="/experience/">teaching experience</a> and <a href="/education/">academic training</a>, or explore a selection of my <a href="/projects/">statistical work</a>. When you're ready, the best first step is to <a href="/ap-stats/">schedule a meet-and-greet</a>.</p>
  </div>

  <p class="pg-personal">I'm based in Seattle, WA. Outside of work, you'll usually find me baking, tuning my espresso setup, collecting ceramics, or hanging out with my cat, <a href="#blue-photo">Blue</a>.</p>

  <div id="blue-photo" class="lightbox" aria-hidden="true">
    <a href="#" class="lb-close" aria-label="Close"></a>
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
