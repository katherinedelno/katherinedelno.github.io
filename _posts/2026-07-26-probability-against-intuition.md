---
layout: post
title: "Probability against intuition"
date: 2026-07-26
description: "Monty Hall, the birthday problem, and Simpson's paradox all become less mysterious once the conditioning information is written explicitly."
course: "AP Statistics"
read_time: "9 min read"
math: true
kind: beyond
sequence: 2
interactive: true
blurb: "Monty Hall, the birthday problem, and Simpson's paradox all become less mysterious once the conditioning information is written explicitly"
image: "/assets/og/probability-against-intuition.png"
---

Some probability results feel wrong until the sample space is made explicit.

That discomfort is useful.

It usually signals that we are [conditioning on information](/2026/07/27/conditional-probability-and-the-base-rate.html) without accounting for how that information was produced.

Three familiar examples show the pattern.

## The Monty Hall problem

There are three doors.

One hides a prize.

You choose a door.

The host, who knows where the prize is, then opens one of the other two doors and deliberately reveals a losing door.

You may stay with your original choice or switch to the remaining unopened door.

Switching wins with probability

$$\frac23.$$

Staying wins with probability

$$\frac13.$$

<div class="viz" markdown="0">
  <canvas id="mh-cv" width="700" height="180"></canvas>
  <div class="viz-controls">
    <button type="button" id="mh-stay" class="res-filter" style="font-size:.72rem">Play 500 staying</button>
    <button type="button" id="mh-switch" class="res-filter" style="font-size:.72rem">Play 500 switching</button>
    <button type="button" id="mh-clear" class="res-filter" style="font-size:.72rem">Reset</button>
    <span class="viz-value" id="mh-read"></span>
  </div>
  <p class="viz-caption">Win rates for each strategy, with the theoretical 1/3 and 2/3 marked as dashed lines. Run a few thousand games of each. The bars settle onto the dashed lines and refuse to settle anywhere else, which is the Law of Large Numbers acting as a referee. Simulation cannot prove the argument, but it can end the dinner argument.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('mh-cv'), c = cv.getContext('2d');
  var read = document.getElementById('mh-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var stayW = 0, stayN = 0, swW = 0, swN = 0;
  function playGame(switching){
    var car = Math.floor(Math.random()*3);
    var pick = Math.floor(Math.random()*3);
    if(!switching) return pick === car;
    // host opens a goat door that is not the pick; player switches to the remaining door
    return pick !== car;   // switching wins exactly when the first pick was wrong
  }
  function bar(y, frac, label, target){
    var x0 = 150, x1 = W - 60;
    c.strokeStyle = '#e0e0e0'; c.beginPath();
    c.moveTo(x0, y); c.lineTo(x1, y); c.stroke();
    c.fillStyle = '#c9c9c6';
    c.fillRect(x0, y - 14, (x1 - x0)*frac, 28);
    c.strokeStyle = '#5c5c5c'; c.setLineDash([4,3]);
    var tx = x0 + (x1 - x0)*target;
    c.beginPath(); c.moveTo(tx, y - 20); c.lineTo(tx, y + 20); c.stroke();
    c.setLineDash([]);
    c.fillStyle = '#1f1f1f'; c.font = '700 13px Hanken Grotesk, sans-serif';
    c.fillText(label, 10, y + 4);
    c.fillText((frac*100).toFixed(1) + '%', x1 + 8, y + 4);
  }
  function draw(){
    c.clearRect(0, 0, W, H);
    bar(55, stayN ? stayW/stayN : 0, 'Stay', 1/3);
    bar(125, swN ? swW/swN : 0, 'Switch', 2/3);
    read.textContent = 'stay: ' + stayW + '/' + stayN + '   switch: ' + swW + '/' + swN;
  }
  document.getElementById('mh-stay').addEventListener('click', function(){
    for(var i = 0; i < 500; i++){ if(playGame(false)) stayW++; stayN++; } draw();
  });
  document.getElementById('mh-switch').addEventListener('click', function(){
    for(var i = 0; i < 500; i++){ if(playGame(true)) swW++; swN++; } draw();
  });
  document.getElementById('mh-clear').addEventListener('click', function(){ stayW = stayN = swW = swN = 0; draw(); });
  draw();
})();
</script>

The easiest explanation starts before the host opens anything.

Your first choice is correct with probability

$$\frac13.$$

It is wrong with probability

$$\frac23.$$

If the first choice is correct, switching loses.

If the first choice is wrong, the host is forced to reveal the other losing door, so switching wins.

Therefore switching wins exactly when the original choice was wrong.

That happens two thirds of the time.

The host's action is not an ordinary random door opening.

It depends on knowledge of the prize location.

That is the conditioning information that changes the problem.

## The birthday problem

How many people are needed before the probability of at least one shared birthday exceeds 50%?

The answer is 23, under the usual simplifying assumptions of 365 equally likely birthdays and no leap day.

The direct calculation is awkward.

The complement is easier.

First compute the probability that all birthdays are different:

$$P(\text{all different}) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{343}{365}.$$

Then

$$P(\text{at least one match}) = 1-P(\text{all different}).$$

For 23 people, this is about

$$0.507.$$

The result feels surprising because 23 is small relative to 365.

But the number of pairs is

$$\binom{23}{2}=253.$$

There are 253 opportunities for a match.

The number of comparisons grows much faster than the number of people.

At 50 people, the probability of a shared birthday is already about 97%.

At 70, it is above 99.9%.

## Simpson's paradox

Suppose Treatment A has a higher success rate than Treatment B among both mild cases and severe cases.

It can still have a lower success rate overall.

| | Severe cases | Mild cases | All cases |
|---|---|---|---|
| Treatment A | 210 of 300 survive (70%) | 95 of 100 survive (95%) | 305 of 400 (76%) |
| Treatment B | 30 of 50 survive (60%) | 300 of 350 survive (86%) | 330 of 400 (83%) |

The reversal is possible because the overall rate is a weighted average of the subgroup rates.

If Treatment A is used much more often for severe cases and Treatment B much more often for mild cases, the groups are being compared under different case mixes.

The aggregate rate then reflects both treatment performance and severity.

Separating the data by [the relevant third variable](/2026/07/27/simpsons-paradox.html) can reverse the apparent association.

This is Simpson's paradox.

The arithmetic is not contradictory.

The weights changed.

## The common structure

Monty Hall changes because the host's action depends on hidden information.

The birthday problem becomes manageable after we condition on the event that previous birthdays were all distinct.

Simpson's paradox changes when we condition on a third variable that is related to both the explanatory and response variables.

In each case, the important question is:

What information has been conditioned on, and how was it generated?

Probability statements are always relative to a sample space and a set of assumptions.

If those change, the probability can change.

## A final conditioning puzzle

<div class="article-note" markdown="1">
Suppose a family has two children and at least one is a boy.

Under a simple model where the four ordered sex combinations are equally likely, the possible families are

$$BB,\quad BG,\quad GB.$$

So the probability both are boys is

$$\frac13.$$

But if the information “at least one is a boy” was produced by a different reporting process, the answer can change.

For example, learning that a randomly selected child from the family is a boy is a different experiment.

The wording alone is not always enough.

The mechanism that generated the information matters.

That is the larger lesson behind many probability puzzles.
</div>
