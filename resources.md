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

  .res-filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:1.8rem}
  .res-filter{font:inherit;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);background:none;border:1px solid var(--line);border-radius:999px;padding:7px 14px;cursor:pointer;transition:all .15s ease}
  .res-filter:hover{border-color:var(--accent);color:var(--accent)}
  .res-filter.is-active{background:var(--accent);border-color:var(--accent);color:#fff}

  .res-list{margin-top:1.6rem;border-top:1px solid var(--line)}
  .pg .res-item{display:block;padding:24px 2px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
  .pg .res-item .res-title{color:var(--ink)}
  .pg .res-item:hover .res-title{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
  .pg .res-item:hover .res-more{opacity:1}
  .res-date{display:block;font-size:.72rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin:0 0 .5rem}
  .res-date .res-course{color:var(--accent)}
  .res-date .res-sep{margin:0 .45em;color:var(--line)}
  .res-title{display:block;font-size:1.3rem;font-weight:700;letter-spacing:-.015em;line-height:1.22;margin:0 0 .45rem}
  .res-desc{display:block;font-size:.98rem;color:var(--muted);max-width:68ch;line-height:1.55}
  .res-more{display:inline-block;margin-top:.75rem;font-size:.74rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--accent);opacity:.7;transition:opacity .15s ease}

  @media (max-width:720px){.pg-hero h1{font-size:1.7rem}.res-title{font-size:1.18rem}}
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Writing</p>
    <h1>Notes on mathematics and statistics</h1>
    <p>Occasional writing for students: the reasoning beneath the courses, the habits that produce clean work under pressure, and previews of what waits past the AP curriculum. Written for the students I teach, and open to anyone.</p>
  </div>

  <div class="res-filters" role="tablist" aria-label="Filter articles by course">
    <button type="button" class="res-filter is-active" data-filter="all">All</button>
    <button type="button" class="res-filter" data-filter="calculus">AP Calculus</button>
    <button type="button" class="res-filter" data-filter="precalculus">AP Precalculus</button>
    <button type="button" class="res-filter" data-filter="statistics">AP Statistics</button>
    <button type="button" class="res-filter" data-filter="beyond">After the AP course</button>
  </div>

  <div class="res-list">
    {% for post in site.posts %}
    <a class="res-item" href="{{ post.url | relative_url }}" data-course="{{ post.course }}" data-section="{{ post.section | default: 'core' }}">
      <span class="res-date"><span class="res-course">{{ post.course }}</span><span class="res-sep">&bull;</span>{{ post.date | date: "%B %Y" }}</span>
      <span class="res-title">{{ post.title }}</span>
      {% if post.description %}<span class="res-desc">{{ post.description }}</span>{% endif %}
      <span class="res-more">Read &rarr;</span>
    </a>
    {% endfor %}
  </div>

  <script>
  (function(){
    var chips = document.querySelectorAll('.res-filter');
    var items = document.querySelectorAll('.res-item');
    function apply(filter){
      items.forEach(function(it){
        var course = it.getAttribute('data-course') || '';
        var section = it.getAttribute('data-section') || 'core';
        var show;
        if(filter === 'all'){ show = true; }
        else if(filter === 'beyond'){ show = section === 'beyond'; }
        else if(filter === 'calculus'){ show = section !== 'beyond' && course.indexOf('AP Calculus') !== -1; }
        else if(filter === 'precalculus'){ show = section !== 'beyond' && course === 'AP Precalculus'; }
        else if(filter === 'statistics'){ show = section !== 'beyond' && course === 'AP Statistics'; }
        it.style.display = show ? '' : 'none';
      });
    }
    chips.forEach(function(chip){
      chip.addEventListener('click', function(){
        chips.forEach(function(c){ c.classList.remove('is-active'); });
        chip.classList.add('is-active');
        apply(chip.getAttribute('data-filter'));
      });
    });
  })();
  </script>

</div>
