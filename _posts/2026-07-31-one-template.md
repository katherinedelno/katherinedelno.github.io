---
layout: post
title: "One template for every interval"
date: 2026-07-31
description: "Most inference procedures in the course are built from two general forms. The procedure changes mainly through the standard error."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 12
interactive: true
blurb: "Most inference procedures in the course are built from two general forms. The procedure changes mainly through the standard error"
image: "/assets/og/one-template.png"
---

Most of the inference formulas in AP Statistics can be organized around two structures.

A confidence interval has the form

$$\text{statistic} \pm (\text{critical value})(\text{standard error}).$$

A standardized test statistic has the form

$$\frac{\text{statistic}-\text{null parameter value}}{\text{standard error}}.$$

The procedure determines which statistic, critical value, and standard error belong in those slots.

## Assemble one

Pick a procedure and switch between interval and test.

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

The overall structure stays nearly fixed.

What changes most often is the standard error.

For example, a one-proportion confidence interval uses

$$\hat p \pm z^* \sqrt{\frac{\hat p(1-\hat p)}{n}}.$$

A one-sample $$t$$-interval for a mean uses

$$\bar x \pm t^* \frac{s}{\sqrt n}.$$

A two-sample interval changes the statistic and standard error but not the general form.

## Paired data fit the same template

A matched-pairs problem is converted into one sample of differences.

If

$$d_i$$

is the difference for pair $$i$$, then inference concerns

$$\mu_d.$$

The interval is therefore a one-sample $$t$$-interval applied to the differences:

$$\bar d \pm t^* \frac{s_d}{\sqrt n}.$$

There is no need for an entirely separate formula family.

The design changes the variable being analyzed.

## Why means use $$t$$

For a population mean, the standard deviation $$\sigma$$ is usually unknown.

The standard error is estimated using

$$\frac{s}{\sqrt n}.$$

That substitution adds uncertainty.

The $$t$$-distribution accounts for it.

As the degrees of freedom increase, $$t$$ approaches the standard normal distribution.

## Why proportion intervals and tests use different standard errors

A one-proportion confidence interval does not assume a population value for $$p$$.

So its standard error is estimated with the sample proportion:

$$\sqrt{\frac{\hat p(1-\hat p)}{n}}.$$

A hypothesis test specifies a null value

$$p_0.$$

Under the null, the sampling distribution is built using that hypothesized parameter:

$$\sqrt{\frac{p_0(1-p_0)}{n}}.$$

The difference comes from the question.

The interval estimates an unknown parameter.

The test temporarily assumes a particular value.

## Pooling in a two-proportion test

For a two-proportion interval, the two sample proportions remain separate in the standard error.

A two-proportion test under

$$H_0:p_1=p_2$$

assumes the groups share one population proportion under the null.

That allows a pooled estimate

$$\hat p_c = \frac{x_1+x_2}{n_1+n_2}.$$

The test standard error uses this combined value.

The interval does not pool because it is estimating the difference without assuming equality.

## Chi-square is different

Chi-square procedures use

$$\chi^2 = \sum \frac{(O-E)^2}{E}.$$

This is not a single standardized difference between a statistic and a parameter.

It accumulates discrepancies across several cells of a table.

That is why chi-square sits outside the two general templates and appears only as a test in this course.

<div class="article-note" markdown="1">
The reference sheet is easier to use once the formulas are seen this way.

Most of the work is identifying the design and choosing the matching standard error.
</div>
