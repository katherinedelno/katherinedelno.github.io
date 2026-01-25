---
layout: default
title: Home
permalink: /
---

<style>
  .page-heading{display:none}

  /* Title + first paragraph + photo */
  .hero { margin-bottom: 8px; }
  .hero h1 { margin: 0 0 .75rem; }

  .intro-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 200px; /* text | photo */
    column-gap: 24px;
    align-items: center;                         /* centers photo to paragraph */
  }
  .intro-grid p { margin: 0 0 0.75rem; max-width: 72ch; }

  .headshot {
    width: 200px; height: 200px;
    border-radius: 50%;
    object-fit: cover;
    /* prevent theme dimming */
    opacity: 1 !important;
    filter: none !important;
    -webkit-filter: none !important;
    mix-blend-mode: normal !important;
    box-shadow: none;
  }

  /* Lightbox */
  .lightbox { display:none; position:fixed; inset:0; background:rgba(0,0,0,.6);
              align-items:center; justify-content:center; padding:24px; z-index:9999; }
  .lightbox:target { display:flex; }
  .lightbox img { max-width:720px; max-height:85vh; border-radius:12px;
                  box-shadow:0 10px 30px rgba(0,0,0,.35); }
  .lb-close { position:absolute; inset:0; cursor:zoom-out; }

  /* Mobile: stack nicely */
  @media (max-width:700px){
    .intro-grid { grid-template-columns: 1fr; row-gap: 8px; }
    .headshot { justify-self: start; }
  }
</style>

<div class="hero">
  <h1>Hi, I’m Katherine.</h1>

  <div class="intro-grid">
    <div>
      <p>
        I’m a statistician by training (M.S. in Statistics, University of Washington) who now focuses on
        private, one-on-one statistics instruction for high school and early college students. I specialize
        in AP Statistics and introductory statistics, blending strong theoretical grounding with clear,
        step-by-step teaching and custom materials.
      </p>

      <p>
        In addition to my training in statistics, I’ve built hands-on teaching experience through one-on-one     instruction and mentoring in AP Statistics and introductory statistics. I enjoy translating technical ideas into clear explanations and structured practice that helps learners build real confidence. If you’re a parent or student looking
        for structured, instructor-led support in AP Statistics, you can learn more about my approach and
        rates on my <a href="/ap-stats/">premium one-on-one statistics instruction page</a>.
      </p>

      <p>
        Alongside teaching, I maintain an active interest in applied statistics, data science, and machine
        learning. I enjoy turning careful analysis into decisions people can actually use, building clear,
        reproducible workflows in Python and R, and communicating results in plain language so collaborators
        don’t need a stats background to act. I'm open to select full-time roles where I can bring that same
        rigor and clarity to an applied setting.
      </p>

      <p>
        You can explore my <a href="/projects/">recent projects</a>,
        <a href="/experience/">work experience</a>, and
        <a href="/education/">academic background</a>, or download my
        <a href="/assets/resume.pdf">resume</a> and  
        <a href="https://www.linkedin.com/in/katherinedelno">connect with me on LinkedIn</a>.
      </p>
    </div>

    <img
      src="/assets/img/headshot.jpeg"
      alt="Katherine Delno headshot"
      class="headshot"
      width="200"
      height="200"
      loading="lazy"
      decoding="async"
    >
  </div>
</div>

<p>
  I'm based in Seattle, WA. Outside of work, you'll usually find me baking, tuning my espresso setup,
  collecting ceramics, or hanging out with my cat, <a href="#blue-photo">Blue</a>.
</p>

<!-- Lightbox -->
<div id="blue-photo" class="lightbox" aria-hidden="true">
  <a href="#" class="lb-close" aria-label="Close"></a>
  <img src="/assets/img/blue.jpeg" alt="Blue the cat">
</div>