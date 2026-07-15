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
  .pg{--ink:#181b21;--muted:#565e69;--line:#e4e6eb;--accent:#343d4a;--accent-soft:#e5e8ee;--card:#f9fafb;color:var(--ink);line-height:1.6}
  .pg p{max-width:74ch}
  .pg h1,.pg h2,.pg h3,.pg h4{font-weight:700}
  .pg b,.pg strong{font-weight:600}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .5rem}

  .hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 210px;column-gap:32px;align-items:center;margin-bottom:.5rem}
  .hero-grid h1{font-size:2.2rem;line-height:1.12;margin:0 0 .5rem;letter-spacing:-.02em;font-weight:700}
  .hero-grid .tagline{font-size:1.12rem;color:var(--muted);margin:0 0 1rem;max-width:60ch}
  .hero-grid p{margin:0 0 .85rem}
  .headshot{width:210px;height:210px;border-radius:50%;object-fit:cover;opacity:1 !important;filter:none !important;-webkit-filter:none !important;mix-blend-mode:normal !important}

  .pg-btn{display:inline-block;background:var(--accent);color:#fff !important;padding:12px 24px;border-radius:10px;text-decoration:none;font-weight:600;border:1px solid var(--accent);margin-top:.4rem}
  .pg-btn:hover{opacity:.9}
  .pg-btn-outline{display:inline-block;background:transparent;color:var(--accent) !important;padding:12px 24px;border-radius:10px;text-decoration:none;font-weight:600;border:1px solid var(--accent);margin-top:.4rem}
  .pg-btn-outline:hover{background:var(--accent-soft)}
  .pg-btn-row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
  .pg-cta-actions{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:0 0 .9rem}
  .pg-cta-email{margin:.2rem auto 0;font-size:.95rem;color:var(--muted)}
  .hero-teach-label{font-weight:700;color:var(--ink);margin:.2rem 0 .45rem !important}
  .hero-teach{list-style:none;padding:0;margin:0 0 .4rem;display:flex;flex-direction:column;gap:.32rem}
  .hero-teach li{position:relative;padding-left:1.15rem;font-weight:600;color:var(--ink);font-size:1.02rem}
  .hero-teach li::before{content:"";position:absolute;left:0;top:.52em;width:7px;height:7px;border-radius:2px;background:var(--accent)}
  .hero-teach-note{font-size:.92rem;color:var(--muted);margin:.15rem 0 1.1rem !important}

  .pg-section{margin:2.6rem 0;padding-top:2.2rem;border-top:1px solid var(--line)}
  .pg-section h2{font-size:1.3rem;margin:0 0 1rem;letter-spacing:-.01em}
  .pg-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:1.1rem}
  .pg-card{border:1px solid var(--line);border-radius:14px;padding:20px;background:var(--card)}
  .pg-card h3{margin:0 0 .35rem;font-size:1.05rem}
  .pg-card p{margin:0;font-size:.94rem;color:var(--muted)}
  .pg-links{font-size:.96rem}
  .pg-personal{margin-top:2.4rem;padding-top:1.6rem;border-top:1px solid var(--line);color:var(--muted);font-size:.95rem}

  .pg-note{margin-top:1.1rem;padding:20px 24px;background:var(--accent-soft);border-radius:12px}
  .pg-note p{margin:0;max-width:none}
  .pg-note .pg-btn{margin-top:1rem}
  .pg-quote{margin-top:1.2rem;border-left:3px solid var(--accent);padding:2px 0 2px 18px}
  .pg-quote p{margin:0 0 .45rem;font-size:1rem;font-style:italic}
  .pg-quote .who{font-size:.84rem;color:var(--muted);font-weight:600}
  .pg-cta{text-align:center;margin:2.8rem 0 .5rem;padding:2.4rem 1rem;background:var(--accent-soft);border-radius:16px}
  .pg-cta h2{margin:0 0 .5rem}
  .pg-cta p{margin:0 auto 1.3rem;color:var(--muted);max-width:54ch}

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
      <p class="label">Private Mathematics &amp; Statistics Instructor</p>
      <h1>Hi, I'm Katherine</h1>
      <p>I run a private instruction practice focused entirely on one-on-one work in mathematics and statistics with high school and college students. My work centers on how each student actually thinks: I watch closely while they solve problems, find what is really getting in the way, and teach until they can reason through it on their own.</p>
      <p>I'm a statistician and mathematician by training, with an M.S. in Statistics from the University of Washington and a B.S. in Mathematics from the University of Nevada, Reno. That depth is what lets me see the structure underneath a problem, tell a careless slip apart from a real gap, and teach with precision rather than from a script. AP coursework is where I focus most of my work.</p>
      <p class="hero-teach-label">Courses I teach</p>
      <ul class="hero-teach">
        <li>AP Statistics</li>
        <li>AP Calculus (AB/BC)</li>
        <li>AP Precalculus</li>
      </ul>
      <div class="pg-btn-row">
        <a href="/private-instruction/" class="pg-btn">Explore private instruction</a>
        <a href="mailto:hi@katherinedelno.com" class="pg-btn-outline">Email me</a>
      </div>
    </div>
    <img src="/assets/img/headshot.jpeg" alt="Katherine Delno" class="headshot" width="210" height="210" loading="lazy" decoding="async">
  </div>

  <div class="pg-section">
    <p class="label">The difference</p>
    <h2>More than getting unstuck</h2>
    <p>A clear explanation is easy to find. Harder to find is someone who watches how your student works, notices the mistake behind the mistake, and adjusts the teaching in real time based on what they see. That is the center of my practice.</p>
    <p>We work through problems together so I can follow the reasoning as it unfolds: the setup, the notation, where they hesitate, which errors keep returning. Then I step back and let the student work on their own, because understanding isn't following along while I explain. It's producing the reasoning when the help is gone.</p>
  </div>

  <div class="pg-section">
    <p class="label">Free this summer</p>
    <h2>Webinars on succeeding in each course</h2>
    <p>Before the school year begins, I'm hosting two free 45-minute webinars on how to start the year strong: one for <b>AP Statistics on Tuesday, August 25</b>, and one for <b>AP Calculus (AB/BC) on Thursday, August 27</b>, both at <b>5:30 p.m. Pacific</b>. Everyone who registers also receives my getting-started guide for that course. It covers how to begin the year on the right foot, from mindset and study habits to the technical setup and exam structure, and it's free to keep whether or not you attend live. Studying AP Precalculus? Register as well and I'll send you the Precalc getting-started guide.</p>
    <a href="https://forms.gle/PMQRaH75zCRBTLg3A" class="pg-btn" style="margin-top:1.1rem;" target="_blank" rel="noopener">Register for a free webinar</a>
  </div>

  <div class="pg-section">
    <p class="label">The practice</p>
    <h2>Why I keep the roster small</h2>
    <p>I take a limited number of students each academic year because good instruction depends on attention before, during, and after each session, and on carrying what I learn from one week into the next. Over time I come to know the patterns in a student's work: where they rush, what they forget, which errors return. The instruction gets more precise the longer we work together. The strongest results come when we start at the beginning of the course, so spots are best reserved before the term begins. You can read more about my approach, structure, and rates on the <a href="/private-instruction/">private instruction page</a>.</p>
    <div class="pg-quote">
      <p>&ldquo;Katherine is an attentive, thoughtful, and highly effective tutor. She helped my daughter build both confidence and understanding, making challenging material feel approachable.&rdquo;</p>
      <span class="who">Parent of 2025 AP Statistics student</span>
    </div>
  </div>

  <div class="pg-section">
    <p class="label">Background</p>
    <h2>Training and experience</h2>
    <p class="pg-links">Learn more about my <a href="/experience/">teaching experience</a> and <a href="/education/">academic training</a>, or explore a selection of my <a href="/projects/">statistical work</a>. When you're ready, head to <a href="/private-instruction/">private instruction</a> or <a href="mailto:hi@katherinedelno.com">email me</a>.</p>
  </div>

  <div class="pg-section">
    <p class="label">A little about me</p>
    <h2>Beyond teaching</h2>
    <p>I'm based in Seattle, WA. Outside of work, you'll usually find me baking, tuning my espresso setup, collecting ceramics, or hanging out with my cat, <a href="#blue-photo">Blue</a>.</p>
  </div>

  <div class="pg-cta">
    <h2>Ready to talk?</h2>
    <p>The <strong>Private Instruction</strong> page has everything in detail: my approach, session structure, rates, and FAQ. Or send a quick email and I'll get right back to you. I take a limited number of students each year, so reaching out early is best.</p>
    <div class="pg-cta-actions">
      <a href="/private-instruction/" class="pg-btn">See private instruction &amp; rates</a>
      <a href="mailto:hi@katherinedelno.com" class="pg-btn-outline">Email me directly</a>
    </div>
    <p class="pg-cta-email">or email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a></p>
  </div>

  <div id="blue-photo" class="lightbox" aria-hidden="true">
    <a href="#" class="lb-close" aria-label="Close"></a>
    <img src="/assets/img/blue.jpeg" alt="Blue the cat">
  </div>

</div>
