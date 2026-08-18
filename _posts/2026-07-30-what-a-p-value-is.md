---
layout: post
title: "What a p-value cannot tell you"
date: 2026-07-30
description: "A p-value measures how unusual the observed result would be if the null hypothesis were true. It is not the probability that the null is true."
course: "AP Statistics"
read_time: "5 min read"
math: true
kind: foundations
sequence: 13
interactive: true
blurb: "A p-value measures how unusual the observed result would be if the null hypothesis were true. It is not the probability that the null is true"
image: "/assets/og/what-a-p-value-is.png"
---

A p-value is calculated under the assumption that the null hypothesis is true. It measures how unusual the observed result would be in that null world, and it does not measure the probability that the null hypothesis itself is true.

## A null distribution

Suppose a testing service claims that exam scores have mean $$\mu=50$$ with known standard deviation 10, and a school samples 25 students and obtains $$\bar x=53.92$$. Under the null hypothesis $$H_0:\mu=50$$, [the sampling distribution](/2026/07/25/central-limit-theorem-watched-live.html) of $$\bar X$$ has mean 50 and standard deviation $$\tfrac{10}{\sqrt{25}}=2$$.

<div class="viz" markdown="0">
  <canvas id="pv-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <button type="button" id="pv-sim" class="res-filter is-active" style="font-size:.72rem">Simulation</button>
    <button type="button" id="pv-thy" class="res-filter" style="font-size:.72rem">Theory</button>
    <span style="width:14px"></span>
    <label for="pv-alt">Alternative</label>
    <button type="button" id="pv-lt" class="res-filter" style="font-size:.72rem">&mu; &lt; 50</button>
    <button type="button" id="pv-gt" class="res-filter is-active" style="font-size:.72rem">&mu; &gt; 50</button>
    <button type="button" id="pv-ne" class="res-filter" style="font-size:.72rem">&mu; &ne; 50</button>
  </div>
  <div class="viz-controls">
    <label for="pv-x">Observed mean</label>
    <input type="range" id="pv-x" min="4400" max="5800" step="1" value="5392">
    <label for="pv-n">n</label>
    <input type="range" id="pv-n" min="4" max="400" step="1" value="25">
    <label for="pv-a">&alpha;</label>
    <button type="button" id="pv-a10" class="res-filter" style="font-size:.72rem">0.10</button>
    <button type="button" id="pv-a05" class="res-filter is-active" style="font-size:.72rem">0.05</button>
    <button type="button" id="pv-a01" class="res-filter" style="font-size:.72rem">0.01</button>
  </div>
  <div class="viz-controls">
    <button type="button" id="pv-d100" class="res-filter" style="font-size:.72rem">Draw 100</button>
    <button type="button" id="pv-d1k" class="res-filter" style="font-size:.72rem">Draw 1000</button>
    <button type="button" id="pv-clr" class="res-filter" style="font-size:.72rem">Clear</button>
    <span class="viz-value" id="pv-read" style="min-width:100%"></span>
  </div>
  <p class="viz-caption">Every dot is one study run in a world where the mean really is 50. Dark dots are the studies that came out as extreme as the observed result or more so; the running share of them is what the p-value counts. Switch to Theory and the same region appears as area under the curve, which is what we compute instead of counting. Drag the observed mean, or the sample size, and watch both numbers move together. Changing the alternative recolors the dots without redrawing them: the studies, the distribution, and the observed result do not depend on the question being asked.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('pv-cv'), c = cv.getContext('2d');
  var read = document.getElementById('pv-read');
  var slX = document.getElementById('pv-x'), slN = document.getElementById('pv-n');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);

  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97',
      PALE = '#d6d6d3', SHADE = 'rgba(31,31,31,0.13)';
  var FONT = 'Hanken Grotesk, sans-serif';

  var MU0 = 50, SIGMA = 10;
  var XLO = 42, XHI = 58;
  var PADL = 44, PADR = 22, TOP = 16, AXIS = H - 62;
  var view = 'sim', dir = 'gt', alpha = 0.05;
  var sims = [], drag = false;

  function se(){ return SIGMA/Math.sqrt(+slN.value); }
  function xobs(){ return (+slX.value)/100; }
  function px(x){ return PADL + (x - XLO)/(XHI - XLO)*(W - PADL - PADR); }

  // Standard normal CDF, Hart 1968. Absolute error below 3e-16 against
  // published values; the article's ledger records the check.
  function Phi(z){
    var x = Math.abs(z), r;
    if(x > 37) r = 0;
    else {
      var e = Math.exp(-x*x/2), b, q;
      if(x < 7.07106781186547){
        b = 3.52624965998911e-02*x + 0.700383064443688;
        b = b*x + 6.37396220353165;   b = b*x + 33.912866078383;
        b = b*x + 112.079291497871;   b = b*x + 221.213596169931;
        b = b*x + 220.206867912376;
        q = 8.83883476483184e-02*x + 1.75566716318264;
        q = q*x + 16.064177579207;    q = q*x + 86.7807322029461;
        q = q*x + 296.564248779674;   q = q*x + 637.333633378831;
        q = q*x + 793.826512519948;   q = q*x + 440.413735824752;
        r = e*b/q;
      } else {
        b = x + 0.65; b = x + 4/b; b = x + 3/b; b = x + 2/b; b = x + 1/b;
        r = e/(b*2.506628274631);
      }
    }
    return z <= 0 ? r : 1 - r;
  }
  function phi(z){ return Math.exp(-z*z/2)/Math.sqrt(2*Math.PI); }
  function gauss(){
    var u = 1 - Math.random(), v = Math.random();
    return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);
  }
  function zOf(){ return (xobs() - MU0)/se(); }
  function tails(){
    var z = zOf(), one = 1 - Phi(Math.abs(z));
    if(dir === 'lt') return { p: Phi(z), lo: Phi(z), hi: 0 };
    if(dir === 'gt') return { p: 1 - Phi(z), lo: 0, hi: 1 - Phi(z) };
    return { p: 2*one, lo: one, hi: one };
  }
  function extreme(xs){
    var xo = xobs();
    if(dir === 'lt') return xs <= xo;
    if(dir === 'gt') return xs >= xo;
    return Math.abs(xs - MU0) >= Math.abs(xo - MU0);
  }
  function fmtP(p){
    if(p < 0.0001) return p.toExponential(1).replace('e-', ' x 10^-');
    return p.toFixed(4);
  }

  function axes(){
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(PADL, AXIS + 0.5); c.lineTo(W - PADR, AXIS + 0.5); c.stroke();
    c.fillStyle = MUTED; c.font = '700 11px ' + FONT; c.textAlign = 'center';
    for(var v = XLO; v <= XHI; v += 2){
      c.beginPath(); c.moveTo(px(v), AXIS); c.lineTo(px(v), AXIS + 4); c.stroke();
      c.fillText(String(v), px(v), AXIS + 17);
    }
    c.fillStyle = FAINT; c.font = '700 10px ' + FONT;
    c.fillText('sample mean', px((XLO + XHI)/2), AXIS + 32);
    // null value marker
    c.strokeStyle = PALE; c.setLineDash([3,3]); c.lineWidth = 1;
    c.beginPath(); c.moveTo(px(MU0), TOP); c.lineTo(px(MU0), AXIS); c.stroke();
    c.setLineDash([]);
    c.fillStyle = FAINT; c.font = '700 10px ' + FONT; c.textAlign = 'left';
    c.fillText('null: 50', px(MU0) + 5, TOP + 9);
  }
  function observedLine(){
    var X = px(xobs());
    c.strokeStyle = INK; c.lineWidth = 2;
    c.beginPath(); c.moveTo(X, TOP - 4); c.lineTo(X, AXIS); c.stroke();
    c.fillStyle = INK; c.beginPath();
    c.moveTo(X, TOP - 4); c.lineTo(X - 4, TOP - 10); c.lineTo(X + 4, TOP - 10); c.closePath(); c.fill();
    c.font = '700 11px ' + FONT; c.textAlign = X > W - 110 ? 'right' : 'left';
    c.fillText('observed ' + xobs().toFixed(2), X + (X > W - 110 ? -6 : 6), TOP + 6);
  }

  function drawSim(){
    var bins = 128, lo = XLO, hi = XHI, wBin = (hi - lo)/bins;
    var col = new Array(bins), colX = new Array(bins), tallest = 0, k;
    for(k = 0; k < bins; k++){ col[k] = 0; colX[k] = 0; }
    for(var i = 0; i < sims.length; i++){
      var b = Math.floor((sims[i] - lo)/wBin);
      if(b < 0 || b >= bins) continue;
      col[b]++; if(extreme(sims[i])) colX[b]++;
      if(col[b] > tallest) tallest = col[b];
    }
    var room = AXIS - TOP - 6;
    var step = tallest > 0 ? Math.min(4.2, room/tallest) : 4.2;
    var rad = Math.max(0.85, Math.min(1.9, step*0.42));
    for(k = 0; k < bins; k++){
      if(!col[k]) continue;
      var cx = px(lo + (k + 0.5)*wBin);
      for(var j = 0; j < col[k]; j++){
        c.fillStyle = j < colX[k] ? INK : PALE;
        c.beginPath(); c.arc(cx, AXIS - 3 - j*step, rad, 0, 7); c.fill();
      }
    }
    var hits = 0;
    for(i = 0; i < sims.length; i++) if(extreme(sims[i])) hits++;
    var share = sims.length ? hits/sims.length : 0;
    c.fillStyle = MUTED; c.font = '700 11px ' + FONT; c.textAlign = 'left';
    if(sims.length){
      c.fillText(hits.toLocaleString() + ' of ' + sims.length.toLocaleString() +
                 ' studies as extreme or more:  ' + share.toFixed(4), PADL, AXIS + 47);
    } else {
      c.fillText('No studies yet. Press Draw 1000.', PADL, AXIS + 47);
    }
  }

  function drawTheory(){
    var s = se(), pk = phi(0)/s, room = AXIS - TOP - 10;
    function py(dens){ return AXIS - dens/pk*room; }
    function dens(x){ return phi((x - MU0)/s)/s; }
    var t = tails(), xo = xobs(), gap = Math.abs(xo - MU0), i, x;
    // shaded regions
    function shade(from, to){
      c.fillStyle = SHADE; c.beginPath(); c.moveTo(px(from), AXIS);
      for(i = 0; i <= 240; i++){ x = from + (to - from)*i/240; c.lineTo(px(x), py(dens(x))); }
      c.lineTo(px(to), AXIS); c.closePath(); c.fill();
    }
    if(dir === 'lt') shade(XLO - 6, xo);
    else if(dir === 'gt') shade(xo, XHI + 6);
    else { shade(XLO - 6, MU0 - gap); shade(MU0 + gap, XHI + 6); }
    // curve
    c.strokeStyle = INK; c.lineWidth = 2; c.beginPath();
    for(i = 0; i <= 480; i++){
      x = XLO + (XHI - XLO)*i/480;
      i ? c.lineTo(px(x), py(dens(x))) : c.moveTo(px(x), py(dens(x)));
    }
    c.stroke();
    // mirrored bound for the two-sided case
    if(dir === 'ne'){
      var m = MU0 - gap;
      c.strokeStyle = MUTED; c.setLineDash([4,3]); c.lineWidth = 1.5;
      c.beginPath(); c.moveTo(px(m), TOP); c.lineTo(px(m), AXIS); c.stroke();
      c.setLineDash([]);
      c.fillStyle = MUTED; c.font = '700 11px ' + FONT; c.textAlign = 'right';
      c.fillText('mirror ' + m.toFixed(2), px(m) - 6, TOP + 6);
    }
    c.fillStyle = MUTED; c.font = '700 11px ' + FONT; c.textAlign = 'left';
    var msg = dir === 'ne'
      ? 'left tail ' + t.lo.toFixed(4) + '   +   right tail ' + t.hi.toFixed(4) +
        '   =   ' + t.p.toFixed(4)
      : 'shaded area  =  ' + fmtP(t.p);
    c.fillText(msg, PADL, AXIS + 47);
  }

  function draw(){
    c.clearRect(0, 0, W, H);
    axes();
    view === 'sim' ? drawSim() : drawTheory();
    observedLine();
    var t = tails(), z = zOf(), n = +slN.value;
    var verdict = t.p <= alpha
      ? 'reject the null: the data are too surprising under it'
      : 'fail to reject the null: the data are not surprising under it';
    read.innerHTML = 'n = ' + n + ',  SE = ' + se().toFixed(4) +
      ',  z = ' + z.toFixed(3) + ',  p = ' + fmtP(t.p) +
      '<br>p ' + (t.p <= alpha ? '&le;' : '&gt;') + ' &alpha; = ' + alpha.toFixed(2) + ', so ' + verdict;
  }

  function drawStudies(m){
    var n = +slN.value, s = se();
    for(var i = 0; i < m; i++) sims.push(MU0 + s*gauss());
    if(sims.length > 60000) sims = sims.slice(sims.length - 60000);
    if(view !== 'sim'){ view = 'sim'; setView(); }
    draw();
  }
  function setActive(id, on){
    document.getElementById(id).classList[on ? 'add' : 'remove']('is-active');
  }
  function setView(){
    setActive('pv-sim', view === 'sim'); setActive('pv-thy', view === 'thy');
  }
  function setDir(d){
    dir = d;
    setActive('pv-lt', d === 'lt'); setActive('pv-gt', d === 'gt'); setActive('pv-ne', d === 'ne');
    draw();
  }
  function setAlpha(a){
    alpha = a;
    setActive('pv-a10', a === 0.10); setActive('pv-a05', a === 0.05); setActive('pv-a01', a === 0.01);
    draw();
  }

  document.getElementById('pv-sim').addEventListener('click', function(){ view = 'sim'; setView(); draw(); });
  document.getElementById('pv-thy').addEventListener('click', function(){ view = 'thy'; setView(); draw(); });
  document.getElementById('pv-lt').addEventListener('click', function(){ setDir('lt'); });
  document.getElementById('pv-gt').addEventListener('click', function(){ setDir('gt'); });
  document.getElementById('pv-ne').addEventListener('click', function(){ setDir('ne'); });
  document.getElementById('pv-a10').addEventListener('click', function(){ setAlpha(0.10); });
  document.getElementById('pv-a05').addEventListener('click', function(){ setAlpha(0.05); });
  document.getElementById('pv-a01').addEventListener('click', function(){ setAlpha(0.01); });
  document.getElementById('pv-d100').addEventListener('click', function(){ drawStudies(100); });
  document.getElementById('pv-d1k').addEventListener('click', function(){ drawStudies(1000); });
  document.getElementById('pv-clr').addEventListener('click', function(){ sims = []; draw(); });
  slX.addEventListener('input', draw);
  slN.addEventListener('input', function(){ sims = []; draw(); });

  function fromEvent(ev){
    var r = cv.getBoundingClientRect();
    var cx = (ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left;
    var x = XLO + (cx/r.width*W - PADL)/(W - PADL - PADR)*(XHI - XLO);
    slX.value = Math.round(Math.max(XLO + 2, Math.min(XHI, x))*100);
    draw();
  }
  cv.addEventListener('mousedown', function(ev){ drag = true; fromEvent(ev); });
  window.addEventListener('mousemove', function(ev){ if(drag) fromEvent(ev); });
  window.addEventListener('mouseup', function(){ drag = false; });
  cv.addEventListener('touchstart', function(ev){ drag = true; fromEvent(ev); ev.preventDefault(); });
  cv.addEventListener('touchmove', function(ev){ if(drag){ fromEvent(ev); ev.preventDefault(); } });
  cv.addEventListener('touchend', function(){ drag = false; });

  drawStudies(1000);
})();
</script>

