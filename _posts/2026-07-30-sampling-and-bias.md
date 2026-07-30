---
layout: post
title: "Sampling and bias"
date: 2026-07-30
description: "A bad sampling method does not become good when you enlarge it. Three hundred simulated studies show bias sitting still while the spread around it shrinks, which is the distinction the design unit is built on."
course: "AP Statistics"
read_time: "10 min read"
math: true
kind: foundations
sequence: 3
interactive: true
blurb: "Watch a bad method stay wrong no matter how many people you ask"
---

A biased sampling method does not improve when you ask more people. It gets more precisely wrong: the estimates cluster more tightly around a value that was never the right one. That single sentence is most of the design unit, and it is the one thing a student can carry into every question about how data were collected.

The framework puts it exactly this way. Bias is "a systematic error in the sampling procedure that results in a statistic being consistently larger or consistently smaller than the parameter." Consistently. Not sometimes, and not fixably by working harder.

## Three ways to choose thirty students

Below are 400 students at one school. Each is plotted by where on campus they spend their time and by how many hours they slept last night, and the two are related: the students who cluster near the library sleep less. The true mean for all 400 is 7.10 hours, drawn as the vertical line in the lower panels. In real life nobody gets to see it.

<div class="viz" markdown="0">
  <canvas id="sb-cv" width="700" height="392"></canvas>
  <div class="viz-controls">
    <label for="sb-m">Method</label>
    <button type="button" id="sb-conv" class="res-filter is-active" style="font-size:.72rem">Convenience</button>
    <button type="button" id="sb-vol" class="res-filter" style="font-size:.72rem">Voluntary response</button>
    <button type="button" id="sb-srs" class="res-filter" style="font-size:.72rem">Simple random sample</button>
  </div>
  <div class="viz-controls">
    <label for="sb-n">Sample size</label>
    <input type="range" id="sb-n" min="5" max="60" step="1" value="30">
    <button type="button" id="sb-one" class="res-filter" style="font-size:.72rem">Draw one sample</button>
    <button type="button" id="sb-many" class="res-filter" style="font-size:.72rem">Run 300 of each</button>
    <button type="button" id="sb-clr" class="res-filter" style="font-size:.72rem">Clear</button>
    <span class="viz-value" id="sb-read" style="min-width:100%"></span>
  </div>
  <p class="viz-caption">Top: the whole population, plotted by campus position and hours of sleep. Choosing a method and drawing one sample inks the students it selected, and the shape of the ink is the argument. Convenience takes a vertical slice near the surveyor. Voluntary response takes a horizontal band along the bottom, because the students sleeping least are the ones with something to say. A simple random sample scatters. Bottom: three hundred studies by each method, with the true mean marked. Raise the sample size and watch every distribution narrow while two of them stay exactly as far from the line as they were.</p>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('sb-cv'), c = cv.getContext('2d');
  var read = document.getElementById('sb-read'), slN = document.getElementById('sb-n');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);

  var INK='#1f1f1f', MUTED='#5c5c5c', LINE='#e6e6e6', FAINT='#9a9a97', PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';

  // Seeded so the population is identical for every reader.
  function mulberry32(a){ return function(){
    a |= 0; a = a + 0x6D2B79F5 | 0;
    var t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };}
  var POP = (function(){
    var r = mulberry32(20260730), P = [];
    for(var i = 0; i < 400; i++){
      var x = r(), y = r(), u = 1 - r(), v = r();
      var z = Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);
      P.push({ x:x, y:y, v: 6.2 + 1.8*x + 0.45*z });
    }
    return P;
  })();
  var MU = (function(){ var s=0; for(var i=0;i<POP.length;i++) s+=POP[i].v; return s/POP.length; })();
  var rnd = mulberry32(99);

  function weighted(n, wf){
    var w = POP.map(wf), pool = [], out = [], tot = 0, i;
    for(i=0;i<POP.length;i++){ pool.push(i); tot += w[i]; }
    for(var k=0;k<n;k++){
      var t = rnd()*tot, acc = 0, pick = pool.length-1;
      for(i=0;i<pool.length;i++){ acc += w[pool[i]]; if(acc >= t){ pick = i; break; } }
      tot -= w[pool[pick]]; out.push(pool[pick]); pool.splice(pick,1);
    }
    return out;
  }
  var METHODS = {
    conv: { name:'Convenience',
      pick:function(n){ return weighted(n, function(p){ return Math.exp(-3.2*p.x); }); } },
    vol:  { name:'Voluntary response',
      pick:function(n){ return weighted(n, function(p){ return Math.exp(-1.7*(p.v-6.2)); }); } },
    srs:  { name:'Simple random sample',
      pick:function(n){ return weighted(n, function(){ return 1; }); } }
  };
  var ORDER = ['conv','vol','srs'];
  var method = 'conv', chosen = [], hist = { conv:[], vol:[], srs:[] };

  var PADL=44, PADR=18, TOPT=16, TOPB=176;          // scatter panel
  var HT=60, HGAP=8, HIST0=206;                      // three histogram rows
  var XLO=5.2, XHI=9.0;                              // sleep axis for the scatter
  var HLO=6.0, HHI=7.7;                              // sampling-distribution axis
  function sx(x){ return PADL + x*(W-PADL-PADR); }
  function sy(v){ return TOPB - (v-XLO)/(XHI-XLO)*(TOPB-TOPT); }
  function hx(v){ return PADL + (v-HLO)/(HHI-HLO)*(W-PADL-PADR); }

  function drawScatter(){
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,TOPB+0.5); c.lineTo(W-PADR,TOPB+0.5); c.stroke();
    c.beginPath(); c.moveTo(PADL+0.5,TOPT); c.lineTo(PADL+0.5,TOPB); c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='right';
    for(var v=6;v<=8;v+=1){ c.fillText(String(v), PADL-6, sy(v)+3);
      c.strokeStyle='#f2f2f2'; c.beginPath(); c.moveTo(PADL,sy(v)); c.lineTo(W-PADR,sy(v)); c.stroke(); }
    c.save(); c.translate(11, (TOPT+TOPB)/2); c.rotate(-Math.PI/2);
    c.textAlign='center'; c.fillStyle=FAINT; c.font='700 10px '+FONT;
    c.fillText('hours of sleep', 0, 0); c.restore();
    c.textAlign='left'; c.fillStyle=FAINT;
    c.fillText('surveyor stands here', PADL+3, TOPB+13);
    c.textAlign='right'; c.fillText('far side of campus', W-PADR, TOPB+13);
    var sel = {}; for(var i=0;i<chosen.length;i++) sel[chosen[i]]=1;
    for(i=0;i<POP.length;i++){
      var p=POP[i], on=sel[i];
      c.fillStyle = on ? INK : PALE;
      c.beginPath(); c.arc(sx(p.x), sy(p.v), on?3.1:2, 0, 7); c.fill();
    }
  }

  function drawHists(){
    var bins=68, i, k;
    for(k=0;k<3;k++){
      var key=ORDER[k], top=HIST0+k*(HT+HGAP), bot=top+HT, data=hist[key];
      c.strokeStyle=LINE; c.lineWidth=1;
      c.beginPath(); c.moveTo(PADL,bot+0.5); c.lineTo(W-PADR,bot+0.5); c.stroke();
      c.fillStyle = key===method ? INK : MUTED;
      c.font='700 10px '+FONT; c.textAlign='left';
      c.fillText(METHODS[key].name.toUpperCase(), PADL, top+9);
      if(data.length){
        var col=new Array(bins), tallest=0;
        for(i=0;i<bins;i++) col[i]=0;
        for(i=0;i<data.length;i++){
          var b=Math.floor((data[i]-HLO)/(HHI-HLO)*bins);
          if(b>=0&&b<bins){ col[b]++; if(col[b]>tallest) tallest=col[b]; }
        }
        var bw=(W-PADL-PADR)/bins;
        for(i=0;i<bins;i++){
          if(!col[i]) continue;
          var h=col[i]/tallest*(HT-14);
          c.fillStyle = key===method ? INK : PALE;
          c.fillRect(PADL+i*bw, bot-h, Math.max(1,bw-0.6), h);
        }
        var m=0; for(i=0;i<data.length;i++) m+=data[i]; m/=data.length;
        c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='right';
        c.fillText('centre '+m.toFixed(3), W-PADR, top+9);
      }
      // the truth, through every row
      c.strokeStyle=INK; c.lineWidth=1.5; c.setLineDash([4,3]);
      c.beginPath(); c.moveTo(hx(MU),top); c.lineTo(hx(MU),bot); c.stroke(); c.setLineDash([]);
    }
    var last=HIST0+2*(HT+HGAP)+HT;
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    for(var t=6.0;t<=7.7;t+=0.5) c.fillText(t.toFixed(1), hx(t), last+14);
    c.fillStyle=INK; c.textAlign='left';
    c.fillText('true mean '+MU.toFixed(2), hx(MU)+5, HIST0-4);
  }

  function draw(){
    c.clearRect(0,0,W,H);
    drawScatter(); drawHists();
    var n=+slN.value, txt='n = '+n+'.  ';
    if(chosen.length){
      var s=0; for(var i=0;i<chosen.length;i++) s+=POP[chosen[i]].v;
      var est=s/chosen.length;
      txt += METHODS[method].name+' estimate '+est.toFixed(3)+
             ',  true mean '+MU.toFixed(3)+',  off by '+(est-MU>=0?'+':'')+(est-MU).toFixed(3)+'.';
    } else txt += 'Draw a sample, or run 300 of each.';
    read.textContent = txt;
  }

  function one(){ chosen = METHODS[method].pick(+slN.value); draw(); }
  function many(){
    var n=+slN.value;
    for(var k=0;k<3;k++){
      var key=ORDER[k];
      for(var t=0;t<300;t++){
        var idx=METHODS[key].pick(n), s=0;
        for(var i=0;i<idx.length;i++) s+=POP[idx[i]].v;
        hist[key].push(s/idx.length);
      }
      if(hist[key].length>6000) hist[key]=hist[key].slice(hist[key].length-6000);
    }
    draw();
  }
  function setMethod(m){
    method=m;
    document.getElementById('sb-conv').classList[m==='conv'?'add':'remove']('is-active');
    document.getElementById('sb-vol').classList[m==='vol'?'add':'remove']('is-active');
    document.getElementById('sb-srs').classList[m==='srs'?'add':'remove']('is-active');
    one();
  }
  document.getElementById('sb-conv').addEventListener('click', function(){ setMethod('conv'); });
  document.getElementById('sb-vol').addEventListener('click', function(){ setMethod('vol'); });
  document.getElementById('sb-srs').addEventListener('click', function(){ setMethod('srs'); });
  document.getElementById('sb-one').addEventListener('click', one);
  document.getElementById('sb-many').addEventListener('click', many);
  document.getElementById('sb-clr').addEventListener('click', function(){
    hist={conv:[],vol:[],srs:[]}; chosen=[]; draw();
  });
  slN.addEventListener('input', function(){ hist={conv:[],vol:[],srs:[]}; one(); });

  one(); many();
})();
</script>

