---
layout: post
title: "Conditional probability and the base rate"
date: 2026-07-27
description: "A test that is 99% accurate can produce positives that are usually wrong. The distinction between two conditional probabilities, and the population picture that keeps them apart."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 5
interactive: true
blurb: "Why a 99% accurate test can produce positives that are usually wrong"
---

Here is a question that most people, including most physicians when it was put to them in studies, answer incorrectly. A disease affects 1% of a population. A screening test correctly identifies 99% of the people who have the disease, and correctly clears 95% of the people who do not. A randomly selected person tests positive. What is the probability that they actually have the disease?

The tempting answer is 99%, or something near it. The correct answer is about 17%. A positive result from this excellent test is wrong more than four times out of five, and the reasoning that explains why is precisely the conditional probability of Unit 2, applied with more care than intuition supplies.

## Two probabilities that sound alike

The test's accuracy is a statement of the form $$P(\text{positive} \mid \text{disease})$$: among people who have the disease, how often does the test say so? The question asked of a patient is the reverse: $$P(\text{disease} \mid \text{positive})$$, among people the test flagged, how many are actually sick? These are different fractions with different denominators, and nothing in mathematics obliges them to be close. Treating them as interchangeable is called the confusion of the inverse, and it is the single most common conditional probability error, on the exam and in life.

What drives the two numbers apart is the **base rate**: the underlying prevalence of the condition. When a disease is rare, the healthy population is so much larger than the sick one that even a small false-positive rate applied to the large group produces more false alarms than the large true-positive rate produces genuine detections.

## The population, drawn

The picture below shows a population of 10,000 people. Those with the condition who test positive are black; healthy people incorrectly flagged are medium gray; everyone else is faint. Adjust the three quantities that govern the situation and watch the answer move.

<div class="viz" markdown="0">
  <canvas id="br-cv" width="700" height="270"></canvas>
  <div class="viz-controls">
    <label for="br-prev">Prevalence</label>
    <input type="range" id="br-prev" min="1" max="100" step="1" value="10">
    <label for="br-sens">Sensitivity</label>
    <input type="range" id="br-sens" min="50" max="100" step="1" value="99">
    <label for="br-spec">Specificity</label>
    <input type="range" id="br-spec" min="50" max="100" step="1" value="95">
  </div>
  <div class="viz-controls"><span class="viz-value" id="br-read" style="min-width:100%"></span></div>
  <p class="viz-caption">Each square is one person in a population of 10,000. Black squares are true positives; gray squares are false positives; the faint field is everyone who tested negative. The readout computes the probability that a positive result is genuine, which is simply the black squares as a fraction of all shaded squares. At the default settings, gray squares outnumber black ones roughly five to one. Now raise the prevalence and watch the same test become trustworthy: the test never changed, only the population did. This is the base rate doing its quiet work.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('br-cv'), c = cv.getContext('2d');
  var sp = document.getElementById('br-prev'), ss = document.getElementById('br-sens'), sc = document.getElementById('br-spec');
  var read = document.getElementById('br-read');
  var W = cv.width, H = cv.height;
  var COLS = 125, ROWS = 80, N = COLS*ROWS;
  var cw = W/COLS, ch = H/ROWS;
  function draw(){
    var prev = sp.value/1000, sens = ss.value/100, spec = sc.value/100;
    var sick = Math.round(N*prev);
    var tp = Math.round(sick*sens);
    var fp = Math.round((N - sick)*(1 - spec));
    c.clearRect(0, 0, W, H);
    for(var i = 0; i < N; i++){
      var x = (i%COLS)*cw, y = Math.floor(i/COLS)*ch;
      if(i < tp) c.fillStyle = '#1f1f1f';
      else if(i < tp + fp) c.fillStyle = '#9a9a97';
      else c.fillStyle = '#f0f0ee';
      c.fillRect(x + 0.5, y + 0.5, cw - 1, ch - 1);
    }
    var ppv = tp + fp > 0 ? tp/(tp + fp) : 0;
    read.textContent = 'prevalence ' + (prev*100).toFixed(1) + '%   sensitivity ' + ss.value + '%   specificity ' + sc.value + '%   →   P(disease given positive) = ' + tp + '/' + (tp + fp) + ' ≈ ' + (ppv*100).toFixed(1) + '%';
  }
  [sp, ss, sc].forEach(function(s){ s.addEventListener('input', draw); });
  draw();
})();
</script>

## The computation, in AP form

The exam expects this reasoning through a tree diagram or a two-way table, and the table is the sturdier tool. Out of 10,000 people at 1% prevalence, 100 have the disease and 9,900 do not. Of the 100, the test catches 99. Of the 9,900, the test wrongly flags 5%, which is 495 people. The positive group therefore contains $$99 + 495 = 594$$ people, of whom 99 are genuinely sick:

$$P(\text{disease} \mid \text{positive}) = \frac{99}{594} \approx 0.167$$

Every quantity in that fraction is a count of actual people, which is why this presentation, sometimes called natural frequencies, is so much harder to get wrong than the formula. The formula is Bayes' theorem, and the table is Bayes' theorem wearing work clothes.

## Where the exam tests it

Conditional probability from a two-way table appears on nearly every AP Statistics exam, and the wording is precise: the condition follows the word "given," and the given event determines the denominator. "What proportion of positive tests come from healthy people" and "what proportion of healthy people test positive" are different cells divided by different totals. Reading the sentence slowly, deciding which group is the denominator before touching any numbers, is the whole skill.

The deeper lesson reaches past the exam. Screening programs for rare conditions, security systems flagging rare threats, and algorithms detecting rare fraud all live under the same arithmetic: when the base rate is low, most alarms are false, no matter how good the alarm. A student who has internalized the picture above owns a piece of quantitative literacy that most adults lack.

<div class="article-note" markdown="1">
A check worth performing on the interactive: set the prevalence to 10% and the answer rises to about 69%, and at 50% prevalence, with the same test, a positive is right about 95% of the time. This is why physicians order confirmatory tests rather than repeating the screen: the first positive raises the base rate for the second test, and the same instrument becomes far more informative the second time it is used.
</div>
