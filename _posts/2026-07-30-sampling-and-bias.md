---
layout: post
title: "Sampling and bias"
date: 2026-07-30
description: "A larger sample reduces sampling variability. It does not repair a biased sampling method."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 4
interactive: true
blurb: "A larger sample reduces sampling variability. It does not repair a biased sampling method"
image: "/assets/og/sampling-and-bias.png"
---

Increasing a sample size reduces sampling variability. It does not correct systematic bias, and a biased method can therefore become more precise without becoming more accurate.

## Three ways to sample

The population below contains 400 students, and their campus location is associated with their hours of sleep. The population mean is 7.10 hours.

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
        c.fillText('center '+m.toFixed(3), W-PADR, top+9);
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

A convenience sample selects students who are easy to reach. A voluntary response sample overrepresents people who choose to respond, often because they have stronger opinions or experiences. A simple random sample gives every possible sample of the specified size an equal chance of selection.

In the simulation, the simple random samples center around the population mean. The convenience and voluntary-response methods systematically overrepresent students who sleep less, and their sampling distributions center below the truth.

## Bias and variability are different

Bias concerns the center of a sampling distribution, and a method is biased when it systematically overestimates or underestimates the population parameter. Variability concerns the spread of estimates from sample to sample. Increasing $$n$$ reduces that spread, but it does not move the center of a biased sampling distribution toward the truth.

In the simulation, raising the sample size makes all three distributions narrower. Only the random-sampling distribution is centered correctly, and the other two become more tightly concentrated around biased values.

## Population, sample, parameter, statistic

The population is the full group we want to describe, and the sample is the subset actually observed. A [parameter](/2026/07/14/writing-parameters-in-ap-statistics.html) is a numerical characteristic of the population, and a statistic is calculated from the sample. Inference uses statistics to learn about parameters, and the sampling method determines whether that inference can reasonably generalize to the population of interest.

## Four probability sampling methods

## Simple random sample

Every possible sample of size $$n$$ has the same chance of being selected.

## Stratified random sample

Divide the population into nonoverlapping strata and take a random sample within each. Strata are usually chosen so individuals are relatively similar within each group and meaningfully different across groups, and stratification can reduce sampling variability when the grouping variable is informative.

## Cluster sample

Divide the population into clusters, randomly select clusters, and sample everyone or many individuals within the selected clusters. Good clusters resemble small versions of the population, and cluster sampling is often attractive for logistical reasons.

## Systematic sample

Choose a random starting position, then select every $$k$$-th individual. The method still depends on having a sampling frame without a problematic periodic pattern.

## Common sources of bias

Undercoverage occurs when some parts of the population are excluded or systematically less likely to be sampled. Nonresponse occurs when selected individuals do not respond and the respondents differ meaningfully from the nonrespondents. Response bias occurs when recorded answers systematically differ from the truth because of wording, interviewer effects, memory, social desirability, or other features of measurement. Voluntary response bias occurs when participation is self-selected.

These are different mechanisms, and a strong response names the one that matches the design.

## Random selection and random assignment

Random selection and random assignment solve different problems. Random selection supports generalization from the sample to the population, and random assignment supports causal comparison by balancing other variables across treatment groups, apart from chance. The conclusions depend on which forms of randomization were used.

| | Random assignment | No random assignment |
|---|---|---|
| Random selection | Causal conclusion may be supported, with generalization to the sampled population | Association only, with generalization to the sampled population |
| No random selection | Causal conclusion may be supported for individuals like those studied | Association only, with limited generalization |

An observational study does not impose treatments. Without random assignment, [confounding](/2026/07/27/simpsons-paradox.html) remains a possible explanation for an association.

<div class="article-note" markdown="1">
A useful final distinction is precision versus accuracy. A biased estimate can have a very small standard error, and a narrow confidence interval centered on the wrong value is still wrong.
</div>