Run 300 of each and the three rows separate immediately. The simple random sample sits on the line. The other two sit to its left, because both of them systematically over-recruit students who sleep less: convenience because those students are the ones standing nearby, voluntary response because those are the students who feel strongly enough to answer.

Now drag the sample size from 5 to 60 and watch what changes. All three distributions narrow, by about three-quarters. Not one of the three moves sideways. At $$n = 10$$ the convenience method centres near 6.68 and the voluntary method near 6.40; at $$n = 60$$ they centre near 6.71 and 6.49, still short of 7.10 by about four-tenths and six-tenths of an hour. The simple random sample centres on 7.10 at both.

## Bias is about centre, variability about spread

Those are two different failures with two different remedies, and the interactive separates them cleanly.

Variability is the spread of the estimates around wherever they centre. It is a nuisance rather than an error, and a bigger sample fixes it, which is why the spread shrank when you raised $$n$$.

Bias is the distance from that centre to the truth. No sample size touches it. The only repair is a different sampling method, because the fault is in how individuals were chosen and not in how many.

A student who has these straight can answer the standard exam question — *will increasing the sample size correct this problem?* — without hesitating. For variability, yes. For bias, never.

## The vocabulary, and the four methods

The *population* is every individual you want to describe; the *sampling frame* is the list you actually draw from, and the gap between them is where undercoverage lives. The *sample* is who you reach. A *parameter* describes the population and a *statistic* describes the sample, a distinction developed in [writing parameters in AP Statistics](/2026/07/14/writing-parameters-in-ap-statistics.html).

