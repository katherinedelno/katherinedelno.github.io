---
layout: post
title: "Probability against intuition"
date: 2026-07-26
description: "Monty Hall, the birthday problem, and Simpson's paradox: three places where computed probability corrects the felt kind."
course: "AP Statistics"
read_time: "8 min read"
math: true
kind: beyond
sequence: 6
interactive: true
---

Probability is the branch of mathematics most likely to start an argument at dinner. The reason is that human intuition about chance is systematically miscalibrated, and a few famous problems expose the miscalibration so cleanly that they have become classics. Each one below looks like a trick. Each one is actually a fair test of the conditional-probability reasoning from Unit 2, and in each case the AP toolkit gets the right answer while intuition gets the wrong one.

## The Monty Hall problem

A game show host shows you three doors. Behind one is a car; behind the other two, goats. You pick a door. The host, who knows where the car is, opens one of the other two doors to reveal a goat, and offers you a choice: stay with your original door, or switch to the remaining closed one.

Nearly everyone's intuition says the two closed doors are now equally likely, so switching cannot matter. When the columnist Marilyn vos Savant published the correct answer in 1990, thousands of readers, including mathematics professors, wrote in to insist she was wrong. She was not: switching wins the car two times out of three.

The clean argument runs through what you knew at the start. Your first pick is right with probability $$\tfrac13$$ and wrong with probability $$\tfrac23$$, and the host's reveal cannot change that: he can always open a goat door, whatever you picked. If your first pick was wrong, which happens $$\tfrac23$$ of the time, the host's action leaves the car behind the other closed door, and switching wins. Staying wins only when your first pick was right: $$\tfrac13$$.

If the argument does not convince you, the simulator will. It plays complete games honestly: hides the car at random, lets the player pick, has the host open a goat door, then either stays or switches.

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

The lesson generalizes: the host's choice carries information, because his behavior depended on where the car is. Updating correctly on information that arrived through someone's constrained choice is exactly what conditional probability is for, and exactly what intuition skips.

## The birthday paradox

How many people must be in a room before a shared birthday becomes more likely than not? Intuition, anchoring on 365 days, guesses somewhere near 180. The answer is 23.

The AP move is the complement. The probability that all $$n$$ people have different birthdays is

$$P(\text{all different}) = \frac{365}{365}\cdot\frac{364}{365}\cdot\frac{363}{365}\cdots\frac{365-n+1}{365},$$

and at $$n = 23$$ this product has fallen to about $$0.493$$, so a match has probability about $$0.507$$. By $$n = 50$$ a match is a 97% favorite; by 70 it is 99.9%.

Why does intuition miss so badly? Because it asks the wrong question: the chance that someone matches *your* birthday really does stay small (about 6% in a room of 23). But a match between *any* pair counts, and 23 people contain $$\binom{23}{2} = 253$$ pairs. The paradox dissolves the moment you count the pairs, which is why this problem, dressed in different clothes, appears in cryptography courses: the "birthday attack" on digital signatures is this arithmetic weaponized, and it forces real security systems to use enormously long codes.

## Simpson's paradox

A treatment can be better for men, better for women, and worse for people. That sentence sounds impossible; here are numbers that do it. Two hospitals treat a disease. Hospital A takes many severe cases; Hospital B mostly mild ones.

| | Severe cases | Mild cases | All cases |
|---|---|---|---|
| Hospital A | 210 of 300 survive (70%) | 95 of 100 survive (95%) | 305 of 400 (76%) |
| Hospital B | 30 of 50 survive (60%) | 300 of 350 survive (86%) | 330 of 400 (83%) |

Hospital A wins among severe cases (70% to 60%) and wins among mild cases (95% to 86%), yet loses overall (76% to 83%). Nothing is miscounted. Hospital A's overall rate is dragged down because its caseload is mostly severe patients, whose survival is lower everywhere. The lurking variable, severity, is doing all the work, and the aggregate comparison silently lets it.

This is the deepest of the three problems because it is not a puzzle: it happens constantly in real data. A famous case involved graduate admissions at Berkeley in 1973, where the university appeared to favor male applicants overall while most individual departments slightly favored women; the explanation was that women had applied to the most competitive departments. Every observational-study warning in AP Statistics, every "association is not causation," is preparation for recognizing this pattern, and the college subject that studies when aggregation is safe, called causal inference, is one of the liveliest research areas in statistics today.

## The common thread

All three problems yield to the same discipline: state exactly what is being conditioned on, and compute rather than feel. That discipline is the actual content of Unit 2, and these problems are why it matters beyond the exam. Probability runs medical testing, security, forecasting, and risk, and in each of those fields, the intuition these puzzles defeat is the same intuition that misprices real decisions.

<div class="article-note" markdown="1">
One more for the road, no answer supplied: a family has two children, and you learn at least one is a boy. What is the probability both are? Then instead: you learn at least one is a boy *born on a Tuesday*. Strangely, the extra detail changes the answer. Work out the first; look up the second only after you have a guess. It is the Monty Hall lesson again: how you learned a fact is part of the fact.
</div>
