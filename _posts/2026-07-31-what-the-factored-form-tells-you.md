---
layout: post
title: "What the factored form tells you"
date: 2026-07-31
description: "Zeros, tangencies, holes, and asymptotes are four readings of one factored expression. The rule that separates a hole from an asymptote is a comparison, not a cancellation."
course: "AP Precalculus"
read_time: "8 min read"
math: true
kind: foundations
sequence: 2
interactive: true
blurb: "One expression, read four ways: zeros, tangencies, holes, and asymptotes"
---

A factored expression is not a step on the way to a graph. It is the graph, written down, and almost every question Unit 1 asks is a request to read one line of it out loud.

The framework starts from a single equivalence: if $$a$$ is a real number, then $$(x-a)$$ is a linear factor of a polynomial exactly when $$a$$ is a zero of it. Every other reading in this article is that sentence with something attached — a repeated factor, a factor downstairs, or the largest factor of all.

## Two zeros, becoming one

The slider below moves one root. The other factors stay where they are.

<div class="viz" markdown="0">
  <div class="viz-controls" id="ff-modes"></div>
  <canvas id="ff-cv" width="700" height="322"></canvas>
  <div class="viz-controls">
    <label for="ff-a">a</label>
    <input type="range" id="ff-a" min="-320" max="320" step="1" value="-280">
    <span class="viz-value" id="ff-expr" style="min-width:100%"></span>
  </div>
  <div class="ff-read" id="ff-read"></div>
  <p class="viz-caption">Four expressions, all in factored form, with one root under the slider. The curve is drawn from the factors directly, and every marker on it is placed by comparing multiplicities rather than by inspecting the picture: a filled dot is a zero, an open dot is a hole, a dashed vertical is an asymptote. On the first two, slide a onto the neighbouring root and watch what the graph does at the moment the two become one. On the last two, slide a onto 1 and compare the results, because those two expressions differ only in an exponent and they do not end up the same.</p>
  <style>
    .ff-read{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .ff-read .ff-lab{color:var(--muted);display:inline-block;min-width:11rem}
    .ff-read .ff-val{font-weight:700}
    .ff-read .ff-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('ff-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('ff-a'), read = document.getElementById('ff-read');
  var expr = document.getElementById('ff-expr'), modes = document.getElementById('ff-modes');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97', PALE = '#c9c9c6';
  var FONT = 'Hanken Grotesk, sans-serif';
  var XLO = -4.6, XHI = 5.6, YLO = -6, YHI = 6;
  var PADL = 34, PADR = 14, TOP = 12, BOT = 300;

  // each preset lists numerator and denominator roots as [root, multiplicity];
  // the string 'a' means the root under the slider
  var P = [
    { lab: '(x−a)(x+1)(x−3)',        num: [['a',1], [-1,1], [3,1]], den: [] },
    { lab: '(x−a)(x+1)²(x−3)',       num: [['a',1], [-1,2], [3,1]], den: [] },
    { lab: '(x−1)(x+2) ⁄ (x−a)(x−4)',  num: [[1,1], [-2,1]], den: [['a',1], [4,1]] },
    { lab: '(x−1)(x+2) ⁄ (x−a)²(x−4)', num: [[1,1], [-2,1]], den: [['a',2], [4,1]] }
  ];
  var mode = 0;

  function px(x){ return PADL + (x - XLO)/(XHI - XLO)*(W - PADL - PADR); }
  function py(y){ return TOP + (YHI - y)/(YHI - YLO)*(BOT - TOP); }
  function roots(list, a){
    return list.map(function(r){ return [r[0] === 'a' ? a : r[0], r[1]]; });
  }
  // net multiplicity at each distinct root, which is what the framework compares
  function features(a){
    var num = roots(P[mode].num, a), den = roots(P[mode].den, a), map = {};
    num.forEach(function(r){ var k = r[0].toFixed(4); map[k] = map[k] || [r[0],0,0]; map[k][1] += r[1]; });
    den.forEach(function(r){ var k = r[0].toFixed(4); map[k] = map[k] || [r[0],0,0]; map[k][2] += r[1]; });
    var out = [];
    for(var k in map){
      var x = map[k][0], m = map[k][1], d = map[k][2];
      if(d === 0)      out.push({ x: x, kind: 'zero', mult: m });
      else if(m >= d)  out.push({ x: x, kind: 'hole', mult: m - d });
      else             out.push({ x: x, kind: 'asymptote', mult: d - m });
    }
    return out.sort(function(p, q){ return p.x - q.x; });
  }
  // evaluate the reduced form, so a cancelled factor never produces 0/0
  function f(x, a){
    var fs = features(a), y = 1, i;
    for(i = 0; i < fs.length; i++){
      var t = fs[i];
      if(t.kind === 'asymptote') y /= Math.pow(x - t.x, t.mult);
      else y *= Math.pow(x - t.x, t.mult);
    }
    return y;
  }

  function draw(){
    var a = (+sl.value)/64, fs = features(a);
    c.clearRect(0, 0, W, H);

    // axes
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(PADL, py(0)); c.lineTo(W - PADR, py(0)); c.stroke();
    c.beginPath(); c.moveTo(px(0), TOP); c.lineTo(px(0), BOT); c.stroke();
    c.fillStyle = MUTED; c.font = '700 10px ' + FONT; c.textAlign = 'center';
    for(var t = -4; t <= 5; t++){ if(t) c.fillText(String(t), px(t), py(0) + 14); }

    // asymptotes
    c.strokeStyle = PALE; c.setLineDash([5, 4]); c.lineWidth = 1.2;
    fs.forEach(function(t){
      if(t.kind !== 'asymptote') return;
      c.beginPath(); c.moveTo(px(t.x), TOP); c.lineTo(px(t.x), BOT); c.stroke();
    });
    c.setLineDash([]);

    // the curve, broken at every asymptote and wherever it leaves the window
    c.strokeStyle = INK; c.lineWidth = 2;
    var N = 2400, started = false, prev = null;
    c.beginPath();
    for(var i = 0; i <= N; i++){
      var x = XLO + (XHI - XLO)*i/N;
      var brk = fs.some(function(t){ return t.kind === 'asymptote' && Math.abs(x - t.x) < 0.012; });
      var y = f(x, a);
      if(brk || !isFinite(y) || y < YLO - 2 || y > YHI + 2){ started = false; prev = y; continue; }
      if(prev !== null && started && Math.abs(y - prev) > 8){ started = false; }
      started ? c.lineTo(px(x), py(y)) : (c.moveTo(px(x), py(y)), started = true);
      prev = y;
    }
    c.stroke();

    // markers
    fs.forEach(function(t){
      if(t.kind === 'asymptote') return;
      var yv = t.kind === 'zero' ? 0 : f(t.x + 1e-7, a);
      if(!isFinite(yv) || yv < YLO || yv > YHI) return;
      c.beginPath(); c.arc(px(t.x), py(yv), 5, 0, 7);
      if(t.kind === 'zero'){ c.fillStyle = INK; c.fill(); }
      else { c.fillStyle = '#fff'; c.fill(); c.strokeStyle = INK; c.lineWidth = 2; c.stroke(); }
    });

    // readout
    expr.textContent = P[mode].lab.replace('a', a.toFixed(2));
    var lines = fs.map(function(t){
      var word = t.kind === 'zero'
          ? (t.mult === 1 ? 'crosses' : (t.mult % 2 === 0 ? 'tangent to the axis' : 'flattens through'))
          : (t.kind === 'hole' ? 'hole' : 'vertical asymptote');
      return '<div><span class="ff-lab">x = ' + t.x.toFixed(2) + '</span><span class="ff-val">' +
             word + '</span> <span class="ff-note">' +
             (t.kind === 'zero' ? 'multiplicity ' + t.mult
              : t.kind === 'hole' ? 'numerator multiplicity at least the denominator&rsquo;s'
              : 'denominator multiplicity exceeds the numerator&rsquo;s by ' + t.mult) +
             '</span></div>';
    });
    read.innerHTML = lines.join('');
  }

  P.forEach(function(p, i){
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'res-filter' + (i === 0 ? ' is-active' : '');
    b.style.fontSize = '.72rem'; b.textContent = p.lab;
    b.addEventListener('click', function(){
      mode = i;
      Array.prototype.forEach.call(modes.children, function(o, j){
        o.classList[j === i ? 'add' : 'remove']('is-active');
      });
      sl.value = i < 2 ? -280 : 192;
      draw();
    });
    modes.appendChild(b);
  });
  sl.addEventListener('input', draw);
  draw();
})();
</script>