Four random methods are named in the course, and the framework defines each by its mechanism:

- **Simple random sample.** Every sample of size $$n$$ has the same chance of being selected.
- **Stratified.** Split the population into non-overlapping strata that are internally similar, take a simple random sample within each, and combine. Because each stratum is homogeneous, the estimate carries less variability than a simple random sample of the same size.
- **Cluster.** Split into clusters, each ideally mirroring the whole population, take a simple random sample of clusters, and use everyone inside the chosen ones. Its advantage is logistical rather than statistical.
- **Systematic.** A random start, then every $$k$$th individual.

Strata are built to be similar inside and different from each other; clusters are meant to be miniature copies of the population. That is the whole distinction, and it is what makes stratified sampling reduce variability while cluster sampling mostly saves effort.

## The named biases

The framework names four, and each has a different point of failure. *Undercoverage* happens when the method leaves part of the population out or makes it less likely to be chosen. *Nonresponse* happens when people selected for the sample do not answer, and the ones who did answer differ from the ones who did not. *Response bias* is when the answers themselves lean one direction, from confusing or leading questions — *question wording bias* — or from self-reporting. *Voluntary response bias* is what happens when the sample consists entirely of volunteers, the second row of the interactive.

They are worth telling apart because the exam asks which one a described study suffers from, not whether bias exists.

