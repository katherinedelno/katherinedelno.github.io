---
layout: page
title: About
permalink: /about/
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;color:var(--ink);line-height:1.65}
  .pg p{max-width:66ch}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .6rem}
  .about-grid{display:grid;grid-template-columns:minmax(0,1fr) 200px;column-gap:36px;align-items:start;margin:1rem 0 0}
  .about-grid h1{font-size:2.1rem;line-height:1.12;margin:0 0 .9rem;letter-spacing:-.02em;font-weight:700}
  .headshot{width:200px;height:200px;border-radius:50%;object-fit:cover}
  .about-section{margin:2.6rem 0 0;padding-top:2rem;border-top:1px solid var(--line)}
  .about-section h2{font-size:1.25rem;margin:0 0 .8rem;letter-spacing:-.01em}
  .about-section a{color:var(--ink)}
  .lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);align-items:center;justify-content:center;padding:24px;z-index:9999}
  .lightbox:target{display:flex}
  .lightbox img{max-width:720px;max-height:85vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.35)}
  .lb-close{position:absolute;inset:0;cursor:zoom-out}
  @media (max-width:700px){
    .about-grid{grid-template-columns:1fr;row-gap:18px}
    .headshot{width:150px;height:150px}
  }
</style>

<div class="pg" markdown="0">

  <div class="about-grid">
    <div>
      <p class="label">About</p>
      <h1>Hi, I'm Katherine</h1>
      <p>I teach mathematics and statistics one-on-one, mostly AP Statistics, AP Calculus, and AP Precalculus. Before this was a practice, it was just the part of every job I liked best: sitting next to someone, watching how they think through a problem, and figuring out what would actually help. I eventually decided to make that the whole job.</p>
      <p>What I care about in teaching is the distance between following an explanation and producing the reasoning yourself. Most of my students are capable people who understand things in class and then get stuck alone at the desk. Closing that gap, patiently and without drama, is the work.</p>
    </div>
    <img src="/assets/img/headshot.jpeg" alt="Katherine Delno" class="headshot" width="200" height="200" loading="lazy" decoding="async">
  </div>

  <div class="about-section">
    <h2>Training</h2>
    <p>I hold an M.S. in Statistics from the University of Washington and a B.S. in Mathematics from the University of Nevada, Reno. At UW I taught weekly discussion sections for large introductory statistics courses and mentored in the Directed Reading Program, where I designed and taught a one-on-one course in statistical learning. The details are on the <a href="/education/">education</a> and <a href="/experience/">experience</a> pages, and some of my statistical work is under <a href="/projects/">projects</a>.</p>
    <p>The graduate training matters in tutoring more than you might expect. It's what lets me tell a careless slip from a real gap, explain why a rule is true rather than just how to use it, and answer the good, odd questions students ask when they start genuinely thinking.</p>
  </div>

  <div class="about-section">
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