## Even multiplicity is a tangency

Take the first expression and slide $$a$$ up to $$-1$$. Two separate crossings drift together, meet, and the graph stops crossing: it comes down to the axis, touches, and turns back. The factor $$(x+1)$$ is now repeated, and the framework says what that repetition costs. If a real zero has even multiplicity, the signs of the output values are the same on both sides of it, so the graph is tangent to the $$x$$-axis there.

Sign is the whole mechanism. A factor $$(x-a)$$ changes sign as $$x$$ passes $$a$$; a factor $$(x-a)^2$$ does not, because a square is never negative. Every other factor is far from $$a$$ and holds its sign across the crossing, so the product changes sign exactly when the repeated factor does — which is to say, only when its multiplicity is odd.

Now switch to the second expression and repeat the move. Three factors of $$(x+1)$$ this time, so the sign does change and the graph does cross, but it arrives flattened, pressing itself against the axis before letting go. Odd multiplicity crosses; higher odd multiplicity crosses lazily. The framework counts these carefully because a polynomial of degree $$n$$ has exactly $$n$$ complex zeros when multiplicities are counted, and the count is only right if a repeated factor is allowed to be worth more than one.

## The rule that separates a hole from an asymptote

Most treatments say a common factor cancels and leaves a hole. That is true often enough to be dangerous, and the framework does not say it. It compares multiplicities instead.