The simulation repeatedly generates studies under $$H_0$$. The p-value is the proportion of those null studies that produce a result at least as extreme as the observed one, in the direction specified by the alternative. The theory view calculates the same probability as area under the null distribution.

## The alternative determines the tail

For $$H_a:\mu>50$$, results at least as extreme as $$\bar x=53.92$$ lie in the right tail, and the p-value is about $$0.025$$. For $$H_a:\mu<50$$, the relevant tail runs left from the observed value, producing a very large p-value. For $$H_a:\mu\neq50$$, both tails count, and the two-sided p-value is about $$0.050$$.

The data and null distribution did not change. The definition of “as extreme” changed with the alternative hypothesis.

## What a p-value is not

It is not $$P(H_0\text{ is true}\mid\text{data})$$. The calculation assumes $$H_0$$ in order to generate the reference distribution. It is also not the probability that the test made an error, and the probability of rejecting a true null is controlled by the significance level $$\alpha$$, not by the observed p-value.

A large p-value does not prove the null hypothesis. It says the observed result is not especially unusual under the null model, and many nearby alternatives may also produce unsurprising results. That is why the correct decision language is “fail to reject $$H_0$$,” not “accept $$H_0$$.”

## Significance and effect size

Hold the observed difference from the null fixed while increasing the sample size. The standard error decreases, the same numerical difference then sits farther into the tail of the null distribution, and the p-value becomes smaller. So a very large study can detect a difference that is statistically significant but practically unimportant, and a p-value should therefore be interpreted alongside the size of the observed effect and the study design.

## A complete conclusion

Suppose $$p=0.025<\alpha=0.05$$. A complete contextual conclusion is:

> “Because $$p=0.025<0.05$$, we reject $$H_0$$. There is convincing evidence that the true mean score for students at this school is greater than 50.”

The conclusion should contain:

- the comparison between p-value and $$\alpha$$
- the decision
- a statement about the alternative hypothesis
- the population and variable in context

<div class="article-note" markdown="1">
A significance test gives evidence. It does not establish the probability that a hypothesis is true.
</div>
