---
layout: post
title: "A distribution explorer"
date: 2026-07-30
description: "Enter a distribution and a region, then compare the probability, cutoff, graph, and TI-84 command in one place."
course: "AP Statistics"
read_time: "5 min read"
math: true
kind: mechanics
sequence: 9
interactive: true
blurb: "Enter a distribution and a region, then compare the probability, cutoff, graph, and TI-84 command in one place"
image: "/assets/og/distribution-explorer.png"
---

Probability questions become easier to organize when the distribution, the region, and the calculator command are kept together. The tool below covers the main distributions used in AP Statistics.

<div class="viz de-wrap" markdown="0">
  <div class="de-row de-dists" role="group" aria-label="Distribution">
    <button type="button" class="res-filter de-d is-active" data-d="binom">Binomial</button>
    <button type="button" class="res-filter de-d" data-d="norm">Normal</button>
    <button type="button" class="res-filter de-d" data-d="t">t</button>
    <button type="button" class="res-filter de-d" data-d="chi2">&chi;&sup2;</button>
    <button type="button" class="res-filter de-d" data-d="phat">Sample proportion</button>
    <button type="button" class="res-filter de-d" data-d="xbar">Sample mean</button>
  </div>

  <div class="de-row de-params" id="de-params"></div>

  <canvas id="de-cv" width="700" height="300"></canvas>

  <div class="de-readout">
    <div class="de-big" id="de-big">&mdash;</div>
    <div class="de-expr" id="de-expr"></div>
  </div>

  <div class="de-row" role="group" aria-label="Direction">
    <button type="button" class="res-filter de-dir is-active" data-dir="fwd">Region &rarr; probability</button>
    <button type="button" class="res-filter de-dir" data-dir="inv">Probability &rarr; cutoff</button>
  </div>

  <div class="de-row de-modes" id="de-modes" role="group" aria-label="Region"></div>
  <div class="de-row de-bounds" id="de-bounds"></div>

  <div class="de-calc">
    <div class="de-calcline" id="de-calc">&mdash;</div>
    <div class="de-menu" id="de-menu"></div>
  </div>

  <div class="de-flags" id="de-flags"></div>

  <div class="de-row">
    <button type="button" class="res-filter" id="de-present">Presentation mode</button>
  </div>

  <p class="viz-caption">Six distributions, typed parameters, four region shapes, and both directions: a region gives a probability, a probability gives a cutoff. The binomial keeps P(X = k) and P(X &le; k) side by side, because those are the two the calculator distinguishes as binompdf and binomcdf and they are the pair most often swapped. The t curve carries the standard normal behind it in outline, so raising the degrees of freedom shows one collapsing onto the other. For the two sampling distributions the center and spread are printed as expressions with the numbers substituted, and a warning appears when a normal-approximation condition fails.</p>

  <style>
    .de-wrap .de-row{display:flex;align-items:center;gap:8px;margin:0 0 .7rem;flex-wrap:wrap}
    .de-wrap .de-row:last-of-type{margin-bottom:0}
    .de-wrap .res-filter{font-size:.72rem}
    .de-wrap label{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
    .de-wrap input[type=number]{font:inherit;font-size:.95rem;font-weight:700;width:6.5em;padding:3px 7px;
      border:1px solid var(--line);border-radius:8px;background:#fff;color:var(--ink)}
    .de-wrap input[type=number]:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
    .de-wrap input[type=range]{flex:0 1 130px;min-width:90px;accent-color:var(--accent)}
    .de-wrap .de-pair{display:flex;align-items:center;gap:6px}
    .de-readout{margin:.9rem 0 1rem;padding-top:.8rem;border-top:1px solid var(--line)}
    .de-big{font-size:2.6rem;font-weight:700;letter-spacing:-.03em;line-height:1.05;color:var(--ink);
      font-variant-numeric:tabular-nums}
    .de-expr{font-size:.9rem;color:var(--muted);margin-top:.25rem;line-height:1.5}
    .de-calc{margin:.9rem 0 .8rem;padding:12px 14px;background:var(--accent-soft);border-radius:12px}
    .de-calcline{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:1rem;font-weight:600;
      color:var(--ink);word-break:break-word}
    .de-menu{font-size:.72rem;color:var(--muted);margin-top:.35rem;letter-spacing:.04em}
    .de-flags{font-size:.86rem;color:var(--ink);line-height:1.5}
    .de-flags:empty{display:none}
    .de-flags p{margin:.5rem 0 0;padding-left:11px;border-left:3px solid var(--accent)}
    .de-wrap.is-present{position:relative;width:100vw;margin-left:calc(50% - 50vw);
      padding:32px clamp(24px,6vw,90px);border-radius:0;border-left:none;border-right:none}
    .de-wrap.is-present .de-params,.de-wrap.is-present .de-dists,
    .de-wrap.is-present .viz-caption,.de-wrap.is-present .de-menu{display:none}
    .de-wrap.is-present .de-big{font-size:clamp(3.4rem,9vw,7rem)}
    .de-wrap.is-present .de-expr{font-size:1.15rem}
    .de-wrap.is-present .de-calcline{font-size:1.35rem}
    .de-wrap.is-present canvas{max-height:none}
    @media (max-width:640px){ .de-big{font-size:2rem} .de-wrap input[type=number]{width:5.2em} }
  </style>
</div>

<script>
(function(){
  'use strict';

  /* ---------- mathematics: no libraries, checked in the article's ledger ---------- */
  var LZ = [0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,
            -176.61502916214059,12.507343278686905,-0.13857109526572012,
            9.9843695780195716e-6,1.5056327351493116e-7];
  function lgamma(x){
    if(x < 0.5) return Math.log(Math.PI/Math.sin(Math.PI*x)) - lgamma(1-x);
    x -= 1; var a = LZ[0], t = x + 7.5;
    for(var i = 1; i < 9; i++) a += LZ[i]/(x+i);
    return 0.5*Math.log(2*Math.PI) + (x+0.5)*Math.log(t) - t + Math.log(a);
  }
  // Hart 1968; absolute error below 3e-16 against published values.
  function normcdf(z){
    var x = Math.abs(z), r;
    if(x > 37) r = 0; else {
      var e = Math.exp(-x*x/2), b, q;
      if(x < 7.07106781186547){
        b = 3.52624965998911e-02*x + 0.700383064443688;
        b = b*x + 6.37396220353165;  b = b*x + 33.912866078383;
        b = b*x + 112.079291497871;  b = b*x + 221.213596169931;
        b = b*x + 220.206867912376;
        q = 8.83883476483184e-02*x + 1.75566716318264;
        q = q*x + 16.064177579207;   q = q*x + 86.7807322029461;
        q = q*x + 296.564248779674;  q = q*x + 637.333633378831;
        q = q*x + 793.826512519948;  q = q*x + 440.413735824752;
        r = e*b/q;
      } else { b = x+0.65; b = x+4/b; b = x+3/b; b = x+2/b; b = x+1/b; r = e/(b*2.506628274631); }
    }
    return z <= 0 ? r : 1 - r;
  }
  function normpdf(z){ return Math.exp(-z*z/2)/Math.sqrt(2*Math.PI); }
  // Acklam rational approximation, then two Newton steps against normcdf.
  function norminv(p){
    if(p <= 0) return -Infinity; if(p >= 1) return Infinity;
    var a=[-3.969683028665376e+01,2.209460984245205e+02,-2.759285104469687e+02,
           1.383577518672690e+02,-3.066479806614716e+01,2.506628277459239e+00],
        b=[-5.447609879822406e+01,1.615858368580409e+02,-1.556989798598866e+02,
           6.680131188771972e+01,-1.328068155288572e+01],
        c=[-7.784894002430293e-03,-3.223964580411365e-01,-2.400758277161838e+00,
           -2.549732539343734e+00,4.374664141464968e+00,2.938163982698783e+00],
        d=[7.784695709041462e-03,3.224671290700398e-01,2.445134137142996e+00,3.754408661907416e+00];
    var pl=0.02425, x, q, r;
    if(p < pl){ q=Math.sqrt(-2*Math.log(p));
      x=(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5])/((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);
    } else if(p <= 1-pl){ q=p-0.5; r=q*q;
      x=(((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q/(((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1);
    } else { q=Math.sqrt(-2*Math.log(1-p));
      x=-(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5])/((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1); }
    for(var i=0;i<2;i++){ var e=normcdf(x)-p, u=normpdf(x); if(u<1e-300) break; x-=e/u; }
    return x;
  }
  function betacf(a,b,x){
    var F=1e-300, qab=a+b, qap=a+1, qam=a-1, c=1, d=1-qab*x/qap;
    if(Math.abs(d)<F) d=F; d=1/d; var h=d;
    for(var m=1;m<=300;m++){
      var m2=2*m, aa=m*(b-m)*x/((qam+m2)*(a+m2));
      d=1+aa*d; if(Math.abs(d)<F) d=F; c=1+aa/c; if(Math.abs(c)<F) c=F; d=1/d; h*=d*c;
      aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
      d=1+aa*d; if(Math.abs(d)<F) d=F; c=1+aa/c; if(Math.abs(c)<F) c=F; d=1/d;
      var de=d*c; h*=de; if(Math.abs(de-1)<3e-16) break;
    }
    return h;
  }
  function ibeta(a,b,x){
    if(x<=0) return 0; if(x>=1) return 1;
    var L=Math.exp(lgamma(a+b)-lgamma(a)-lgamma(b)+a*Math.log(x)+b*Math.log(1-x));
    return x < (a+1)/(a+b+2) ? L*betacf(a,b,x)/a : 1 - L*betacf(b,a,1-x)/b;
  }
  function gammainc(s,x){
    if(x<=0) return 0;
    if(x < s+1){
      var ap=s, sum=1/s, del=sum;
      for(var i=0;i<500;i++){ ap+=1; del*=x/ap; sum+=del;
        if(Math.abs(del) < Math.abs(sum)*3e-16) break; }
      return sum*Math.exp(-x + s*Math.log(x) - lgamma(s));
    }
    var F=1e-300, b=x+1-s, c=1/F, d=1/b, h=d;
    for(var j=1;j<=500;j++){
      var an=-j*(j-s); b+=2; d=an*d+b; if(Math.abs(d)<F) d=F;
      c=b+an/c; if(Math.abs(c)<F) c=F; d=1/d;
      var dl=d*c; h*=dl; if(Math.abs(dl-1)<3e-16) break;
    }
    return 1 - Math.exp(-x + s*Math.log(x) - lgamma(s))*h;
  }
  function tcdf(t,df){ var h=0.5*ibeta(df/2,0.5,df/(df+t*t)); return t>=0 ? 1-h : h; }
  function tpdf(t,df){
    return Math.exp(lgamma((df+1)/2)-lgamma(df/2))/Math.sqrt(df*Math.PI)*Math.pow(1+t*t/df,-(df+1)/2);
  }
  function tinv(p,df){
    if(p<=0) return -Infinity; if(p>=1) return Infinity;
    var x=norminv(p);
    for(var i=0;i<60;i++){
      var e=tcdf(x,df)-p, u=tpdf(x,df); if(u<1e-300) break;
      var s=e/u; if(s>2) s=2; if(s<-2) s=-2; x-=s;
      if(Math.abs(s)<1e-13) break;
    }
    return x;
  }
  function chi2cdf(x,df){ return x<=0 ? 0 : gammainc(df/2,x/2); }
  function chi2pdf(x,df){
    if(x<=0) return 0;
    return Math.exp((df/2-1)*Math.log(x) - x/2 - lgamma(df/2) - (df/2)*Math.LN2);
  }
  function chi2inv(p,df){
    if(p<=0) return 0; if(p>=1) return Infinity;
    var x=df*Math.pow(1-2/(9*df)+norminv(p)*Math.sqrt(2/(9*df)),3);
    if(!(x>0)||!isFinite(x)) x=df;
    for(var i=0;i<80;i++){
      var e=chi2cdf(x,df)-p, u=chi2pdf(x,df); if(u<1e-300) break;
      var s=e/u; if(s>x/2) s=x/2; if(s<-x) s=-x; x-=s;
      if(Math.abs(s)<1e-12*Math.max(1,x)) break;
    }
    return x;
  }
  function binompdf(n,p,k){
    if(k<0||k>n||k!==Math.round(k)) return 0;
    if(p===0) return k===0?1:0;
    if(p===1) return k===n?1:0;
    return Math.exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)+k*Math.log(p)+(n-k)*Math.log1p(-p));
  }
  function binomcdf(n,p,k){
    if(k<0) return 0; if(k>=n) return 1;
    var s=0; for(var i=0;i<=Math.floor(k);i++) s+=binompdf(n,p,i);
    return Math.min(1,s);
  }

  /* ---------- distribution registry ---------- */
  var S = { d:'binom', dir:'fwd', mode:'le', a:5, b:8, area:0.95, present:false,
            P:{ n:20, p:0.5, mu:0, sigma:1, df:10, pn:100, pp:0.5, xn:25, xmu:50, xsig:10 } };

  var DEFS = {
    binom: { name:'Binomial', disc:true,
      fields:[['n','n',1,200,1],['p','p',0,1,0.01]],
      get:function(){ return { n:S.P.n, p:S.P.p }; },
      mean:function(q){ return q.n*q.p; }, sd:function(q){ return Math.sqrt(q.n*q.p*(1-q.p)); },
      pmf:function(x,q){ return binompdf(q.n,q.p,x); },
      cdf:function(x,q){ return binomcdf(q.n,q.p,x); } },
    norm: { name:'Normal', disc:false,
      fields:[['mu','μ',-1e6,1e6,0.1],['sigma','σ',1e-6,1e6,0.1]],
      get:function(){ return { m:S.P.mu, s:S.P.sigma }; },
      mean:function(q){ return q.m; }, sd:function(q){ return q.s; },
      pdf:function(x,q){ return normpdf((x-q.m)/q.s)/q.s; },
      cdf:function(x,q){ return normcdf((x-q.m)/q.s); },
      inv:function(p,q){ return q.m + q.s*norminv(p); } },
    t: { name:'Student’s t', disc:false,
      fields:[['df','df',1,300,1]],
      get:function(){ return { df:S.P.df }; },
      mean:function(){ return 0; },
      sd:function(q){ return q.df>2 ? Math.sqrt(q.df/(q.df-2)) : 2.5; },
      pdf:function(x,q){ return tpdf(x,q.df); },
      cdf:function(x,q){ return tcdf(x,q.df); },
      inv:function(p,q){ return tinv(p,q.df); } },
    chi2: { name:'χ²', disc:false, pos:true,
      fields:[['df','df',1,300,1]],
      get:function(){ return { df:S.P.df }; },
      mean:function(q){ return q.df; }, sd:function(q){ return Math.sqrt(2*q.df); },
      pdf:function(x,q){ return chi2pdf(x,q.df); },
      cdf:function(x,q){ return chi2cdf(x,q.df); },
      inv:function(p,q){ return chi2inv(p,q.df); } },
    phat: { name:'Sample proportion', disc:false,
      fields:[['pp','p',0,1,0.01],['pn','n',1,5000,1]],
      get:function(){ var p=S.P.pp,n=S.P.pn; return { m:p, s:Math.sqrt(p*(1-p)/n), p:p, n:n }; },
      mean:function(q){ return q.m; }, sd:function(q){ return q.s; },
      // At p = 0 or p = 1 the sampling distribution is a point mass, so there is
      // no density to draw. Returning zero keeps the axes finite and leaves the
      // large-counts warning to explain why no curve is there.
      pdf:function(x,q){ return q.s>0 ? normpdf((x-q.m)/q.s)/q.s : 0; },
      cdf:function(x,q){ return q.s>0 ? normcdf((x-q.m)/q.s) : (x<q.m?0:1); },
      inv:function(p,q){ return q.s>0 ? q.m + q.s*norminv(p) : q.m; } },
    xbar: { name:'Sample mean', disc:false,
      fields:[['xmu','μ',-1e6,1e6,0.1],['xsig','σ',1e-6,1e6,0.1],['xn','n',1,5000,1]],
      get:function(){ var n=S.P.xn; return { m:S.P.xmu, s:S.P.xsig/Math.sqrt(n), sig:S.P.xsig, n:n }; },
      mean:function(q){ return q.m; }, sd:function(q){ return q.s; },
      pdf:function(x,q){ return normpdf((x-q.m)/q.s)/q.s; },
      cdf:function(x,q){ return normcdf((x-q.m)/q.s); },
      inv:function(p,q){ return q.m + q.s*norminv(p); } }
  };

  var MODES = [['lt','Left of a'],['gt','Right of a'],['bt','Between a and b'],['out','Outside a and b']];
  var IMODES = [['ileft','Left area → cutoff'],['iright','Right area → cutoff'],
                ['icent','Central area → two cutoffs']];

  var $ = function(id){ return document.getElementById(id); };
  var cv = $('de-cv'), ctx = cv.getContext('2d');
  var W = cv.width, H = cv.height, DPR = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*DPR; cv.height = H*DPR; ctx.setTransform(DPR,0,0,DPR,0,0);
  var INK='#1f1f1f', MUTED='#5c5c5c', LINE='#e6e6e6', FAINT='#9a9a97',
      PALE='#d6d6d3', SHADE='rgba(31,31,31,0.16)';
  var FONT='Hanken Grotesk, sans-serif';
  var PADL=42, PADR=20, TOP=14, AXIS=H-34;

  function def(){ return DEFS[S.d]; }
  function nf(v,dp){ return (Math.round(v*Math.pow(10,dp))/Math.pow(10,dp)).toFixed(dp); }
  function fmtP(v){
    if(!isFinite(v)) return '—';
    if(v > 0 && v < 0.0001) return v.toExponential(3);
    return v.toFixed(4);
  }
  function range(){
    var D=def(), q=D.get(), m=D.mean(q), s=D.sd(q);
    // A binomial at p = 0 or p = 1, and a sample proportion at either end, have
    // zero spread. Without this the window collapses to a single point, every
    // horizontal coordinate becomes 0/0, and the whole figure disappears.
    if(!isFinite(s) || s<=0) s = D.disc ? 1 : Math.max(Math.abs(m), 1)/8;
    if(S.d==='binom') return [Math.max(-0.5,m-4.5*s), Math.min(q.n+0.5, m+4.5*s)];
    if(D.pos) return [0, m+4.5*s];
    return [m-4*s, m+4*s];
  }

  /* ---------- controls ---------- */
  function paramRow(){
    var D=def(), html='';
    D.fields.forEach(function(f){
      var key=f[0], lab=f[1], lo=f[2], hi=f[3], st=f[4];
      html += '<span class="de-pair"><label for="de-f-'+key+'">'+lab+'</label>'+
        '<input type="number" id="de-f-'+key+'" value="'+S.P[key]+'" min="'+lo+'" max="'+hi+'" step="'+st+'">'+
        '<input type="range" id="de-r-'+key+'" value="'+S.P[key]+'" min="'+lo+'" max="'+hi+'" step="'+st+
        '" aria-label="'+lab+' slider"></span>';
    });
    $('de-params').innerHTML = html;
    D.fields.forEach(function(f){
      var key=f[0], num=$('de-f-'+key), rng=$('de-r-'+key);
      function set(v){ S.P[key]=v; num.value=v; rng.value=v; resetBounds(); draw(); }
      num.addEventListener('input', function(){ var v=parseFloat(num.value); if(isFinite(v)){ S.P[key]=v; rng.value=v; resetBounds(); draw(); } });
      rng.addEventListener('input', function(){ set(parseFloat(rng.value)); });
    });
  }
  function modeRow(){
    var list = S.dir==='fwd' ? MODES : IMODES, html='';
    if(S.dir==='inv' && ['ileft','iright','icent'].indexOf(S.mode)<0) S.mode='ileft';
    if(S.dir==='fwd' && ['lt','gt','bt','out'].indexOf(S.mode)<0) S.mode='le';
    if(S.dir==='fwd' && S.mode==='le') S.mode='lt';
    list.forEach(function(m){
      html += '<button type="button" class="res-filter de-m'+(S.mode===m[0]?' is-active':'')+
              '" data-m="'+m[0]+'">'+m[1]+'</button>';
    });
    $('de-modes').innerHTML = html;
    Array.prototype.forEach.call(document.querySelectorAll('.de-m'), function(btn){
      btn.addEventListener('click', function(){ S.mode=btn.getAttribute('data-m'); modeRow(); boundsRow(); draw(); });
    });
  }
  function boundsRow(){
    var html='';
    if(S.dir==='fwd'){
      var two = (S.mode==='bt'||S.mode==='out');
      html += '<span class="de-pair"><label for="de-a">'+(two?'a':'value')+'</label>'+
              '<input type="number" id="de-a" value="'+S.a+'" step="any"></span>';
      if(two) html += '<span class="de-pair"><label for="de-b">b</label>'+
              '<input type="number" id="de-b" value="'+S.b+'" step="any"></span>';
    } else {
      html += '<span class="de-pair"><label for="de-area">area</label>'+
              '<input type="number" id="de-area" value="'+S.area+'" min="0" max="1" step="0.001"></span>';
    }
    $('de-bounds').innerHTML = html;
    if($('de-a')) $('de-a').addEventListener('input', function(){ var v=parseFloat(this.value); if(isFinite(v)){ S.a=v; draw(); } });
    if($('de-b')) $('de-b').addEventListener('input', function(){ var v=parseFloat(this.value); if(isFinite(v)){ S.b=v; draw(); } });
    if($('de-area')) $('de-area').addEventListener('input', function(){ var v=parseFloat(this.value); if(isFinite(v)&&v>0&&v<1){ S.area=v; draw(); } });
  }
  function resetBounds(){
    var D=def(), q=D.get(), m=D.mean(q), s=D.sd(q);
    if(S.d==='binom'){ S.a=Math.round(m); S.b=Math.round(m+s); }
    else { S.a=+nf(m,4); S.b=+nf(m+s,4); }
  }

  /* ---------- computation ---------- */
  function compute(){
    var D=def(), q=D.get(), out={ };
    if(S.dir==='fwd'){
      if(D.disc){
        var k=Math.round(S.a), k2=Math.round(S.b);
        if(S.mode==='lt') out.p=D.cdf(k,q);
        else if(S.mode==='gt') out.p=1-D.cdf(k-1,q);
        else if(S.mode==='bt') out.p=D.cdf(k2,q)-D.cdf(k-1,q);
        else out.p=1-(D.cdf(k2,q)-D.cdf(k-1,q));
        out.eq=D.pmf(k,q); out.le=D.cdf(k,q);
      } else {
        if(S.mode==='lt') out.p=D.cdf(S.a,q);
        else if(S.mode==='gt') out.p=1-D.cdf(S.a,q);
        else if(S.mode==='bt') out.p=D.cdf(Math.max(S.a,S.b),q)-D.cdf(Math.min(S.a,S.b),q);
        else out.p=1-(D.cdf(Math.max(S.a,S.b),q)-D.cdf(Math.min(S.a,S.b),q));
      }
    } else {
      if(!D.inv){ out.err='The binomial is discrete, so an exact cutoff for a given area generally does not exist. Use the forward direction and step k.'; return out; }
      if(S.mode==='ileft'){ out.cut=D.inv(S.area,q); }
      else if(S.mode==='iright'){ out.cut=D.inv(1-S.area,q); }
      else { out.cutLo=D.inv((1-S.area)/2,q); out.cutHi=D.inv(1-(1-S.area)/2,q); }
    }
    return out;
  }

  /* ---------- the TI-84 line ----------
     Syntax and menu positions verified against the Texas Instruments
     "Reference Guide for the TI-84 Plus CE" (Commands and Functions Listing).  */
  function calcLine(){
    var D=def(), q=D.get(), r=range(), N='-1' + 'ᴇ' + '99', P='1' + 'ᴇ' + '99';
    var LO='ˉ'+'1ᴇ99';   // typographic minus for the calculator's (-)
    function nn(v){ return String(+nf(v,6)); }
    if(S.d==='binom'){
      var k=Math.round(S.a), k2=Math.round(S.b);
      if(S.mode==='lt') return ['binomcdf('+q.n+','+q.p+','+k+')','2nd DISTR → B:binomcdf('];
      if(S.mode==='gt') return ['1 − binomcdf('+q.n+','+q.p+','+(k-1)+')','2nd DISTR → B:binomcdf('];
      if(S.mode==='bt') return ['binomcdf('+q.n+','+q.p+','+k2+') − binomcdf('+q.n+','+q.p+','+(k-1)+')','2nd DISTR → B:binomcdf('];
      return ['1 − (binomcdf('+q.n+','+q.p+','+k2+') − binomcdf('+q.n+','+q.p+','+(k-1)+'))','2nd DISTR → B:binomcdf('];
    }
    if(S.d==='t'){
      if(S.dir==='inv'){
        if(S.mode==='ileft') return ['invT('+S.area+','+q.df+')','2nd DISTR → 4:invT('];
        if(S.mode==='iright') return ['invT('+(1-S.area).toFixed(6).replace(/0+$/,'')+','+q.df+')','2nd DISTR → 4:invT('];
        return ['invT('+((1-S.area)/2).toFixed(6).replace(/0+$/,'')+','+q.df+')  and  invT('+(1-(1-S.area)/2).toFixed(6).replace(/0+$/,'')+','+q.df+')','2nd DISTR → 4:invT('];
      }
      var lo = S.mode==='gt' ? nn(S.a) : (S.mode==='lt' ? LO : nn(Math.min(S.a,S.b)));
      var hi = S.mode==='lt' ? nn(S.a) : (S.mode==='gt' ? '1ᴇ99' : nn(Math.max(S.a,S.b)));
      var body = 'tcdf('+lo+','+hi+','+q.df+')';
      return [S.mode==='out' ? '1 − '+body : body, '2nd DISTR → 6:tcdf('];
    }
    if(S.d==='chi2'){
      if(S.dir==='inv') return ['—  the TI-84 has no inverse χ² command','use χ²cdf and adjust, or a table'];
      var lo2 = S.mode==='gt' ? nn(S.a) : (S.mode==='lt' ? '0' : nn(Math.min(S.a,S.b)));
      var hi2 = S.mode==='lt' ? nn(S.a) : (S.mode==='gt' ? '1ᴇ99' : nn(Math.max(S.a,S.b)));
      var b2 = 'χ²cdf('+lo2+','+hi2+','+q.df+')';
      return [S.mode==='out' ? '1 − '+b2 : b2, '2nd DISTR → 8:χ²cdf('];
    }
    // normal family: normal, sample proportion, sample mean
    var m=nn(D.mean(q)), s=nn(D.sd(q));
    if(S.dir==='inv'){
      if(S.mode==='ileft') return ['invNorm('+S.area+','+m+','+s+')','2nd DISTR → 3:invNorm(  ·  invNorm(area[,μ,σ,tail])'];
      if(S.mode==='iright') return ['invNorm('+(1-S.area).toFixed(6).replace(/0+$/,'')+','+m+','+s+')','2nd DISTR → 3:invNorm(  ·  or invNorm('+S.area+','+m+','+s+',RIGHT)'];
      return ['invNorm('+((1-S.area)/2).toFixed(6).replace(/0+$/,'')+','+m+','+s+')  and  invNorm('+(1-(1-S.area)/2).toFixed(6).replace(/0+$/,'')+','+m+','+s+')','2nd DISTR → 3:invNorm(  ·  or invNorm('+S.area+','+m+','+s+',CENTER)'];
    }
    var lo3 = S.mode==='gt' ? nn(S.a) : (S.mode==='lt' ? LO : nn(Math.min(S.a,S.b)));
    var hi3 = S.mode==='lt' ? nn(S.a) : (S.mode==='gt' ? '1ᴇ99' : nn(Math.max(S.a,S.b)));
    var b3 = 'normalcdf('+lo3+','+hi3+','+m+','+s+')';
    return [S.mode==='out' ? '1 − '+b3 : b3, '2nd DISTR → 2:normalcdf(  ·  normalcdf(lower,upper[,μ,σ])'];
  }

  /* ---------- drawing ---------- */
  function draw(){
    var D=def(), q=D.get(), r=range(), lo=r[0], hi=r[1], out=compute();
    var px=function(x){ return PADL + (x-lo)/(hi-lo)*(W-PADL-PADR); };
    ctx.clearRect(0,0,W,H);

    var peak=0, i, x;
    if(D.disc){ for(i=0;i<=q.n;i++) peak=Math.max(peak, D.pmf(i,q)); }
    else { for(i=0;i<=400;i++){ x=lo+(hi-lo)*i/400; peak=Math.max(peak, D.pdf(x,q)); } }
    if(!(peak>0)) peak=1;
    var py=function(d){ return AXIS - d/peak*(AXIS-TOP-6); };

    function inRegion(x){
      if(S.dir!=='fwd') return false;
      if(D.disc){
        var k=Math.round(x), a=Math.round(S.a), b=Math.round(S.b);
        if(S.mode==='lt') return k<=a;
        if(S.mode==='gt') return k>=a;
        if(S.mode==='bt') return k>=Math.min(a,b)&&k<=Math.max(a,b);
        return k<Math.min(a,b)||k>Math.max(a,b);
      }
      var A=Math.min(S.a,S.b), B=Math.max(S.a,S.b);
      if(S.mode==='lt') return x<=S.a;
      if(S.mode==='gt') return x>=S.a;
      if(S.mode==='bt') return x>=A&&x<=B;
      return x<A||x>B;
    }

    if(D.disc){
      var wBar=(W-PADL-PADR)/(hi-lo)*0.86;
      for(i=Math.max(0,Math.ceil(lo)); i<=Math.min(q.n,Math.floor(hi)); i++){
        var d=D.pmf(i,q), X=px(i), Y=py(d);
        ctx.fillStyle = inRegion(i) ? INK : PALE;
        ctx.fillRect(X-wBar/2, Y, Math.max(1,wBar), AXIS-Y);
      }
    } else {
      // t gets the standard normal behind it, in outline
      if(S.d==='t'){
        ctx.strokeStyle=PALE; ctx.lineWidth=1.5; ctx.setLineDash([4,3]); ctx.beginPath();
        for(i=0;i<=400;i++){ x=lo+(hi-lo)*i/400;
          var yn=normpdf(x); i?ctx.lineTo(px(x),py(yn)):ctx.moveTo(px(x),py(yn)); }
        ctx.stroke(); ctx.setLineDash([]);
      }
      // shaded region
      ctx.fillStyle=SHADE; ctx.beginPath(); var started=false;
      for(i=0;i<=600;i++){
        x=lo+(hi-lo)*i/600;
        if(inRegion(x)){
          if(!started){ ctx.moveTo(px(x),AXIS); started=true; }
          ctx.lineTo(px(x),py(D.pdf(x,q)));
        } else if(started){ ctx.lineTo(px(lo+(hi-lo)*(i-1)/600),AXIS); ctx.closePath(); ctx.fill();
          ctx.beginPath(); started=false; }
      }
      if(started){ ctx.lineTo(px(hi),AXIS); ctx.closePath(); ctx.fill(); }
      // curve
      ctx.strokeStyle=INK; ctx.lineWidth=2; ctx.beginPath();
      for(i=0;i<=600;i++){ x=lo+(hi-lo)*i/600; var y=D.pdf(x,q);
        i?ctx.lineTo(px(x),py(y)):ctx.moveTo(px(x),py(y)); }
      ctx.stroke();
    }

    // cutoff markers in inverse mode
    function marker(v,label){
      if(!isFinite(v)) return;
      var X=px(v);
      ctx.strokeStyle=INK; ctx.lineWidth=2; ctx.beginPath();
      ctx.moveTo(X,TOP); ctx.lineTo(X,AXIS); ctx.stroke();
      ctx.fillStyle=INK; ctx.font='700 12px '+FONT;
      ctx.textAlign = X > W-90 ? 'right' : 'left';
      ctx.fillText(label, X + (X>W-90?-6:6), TOP+11);
    }
    if(S.dir==='inv'){
      if(out.cut!==undefined) marker(out.cut, nf(out.cut,4));
      if(out.cutLo!==undefined){ marker(out.cutLo, nf(out.cutLo,4)); marker(out.cutHi, nf(out.cutHi,4)); }
    } else if(!D.disc){
      marker(S.a, 'a = '+nf(S.a,4));
      if(S.mode==='bt'||S.mode==='out') marker(S.b, 'b = '+nf(S.b,4));
    }

    // axis
    ctx.strokeStyle=LINE; ctx.lineWidth=1;
    ctx.beginPath(); ctx.moveTo(PADL,AXIS+0.5); ctx.lineTo(W-PADR,AXIS+0.5); ctx.stroke();
    ctx.fillStyle=MUTED; ctx.font='700 11px '+FONT; ctx.textAlign='center';
    for(i=0;i<=6;i++){
      var tv=lo+(hi-lo)*i/6, TX=px(tv);
      ctx.beginPath(); ctx.moveTo(TX,AXIS); ctx.lineTo(TX,AXIS+4); ctx.stroke();
      ctx.fillText(nf(tv, Math.abs(hi-lo)>20?0:(Math.abs(hi-lo)>2?2:4)), TX, AXIS+17);
    }
    render(out, q, D);
  }

  function render(out,q,D){
    var big=$('de-big'), expr=$('de-expr'), flags=$('de-flags');
    if(out.err){ big.textContent='—'; expr.textContent=out.err; }
    else if(S.dir==='fwd'){
      big.textContent=fmtP(out.p);
      var words = { lt: D.disc?('P(X ≤ '+Math.round(S.a)+')'):('P(X ≤ '+nf(S.a,4)+')'),
                    gt: D.disc?('P(X ≥ '+Math.round(S.a)+')'):('P(X ≥ '+nf(S.a,4)+')'),
                    bt: 'P('+nf(Math.min(S.a,S.b),4)+' ≤ X ≤ '+nf(Math.max(S.a,S.b),4)+')',
                    out:'P(X < '+nf(Math.min(S.a,S.b),4)+' or X > '+nf(Math.max(S.a,S.b),4)+')' }[S.mode];
      expr.textContent = words + '  =  ' + fmtP(out.p);
    } else {
      if(out.cut!==undefined){
        big.textContent=nf(out.cut,4);
        expr.textContent=(S.mode==='ileft'?'the value with area '+S.area+' to its left'
                                           :'the value with area '+S.area+' to its right');
      } else {
        big.textContent=nf(out.cutLo,4)+'  and  '+nf(out.cutHi,4);
        expr.textContent='the two values with central area '+S.area+' between them';
      }
    }
    // binomial keeps both forms on screen, permanently
    if(D.disc && S.dir==='fwd'){
      var k=Math.round(S.a);
      expr.innerHTML = expr.textContent +
        '<br><strong>P(X = '+k+') = '+fmtP(out.eq)+'</strong> &nbsp;(binompdf) &nbsp;&middot;&nbsp; ' +
        '<strong>P(X ≤ '+k+') = '+fmtP(out.le)+'</strong> &nbsp;(binomcdf)';
    }
    var cl=calcLine();
    $('de-calc').textContent=cl[0];
    $('de-menu').textContent=cl[1];

    // sampling-distribution expressions and condition flags
    var f='';
    if(S.d==='phat'){
      f += '<p>center '+nf(q.m,4)+' = p &nbsp;&middot;&nbsp; spread &radic;(p(1−p)/n) = &radic;('+
           nf(q.p,4)+'·'+nf(1-q.p,4)+'/'+q.n+') = '+nf(q.s,5)+'</p>';
      var np=q.n*q.p, nq=q.n*(1-q.p);
      if(np<10||nq<10) f += '<p>Large counts fails: np = '+nf(np,2)+', n(1−p) = '+nf(nq,2)+
        '. Both must be at least 10 before this normal curve is a fair stand-in for the true (binomial) sampling distribution.</p>';
    }
    if(S.d==='xbar'){
      f += '<p>center '+nf(q.m,4)+' = μ &nbsp;&middot;&nbsp; spread σ/&radic;n = '+nf(q.sig,4)+'/&radic;'+q.n+' = '+nf(q.s,5)+'</p>';
      if(q.n<30) f += '<p>n = '+q.n+' is below 30. If the population is normal this curve is exact; if it is not, the Central Limit Theorem has not yet earned you the normal shape.</p>';
    }
    flags.innerHTML=f;
  }

  /* ---------- wiring ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.de-d'), function(b){
    b.addEventListener('click', function(){
      S.d=b.getAttribute('data-d');
      Array.prototype.forEach.call(document.querySelectorAll('.de-d'), function(o){
        o.classList[o===b?'add':'remove']('is-active'); });
      paramRow(); resetBounds(); modeRow(); boundsRow(); draw();
    });
  });
  Array.prototype.forEach.call(document.querySelectorAll('.de-dir'), function(b){
    b.addEventListener('click', function(){
      S.dir=b.getAttribute('data-dir');
      Array.prototype.forEach.call(document.querySelectorAll('.de-dir'), function(o){
        o.classList[o===b?'add':'remove']('is-active'); });
      modeRow(); boundsRow(); draw();
    });
  });
  $('de-present').addEventListener('click', function(){
    S.present=!S.present;
    document.querySelector('.de-wrap').classList[S.present?'add':'remove']('is-present');
    this.textContent = S.present ? 'Exit presentation mode' : 'Presentation mode';
  });

  // dragging a bound on the plot
  var dragging=null;
  function xAt(ev){
    var rct=cv.getBoundingClientRect(), r=range();
    var cx=((ev.touches?ev.touches[0].clientX:ev.clientX)-rct.left)/rct.width*W;
    return r[0] + (cx-PADL)/(W-PADL-PADR)*(r[1]-r[0]);
  }
  function grab(ev){
    if(S.dir!=='fwd') return;
    var v=xAt(ev), two=(S.mode==='bt'||S.mode==='out');
    dragging = (two && Math.abs(v-S.b) < Math.abs(v-S.a)) ? 'b' : 'a';
    move(ev);
  }
  function move(ev){
    if(!dragging) return;
    var v=xAt(ev);
    if(def().disc) v=Math.round(v);
    S[dragging]=+nf(v,4);
    var el=$('de-'+dragging); if(el) el.value=S[dragging];
    draw();
  }
  cv.addEventListener('mousedown', grab);
  window.addEventListener('mousemove', move);
  window.addEventListener('mouseup', function(){ dragging=null; });
  cv.addEventListener('touchstart', function(e){ grab(e); e.preventDefault(); });
  cv.addEventListener('touchmove', function(e){ move(e); e.preventDefault(); });
  cv.addEventListener('touchend', function(){ dragging=null; });

  paramRow(); resetBounds(); modeRow(); boundsRow(); draw();
})();
</script>

Enter the parameters from a problem, choose the region, and compare the graph with the corresponding numerical probability or cutoff. The TI-84 command is shown underneath.

## Forward and inverse questions

A forward probability question gives a boundary and asks for area. Examples include:

- $$P(X<70)$$
- $$P(2<T<3)$$
- the probability of at most 6 successes

Calculator commands such as `normalcdf`, `tcdf`, and `binomcdf` work in this direction. An inverse question gives a probability and asks for the boundary. Examples include:

- the 90th percentile
- the critical value leaving 2.5% in the upper tail

Commands such as `invNorm` and `invT` work in the inverse direction. Before choosing a command, ask which of those two quantities the problem supplied.

## Binomial probability

For a binomial random variable, `binompdf` gives $$P(X=k)$$, the probability of exactly $$k$$ successes, and `binomcdf` gives $$P(X\le k)$$. For “at least 6,” use the complement $$P(X\ge6) = 1-P(X\le5)$$. The off-by-one matters, and the complement stops at 5 because 6 belongs in the event we want to keep.

## Normal and $$t$$

For a standard normal variable, $$P(-1.96<Z<1.96) \approx0.95$$. A $$t$$-distribution with small degrees of freedom has heavier tails, so the same fixed interval contains less probability. As the degrees of freedom increase, the $$t$$-distribution approaches the standard normal distribution, which is why $$t$$ critical values are larger when the sample is small.

## Sampling distributions

The sample-proportion and sample-mean modes use normal curves as sampling models. For a sample proportion, $$\mu_{\hat p}=p$$ and $$\sigma_{\hat p} = \sqrt{\tfrac{p(1-p)}{n}}$$, and the usual large-count condition requires expected successes and failures to be sufficiently large.

For a sample mean, $$\mu_{\bar X}=\mu$$ and $$\sigma_{\bar X} = \tfrac{\sigma}{\sqrt n}$$. Normality is exact when the population is normal and approximate for sufficiently large samples under [the Central Limit Theorem](/2026/07/25/central-limit-theorem-watched-live.html).

<div class="article-note" markdown="1">
The warnings in the tool are part of the statistical reasoning. A calculator can evaluate a probability even when the model used to justify that calculation is poor.
</div>