A vertical asymptote occurs at $$x = a$$ when the multiplicity of $$a$$ in the denominator is greater than its multiplicity in the numerator. A hole occurs when the multiplicity in the numerator is greater than or equal to the multiplicity in the denominator. One comparison, both outcomes, and no cancelling.

The last two expressions are built to show why the distinction is not pedantry. They are identical except for one exponent. Slide $$a$$ onto 1 in the third and the factor $$(x-1)$$ appears once above and once below, the multiplicities tie, and the asymptote collapses into a hole at $$(1, -1)$$ — a single missing point on an otherwise ordinary curve. Slide $$a$$ onto 1 in the fourth and the same $$(x-1)$$ appears once above and *twice* below. A factor cancels there too. The asymptote stays.

Anyone reasoning by cancellation gets the fourth one wrong, and the readout underneath is doing the comparison rather than looking at the picture, which is the habit worth copying.

## The largest factor decides the ends

The last reading is the coarsest. For inputs of large magnitude a polynomial is dominated by its leading term, so the end behaviour of a rational function is the end behaviour of the quotient of the two leading terms — a claim that ignores every factor except the biggest one.

Three outcomes follow, and the framework organises them by which polynomial dominates. When the denominator wins, the quotient tends to zero and the graph flattens onto the horizontal axis. When neither wins, the quotient is the ratio of the leading coefficients and the graph flattens onto that height. When the numerator wins, there is no horizontal asymptote at all, and the graph instead takes on the end behaviour of the leftover polynomial — which, in the single case where that leftover is linear, is a slant asymptote.

<div class="article-note" markdown="1">
A prediction to test at the slider: on the fourth expression, set $$a$$ to 1 and then ask what would have to change for the asymptote to become a hole. Not the cancelling, which already happens. The numerator would need a second factor of $$(x-1)$$, so that the multiplicities tie at two apiece. Write the resulting expression and check that its graph has a hole where an asymptote used to be. A student who can construct that example on demand has stopped reading rational functions by cancellation and started reading them by multiplicity, which is the only version that survives contact with a repeated factor.
</div>
