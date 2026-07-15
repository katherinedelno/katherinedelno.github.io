---
layout: page
title: Resources
permalink: /resources/
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;color:var(--ink);line-height:1.6}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .7rem}

  .pg-hero{margin:0 0 1rem;max-width:60ch}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .6rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero p{font-size:1.06rem;color:var(--muted);line-height:1.55;margin:0}

  .res-list{margin-top:2.4rem;border-top:1px solid var(--line)}
  .pg .res-item{display:block;padding:24px 2px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
  .pg .res-item .res-title{color:var(--ink)}
  .pg .res-item:hover .res-title{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
  .pg .res-item:hover .res-more{opacity:1}
  .res-date{display:block;font-size:.72rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin:0 0 .5rem}
  .res-title{display:block;font-size:1.3rem;font-weight:700;letter-spacing:-.015em;line-height:1.22;margin:0 0 .45rem}
  .res-desc{display:block;font-size:.98rem;color:var(--muted);max-width:68ch;line-height:1.55}
  .res-more{display:inline-block;margin-top:.75rem;font-size:.74rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--accent);opacity:.7;transition:opacity .15s ease}

  @media (max-width:720px){.pg-hero h1{font-size:1.7rem}.res-title{font-size:1.18rem}}
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Writing</p>
    <h1>Notes on studying mathematics and statistics</h1>
    <p>Occasional pieces on the reasoning, notation, and habits that separate understanding a topic from executing it under exam pressure, the same things I work on with students.</p>
  </div>

  <div class="res-list">
    {% for post in site.posts %}
    <a class="res-item" href="{{ post.url | relative_url }}">
      <span class="res-date">{{ post.date | date: "%B %Y" }}</span>
      <span class="res-title">{{ post.title }}</span>
      {% if post.description %}<span class="res-desc">{{ post.description }}</span>{% endif %}
      <span class="res-more">Read &rarr;</span>
    </a>
    {% endfor %}
  </div>

</div>
