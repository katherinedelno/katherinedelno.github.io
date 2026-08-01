---
layout: post
title: "Increasing at a decreasing rate"
date: 2026-07-31
description: "The phrase reads like a contradiction because its two halves describe different things. A table of successive average rates settles all four cases without a graph."
course: "AP Precalculus"
read_time: "8 min read"
math: true
kind: foundations
sequence: 1
interactive: true
featured: true
blurb: "The second half of the phrase is about the rate, not the function"
---

A quantity can be increasing and slowing down at the same time, and AP Precalculus has a phrase for it. The phrase reads like a contradiction only because its two halves are about different things: the first describes the function, and the second describes the function's rate of change.

This is the language the course adds that a previous precalculus course did not, and it is the reason the course counts as preparation for calculus. Crop yield rising but by less each year, a medicine losing efficacy faster and faster — the framework names both as understandings that inform real decisions, and both need two pieces of information rather than one.

## Two questions, asked separately

The first question is whether the output values go up or down. The framework's definition is about ordering and nothing else: a function is increasing over an interval if, for all $$a$$ and $$b$$ in it, $$a < b$$ implies $$f(a) < f(b)$$.

The second question is what the *rate* is doing, and it has its own definition. The average rate of change over $$[a,b]$$ is the slope of the secant line from $$\big(a, f(a)\big)$$ to $$\big(b, f(b)\big)$$. Compute it over consecutive equal-length intervals and a second sequence of numbers appears, one that describes the first sequence's behaviour. That second sequence is what the phrase's second half is about, and the framework attaches concavity to it directly: the graph is concave up on intervals where the rate of change is increasing, and concave down where it is decreasing.

Two sequences, two questions, four combinations. All four are examinable and all four appear below.

## Read the second column

<div class="viz" markdown="0">
  <div class="viz-controls" id="rc-modes"></div>
  <canvas id="rc-cv" width="700" height="268"></canvas>
  <div class="viz-controls">
    <label for="rc-i">Interval</label>
    <input type="range" id="rc-i" min="0" max="5" step="1" value="2">
    <span class="viz-value" id="rc-sec"></span>
  </div>
  <div class="rc-read" id="rc-read"></div>
  <p class="viz-caption">Four functions on the same seven inputs, one class of behaviour each. The curve carries every secant, with the selected one drawn dark, and the table underneath gives the outputs, the average rate of change over each interval, and the change in those rates. Read the third column's signs to answer the first question and the fourth column's signs to answer the second. All four functions here are quadratics, which is why the last column is constant: the framework notes that a quadratic's average rates over consecutive equal-length intervals are themselves given by a linear function, so they change at a constant rate.</p>
  <style>
    .rc-read{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line);
      font-size:.9rem;line-height:1.55;color:var(--ink);font-variant-numeric:tabular-nums}
    .rc-read table{border-collapse:collapse;width:100%}
    .rc-read th{text-align:right;font-size:.68rem;letter-spacing:.07em;text-transform:uppercase;
      color:var(--muted);font-weight:700;padding:0 0 6px}
    .rc-read td{text-align:right;padding:3px 0;border-top:1px solid var(--line)}
    .rc-read tr.on td{font-weight:700}
    .rc-read .rc-say{margin-top:.8rem;font-size:1.05rem;font-weight:700;letter-spacing:-.01em}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('rc-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('rc-i'), read = document.getElementById('rc-read');
  var sec = document.getElementById('rc-sec'), modes = document.getElementById('rc-modes');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97', PALE = '#c9c9c6';
  var FONT = 'Hanken Grotesk, sans-serif';
  var XLO = -0.4, XHI = 6.4, YLO = 0, YHI = 12.4;
  var PADL = 34, PADR = 14, TOP = 14, BOT = 246;

  var P = [
    { lab: 'up, faster',   f: function(x){ return x*x/4 + 2; } },
    { lab: 'up, slower',   f: function(x){ return -x*x/4 + 3*x + 2; } },
    { lab: 'down, faster', f: function(x){ return -x*x/4 + 11; } },
    { lab: 'down, slower', f: function(x){ return x*x/4 - 3*x + 11; } }
  ];
  var mode = 0;

  function px(x){ return PADL + (x - XLO)/(XHI - XLO)*(W - PADL - PADR); }
  function py(y){ return TOP + (YHI - y)/(YHI - YLO)*(BOT - TOP); }
  function num(v){ return (v > 0 ? '+' : v < 0 ? '−' : '') + Math.abs(v).toFixed(2); }

  function draw(){
    var f = P[mode].f, k = +sl.value, i;
    var xs = [0,1,2,3,4,5,6], ys = xs.map(f);
    var roc = [], dif = [];
    for(i = 0; i < 6; i++) roc.push(ys[i+1] - ys[i]);
    for(i = 0; i < 5; i++) dif.push(roc[i+1] - roc[i]);

    c.clearRect(0, 0, W, H);
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(PADL, py(0)); c.lineTo(W - PADR, py(0)); c.stroke();
    c.fillStyle = MUTED; c.font = '700 10px ' + FONT; c.textAlign = 'center';
    for(i = 0; i <= 6; i++) c.fillText(String(i), px(i), py(0) + 15);

    // the curve
    c.strokeStyle = PALE; c.lineWidth = 1.6; c.beginPath();
    for(i = 0; i <= 400; i++){
      var x = XLO + (XHI - XLO)*i/400, y = f(x);
      i ? c.lineTo(px(x), py(y)) : c.moveTo(px(x), py(y));
    }
    c.stroke();

    // every secant, faint, with the selected one dark
    for(i = 0; i < 6; i++){
      c.strokeStyle = i === k ? INK : '#dcdcda';
      c.lineWidth = i === k ? 2.4 : 1.4;
      c.beginPath(); c.moveTo(px(xs[i]), py(ys[i])); c.lineTo(px(xs[i+1]), py(ys[i+1])); c.stroke();
    }
    for(i = 0; i <= 6; i++){
      c.fillStyle = (i === k || i === k + 1) ? INK : FAINT;
      c.beginPath(); c.arc(px(xs[i]), py(ys[i]), (i === k || i === k + 1) ? 4.5 : 3, 0, 7); c.fill();
    }
    sec.textContent = 'slope of the secant from x = ' + k + ' to x = ' + (k+1) + ' is ' + num(roc[k]);

    // table
    var rows = '<tr><th style="text-align:left">x</th><th>f(x)</th>' +
               '<th>average rate of change</th><th>change in that rate</th></tr>';
    for(i = 0; i <= 6; i++){
      var on = (i === k || i === k + 1) ? ' class="on"' : '';
      rows += '<tr' + on + '><td style="text-align:left">' + i + '</td><td>' + ys[i].toFixed(2) + '</td>' +
              '<td>' + (i < 6 ? num(roc[i]) : '') + '</td>' +
              '<td>' + (i < 5 ? num(dif[i]) : '') + '</td></tr>';
    }
    var up = roc.every(function(v){ return v > 0; });
    var faster = dif.every(function(v){ return v > 0; });
    read.innerHTML = '<table>' + rows + '</table>' +
      '<div class="rc-say">' + (up ? 'increasing' : 'decreasing') + ' at ' +
      (faster ? 'an increasing' : 'a decreasing') + ' rate' +
      '<span style="font-weight:400;color:var(--muted);font-size:.9rem"> &mdash; concave ' +
      (faster ? 'up' : 'down') + '</span></div>';
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
      draw();
    });
    modes.appendChild(b);
  });
  sl.addEventListener('input', draw);
  draw();
})();
</script>

