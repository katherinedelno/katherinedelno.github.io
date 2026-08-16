---
layout: post
title: "Independence and mutual exclusivity"
date: 2026-07-27
description: "Mutual exclusivity is about overlap. Independence is about whether learning one event changes the probability of the other."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 5
interactive: true
blurb: "Mutual exclusivity is about overlap. Independence is about whether learning one event changes the probability of the other"
image: "/assets/og/independence-and-mutual-exclusivity.png"
---

Independence and mutual exclusivity describe different relationships between events.

Mutual exclusivity is about whether two events can happen together.

Independence is about whether learning that one event occurred changes the probability of the other.

For events with positive probability, mutually exclusive events cannot be independent.

## Mutual exclusivity

Events $$A$$ and $$B$$ are mutually exclusive when

$$P(A\cap B)=0.$$

They have no overlap.

If one occurs, the other did not.

This condition simplifies the addition rule:

$$P(A\cup B) = P(A)+P(B)$$

when the events are mutually exclusive.

## Independence

Events $$A$$ and $$B$$ are independent when

$$P(A\mid B)=P(A).$$

Knowing that $$B$$ occurred gives no new information about the probability of $$A$$.

An equivalent condition is

$$P(A\cap B) = P(A)P(B).$$

Independence is therefore a numerical relationship among probabilities.

## Watch the overlap change

The events below have fixed probabilities

$$P(A)=0.5$$

and

$$P(B)=0.4.$$

<div class="viz" markdown="0">
  <canvas id="ie-cv" width="700" height="250"></canvas>
  <div class="viz-controls">
    <label for="ie-ov">P(A and B)</label>
    <input type="range" id="ie-ov" min="0" max="40" step="1" value="20">
    <span class="viz-value" id="ie-read"></span>
  </div>
  <p class="viz-caption">The rectangle is the sample space; the two regions are the events, and the dark region is their overlap. Independence requires the overlap to equal P(A) times P(B), which is 0.20 here, marked on the slider's scale by the readout. Slide fully left to make the events mutually exclusive and watch the conditional probability P(A given B) fall to zero, as far from P(A) = 0.5 as it can be. Slide to 0.20 and the conditional probability matches P(A) exactly: knowing B tells you nothing about A. Independence is that single point on the slider; exclusivity is the far end of it.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('ie-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('ie-ov'), read = document.getElementById('ie-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var PA = 0.5, PB = 0.4;
  function draw(){
    var ov = sl.value/100;
    c.clearRect(0, 0, W, H);
    var pad = 30, bw = W - 2*pad, bh = H - 2*pad;
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.strokeRect(pad, pad, bw, bh);
    // represent events as horizontal bands sized by probability; overlap drawn where they intersect
    var aw = PA*bw, bwid = PB*bw;
    var bx = pad + aw - ov*bw;   // B starts so that the intersection has width ov*bw
    c.fillStyle = 'rgba(31,31,31,0.10)';
    c.fillRect(pad, pad, aw, bh);
    c.fillStyle = 'rgba(92,92,92,0.16)';
    c.fillRect(bx, pad, bwid, bh);
    c.fillStyle = 'rgba(31,31,31,0.42)';
    if(ov > 0) c.fillRect(bx, pad, ov*bw, bh);
    c.fillStyle = '#1f1f1f'; c.font = '700 13px Hanken Grotesk, sans-serif';
    c.fillText('A', pad + 8, pad + 20);
    c.fillText('B', bx + bwid - 16, pad + 20);
    var pab = PB > 0 ? ov/PB : 0;
    read.textContent = 'P(A and B) = ' + ov.toFixed(2) + '   P(A)·P(B) = 0.20   P(A given B) = ' + pab.toFixed(2) + '   P(A) = 0.50';
  }
  sl.addEventListener('input', draw);
  draw();
})();
</script>

Independence requires

$$P(A\cap B) = (0.5)(0.4) = 0.20.$$

At overlap 0.20,

$$P(A\mid B)=P(A)=0.5.$$

Move the overlap to zero.

The events are now mutually exclusive.

Then

$$P(A\mid B)=0,$$

which is very different from

$$P(A)=0.5.$$

Learning that $$B$$ happened tells us with certainty that $$A$$ did not.

That is dependence, not independence.

## An overlapping pair can be independent

Draw one card from a standard deck.

Let $$A$$ be the event that the card is a heart.

Let $$B$$ be the event that the card is a king.

The events overlap because the king of hearts belongs to both.

But

$$P(A\cap B) = \frac1{52},$$

and

$$P(A)P(B) = \frac{13}{52}\cdot\frac4{52} = \frac1{52}.$$

So the events are independent.

Overlap and independence are compatible.

No overlap and independence are not compatible when both events have positive probability.

## Two-way tables

In a two-way table, independence can be checked by comparing a conditional proportion with the corresponding marginal proportion.

For example, compare

$$P(A\mid B)$$

with

$$P(A).$$

Or use the multiplication condition

$$P(A\cap B)=P(A)P(B).$$

<div class="article-note" markdown="1">
The wording of the categories does not determine independence.

The probabilities do.
</div>
