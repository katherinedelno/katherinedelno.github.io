---
layout: post
title: "Independence and mutual exclusivity"
date: 2026-07-27
description: "Two properties that students treat as siblings are nearly opposites: mutually exclusive events are as dependent as events can be. An interactive pair of events makes the distinction concrete."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 4
interactive: true
blurb: "Mutually exclusive events are as dependent as events can be"
---

Ask a class whether mutually exclusive events are independent and a majority will say yes, on the reasonable-sounding grounds that both words describe events with nothing to do with each other. The truth is nearly the reverse. Mutually exclusive events are as strongly dependent as two events can be, and the confusion between the two properties is among the most reliable point-losers in the probability units of AP Statistics.

The cure is to state both definitions in terms of what they actually control, and then to watch them move.

## What each property says

**Mutual exclusivity** is a statement about overlap: events $$A$$ and $$B$$ are mutually exclusive when they cannot occur together, so that $$P(A \text{ and } B) = 0$$. It is a fact about the geometry of the sample space, visible in a Venn diagram as two regions that do not touch.

**Independence** is a statement about information: $$A$$ and $$B$$ are independent when knowing that one occurred leaves the probability of the other unchanged, so that $$P(A \mid B) = P(A)$$, or equivalently $$P(A \text{ and } B) = P(A)\,P(B)$$. It is not visible in a Venn diagram at all, because it is a numerical coincidence between areas, not a shape.

Now put the two together. If $$A$$ and $$B$$ are mutually exclusive, and you learn that $$B$$ occurred, you have learned something enormous about $$A$$: it did not happen. Formally, $$P(A \mid B) = 0$$, which differs from $$P(A)$$ whenever $$A$$ is possible at all. Mutually exclusive events with nonzero probabilities are therefore never independent. Exclusivity is maximal dependence.

## Watching the two properties separate

The events below have fixed probabilities $$P(A) = 0.5$$ and $$P(B) = 0.4$$. The slider controls the only remaining freedom, the probability of the overlap, from 0 up to its largest possible value. The readout tracks the quantity independence cares about.

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

## The two-way table version

The exam most often probes this distinction through a two-way table, where both properties become arithmetic. Exclusivity is a zero in the joint cell. Independence is the multiplicative check: does the joint cell equal the product of the marginal totals, divided appropriately? A table can fail both, satisfy exclusivity alone, or satisfy independence alone; the one combination that is impossible, for events of positive probability, is both at once.

Two habits keep the distinction secure under exam conditions. First, always test independence numerically, by comparing $$P(A \text{ and } B)$$ with $$P(A)\,P(B)$$, or $$P(A \mid B)$$ with $$P(A)$$; the words in the problem never settle it, and "the groups seem unrelated" is not a justification the rubric accepts. Second, reserve the phrase "mutually exclusive" for the addition rule, where it does its real work: $$P(A \text{ or } B) = P(A) + P(B)$$ holds exactly when the overlap contributes nothing. Each property licenses its own rule, the overlap term is the hinge for both, and neither property can be inferred from the other.

<div class="article-note" markdown="1">
A question that separates the two ideas cleanly: draw one card from a standard deck, with $$A$$ the event of drawing a heart and $$B$$ the event of drawing a king. These events overlap, in the king of hearts, and they are independent, since $$P(A \text{ and } B) = \tfrac{1}{52}$$ while $$P(A)\,P(B) = \tfrac{13}{52}\cdot\tfrac{4}{52} = \tfrac{1}{52}$$ as well. Overlapping yet independent, the exact opposite of the intuition the vocabulary suggests, which is why the numerical test, not the vocabulary, is what earns the point.
</div>
