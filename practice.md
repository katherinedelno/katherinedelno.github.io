---
layout: page
title: Practice
permalink: /practice/
description: "AP practice sets with full solutions for AP Calculus AB and BC, AP Precalculus, and AP Statistics. Multiple choice and free response, built to the May 2027 exam format."
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;--faint:#9a9a97;color:var(--ink);line-height:1.6}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .7rem}

  .pg-hero{margin:0 0 1rem;max-width:60ch}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .6rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero p{font-size:1.06rem;color:var(--muted);line-height:1.55;margin:0 0 .9rem}
  .pg-hero p:last-child{margin-bottom:0}

  /* The standard. This is the part that distinguishes these pages from the
     free practice a student has already found, so it sits above the grid. */
  .px-standard{margin:2.4rem 0 0;padding:26px 28px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
  .px-standard .label{margin-bottom:1rem}
  .px-standard dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 32px;margin:0}
  .px-standard dt{font-size:.95rem;font-weight:700;letter-spacing:-.01em;margin:0 0 .25rem}
  .px-standard dd{margin:0;font-size:.875rem;color:var(--muted);line-height:1.55}

  .res-filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:2.4rem}
  .res-filters[hidden]{display:none}
  .res-filter{font:inherit;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);background:none;border:1px solid var(--line);border-radius:999px;padding:7px 14px;cursor:pointer;transition:all .15s ease}
  .res-filter:hover{border-color:var(--accent);color:var(--accent)}
  .res-filter.is-active{background:var(--accent);border-color:var(--accent);color:#fff}
  .res-filter:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .rxm-live{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}

  .rxm-section{margin-top:96px;scroll-margin-top:24px}
  .rxm-section:first-of-type{margin-top:56px}
  .rxm-sechead{border-top:1px solid var(--line);padding-top:18px;margin:0 0 24px;display:flex;align-items:baseline;gap:16px;flex-wrap:wrap}
  .rxm-secname{font-size:1.625rem;font-weight:700;letter-spacing:-.02em;margin:0}
  .rxm-seccount{font-size:.72rem;color:var(--faint);letter-spacing:.06em;margin:0}

  .rxm-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
  .pg .rxm-box{grid-column:span 1;display:block;border:1px solid var(--line);border-radius:10px;padding:22px;text-decoration:none;color:var(--ink);background:transparent;transition:border-color .12s ease}
  .pg .rxm-box:hover,.pg .rxm-box:focus-visible{border-color:var(--accent);outline:none}
  .pg .rxm-box:hover .rxm-title,.pg .rxm-box:focus-visible .rxm-title{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;text-decoration-color:var(--faint)}
  .rxm-eyebrow{font-size:.594rem;letter-spacing:.16em;text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 .55rem}
  .rxm-eyebrow span+span::before{content:"\00B7";margin:0 .6em;color:var(--line)}
  .rxm-title{font-size:1.1875rem;font-weight:700;letter-spacing:-.015em;line-height:1.3;margin:0 0 .4rem}
  .rxm-blurb{font-size:.84375rem;color:var(--muted);line-height:1.55;margin:0 0 .7rem}
  .rxm-count{font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0}

  .px-empty{border:1px dashed var(--line);border-radius:10px;padding:22px;color:var(--muted);font-size:.9rem;margin:0}

  .px-foot{margin-top:96px;padding-top:24px;border-top:1px solid var(--ink);max-width:70ch;font-size:.95rem;color:var(--muted)}
  .px-foot p{margin:0 0 .9rem}
  .px-foot p:last-child{margin:0}
  .px-foot a{color:var(--ink)!important;text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;text-decoration-color:var(--faint)}

  @media (max-width:900px){
    .rxm-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
    .px-standard dl{grid-template-columns:1fr;gap:16px}
  }
  @media (max-width:640px){
    .rxm-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
    .rxm-section{margin-top:64px}
    .rxm-sechead{margin-bottom:18px}
    .rxm-secname{font-size:1.375rem}
    .pg .rxm-box{padding:14px}
    .rxm-title{font-size:1rem}
    .rxm-blurb{font-size:.78125rem}
    .pg-hero h1{font-size:1.7rem}
    .px-standard{padding:20px}
  }
  @media (prefers-reduced-motion: reduce){
    .pg .rxm-box,.res-filter{transition:none}
  }
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Practice</p>
    <h1>Problems, worked the way they are scored</h1>
    <p>Each set below is a single archetype: the questions the exam asks about one idea, in the proportions and under the conditions it asks them. Multiple choice split into a no-calculator part and a calculator part, then free response with rubric points attached.</p>
    <p>These are written for my own students and left open for anyone. Work a set cold and timed before reading a solution.</p>
  </div>

  <div class="px-standard">
    <p class="label">The standard</p>
    <dl>
      <div>
        <dt>Every distractor is named</dt>
        <dd>A wrong option here is not filler. Each one is generated by a specific error, and the solution says which error it is, so a missed question tells you what to fix rather than only that you missed it.</dd>
      </div>
      <div>
        <dt>Every free-response part carries its points</dt>
        <dd>Each set shows how the nine points of a question are actually distributed, including the ones awarded for units, for naming a procedure, and for a justification rather than an answer.</dd>
      </div>
      <div>
        <dt>Built to the May 2027 format</dt>
        <dd>Counts, timing, calculator rules, and the number of free-response questions follow the current Course and Exam Description for each course, including the revisions that took effect in fall 2026.</dd>
      </div>
      <div>
        <dt>Every value recomputed</dt>
        <dd>Correct answers and incorrect options alike are verified independently before a set is published, so the error named under a distractor is the error that produces it.</dd>
      </div>
    </dl>
  </div>

  <div class="res-filters" role="group" aria-label="Jump to a course section" id="rxm-filters" hidden>
    <button type="button" class="res-filter is-active" data-target="top" aria-pressed="true">All</button>
    <button type="button" class="res-filter" data-target="calculus" aria-pressed="false">AP Calculus</button>
    <button type="button" class="res-filter" data-target="precalculus" aria-pressed="false">AP Precalculus</button>
    <button type="button" class="res-filter" data-target="statistics" aria-pressed="false">AP Statistics</button>
  </div>
  <p class="rxm-live" aria-live="polite" id="rxm-live"></p>

  {%- comment -%}
    Course bands, keyed the same way the resources page keys them, so a page
    tagged "AP Calculus AB & BC" lands in the Calculus band without any extra
    front matter. Sorting is by `sequence` within a band, which follows the
    order the material is taught rather than the order the sets were written.
  {%- endcomment -%}
  {%- assign all = site.practice | sort: "sequence" -%}
  {%- assign secdefs = "calculus|AP Calculus,precalculus|AP Precalculus,statistics|AP Statistics" | split: "," -%}
  {%- for sd in secdefs -%}
    {%- assign bits = sd | split: "|" -%}
    {%- assign cat = bits[0] -%}
    {%- assign name = bits[1] -%}
    {%- assign items = "" | split: "" -%}
    {%- for p in all -%}
      {%- capture pcat -%}{%- if p.course == "AP Precalculus" -%}precalculus{%- elsif p.course == "AP Statistics" -%}statistics{%- else -%}calculus{%- endif -%}{%- endcapture -%}
      {%- if pcat == cat -%}{%- assign items = items | push: p -%}{%- endif -%}
    {%- endfor -%}
  <section class="rxm-section" id="sec-{{ cat }}" data-cat="{{ cat }}" aria-label="{{ name }}">
    <div class="rxm-sechead">
      <h2 class="rxm-secname">{{ name }}</h2>
      <p class="rxm-seccount">{{ items.size }} {% if items.size == 1 %}set{% else %}sets{% endif %}</p>
    </div>
    {%- if items.size == 0 -%}
    <p class="px-empty">In preparation. The essays for this course are on the <a href="{{ "/resources/" | relative_url }}">resources page</a> in the meantime.</p>
    {%- else -%}
    <div class="rxm-grid">
      {%- for p in items -%}
      {%- assign mcq = p.mcq_no_calc | plus: p.mcq_calc -%}
      <a class="rxm-box" href="{{ p.url | relative_url }}">
        <p class="rxm-eyebrow">
          {%- if p.course == "AP Calculus AB & BC" -%}<span>AB &amp; BC</span>
          {%- elsif p.course == "AP Calculus AB" -%}<span>AB</span>
          {%- elsif p.course == "AP Calculus BC" -%}<span>BC</span>{%- endif -%}
          {%- if p.ced_topics %}<span>CED {{ p.ced_topics | join: ", " }}</span>{% endif -%}
        </p>
        <p class="rxm-title">{{ p.title }}</p>
        <p class="rxm-blurb">{{ p.blurb }}</p>
        <p class="rxm-count">{{ mcq }} multiple choice &middot; {{ p.frq_count }} free response</p>
      </a>
      {%- endfor -%}
    </div>
    {%- endif -%}
  </section>
  {%- endfor -%}

  <div class="px-foot">
    <p>The sets are written fresh for this page. Nothing here is drawn from the assessments my own students sit, and nothing here is a reprint of a released College Board exam.</p>
    <p>If an answer here looks wrong to you, it is worth telling me: <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>. Corrections are made the same week.</p>
  </div>

  <script>
  (function(){
    var wrap = document.getElementById('rxm-filters');
    wrap.hidden = false;   // rendered only when it can function
    var chips = wrap.querySelectorAll('.res-filter');
    var live = document.getElementById('rxm-live');
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function countOf(t){ return document.querySelectorAll('#sec-' + t + ' .rxm-box').length; }
    function activate(t){
      chips.forEach(function(c){
        var on = c.getAttribute('data-target') === t;
        c.classList.toggle('is-active', on);
        c.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
    }

    chips.forEach(function(chip){
      chip.addEventListener('click', function(){
        var t = chip.getAttribute('data-target');
        activate(t);
        if(t === 'top'){
          history.pushState(null, '', location.pathname + location.search);
          window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
          live.textContent = 'All sections, ' + document.querySelectorAll('.rxm-box').length + ' sets';
        } else {
          location.hash = 'sec-' + t;   // browser scrolls; back button works
          live.textContent = chip.textContent + ', ' + countOf(t) + ' sets';
        }
        chip.focus({ preventScroll: true });
      });
    });

    var m = (location.hash || '').match(/^#sec-(\w+)$/);
    if(m) activate(m[1]);
    window.addEventListener('hashchange', function(){
      var h = (location.hash || '').match(/^#sec-(\w+)$/);
      activate(h ? h[1] : 'top');
    });
  })();
  </script>

</div>
