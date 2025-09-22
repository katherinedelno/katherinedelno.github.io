---
layout: default
title: Home
permalink: /
---

<style>
  .page-heading{display:none}

  /* Put the image only beside the first paragraph */
  .intro { margin-bottom: 16px; }

  .headshot {
    float: right;                 /* sit next to paragraph 1 */
    width: 200px; height: 200px;
    border-radius: 50%;
    object-fit: cover;
    margin: .25rem 0 .5rem 24px;  /* space from the paragraph */
    shape-outside: circle(50%);   /* nicer wrap around the circle */

    /* prevent theme dimming */
    opacity: 1 !important;
    filter: none !important;
    -webkit-filter: none !important;
    mix-blend-mode: normal !important;
    box-shadow: none;
  }

  /* Start paragraph 2 below the floated image */
  .intro-text p:nth-of-type(2) { clear: both; }

  /* Lightbox */
  .lightbox { display:none; position:fixed; inset:0; background:rgba(0,0,0,.6);
              align-items:center; justify-content:center; padding:24px; z-index:9999; }
  .lightbox:target { display:flex; }
  .lightbox img { max-width:720px; max-height:85vh; border-radius:12px;
                  box-shadow:0 10px 30px rgba(0,0,0,.35); }
  .lb-close { position:absolute; inset:0; cursor:zoom-out; }

  /* Mobile: stack image above text, no float */
  @media (max-width:700px){
    .headshot { float:none; display:block; margin: 8px auto 12px; }
    .intro-text p:nth-of-type(2) { clear: none; }
  }
</style>

<div class="intro">
  <div class="intro-text" markdown="1">
# Hi, my name is Katherine

<img src="/assets/img/headshot.JPG"
     alt="Katherine Delno headshot"
     class="headshot"
     width="200" height="200"
     loading="lazy" decoding="async">

I’m a statistician by training (M.S., University of Washington) who enjoys turning careful analysis into decisions people can actually use. I build clear, reproducible workflows in Python and R and translate results into plain language so collaborators don’t need a stats background to act. I care about honest uncertainty and work that others can re-run and trust. I’m currently exploring data scientist and machine learning roles where I can contribute that same rigor and clarity. See my [recent projects](/projects/), [work experience](/experience/), and [academic background](/education/). Feel free to download my [resume](/assets/resume.pdf) or connect with me on [LinkedIn](https://www.linkedin.com/in/katherinedelno).

In parallel, I keep a small teaching practice: instructor-led one-on-one AP Statistics tutoring with limited availability. Click [here](/tutoring/) for more details.
  </div>
</div>

Outside of work, you can find me in Seattle, usually baking, tuning my espresso setup, collecting ceramics, or hanging out with my cat, [Blue](#blue-photo).

<!-- Lightbox -->
<div id="blue-photo" class="lightbox" aria-hidden="true">
  <a href="#" class="lb-close" aria-label="Close"></a>
  <img src="/assets/img/blue.jpeg" alt="Blue the cat">
</div>