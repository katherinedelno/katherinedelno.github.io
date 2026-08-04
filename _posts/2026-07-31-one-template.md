---
layout: post
title: "One template for every interval"
date: 2026-07-31
description: "The formula sheet supplied on exam day carries two formulas for inference. Everything students think of as twelve separate procedures is one of those two with a different standard error."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 12
interactive: true
blurb: "Two formulas, a table of standard errors, and nothing else"
image: "/assets/og/one-template.png"
---

The formula sheet handed out on exam day carries two formulas for inference. Not twelve, and not one per procedure. Two:

$$\text{statistic} \pm (\text{critical value})(\text{standard error}), \qquad \frac{\text{statistic} - \text{parameter}}{\text{standard error}}.$$

The first is every confidence interval in the course. The second is every standardized test statistic. What follows them on the sheet is not more formulas — it is a table of standard errors, one row per sampling distribution, and choosing the row is the whole of what looks like memorizing a dozen procedures.

## Assemble one

Pick a procedure and watch which of the three slots changes.

<div class="viz" markdown="0">
  <div class="viz-controls" id="ot-fam"></div>
  <div class="viz-controls" id="ot-pur"></div>
  <div class="ot-formula" id="ot-formula"></div>
  <div class="ot-parts" id="ot-parts"></div>
  <p class="viz-caption">The large line is the assembled result and the three boxes underneath are the slots it was built from. Step through the six families with the purpose held fixed and the template never moves: only the third box changes, and it changes to whichever row of the sheet's standard-error table matches the sampling distribution. Then hold the family fixed and switch purpose. For means nothing changes but the middle box. For proportions the third box changes as well, which is the one place the two purposes genuinely disagree.</p>
  <style>
    .ot-formula{font-size:1.5rem;font-weight:700;letter-spacing:-.02em;color:var(--ink);
      text-align:center;padding:22px 8px 18px;line-height:1.5;min-height:2.4em}
    .ot-formula .ot-hl{background:var(--accent-soft);border-radius:5px;padding:2px 5px}
    .ot-parts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;
      border-top:1px solid var(--line);padding-top:14px}
    .ot-parts div{font-size:.95rem;color:var(--ink);font-variant-numeric:tabular-nums}
    .ot-parts .ot-k{display:block;font-size:.66rem;letter-spacing:.09em;text-transform:uppercase;
      color:var(--muted);font-weight:700;margin-bottom:5px}
    .ot-parts .ot-sub{display:block;font-size:.82rem;color:var(--muted);margin-top:4px;line-height:1.45}
    @media (max-width:640px){ .ot-parts{grid-template-columns:1fr;gap:10px} .ot-formula{font-size:1.1rem} }
  </style>
</div>

