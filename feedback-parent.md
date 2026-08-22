---
layout: page
title: Feedback
permalink: /feedback/parent/
description: "A short feedback form for parents and guardians of students Katherine Delno has worked with."
noindex: true
sitemap: false
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--card:#fbfbfb;--faint:#9a9a97;color:var(--ink);line-height:1.6}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .7rem}

  .pg-hero{margin:0 0 1rem;max-width:62ch}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .6rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero p{font-size:1.06rem;color:var(--muted);line-height:1.55;margin:0 0 .9rem}
  .pg-hero p:last-child{margin-bottom:0}

  .fb-brief{margin:2.4rem 0 0;padding:26px 28px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
  .fb-brief .label{margin-bottom:1rem}
  .fb-brief dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 32px;margin:0}
  .fb-brief dt{font-size:.95rem;font-weight:700;letter-spacing:-.01em;margin:0 0 .25rem}
  .fb-brief dd{margin:0;font-size:.875rem;color:var(--muted);line-height:1.55}

  @media (max-width:900px){
    .fb-brief dl{grid-template-columns:1fr;gap:16px}
  }
  @media (max-width:640px){
    .pg-hero h1{font-size:1.7rem}
    .fb-brief{padding:20px}
  }
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Feedback</p>
    <h1>Feedback from families</h1>
    <p>This form is for parents and guardians of students I have taught. It asks what changed over the semester or the year, what the instruction was worth to you, and what you would want offered differently.</p>
    <p>It takes about five minutes. Every question is optional, and your answers are anonymous unless you choose to write your name at the end.</p>
  </div>

  <div class="fb-brief">
    <p class="label">Before you start</p>
    <dl>
      <div>
        <dt>Nothing is required</dt>
        <dd>Skip any question that does not apply or that you would rather not answer. A partial response is far more useful to me than none.</dd>
      </div>
      <div>
        <dt>It stays private</dt>
        <dd>Answers go to a spreadsheet only I read. They are not published, not shared with your student, and not passed to anyone else.</dd>
      </div>
      <div>
        <dt>The criticism is the useful part</dt>
        <dd>Pacing, price, communication, materials. Say the thing you would say to another parent who asked you about me.</dd>
      </div>
      <div>
        <dt>Fourteen questions</dt>
        <dd>Most of them are a single click. The written ones are there if you have something to say and blank if you do not.</dd>
      </div>
    </dl>
  </div>

  {% include feedback-form.html
     form="parent"
     button="Submit feedback"
     done_heading="Thank you."
     done="Your answers were recorded. Nothing further is needed. If you thought of something after submitting, write to hi@katherinedelno.com and I will add it to the record." %}

</div>
