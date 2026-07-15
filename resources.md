---
layout: page
title: Resources
permalink: /resources/
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#181b21;--muted:#565e69;--line:#e4e6eb;--accent:#343d4a;--accent-soft:#e5e8ee;--card:#f9fafb;color:var(--ink);line-height:1.6}
  .pg p{max-width:74ch}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .5rem}
  .pg-hero{margin:0 0 2.4rem}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .6rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero p{font-size:1.06rem;color:var(--muted);max-width:64ch;margin:0}

  .res-list{display:flex;flex-direction:column;gap:14px;margin-top:1.2rem}
  .res-item{display:block;border:1px solid var(--line);border-radius:14px;padding:20px 22px;background:var(--card);text-decoration:none;color:var(--ink);transition:border-color .15s ease,box-shadow .15s ease}
  .res-item:hover{border-color:var(--accent);box-shadow:0 5px 18px rgba(31,42,68,.06)}
  .res-date{display:block;font-size:.74rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0 0 .35rem}
  .res-title{display:block;font-size:1.12rem;font-weight:700;letter-spacing:-.01em;margin:0 0 .3rem}
  .res-desc{display:block;font-size:.95rem;color:var(--muted)}
  .res-empty{color:var(--muted);font-size:.96rem;margin-top:1.2rem}
  @media (max-width:720px){.pg-hero h1{font-size:1.7rem}}
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Resources</p>
    <h1>Notes on doing well in AP math &amp; statistics</h1>
    <p>Short, practical pieces on the setups, notation, and common mistakes that separate understanding a topic from executing it under exam conditions. Written for students and the families supporting them.</p>
  </div>

  <div class="res-list">
    {% for post in site.posts %}
    <a class="res-item" href="{{ post.url | relative_url }}">
      <span class="res-date">{{ post.date | date: "%B %-d, %Y" }}</span>
      <span class="res-title">{{ post.title }}</span>
      {% if post.description %}<span class="res-desc">{{ post.description }}</span>{% endif %}
    </a>
    {% endfor %}
  </div>

</div>