<script>
(function(){
  'use strict';
  var famEl = document.getElementById('ot-fam'), purEl = document.getElementById('ot-pur');
  var fEl = document.getElementById('ot-formula'), pEl = document.getElementById('ot-parts');

  var FAM = [
    ['p1',  'One proportion'],
    ['p2',  'Two proportions'],
    ['m1',  'One mean'],
    ['md',  'Paired difference'],
    ['m2',  'Two means'],
    ['chi', 'Chi-square']
  ];
  var PUR = [['ci', 'Confidence interval'], ['ht', 'Significance test']];

  // statistic, parameter, critical value, standard error, reference curve
  var T = {
    p1: { stat: 'p̂', par: 'p₀',
          ciSE: '√( p̂(1−p̂) ⁄ n )', htSE: '√( p₀(1−p₀) ⁄ n )',
          cv: 'z*', ref: 'standard normal',
          note: 'The test knows the null value, so it uses p₀ in the standard error. The interval does not, so it uses p̂.' },
    p2: { stat: 'p̂₁ − p̂₂', par: '0',
          ciSE: '√( p̂₁(1−p̂₁) ⁄ n₁ + p̂₂(1−p̂₂) ⁄ n₂ )',
          htSE: '√( p̂_c(1−p̂_c)(1⁄n₁ + 1⁄n₂) )',
          cv: 'z*', ref: 'standard normal',
          note: 'Under the null the two proportions are equal, so the test pools them into p̂_c. The interval assumes nothing and keeps them apart.' },
    m1: { stat: 'x̄', par: 'μ₀',
          ciSE: 's ⁄ √n', htSE: 's ⁄ √n',
          cv: 't*', ref: 't with n − 1 degrees of freedom',
          note: 'σ is never known, so both purposes use s and both use t. That is the whole reason means get t and proportions get z.' },
    md: { stat: 'x̄_d', par: '0',
          ciSE: 's_d ⁄ √n', htSE: 's_d ⁄ √n',
          cv: 't*', ref: 't with n − 1 degrees of freedom',
          note: 'A paired design is a one-sample procedure on the differences, so n is the number of pairs, not the number of measurements.' },
    m2: { stat: 'x̄₁ − x̄₂', par: '0',
          ciSE: '√( s₁² ⁄ n₁ + s₂² ⁄ n₂ )', htSE: '√( s₁² ⁄ n₁ + s₂² ⁄ n₂ )',
          cv: 't*', ref: 't, with technology supplying the degrees of freedom',
          note: 'Two independent samples, so the two variances add under the root. Standard deviations never add.' },
    chi: { stat: null, ref: 'chi-square with (r − 1)(c − 1) degrees of freedom',
          note: 'The exception. A chi-square statistic is a sum over cells rather than a standardized distance, and it has no interval.' }
  };

  var fam = 'p1', pur = 'ci', prev = null;

  function mark(el, k){
    Array.prototype.forEach.call(el.children, function(b){
      b.classList[b.getAttribute('data-k') === k ? 'add' : 'remove']('is-active');
    });
  }
  function build(el, list, set){
    list.forEach(function(o){
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'res-filter'; b.style.fontSize = '.72rem';
      b.textContent = o[1]; b.setAttribute('data-k', o[0]);
      b.addEventListener('click', function(){ set(o[0]); });
      el.appendChild(b);
    });
  }
  function hl(s, on){ return on ? '<span class="ot-hl">' + s + '</span>' : s; }

  function render(){
    var t = T[fam];
    if(fam === 'chi'){
      fEl.innerHTML = 'χ² = ' + hl('Σ (O − E)² ⁄ E', true);
      pEl.innerHTML =
        '<div><span class="ot-k">statistic</span>a sum over cells<span class="ot-sub">not a statistic minus a parameter</span></div>' +
        '<div><span class="ot-k">critical value</span>none<span class="ot-sub">there is no chi-square interval in this course</span></div>' +
        '<div><span class="ot-k">reference curve</span>' + t.ref + '<span class="ot-sub">' + t.note + '</span></div>';
      prev = null; return;
    }
    var se = pur === 'ci' ? t.ciSE : t.htSE;
    var seChanged = prev && prev.se !== se;
    if(pur === 'ci'){
      fEl.innerHTML = t.stat + ' ± ' + t.cv + ' · ' + hl(se, seChanged);
    } else {
      fEl.innerHTML = '( ' + t.stat + ' − ' + t.par + ' ) ⁄ ' + hl(se, seChanged);
    }
    pEl.innerHTML =
      '<div><span class="ot-k">statistic</span>' + t.stat +
        '<span class="ot-sub">' + (pur === 'ci' ? 'the center of the interval' : 'the top of the fraction, minus the null value ' + t.par) + '</span></div>' +
      '<div><span class="ot-k">' + (pur === 'ci' ? 'critical value' : 'reference curve') + '</span>' +
        (pur === 'ci' ? t.cv : t.ref.split(',')[0]) +
        '<span class="ot-sub">from the ' + t.ref + '</span></div>' +
      '<div><span class="ot-k">standard error</span>' + se +
        '<span class="ot-sub">' + t.note + '</span></div>';
    prev = { se: se };
  }
  build(famEl, FAM, function(k){ fam = k; mark(famEl, k); render(); });
  build(purEl, PUR, function(k){ pur = k; mark(purEl, k); render(); });
  mark(famEl, 'p1'); mark(purEl, 'ci'); render();
})();
</script>

## Only one slot moves

Hold the purpose at *confidence interval* and step through the six families. The shape never changes. A statistic, a critical value, a standard error, and a plus-or-minus. What changes is the third slot, and every value it takes is a row of the sheet's table: one proportion, two proportions, one mean, two means. There is no separate formula for a paired interval, because a paired design is a one-sample procedure on the differences and takes the one-mean row with $$n$$ counting pairs.

That is why the sheet does not print twelve formulas. It prints two, and expects them to be assembled.

## Where the two purposes disagree

Now hold the family fixed and switch between interval and test. For every procedure about means, nothing changes but the critical value, because the standard error is $$s/\sqrt{n}$$ either way.

For proportions, the standard error changes too, and the sheet says why in a way that is easy to read past. It gives two columns rather than one: a *standard deviation* built from the parameter, and a *standard error* built from the statistic. A test has a null hypothesis, so it knows a value for the parameter and can use the first. An interval has no such value, so it must estimate with the second.

This is also the honest answer to a question students ask constantly: why do proportions get $$z$$ and means get $$t$$? Because a proportion's spread is determined by the proportion itself, so a hypothesized $$p_0$$ supplies the standard deviation exactly. A mean's spread depends on $$\sigma$$, which no hypothesis ever supplies, so $$s$$ must stand in — and the extra uncertainty in that substitution is precisely what the $$t$$ distribution is for.

The two-proportion test carries the same idea one step further. Its null says the two proportions are equal, so a test may pool the two samples into a single combined estimate $$\hat{p}_c$$ before computing the standard error. The interval, assuming nothing, keeps them apart. Same statistic on top, two different denominators, and the difference is entirely about what the null hypothesis was willing to tell you.

## The exception, and what it tells you

Chi-square does not fit either template, and the sheet prints it separately for that reason. It is a sum over cells rather than a standardized distance, there is no parameter subtracted, and there is no chi-square interval anywhere in the course.

That is worth noticing rather than filing away. Every other procedure measures how far one number sits from another in standard errors, which is why every other procedure has both an interval and a test. Chi-square measures total disagreement across a whole table, and a total has no natural interval attached. The shape of the formula predicts what questions the procedure can answer.

<div class="article-note" markdown="1">
An exercise for the tool, best done with the reference sheet beside it: choose any procedure, write the assembled formula from memory, then find the standard error you used in the sheet's table and confirm you took the right row. Do that for all eleven combinations and the sheet stops being a page to search under time pressure and becomes a page with two formulas and a lookup table on it. Students who reach that point stop losing time hunting for a formula that was never printed, because they have realized it was theirs to build.
</div>
