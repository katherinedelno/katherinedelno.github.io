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
  .res-filters[hidden]{display:none}
  .res-filter{font:inherit;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);background:none;border:1px solid var(--line);border-radius:999px;padding:7px 14px;cursor:pointer;transition:all .15s ease}
  .res-filter:hover{border-color:var(--accent);color:var(--accent)}
  .res-filter.is-active{background:var(--accent);border-color:var(--accent);color:#fff}
  .res-filter:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .rxm-live{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}

  .rxm-section{margin-top:96px;scroll-margin-top:24px}
  .rxm-section:first-of-type{margin-top:56px}
  .rxm-sechead{border-top:1px solid var(--line);padding-top:18px;margin:0 0 24px;display:flex;align-items:baseline;gap:16px}
  .rxm-secname{font-size:1.625rem;font-weight:700;letter-spacing:-.02em;margin:0}
  .rxm-seccount{font-size:.72rem;color:var(--faint);letter-spacing:.06em;margin:0}

  .rxm-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
  .pg .rxm-box{grid-column:span 1;display:block;border:1px solid var(--line);border-radius:10px;padding:22px;text-decoration:none;color:var(--ink);background:transparent;transition:border-color .12s ease}
  .pg .rxm-feat{grid-column:span 2;padding:26px}
  .pg .rxm-box:hover,.pg .rxm-box:focus-visible{border-color:var(--accent);outline:none}
  .pg .rxm-box:hover .rxm-title,.pg .rxm-box:focus-visible .rxm-title{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;text-decoration-color:var(--faint)}
  .rxm-eyebrow{font-size:.594rem;letter-spacing:.16em;text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 .55rem}
  .rxm-eyebrow span+span::before{content:"\00B7";margin:0 .6em;color:var(--line)}
  .rxm-title{font-size:1.1875rem;font-weight:700;letter-spacing:-.015em;line-height:1.3;margin:0 0 .4rem}
  .rxm-blurb{font-size:.84375rem;color:var(--muted);line-height:1.55;margin:0}
  .rxm-feat .rxm-title{font-size:1.6875rem;line-height:1.2}
  .rxm-feat .rxm-blurb{font-size:.9375rem;max-width:62ch}

  @media (max-width:900px){
    .rxm-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
    .pg .rxm-feat{grid-column:1 / -1}
  }
  @media (max-width:640px){
    .rxm-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
    .rxm-section{margin-top:64px}
    .rxm-sechead{margin-bottom:18px}
    .rxm-secname{font-size:1.375rem}
    .pg .rxm-box{padding:14px}
    .pg .rxm-feat{padding:18px}
    .rxm-title{font-size:1rem}
    .rxm-blurb{font-size:.78125rem}
    .rxm-feat .rxm-title{font-size:1.375rem}
    .rxm-feat .rxm-blurb{font-size:.875rem}
    .pg-hero h1{font-size:1.7rem}
  }
  @media (prefers-reduced-motion: reduce){
    .pg .rxm-box,.res-filter{transition:none}
  }
</style>

<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Writing</p>
    <h1>Notes on mathematics and statistics</h1>
    <p>Occasional writing for students: the reasoning beneath the courses, the habits that produce clean work under pressure, and previews of what waits past the AP curriculum. Written for the students I teach, and open to anyone.</p>
  </div>

  <div class="res-filters" role="group" aria-label="Jump to a course section" id="rxm-filters" hidden>
    <button type="button" class="res-filter is-active" data-target="top" aria-pressed="true">All</button>
    <button type="button" class="res-filter" data-target="calculus" aria-pressed="false">AP Calculus</button>
    <button type="button" class="res-filter" data-target="precalculus" aria-pressed="false">AP Precalculus</button>
    <button type="button" class="res-filter" data-target="statistics" aria-pressed="false">AP Statistics</button>
    <button type="button" class="res-filter" data-target="past" aria-pressed="false">Looking ahead</button>
  </div>
  <p class="rxm-live" aria-live="polite" id="rxm-live"></p>

  {%- assign by_seq = site.posts | sort: "sequence" -%}
  {%- assign secdefs = "calculus|AP Calculus,precalculus|AP Precalculus,statistics|AP Statistics,past|Looking ahead" | split: "," -%}
  {%- for sd in secdefs -%}
    {%- assign bits = sd | split: "|" -%}
    {%- assign cat = bits[0] -%}
    {%- assign items = "" | split: "" -%}
    {%- for p in by_seq -%}
      {%- capture pcat -%}{%- if p.kind == "beyond" -%}past{%- elsif p.course == "AP Precalculus" -%}precalculus{%- elsif p.course == "AP Statistics" -%}statistics{%- else -%}calculus{%- endif -%}{%- endcapture -%}
      {%- if pcat == cat -%}{%- assign items = items | push: p -%}{%- endif -%}
    {%- endfor -%}
    {%- assign feats = "" | split: "" -%}
    {%- for p in items -%}
      {%- if p.featured -%}{%- assign feats = feats | push: p -%}{%- endif -%}
    {%- endfor -%}
    {%- comment -%}
      Featured articles render in sequence position rather than being hoisted to the front,
      so that several of them land spread through a section instead of stacked at the top.
      At most five per section; a sixth breaks the build loudly. Even dispersion is not
      enforced here — the console warns when two featured boxes sit too close together.
    {%- endcomment -%}
    {%- if feats.size > 5 -%}
      {%- include ERROR-more-than-five-featured-articles-in-one-section -%}
    {%- endif -%}
  <section class="rxm-section" id="sec-{{ cat }}" data-cat="{{ cat }}" aria-label="{{ bits[1] }}">
    <div class="rxm-sechead"><h2 class="rxm-secname">{{ bits[1] }}</h2><p class="rxm-seccount">{{ items.size }} articles</p></div>
    <div class="rxm-grid">
      {%- for p in items -%}
        {%- if p.featured -%}
          {%- include resource-entry.html post=p featured=true cat=cat -%}
        {%- else -%}
          {%- include resource-entry.html post=p cat=cat -%}
        {%- endif -%}
      {%- endfor -%}
    </div>
  </section>
  {%- endfor -%}

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
          live.textContent = 'All sections, ' + document.querySelectorAll('.rxm-box').length + ' articles';
        } else {
          location.hash = 'sec-' + t;   // browser scrolls; back button works
          live.textContent = chip.textContent + ', ' + countOf(t) + ' articles';
        }
        chip.focus({ preventScroll: true });   // focus stays on the chip without undoing the jump
      });
    });

    var m = (location.hash || '').match(/^#sec-(\w+)$/);
    if(m) activate(m[1]);
    window.addEventListener('hashchange', function(){
      var h = (location.hash || '').match(/^#sec-(\w+)$/);
      activate(h ? h[1] : 'top');
    });

    // editing aid: warn (only) when a featured description leaves the 90-200 window
    document.querySelectorAll('.rxm-feat .rxm-blurb').forEach(function(el){
      var n = el.textContent.trim().length;
      if(n < 90 || n > 200){
        var t = el.closest('a').querySelector('.rxm-title').textContent;
        console.warn('featured description for "' + t + '" is ' + n + ' characters (want roughly 90–200)');
      }
    });

    // editing aid: warn (only) when two featured boxes in a section sit too close together
    document.querySelectorAll('.rxm-section').forEach(function(sec){
      var boxes = Array.prototype.slice.call(sec.querySelectorAll('.rxm-box'));
      var at = [];
      boxes.forEach(function(b, i){ if(b.classList.contains('rxm-feat')) at.push(i); });
      for(var i = 1; i < at.length; i++){
        var gap = at[i] - at[i-1];
        if(gap < 4){
          console.warn('featured boxes in "' + sec.getAttribute('data-cat') + '" are only ' +
            gap + ' apart (want 4 or more, so they disperse rather than cluster)');
        }
      }
    });
  })();
  </script>

</div>
