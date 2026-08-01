---
layout: post
title: "Which inference procedure?"
date: 2026-07-31
description: "Six procedures, two purposes, and three questions that sort them. The decision is settled by how the data were collected, not by the numbers the problem happens to supply."
course: "AP Statistics"
read_time: "8 min read"
math: true
kind: mechanics
sequence: 14
interactive: true
blurb: "Three questions about the design, asked before any arithmetic"
---

A student who can execute every inference procedure in the course can still lose the question, because choosing the procedure happens before any of that skill is used. The framework treats selection as its own thing, attaching the skill *identify appropriate statistical inference methods* to eleven separate topics, and the reason is that the choice is settled by the study design rather than by the numbers.

Twelve procedures survive in the revised course: six families, each available as an interval and as a test. That sounds like a lot to sort until the sorting is written down, at which point it is three questions.

## Three questions, in order

**What kind of response was recorded?** If each individual contributes a category — yes or no, brand A or B, resolved or not — the parameter is a proportion. If each individual contributes a number, it is a mean. Nothing else about the problem matters until this is answered, because it decides which half of the course you are in.

**How many groups, and where did they come from?** One group gives a one-sample procedure. Two independently collected groups give a two-sample one. A single group classified two ways gives a two-way table and a chi-square procedure.

**If there are two sets of numbers, are they paired?** Two measurements on the same individuals, or on individuals deliberately matched, is not two samples. It is one sample of differences.

Only after those three is there a fourth: is the question asking what the parameter *is*, or whether a claim about it survives? The first is an interval and the second is a test.

## The drill

Classify the design. No arithmetic, and no numbers are supplied for any.

<div class="viz" markdown="0">
  <div class="wi-stem" id="wi-stem"></div>
  <div class="viz-controls" id="wi-fam"></div>
  <div class="viz-controls" id="wi-pur"></div>
  <div class="wi-fb" id="wi-fb"></div>
  <div class="viz-controls">
    <button type="button" class="res-filter" id="wi-next" style="font-size:.72rem">Next scenario</button>
    <span class="viz-value" id="wi-score"></span>
  </div>
  <p class="viz-caption">Twelve scenarios, cycling. Both rows have to be answered before the verdict appears, because the two decisions are independent: the family comes from how the data were collected and the purpose comes from what the question asks for. The feedback never names the arithmetic. It names the feature of the design that settled the choice, which is the only part that transfers to a scenario you have not seen. Four of the twelve are built as confusable pairs and are worth returning to.</p>
  <style>
    .wi-stem{font-size:1.05rem;line-height:1.6;color:var(--ink);padding:6px 0 16px;min-height:5.2em}
    .wi-fb{font-size:.95rem;line-height:1.6;color:var(--ink);min-height:4.6em;
      padding:12px 0 6px;border-top:1px solid var(--line);margin-top:.3rem}
    .wi-fb .wi-ok{font-weight:700}
    .wi-fb .wi-no{font-weight:700;color:var(--muted)}
    .wi-fb .wi-tell{color:var(--muted);display:block;margin-top:.3rem}
  </style>
</div>