## What each kind of randomness buys

Two different randomisations do two different jobs, and mixing them up is the most common way to lose a conclusion question.

Random *selection* is how individuals get into the study. It is what licenses generalising to the population. Random *assignment* is how selected individuals get sorted into treatment groups. It is what licenses a cause-and-effect claim, because it makes the groups alike in every extraneous variable.

The four combinations give four different sentences:

| | Random assignment | No random assignment |
|---|---|---|
| Random selection | Cause and effect, generalisable to the population | Association only, generalisable to the population |
| No random selection | Cause and effect, but only for individuals like those studied | Association only, and only for individuals like those studied |

An observational study is one where treatments are not imposed; the researcher records what is already there. That is why it cannot establish causation on its own: a confounding variable, associated with both the explanatory and the response variable, offers a rival explanation that the design has not ruled out. The reversal in [Simpson's paradox](/2026/07/27/simpsons-paradox.html) is that rival explanation doing its work in public.

<div class="article-note" markdown="1">
A diagnostic worth running: set the sample size to 60, clear, and run 300 of each. The convenience and voluntary distributions are now narrow enough that they barely overlap the truth at all, and a student reporting one of those estimates would quote a small margin of error alongside it. Precision and accuracy have come apart completely. The interval would be tight, confident, and centred on the wrong number, which is the practical reason the design unit comes before the inference units rather than after them.
</div>
