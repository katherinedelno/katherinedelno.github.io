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
    align-items: center;                         /* <-- centers photo to paragraph */
  }
  .intro-grid p { margin: 0; max-width: 72ch; }

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
  <h1>Hi, my name is Katherine. Nice to meet you.</h1>

  <div class="intro-grid">
    <p>
      I’m a statistician by training (M.S., University of Washington) who enjoys turning careful analysis into decisions people can actually use. I build clear, reproducible workflows in Python and R and translate results into plain language so collaborators don’t need a stats background to act. I care about honest uncertainty and work that others can re-run and trust. I’m currently exploring data scientist and machine learning roles where I can contribute that same rigor and clarity. See my
      <a href="/projects/">recent projects</a>, <a href="/experience/">work experience</a>, and
      <a href="/education/">academic background</a>. Feel free to download my
      <a href="/assets/resume.pdf">resume</a> or connect with me on
      <a href="https://www.linkedin.com/in/katherinedelno">LinkedIn</a>.
    </p>

    <img src="/assets/img/headshot.JPG"
         alt="Katherine Delno headshot"
         class="headshot"
         width="200" height="200"
         loading="lazy" decoding="async">
  </div>
</div>

<p>
  In parallel, I keep a small teaching practice: instructor-led one-on-one AP Statistics tutoring with limited availability. Click
  <a href="/tutoring/">here</a> for more details.
</p>

<p>
  Outside of work, you can find me in Seattle, usually baking, tuning my espresso setup, collecting ceramics, or hanging out with my cat,
  <a href="#blue-photo">Blue</a>.
</p>

<!-- Lightbox -->
<div id="blue-photo" class="lightbox" aria-hidden="true">
  <a href="#" class="lb-close" aria-label="Close"></a>
  <img src="/assets/img/blue.jpeg" alt="Blue the cat">
</div>