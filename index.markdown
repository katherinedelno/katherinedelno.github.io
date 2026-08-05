---
layout: default
title: Home
permalink: /
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&display=swap');
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;color:var(--ink);line-height:1.65}
  .pg p{max-width:66ch}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .6rem}

  .hero{margin:2.2rem 0 0}
  .hero h1{font-size:3.1rem;line-height:1.08;margin:0 0 1.3rem;letter-spacing:-.028em;font-weight:700;max-width:18ch}
  .hero .lede{font-size:1.02rem;color:var(--muted);margin:0 0 1.6rem;max-width:60ch;line-height:1.7}
  .pg-btn{display:inline-block;background:var(--accent);color:#fff !important;padding:12px 22px;border-radius:8px;text-decoration:none;font-weight:600}
  .pg-btn:hover{opacity:.88}
  .btn-row{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
  .btn-row-reg{display:flex;gap:12px;flex-wrap:wrap;margin-top:1rem}
  @media (max-width:560px){
    .btn-row-reg{flex-direction:column;align-items:stretch}
    .btn-row-reg .pg-btn{text-align:center}
  }
  .btn-row .quiet{font-size:.97rem;color:var(--muted)}
  .btn-row .quiet a{color:var(--ink)}

  .pg h1,.pg h2,.pg h3{font-weight:700}
  .pg b,.pg strong{font-weight:600}
  .pg-section{margin:3rem 0 0;padding-top:2.2rem;border-top:1px solid var(--line)}
  .pg-section h2{font-size:1.28rem;margin:0 0 .8rem;letter-spacing:-.01em}
  .pg-close{margin:3rem 0 1rem;padding-top:2rem;border-top:1px solid var(--line);color:var(--muted);font-size:.98rem}
  .pg-close a{color:var(--ink)}

  @media (max-width:700px){
    .hero h1{font-size:2.4rem;line-height:1.1}
  }
</style>

<div class="pg" markdown="0">

  <div class="hero">
    <h1>Mathematics and statistics, taught one student at a time.</h1>
    <p class="lede">This is a private teaching practice devoted to the careful study of mathematics and statistics. I work with a small number of students each year, in <b>AP&nbsp;Statistics</b>, <b>AP&nbsp;Calculus&nbsp;AB/BC</b>, and <b>AP&nbsp;Precalculus</b>, through the full arc of a course. I hold an M.S. in Statistics from the University of Washington and a B.S. in Mathematics, and I have found that most difficulty in mathematics is specific, findable, and fixable, provided someone is paying close enough attention.</p>
    <div class="btn-row">
      <a href="/private-instruction/" class="pg-btn">Private instruction &amp; rates</a>
      <span class="quiet">or email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a></span>
    </div>
  </div>

  <div class="pg-section">
    <h2>The practice</h2>
    <p>Sessions are spent working, not watching. We solve problems together so that I can see the reasoning as it forms, in the setup, the notation, and the hesitations, and then I step away and let the student work alone, because that is the only honest measure of what has taken hold. I keep detailed notes from week to week; over a term, the instruction grows more precise as the picture of how a student thinks fills in.</p>
    <p style="margin-top:.9rem;">The structure of sessions, the materials, and rates are set out under <a href="/private-instruction/">private instruction</a>. There is also a short page <a href="/about/">about me</a>.</p>
  </div>

  <div class="pg-section">
    <h2>This August</h2>
    <p>As the school year gets underway, I am giving two free 45-minute sessions on starting the year well: <b>AP&nbsp;Statistics on Tuesday, August&nbsp;25</b>, and <b>AP&nbsp;Calculus on Thursday, August&nbsp;27</b>, both at <b>5:30&nbsp;p.m. Pacific</b>. Those who register receive the getting-started guide for their course within a day, whether or not they attend.</p>
    <div class="btn-row-reg">
      <a href="https://us06web.zoom.us/meeting/register/IeqFGjh3Q7OnCN5nYqqrtw" class="pg-btn" target="_blank" rel="noopener">Register &mdash; AP Statistics, Aug 25</a>
      <a href="https://us06web.zoom.us/meeting/register/vAjK5wd5S4edqx6cp6egKQ" class="pg-btn" target="_blank" rel="noopener">Register &mdash; AP Calculus, Aug 27</a>
    </div>
  </div>

  {% include subscribe.html
     heading="The getting-started guide for your course"
     blurb="Before the term begins I send a short guide for each course: the habits that make the year go well, the setup of calculator and notation, how the course and exam are structured, and the early mistakes most worth avoiding. Choose a course and I'll send it. No charge, and nothing else follows."
     button="Send the guide"
     done="Thank you. I'll send the guide to that address shortly."
     choose="true" %}

  <div class="pg-close">
    <p>Writing for students is collected under <a href="/resources/">resources</a>; my background and statistical work are under <a href="/about/">about</a>. The roster for the academic year is small, and it fills. Families considering the fall are welcome to <a href="mailto:hi@katherinedelno.com">write</a>.</p>
  </div>

</div>
