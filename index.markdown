---
layout: default
title: Home
permalink: /
---

<style>
  .page-heading{display:none}

  /* Title + first paragraph + photo */
  .hero { margin-bottom: 8px; }
  .hero h1 { margin: 0 0 .5rem; }

  .lede-row {
    display: flex;
    align-items: center;      /* centers photo vertically to the first paragraph */
    gap: 24px;
    flex-wrap: wrap;
  }
  .lede {
    flex: 1;
    min-width: 280px;
    max-width: 72ch;
    margin: 0;                /* true centering against this paragraph */
  }
  .headshot {
    width: 200px; height: 200px;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;

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

  @media (max-width:700px){
    .lede-row { flex-direction: column; align-items: flex-start; }
    .headshot { margin-top: 8px; }
  }
</style>

<div class="hero">
  <h1>Hi, my name is Katherine</h1>

  <!-- First paragraph + photo side-by-side -->
  <div class="lede-row" markdown="1">
    <p class="lede">
      I’m a statistician by training (M.S., University of Washington) who enjoys turning careful analysis into decisions people can actually use. I build clear, reproducible workflows in Python and R and translate results into plain language so collaborators don’t need a stats background to act. I care about honest uncertainty and work that others can re-run and trust. I’m currently exploring data scientist and machine learning roles where I can contribute that same rigor and clarity. See my [recent projects](/projects/), [work experience](/experience/), and [academic background](/education/). Feel free to download my [resume](/assets/resume.pdf) or connect with me on [LinkedIn](https://www.linkedin.com/in/katherinedelno).
    </p>

    <img src="/assets/img/headshot.JPG"
         alt="Katherine Delno headshot"
         class="headshot"
         width="200" height="200"
         loading="lazy" decoding="async">
  </div>
</div>

In parallel, I keep a small teaching practice: instructor-led one-on-one AP Statistics tutoring with limited availability. Click [here](/tutoring/) for more details.

Outside of work, you can find me in Seattle, usually baking, tuning my espresso setup, collecting ceramics, or hanging out with my cat, [Blue](#blue-photo).

<!-- Lightbox -->
<div id="blue-photo" class="lightbox" aria-hidden="true">
  <a href="#" class="lb-close" aria-label="Close"></a>
  <img src="/assets/img/blue.jpeg" alt="Blue the cat">
</div>