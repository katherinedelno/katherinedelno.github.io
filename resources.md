---
layout: page
title: Resources
permalink: /resources/
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;--faint:#9a9a97;color:var(--ink);line-height:1.6}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .7rem}

  .pg-hero{margin:0 0 1rem;max-width:60ch}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .6rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero p{font-size:1.06rem;color:var(--muted);line-height:1.55;margin:0}

  .res-filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:1.8rem}
  .res-filters[hidden],.rx-count[hidden]{display:none}
  .res-filter{font:inherit;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);background:none;border:1px solid var(--line);border-radius:999px;padding:7px 14px;cursor:pointer;transition:all .15s ease}
  .res-filter:hover{border-color:var(--accent);color:var(--accent)}
  .res-filter.is-active{background:var(--accent);border-color:var(--accent);color:#fff}
  .res-filter:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .rx-count{font-size:.72rem;color:var(--faint);letter-spacing:.06em;margin:.7rem 0 0;min-height:1.2em}

  .rx-list{max-width:72ch}
  .rx-eyebrow{font-size:.594rem;letter-spacing:.16em;text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 .35rem}
  .rx-dot{color:var(--line)}
  .rx-title{margin:0 0 .3rem;font-size:1.375rem;font-weight:500;letter-spacing:-.015em;line-height:1.25}
  .rx-title a{color:var(--ink);text-decoration:none}
  .rx-title a:hover{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;text-decoration-color:var(--faint)}
  .rx-title a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .rx-desc{font-size:.875rem;color:var(--muted);line-height:1.6;margin:0;max-width:68ch}
  .rx-entry{margin:0 0 28px}
  .rx-featured{margin:2.5rem 0 0}
  .rx-featured .rx-title{font-size:1.875rem;line-height:1.2}
  .rx-featured .rx-desc{font-size:1rem}
  .rx-section{margin-top:64px}
  .rx-featured + .rx-section{margin-top:44px}
  .rx-sechead{font-size:.594rem;letter-spacing:.16em;text-transform:uppercase;color:var(--faint);font-weight:600;border-top:1px solid var(--line);padding-top:14px;margin:0 0 26px}
  @media (prefers-reduced-motion: no-preference){
    .rx-list{transition:opacity .12s ease}
  }
  @media (max-width:480px){
    .rx-title{font-size:1.1875rem}
    .rx-featured .rx-title{font-size:1.5625rem}
    .rx-entry{margin-bottom:19px}
    .rx-section{margin-top:44px}
    .rx-featured + .rx-section{margin-top:32px}
    .rx-sechead{margin-bottom:18px}
    .pg-hero h1{font-size:1.7rem}
  }
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Writing</p>
    <h1>Notes on mathematics and statistics</h1>
    <p>Occasional writing for students: the reasoning beneath the courses, the habits that produce clean work under pressure, and previews of what waits past the AP curriculum. Written for the students I teach, and open to anyone.</p>
  </div>

  {%- comment -%} exactly one featured article; a second one breaks the build loudly {%- endcomment -%}
  {%- assign featured_posts = "" | split: "" -%}
  {%- for p in site.posts -%}
    {%- if p.featured -%}{%- assign featured_posts = featured_posts | push: p -%}{%- endif -%}
  {%- endfor -%}
  {%- if featured_posts.size > 1 -%}
    {%- include ERROR-more-than-one-featured-article -%}
  {%- endif -%}

  <div class="res-filters" role="group" aria-label="Filter articles by course" id="rx-filters" hidden>
    <button type="button" class="res-filter is-active" data-filter="all" aria-pressed="true">All</button>
    <button type="button" class="res-filter" data-filter="calculus" aria-pressed="false">AP Calculus</button>
    <button type="button" class="res-filter" data-filter="precalculus" aria-pressed="false">AP Precalculus</button>
    <button type="button" class="res-filter" data-filter="statistics" aria-pressed="false">AP Statistics</button>
    <button type="button" class="res-filter" data-filter="beyond" aria-pressed="false">Past the course</button>
  </div>
  <p class="rx-count" id="rx-count" aria-live="polite" hidden></p>

  <div class="rx-list" id="rx-list">

    {%- assign by_seq = site.posts | sort: "sequence" -%}

    {%- for p in featured_posts -%}
      {%- include resource-entry.html post=p featured=true -%}
    {%- endfor -%}

    {%- assign kind_names = "mechanics:Under exam conditions,foundations:The idea underneath,beyond:Past the course" | split: "," -%}
    {%- for pair in kind_names -%}
      {%- assign bits = pair | split: ":" -%}
      {%- assign kind = bits[0] -%}
    <section class="rx-section" data-kind="{{ kind }}">
      <h2 class="rx-sechead">{{ bits[1] }}</h2>
      {%- assign cats = "calculus,precalculus,statistics,cross" | split: "," -%}
      {%- for cat in cats -%}
        {%- for p in by_seq -%}
          {%- if p.kind != kind or p.featured -%}{%- continue -%}{%- endif -%}
          {%- capture pcat -%}{%- if p.course == "AP Precalculus" -%}precalculus{%- elsif p.course == "AP Statistics" -%}statistics{%- elsif p.course == "All courses" -%}cross{%- else -%}calculus{%- endif -%}{%- endcapture -%}
          {%- if pcat == cat -%}
            {%- include resource-entry.html post=p -%}
          {%- endif -%}
        {%- endfor -%}
      {%- endfor -%}
    </section>
    {%- endfor -%}

  </div>

  <script>
  (function(){
    var wrap = document.getElementById('rx-filters');
    var count = document.getElementById('rx-count');
    var list = document.getElementById('rx-list');
    wrap.hidden = false;   // rendered only when it can function
    count.hidden = false;
    var chips = wrap.querySelectorAll('.res-filter');
    var entries = list.querySelectorAll('.rx-entry');
    var sections = list.querySelectorAll('.rx-section');
    var valid = ['calculus','precalculus','statistics','beyond'];

    function matches(en, f){
      if(f === 'all') return true;
      if(f === 'beyond') return en.getAttribute('data-kind') === 'beyond';
      var cat = en.getAttribute('data-cat');
      if(cat === f) return true;
      if(cat === 'cross'){
        var courses = en.getAttribute('data-courses') || '';
        if(f === 'calculus') return courses.indexOf('AP Calculus') !== -1;
        if(f === 'precalculus') return courses.indexOf('AP Precalculus') !== -1;
        if(f === 'statistics') return courses.indexOf('AP Statistics') !== -1;
      }
      return false;
    }

    function apply(f){
      list.style.opacity = 0;
      var shown = 0;
      entries.forEach(function(en){
        var show = matches(en, f);
        en.style.display = show ? '' : 'none';
        if(show) shown++;
      });
      sections.forEach(function(s){
        var any = false;
        s.querySelectorAll('.rx-entry').forEach(function(en){
          if(en.style.display !== 'none') any = true;
        });
        s.style.display = any ? '' : 'none';
      });
      count.textContent = shown + (shown === 1 ? ' article' : ' articles');
      chips.forEach(function(c){
        var on = c.getAttribute('data-filter') === f;
        c.classList.toggle('is-active', on);
        c.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      requestAnimationFrame(function(){ list.style.opacity = 1; });
    }

    function fromHash(){
      var h = (location.hash || '').replace('#','');
      return valid.indexOf(h) !== -1 ? h : 'all';
    }

    chips.forEach(function(chip){
      chip.addEventListener('click', function(){
        var f = chip.getAttribute('data-filter');
        if(f === 'all'){
          history.pushState(null, '', location.pathname + location.search);
          apply('all');
        } else {
          location.hash = f;   // hashchange handler applies; back button works
        }
        chip.focus();
      });
    });
    window.addEventListener('hashchange', function(){ apply(fromHash()); });
    window.addEventListener('popstate', function(){ apply(fromHash()); });
    apply(fromHash());
  })();
  </script>

</div>