## The half that catches people

Three of the four cases behave the way the words sound. The fourth does not.

Take the last function. Its outputs fall from 11 to 2, so it is decreasing, and nobody disputes that. Its rates of change are $$-2.75$$, then $$-2.25$$, then $$-1.75$$, and so on up to $$-0.25$$. Those numbers are getting *larger*. The rate of change is increasing, and the correct phrase is *decreasing at an increasing rate* — for a curve that is visibly flattening out as it falls.

The pull is to call it a decreasing rate, because the drop is getting gentler. That reads the size of the rate instead of the rate. The framework's definitions are about the signed quantity throughout, and its own worked example settles it: over $$[\tfrac{\pi}{2}, \pi]$$, where sine falls from 1 to 0 and falls faster as it goes, the framework says the values of sine *decrease at a decreasing rate*. Falling faster is the decreasing rate. Falling more slowly is the increasing one.

So the reliable procedure is the table rather than the phrase. Sign of the third column answers the first half. Sign of the fourth column answers the second half. The compound phrase is then assembled rather than guessed, and the word *concave* can be attached at the same moment, since it is a claim about the same fourth column.

## Why the table is short for these four

Every function above is quadratic, and the fourth column is constant in all four — always $$+0.5$$ or $$-0.5$$. That is not a property of these examples. The framework states it in general: for a quadratic, the average rates of change over consecutive equal-length intervals are given by a linear function, so those rates change at a constant rate. For a linear function the same reasoning gives rates that are constant and therefore change at a rate of zero, which is why a line is neither concave up nor concave down.

This is the numerical fingerprint of degree, and it is the reason the framework can define a polynomial's degree by successive differences: the column where the differences go constant tells you which degree you are looking at.

## Where this goes next

The third column is a difference quotient before it has been given that name. Shrink the interval width toward zero and the average rate of change over $$[a, b]$$ becomes the rate of change *at* a point, which the framework already describes as the limit of exactly this construction — the rate at a point can be approximated by average rates over small intervals containing it.

Calculus renames that limit the derivative and renames the fourth column the second derivative. Nothing else changes. A student who reads these two columns fluently has met [the central idea of the next course](/2026/07/30/derivative-as-a-limit.html) twice before anyone defines it.

<div class="article-note" markdown="1">
A self-test worth doing on paper, with the tool closed: a cup of coffee cools toward room temperature. Its temperature is decreasing, and it cools fastest at the start. Which of the four phrases applies, and is the graph concave up or concave down? Write the third and fourth columns for a few plausible temperatures before answering, because the phrase alone will pull you the wrong way. The answer is that a cooling coffee is decreasing at an increasing rate and its graph is concave up, which sounds wrong and is the whole point of keeping the table.
</div>
