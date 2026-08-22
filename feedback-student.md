---
layout: page
title: Feedback
permalink: /feedback/student/
description: "A short feedback form for students Katherine Delno has taught."
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
    <h1>Feedback from students</h1>
    <p>This is for students I have worked with. It asks how the sessions went, what actually helped, and what would have helped more.</p>
    <p>It takes about five minutes. Every question is optional, and you can leave your name off.</p>
  </div>

  <div class="fb-brief">
    <p class="label">Before you start</p>
    <dl>
      <div>
        <dt>Skip anything</dt>
        <dd>No question has to be answered. Leave blank whatever you would rather not say.</dd>
      </div>
      <div>
        <dt>Only I read this</dt>
        <dd>Answers land in a private spreadsheet. Your parents do not see them, and neither does your school.</dd>
      </div>
      <div>
        <dt>Say the awkward thing</dt>
        <dd>If something went too fast, ran long, or never quite made sense, that is the part worth writing down. It changes how I teach the next student.</dd>
      </div>
      <div>
        <dt>Thirteen questions</dt>
        <dd>Most of them are a single click. The written ones are optional and can be one line.</dd>
      </div>
    </dl>
  </div>

  {% include feedback-form.html
     form="student"
     button="Submit feedback"
     done_heading="Thank you."
     done="Your answers were recorded. Nothing further is needed. If you think of something later, write to hi@katherinedelno.com and I will add it." %}

</div>
