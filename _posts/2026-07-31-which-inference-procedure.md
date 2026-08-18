---
layout: post
title: "Which inference procedure?"
date: 2026-07-31
description: "Choose an inference procedure from the response type, the number and relationship of groups, and whether the goal is estimation or hypothesis testing."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: mechanics
sequence: 16
interactive: true
blurb: "Choose an inference procedure from the response type, the number and relationship of groups, and whether the goal is estimation or hypothesis testing"
featured: true
image: "/assets/og/which-inference-procedure.png"
---

Choosing an inference procedure happens before any formula is used, and the study design usually determines the choice. A useful sequence is to identify the response type, identify the groups and their relationship, and then decide whether the goal is estimation or testing.

## Question 1, the kind of response recorded

If each individual contributes a category, the parameter usually involves a proportion or a categorical distribution. Examples include:

- yes or no
- success or failure
- preferred category

If each individual contributes a numerical measurement, the parameter usually involves a mean. Examples include:

- height
- wait time
- blood pressure
- test score

This first distinction separates proportion procedures from mean procedures.

## Question 2, the number of groups

One sample gives a one-sample procedure, two independently collected groups give a two-sample procedure, and several categorical groups summarized in a two-way table may call for chi-square. The number of columns in a dataset is not enough, and the way the observations were collected matters.

## Question 3, whether numerical observations are paired

Two measurements can look like two samples while actually forming pairs. Examples include:

- before and after measurements on the same people
- twins or deliberately matched subjects
- two measurements on the same experimental unit

For paired data, compute one difference for each pair, and the analysis becomes a one-sample $$t$$-procedure on those differences. The parameter is $$\mu_d$$, [the population mean difference](/2026/07/14/writing-parameters-in-ap-statistics.html), and it is not $$\mu_1-\mu_2$$ for two independent populations.

## Question 4, interval or test

A confidence interval estimates a parameter or difference, and a hypothesis test evaluates evidence about a specific claim. Wording such as “estimate,” “find a plausible range,” or “by how much” usually points toward an interval. Wording such as “is there convincing evidence,” “test the claim,” or “do the data support” usually points toward a test. The purpose and the procedure family are separate decisions.

## Classify the design

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
      f: 'm1', p: 'ht', t: 'One sample of numbers, and a stated claim to be judged against. The 600 is a hypothesized value.' },
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

The drill presents scenarios without arithmetic, and that is intentional. The point is to identify which feature of the design determines the method, and a correct choice should be explainable in words before any calculator command is entered.

## Two chi-square designs

A two-way table can arise in two ways. One sample classified according to two categorical variables calls for a test of independence, and several separate groups compared on one categorical response call for a test of homogeneity. The tables and test statistic can be identical. [The data collection distinguishes the procedures](/2026/07/15/which-chi-square-test.html).

## A compact map

| Design | Typical procedure |
|---|---|
| One categorical sample | One-proportion $$z$$ |
| Two independent categorical groups | Two-proportion $$z$$ |
| One numerical sample | One-sample $$t$$ |
| Two independent numerical groups | Two-sample $$t$$ |
| Paired numerical data | One-sample $$t$$ on differences |
| One sample, two categorical variables | Chi-square test for independence |
| Several groups, one categorical variable | Chi-square test for homogeneity |

Then decide whether the question asks for an interval or a test. Chi-square appears as a test only.

<div class="article-note" markdown="1">
The fastest way to become fluent is to practice classification separately from computation.
</div>
