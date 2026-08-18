---
layout: post
title: "What the factored form tells you"
date: 2026-07-31
description: "Factored form reveals zeros, multiplicity, holes, vertical asymptotes, and much of a function's end behavior before the graph is drawn."
course: "AP Precalculus"
read_time: "6 min read"
math: true
kind: foundations
sequence: 2
interactive: true
blurb: "Factored form reveals zeros, multiplicity, holes, vertical asymptotes, and much of a function's end behavior before the graph is drawn"
image: "/assets/og/what-the-factored-form-tells-you.png"
---

A factored expression contains a large amount of graphical information. Its factors identify zeros, and their multiplicities tell us whether the graph crosses or only touches the axis. For rational functions, comparing multiplicities in the numerator and denominator distinguishes holes from vertical asymptotes, and the leading terms describe end behavior.

## Zeros and factors

For a polynomial, the factor theorem says that $$(x-a)$$ is a factor exactly when $$f(a)=0$$. So a factor of $$(x+3)$$ gives a zero at $$x=-3$$, and a factor of $$(x-2)$$ gives a zero at $$x=2$$. The sign inside the factor is opposite the value of the zero because the factor becomes zero when the two terms cancel.

## Multiplicity changes the crossing

<div class="viz" markdown="0">
  <div class="viz-controls" id="ff-modes"></div>
  <canvas id="ff-cv" width="700" height="322"></canvas>
  <div class="viz-controls">
    <label for="ff-a">a</label>
    <input type="range" id="ff-a" min="-320" max="320" step="1" value="-280">
    <span class="viz-value" id="ff-expr" style="min-width:100%"></span>
  </div>
  <div class="ff-read" id="ff-read"></div>
  <p class="viz-caption">Four expressions, all in factored form, with one root under the slider. The curve is drawn from the factors directly, and every marker on it is placed by comparing multiplicities rather than by inspecting the picture: a filled dot is a zero, an open dot is a hole, a dashed vertical is an asymptote. On the first two, slide a onto the neighboring root and watch what the graph does at the moment the two become one. On the last two, slide a onto 1 and compare the results, because those two expressions differ only in an exponent and they do not end up the same.</p>
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
    // a negative root would otherwise print as "(x−-1.25)", so fold the sign into
    // the operator rather than leaving two of them side by side
    expr.textContent = P[mode].lab.replace(/(.)a\)/, function(whole, minus){
      return (a < 0 ? '+' : minus) + ' ' + Math.abs(a).toFixed(2) + ')';
    });
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

The visualization lets one root move while the other factors stay fixed. Suppose a factor appears once, $$(x-a)$$. Its sign changes as $$x$$ passes through $$a$$, and if the remaining factors keep their signs nearby, the entire product changes sign and the graph crosses the axis. Now suppose the factor appears twice, $$(x-a)^2$$. A square is nonnegative on both sides of $$a$$, so its sign does not change and the graph touches the axis and turns back.

More generally:

- odd multiplicity usually produces a crossing
- even multiplicity produces a touch or tangency
- larger multiplicities make the graph flatter near the zero

A zero of multiplicity 3 still crosses, and it simply does so with more flattening than a simple zero.

## Holes and vertical asymptotes

For rational functions, a denominator factor does not automatically mean a vertical asymptote, and the multiplicities in the numerator and denominator have to be compared. Suppose $$x=a$$ appears with multiplicity $$m$$ in the numerator and $$n$$ in the denominator. If $$n>m$$, a denominator factor remains after simplification, and the graph has a vertical asymptote at $$x=a$$. If $$m\ge n$$, the denominator factor is fully removed, and the original function is still undefined at $$x=a$$, so the graph has a hole.

This distinction matters when factors repeat. For example, one factor of $$(x-1)$$ in the numerator and two in the denominator still leaves $$\tfrac{1}{x-1}$$ after cancellation. The graph therefore still has a vertical asymptote, and the fact that something canceled is not enough to conclude that there is a hole.

## End behavior

For large values of $$\vert x\vert$$, a polynomial is dominated by its leading term, so a rational function has the same end behavior as the quotient of its leading terms. If the denominator has higher degree than the numerator, $$f(x)\to0$$ as $$\vert x\vert \to\infty$$. If the degrees are equal, the function approaches the ratio of the leading coefficients, and if the numerator has higher degree, there is no horizontal asymptote.

Polynomial division can reveal a slant or higher-degree asymptote when appropriate. These conclusions come from the dominant powers, not from the smaller terms.

## Read before graphing

Given a factored rational function, it is worth making a short inventory before touching a calculator. Identify:

- the zeros and their multiplicities
- the excluded inputs
- whether each excluded input produces a hole or vertical asymptote
- the leading terms and end behavior

Then sketch.

<div class="article-note" markdown="1">
The graph should confirm what the algebra already predicted.
</div>