<script>
(function(){
  'use strict';
  var stemEl = document.getElementById('wi-stem'), fbEl = document.getElementById('wi-fb');
  var famEl = document.getElementById('wi-fam'), purEl = document.getElementById('wi-pur');
  var scoreEl = document.getElementById('wi-score');

  var FAM = [['p1','One proportion'], ['p2','Two proportions'], ['chi','Chi-square'],
             ['m1','One mean'], ['md','Paired difference'], ['m2','Two means']];
  var PUR = [['ci','Confidence interval'], ['ht','Significance test']];

  var Q = [
    { s: 'A district surveys one random sample of 400 seniors and records whether each plans to enrol at a four-year college. It wants a range of plausible values for the district-wide proportion.',
      f: 'p1', p: 'ci', t: 'One sample, a yes-or-no response, and a request for plausible values rather than a verdict.' },
    { s: 'Sixty volunteers are randomly assigned a new sleep protocol and sixty the standard one. For each, whether they fell asleep within twenty minutes is recorded. Does the new protocol do better?',
      f: 'p2', p: 'ht', t: 'Two groups formed by random assignment, a categorical response in each, and a claim to be judged.' },
    { s: 'Forty runners record their time on a course, train for a month, then run the same course again. Did training change times?',
      f: 'md', p: 'ht', t: 'The same forty runners appear twice, so each one yields a single difference. One sample of differences, not two samples.' },
    { s: 'Commute times are measured for 45 randomly chosen city employees and 45 randomly chosen suburban employees. Do the two populations differ on average?',
      f: 'm2', p: 'ht', t: 'Two separately drawn groups with no correspondence between them, and nothing pairs a city employee with a suburban one.' },
    { s: 'One random sample of 500 adults is classified by both age band and preferred news source. Are the two variables associated?',
      f: 'chi', p: 'ht', t: 'A single sample cross-classified two ways: the test for independence.' },
    { s: 'Separate random samples of 200 first-years, 200 sophomores, and 200 juniors are each asked their preferred study method. Do the three classes share a distribution?',
      f: 'chi', p: 'ht', t: 'Three separately collected samples compared on one variable: the test for homogeneity. Same statistic as the previous one, different design.' },
    { s: 'A machine should fill bottles to 500 millilitres. A technician measures thirty randomly chosen bottles and wants an interval for the true mean fill volume.',
      f: 'm1', p: 'ci', t: 'One sample, a numerical response, and an estimate requested. The 500 is context, not a hypothesis.' },
    { s: 'A quality manager measures the same twenty-five components with two different gauges. Do the gauges read differently on average?',
      f: 'md', p: 'ht', t: 'Two numbers per component, so subtract within each component first. The pairing is the components, not the gauges.' },
    { s: 'In a random sample of 250 households, 38 reported a power outage last month. Estimate the proportion of all households affected.',
      f: 'p1', p: 'ci', t: 'Counts are supplied, but the response is still categorical and there is still one sample. Counts do not make a mean.' },
    { s: 'Two independent random samples of 300 voters, one drawn in each of two states, are asked whether they support a measure. By how much do the two states differ?',
      f: 'p2', p: 'ci', t: 'Two samples, categorical response, and a question about the size of a difference rather than its existence.' },
    { s: 'A nutritionist records the calorie content of 40 randomly selected items from one restaurant chain. Does the mean exceed the advertised 600?',
      f: 'm1', p: 'ht', t: 'One sample of numbers, and a stated claim to be judged against. The 600 is a hypothesised value.' },
    { s: 'Battery life is measured for 50 randomly chosen units of one brand and 50 of another. Estimate how much longer one brand lasts on average.',
      f: 'm2', p: 'ci', t: 'Two separately drawn samples of numbers, and a question about the size of the gap. Compare this with the two-state voter scenario, which asks the same thing of a categorical response.' }
  ];

  var order = Q.map(function(_, i){ return i; }), at = 0;
  var pickF = null, pickP = null, asked = 0, right = 0, scored = false;

  function shuffle(a){
    for(var i = a.length - 1; i > 0; i--){
      var j = Math.floor(Math.random()*(i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function label(list, key){
    for(var i = 0; i < list.length; i++) if(list[i][0] === key) return list[i][1];
    return key;
  }
  function build(el, list, onPick){
    list.forEach(function(o){
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'res-filter'; b.style.fontSize = '.72rem';
      b.textContent = o[1]; b.setAttribute('data-k', o[0]);
      b.addEventListener('click', function(){ onPick(o[0]); });
      el.appendChild(b);
    });
  }
  function mark(el, key){
    Array.prototype.forEach.call(el.children, function(b){
      b.classList[b.getAttribute('data-k') === key ? 'add' : 'remove']('is-active');
    });
  }
  function render(){
    var q = Q[order[at]];
    stemEl.textContent = q.s;
    if(pickF === null || pickP === null){ fbEl.innerHTML = ''; return; }
    if(!scored){ asked++; if(pickF === q.f && pickP === q.p) right++; scored = true; }
    var okF = pickF === q.f, okP = pickP === q.p;
    var line = okF && okP
      ? '<span class="wi-ok">' + label(FAM, q.f) + ', ' + label(PUR, q.p).toLowerCase() + '.</span>'
      : '<span class="wi-no">Not quite.</span> It is a <span class="wi-ok">' + label(FAM, q.f) +
        '</span> procedure, as a <span class="wi-ok">' + label(PUR, q.p).toLowerCase() + '</span>.';
    fbEl.innerHTML = line + '<span class="wi-tell">' + q.t + '</span>';
    scoreEl.textContent = right + ' of ' + asked + ' correct';
  }
  build(famEl, FAM, function(k){ pickF = k; mark(famEl, k); render(); });
  build(purEl, PUR, function(k){ pickP = k; mark(purEl, k); render(); });
  document.getElementById('wi-next').addEventListener('click', function(){
    at = (at + 1) % order.length;
    if(at === 0) shuffle(order);
    pickF = pickP = null; scored = false;
    mark(famEl, null); mark(purEl, null);
    render();
  });
  shuffle(order);
  render();
})();
</script>

## The pair that looks like two samples

Scenarios three and eight are paired designs, and both invite the two-sample answer because two sets of numbers arrive. The framework's instruction is unusually direct about what to do instead: for a matched pairs design with two dependent samples, the appropriate analysis calculates differences between pairs of values to produce *one* sample of differences, and the procedure is a one-sample $$t$$-interval for a population mean difference.

So a paired design does not get its own family of formulas. It gets converted into a one-sample problem before any formula is used, and the parameter changes with it — from $$\mu_1 - \mu_2$$, the difference of two population means, to $$\mu_d$$, the mean of a population of differences. Those are different quantities, and [defining the parameter correctly](/2026/07/14/writing-parameters-in-ap-statistics.html) is where the distinction is graded.

The tell is never the arithmetic. It is whether the two numbers in a pair came from the same individual, or from two individuals matched deliberately. Forty runners timed twice is forty differences. Forty city employees and forty suburban ones is two samples, and no amount of equal sample size makes them pairs.

## The pair that looks like one table

Scenarios five and six both end in a two-way table, both use $$\chi^2 = \textstyle\sum (O-E)^2/E$$, and both have $$(r-1)(c-1)$$ degrees of freedom. The tables can be identical. [Only the design separates them](/2026/07/15/which-chi-square-test.html): one sample classified two ways is a test for independence, and several separately collected samples compared on one variable is a test for homogeneity.

The framework keeps the distinction alive even in the conditions, where the randomisation requirement is worded one way for independence and another for homogeneity. A procedure whose arithmetic is identical and whose conditions differ is a procedure that is really two.

## Estimate, or judge a claim

The second row of buttons is a separate decision and it fails separately. A question that supplies a specific value to argue about — an advertised 600 calories, a claimed 60% — is offering a null hypothesis and wants a test. A question that asks how large something is, or by how much two things differ, wants an interval.

The wording is reliable enough to use as a rule. *Is there convincing evidence that*, *do the data support*, and *test the claim* are tests. *Estimate*, *find a range of plausible values*, and *by how much* are intervals. Scenario seven mentions 500 millilitres and is still an interval, because the number arrives as context rather than as a claim to be judged.

<div class="article-note" markdown="1">
A drill in the same spirit as the tool, but harder: take a released free-response question, cover everything after the first sentence of the stem, and name the procedure from the design alone. Then uncover the rest and check. The scenarios that resist are the ones where the design is described last, which is a writing choice rather than a statistical one, and noticing it is worth more under time pressure than any formula on the reference sheet.
</div>
