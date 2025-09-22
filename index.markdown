---
layout: default
title: Home
permalink: /
---

<style>.page-heading{display:none}</style>

<div class="intro">
  <img src="/assets/img/headshot.JPG"
       alt="Katherine Delno headshot"
       class="headshot"
       loading="lazy" decoding="async">
  <div class="intro-text" markdown="1">
# Hi, my name is Katherine

I’m a statistician by training (M.S., University of Washington) who enjoys turning careful analysis into decisions people can actually use. I build clear, reproducible workflows in Python and R and translate results into plain language so collaborators don’t need a stats background to act. I care about honest uncertainty and work that others can re-run and trust. I’m currently exploring data scientist and machine learning roles where I can contribute that same rigor and clarity. See my [projects](/projects/), [experience](/experience/), and [education](/education/). Feel free to download my [resume](/assets/resume.pdf) or connect with me on [LinkedIn](https://www.linkedin.com/in/katherinedelno).

In parallel, I keep a small teaching practice: instructor-led one-on-one AP Statistics tutoring with limited availability. Click [here](/tutoring/) for more details.
  </div>
</div>

Outside of work, you can find me in Seattle, usually baking, tuning my espresso setup, collecting ceramics, or hanging out with my cat, [Blue](#blue-photo).

<!-- Lightbox -->
<div id="blue-photo" class="lightbox" aria-hidden="true">
  <a href="#" class="lb-close" aria-label="Close"></a>
  <img src="/assets/img/blue.jpeg" alt="Blue the cat">
</div>

<style>
  .intro { display:flex; gap:24px; align-items:flex-start; flex-wrap:wrap; margin-bottom:16px; }
  .headshot { width:200px; height:200px; border-radius:50%; object-fit:cover; flex-shrink:0; }
  .intro-text h1 { margin-top:0; }

  /* Lightbox */
  .lightbox { display:none; position:fixed; inset:0; background:rgba(0,0,0,.6);
              align-items:center; justify-content:center; padding:24px; z-index:9999; }
  .lightbox:target { display:flex; }
  .lightbox img { max-width:720px; max-height:85vh; border-radius:12px;
                  box-shadow:0 10px 30px rgba(0,0,0,.35); }
  .lb-close { position:absolute; inset:0; cursor:zoom-out; }

  @media (max-width: 700px) { .intro { flex-direction:column; } }
</style>