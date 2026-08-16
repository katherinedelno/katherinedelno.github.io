---
layout: post
title: "Increasing at a decreasing rate"
date: 2026-07-31
description: "Whether a function is increasing and whether its rate of change is increasing are separate questions. A table of average rates makes the distinction clear."
course: "AP Precalculus"
read_time: "8 min read"
math: true
kind: foundations
sequence: 1
interactive: true
featured: true
blurb: "Whether a function is increasing and whether its rate of change is increasing are separate questions. A table of average rates makes the distinction clear"
image: "/assets/og/increasing-at-a-decreasing-rate.png"
---

A function can be increasing while its rate of change is decreasing.

The phrase sounds contradictory only if those two statements are treated as the same question.

They are not.

One describes what the function values are doing.

The other describes what the rates of change are doing.

## Two questions

A function is increasing on an interval when larger inputs produce larger outputs.

The average rate of change over $$[a,b]$$ is

$$\frac{f(b)-f(a)}{b-a}.$$

If we compute average rates over consecutive equal-length intervals, we can then ask a second question.

Are those rates increasing or decreasing?

That gives four possible combinations:

- increasing at an increasing rate
- increasing at a decreasing rate
- decreasing at an increasing rate
- decreasing at a decreasing rate

The first word describes the function.

The second describes its rate of change.

## Read the table in order

<div class="viz" markdown="0">
  <div class="viz-controls" id="rc-modes"></div>
  <canvas id="rc-cv" width="700" height="268"></canvas>
  <div class="viz-controls">
    <label for="rc-i">Interval</label>
    <input type="range" id="rc-i" min="0" max="5" step="1" value="2">
    <span class="viz-value" id="rc-sec"></span>
  </div>
  <div class="rc-read" id="rc-read"></div>
  <p class="viz-caption">Four functions on the same seven inputs, one class of behavior each. The curve carries every secant, with the selected one drawn dark, and the table underneath gives the outputs, the average rate of change over each interval, and the change in those rates. Read the third column's signs to answer the first question and the fourth column's signs to answer the second. All four functions here are quadratics, which is why the last column is constant: the framework notes that a quadratic's average rates over consecutive equal-length intervals are themselves given by a linear function, so they change at a constant rate.</p>
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

The visualization shows four functions over the same inputs.

The table records the function values, the average rate of change on each interval, and the change in those rates.

Use the signs in order.

First, inspect the average rates.

If they are positive, the function is increasing.

If they are negative, the function is decreasing.

Then inspect how those rates change.

If the rates become larger, the rate of change is increasing.

If they become smaller, the rate of change is decreasing.

That procedure is more reliable than trying to guess from the wording.

## Negative rates are where the language gets difficult

Suppose a function is decreasing and its average rates are

$$-2.75,\quad -2.25,\quad -1.75,\quad -1.25.$$

The function is still decreasing because the rates are negative.

But the rates themselves are increasing because

$$-2.25>-2.75.$$

The function is therefore decreasing at an increasing rate.

Visually, it is falling while flattening out.

By contrast, if the rates become

$$-0.5,\quad -1,\quad -1.5,\quad -2,$$

the function is decreasing at a decreasing rate.

It is falling faster because the signed rates are becoming more negative.

The sign of the rate and the direction in which the rate moves have to be kept separate.

## Concavity describes the same second question

When rates of change are increasing, the graph is concave up.

When rates of change are decreasing, the graph is concave down.

So:

- increasing rate of change corresponds to concave up
- decreasing rate of change corresponds to concave down

For the quadratic examples in the visualization, the changes in average rate are constant across equal-length intervals.

That is a numerical feature of quadratics.

A linear function has constant average rate of change, so the changes in those rates are zero.

## This is already close to calculus

Average rate of change is the slope of a secant line.

As the interval becomes narrower, those secant slopes approach the rate of change at a point when the relevant limit exists.

Calculus calls that limiting rate [the derivative](/2026/07/30/derivative-as-a-limit.html).

The question of whether the rate itself is increasing or decreasing then becomes a question about the second derivative.

The language changes later.

The distinction does not.

<div class="article-note" markdown="1">
A useful self-test is a cooling cup of coffee. Its temperature decreases quickly at first and then more slowly as it approaches room temperature. The function is decreasing. Its rates are negative but becoming less negative, so the rate of change is increasing. The graph is concave up.
</div>
