---
layout: post
title: "Implicit differentiation"
date: 2026-07-30
description: "Implicit differentiation uses the chain rule to find slopes on relations that are not solved for y."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: mechanics
sequence: 11
interactive: true
blurb: "Implicit differentiation uses the chain rule to find slopes on relations that are not solved for y"
image: "/assets/og/implicit-differentiation.png"
---

A relation such as $$x^2+xy+y^2=7$$ describes a curve even though it is not solved for $$y$$, and we can still find its slope. Implicit differentiation works because $$y$$ is treated as a function of $$x$$, and when a term involving $$y$$ is differentiated with respect to $$x$$, [the chain rule](/2026/07/30/chain-rule-reading-the-layers.html) contributes a factor of $$dy/dx$$.

## The chain rule is the method

Differentiate $$x^2+xy+y^2=7$$ with respect to $$x$$. The first term gives $$2x$$, the product $$xy$$ requires the product rule, $$\tfrac{d}{dx}(xy)=y+x\tfrac{dy}{dx}$$, and the last term requires the chain rule, $$\tfrac{d}{dx}(y^2)=2y\tfrac{dy}{dx}$$.

So $$2x+y+x\tfrac{dy}{dx}+2y\tfrac{dy}{dx}=0$$, and collecting the derivative terms gives

$$\begin{aligned}
\left(x+2y\right)\frac{dy}{dx} &= -(2x+y)\\
\frac{dy}{dx} &= -\frac{2x+y}{x+2y}
\end{aligned}$$

The extra $$dy/dx$$ factors are not a special rule for implicit differentiation. They are ordinary chain-rule factors.

## The slope depends on both coordinates

An explicit derivative such as $$f'(x)=2x$$ depends only on $$x$$, while an implicit derivative can depend on both $$x$$ and $$y$$. That matters because a vertical line may meet an implicit curve at more than one point.

For the relation above, setting $$x=1$$ gives $$y^2+y-6=0$$, so $$y=2$$ or $$y=-3$$. At $$(1,2)$$, $$\tfrac{dy}{dx} = -\tfrac{2+2}{1+4} = -\tfrac45$$, and at $$(1,-3)$$, $$\tfrac{dy}{dx} = -\tfrac{2-3}{1-6} = -\tfrac15$$. The two points have the same $$x$$-coordinate and different tangent slopes, so when an implicit problem asks for a slope, the full point usually matters.

<div class="viz" markdown="0">
  <div class="viz-controls" id="im-curves"></div>
  <canvas id="im-cv" width="700" height="380"></canvas>
  <div class="viz-controls">
    <label for="im-t">Point on the curve</label>
    <input type="range" id="im-t" min="0" max="1000" step="1" value="120">
  </div>
  <div class="im-read" id="im-read"></div>
  <p class="viz-caption">Four relations, none of them solved for y. The point slides along the curve and the line drawn through it is the tangent whose slope the implicit formula predicts. Below, that formula is shown with its numerator and denominator separated, then checked against a slope obtained a completely different way, by parametrizing the curve and dividing dy by dx. The two agree everywhere, including where they both fail: when the denominator reaches zero the tangent is vertical and there is no slope to report, which is a point the course calls critical rather than an accident of the algebra.</p>
  <style>
    .im-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .im-read .im-lab{color:var(--muted);display:inline-block;min-width:12.5rem}
    .im-read .im-flag{color:var(--muted)}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('im-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var SIDE=336, TOPP=22, CX0=(W-SIDE)/2;   // the plot is a centered square

  var A=Math.sqrt(14/3), B=Math.sqrt(14), R2=Math.SQRT2;
  // Each curve: p(s) for s in [0,1] gives the point and a tangent DIRECTION
  // (dx, dy) — direction only, so any positive common factor is harmless.
  // num/den are the implicit dy/dx as a separated fraction.
  var C=[
    { n:'x² + y² = 25', eq:'-x / y', cx:0, cy:0, w:6.2,
      p:function(s){ var t=2*Math.PI*s;
        return {x:5*Math.cos(t), y:5*Math.sin(t), dx:-5*Math.sin(t), dy:5*Math.cos(t)}; },
      num:function(x,y){ return -x; }, den:function(x,y){ return y; } },
    { n:'x²/9 + y²/4 = 1', eq:'-4x / 9y', cx:0, cy:0, w:3.7,
      p:function(s){ var t=2*Math.PI*s;
        return {x:3*Math.cos(t), y:2*Math.sin(t), dx:-3*Math.sin(t), dy:2*Math.cos(t)}; },
      num:function(x,y){ return -4*x; }, den:function(x,y){ return 9*y; } },
    { n:'x² + xy + y² = 7', eq:'-(2x + y) / (x + 2y)', cx:0, cy:0, w:3.8,
      p:function(s){ var t=2*Math.PI*s, u=A*Math.cos(t), v=B*Math.sin(t),
            du=-A*Math.sin(t), dv=B*Math.cos(t);
        return {x:(u-v)/R2, y:(u+v)/R2, dx:(du-dv)/R2, dy:(du+dv)/R2}; },
      num:function(x,y){ return -(2*x+y); }, den:function(x,y){ return x+2*y; } },
    { n:'x³ + y³ = 6xy', eq:'(2y - x²) / (y² - 2x)', cx:1.62, cy:1.62, w:2.35,
      p:function(s){ var T=Math.tan(s*Math.PI/2*0.995), T3=T*T*T;
        return {x:6*T/(1+T3), y:6*T*T/(1+T3), dx:6*(1-2*T3), dy:6*T*(2-T3)}; },
      num:function(x,y){ return 2*y-x*x; }, den:function(x,y){ return y*y-2*x; } }
  ];
  var k=2;

  function G(){ return C[k]; }
  function px(x){ var g=G(); return CX0+(x-(g.cx-g.w))/(2*g.w)*SIDE; }
  function py(y){ var g=G(); return TOPP+SIDE-(y-(g.cy-g.w))/(2*g.w)*SIDE; }
  // Values below 1e-12 are floating-point residue from sin and cos at multiples
  // of pi/2, not quantities; print them as the zero they are meant to be.
  function fmt(v){ if(!isFinite(v)) return '—';
    var a=Math.abs(v);
    if(a<1e-12) return (0).toFixed(4);
    if(a<1e-3||a>=1e5) return v.toExponential(3);
    return v.toFixed(4); }

  var bar=$('im-curves');
  C.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function draw(){
    var g=G(), s=(+$('im-t').value)/1000, P=g.p(s);
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);

    // grid at integers, then the axes darker
    c.strokeStyle=LINE; c.lineWidth=1;
    var lo=Math.ceil(g.cx-g.w), hi=Math.floor(g.cx+g.w), i;
    for(i=lo;i<=hi;i++){ c.beginPath(); c.moveTo(px(i),TOPP); c.lineTo(px(i),TOPP+SIDE); c.stroke(); }
    lo=Math.ceil(g.cy-g.w); hi=Math.floor(g.cy+g.w);
    for(i=lo;i<=hi;i++){ c.beginPath(); c.moveTo(CX0,py(i)); c.lineTo(CX0+SIDE,py(i)); c.stroke(); }
    c.strokeStyle=PALE; c.lineWidth=1.4;
    if(Math.abs(g.cx)<g.w){ c.beginPath(); c.moveTo(px(0),TOPP); c.lineTo(px(0),TOPP+SIDE); c.stroke(); }
    if(Math.abs(g.cy)<g.w){ c.beginPath(); c.moveTo(CX0,py(0)); c.lineTo(CX0+SIDE,py(0)); c.stroke(); }

    // the curve
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(i=0;i<=1400;i++){
      var q=g.p(i/1400);
      if(i===0) c.moveTo(px(q.x),py(q.y)); else c.lineTo(px(q.x),py(q.y));
    }
    c.stroke();

    // tangent through the point, in the direction (dx, dy)
    var L=Math.hypot(P.dx,P.dy);
    if(L>0){
      var ux=P.dx/L, uy=P.dy/L, r=3*g.w;
      c.strokeStyle=FAINT; c.lineWidth=1.6; c.setLineDash([6,4]);
      c.beginPath();
      c.moveTo(px(P.x-r*ux),py(P.y-r*uy));
      c.lineTo(px(P.x+r*ux),py(P.y+r*uy));
      c.stroke(); c.setLineDash([]);
    }
    c.fillStyle=INK; c.beginPath(); c.arc(px(P.x),py(P.y),4.5,0,6.284); c.fill();
    c.fillStyle=MUTED; c.font='700 11px '+FONT; c.textAlign='left';
    c.fillText(g.n, CX0, TOPP-8);

    // readout
    var N=g.num(P.x,P.y), D=g.den(P.x,P.y);
    var vertical = Math.abs(P.dx) < 1e-9*(Math.abs(P.dx)+Math.abs(P.dy));
    // At the folium's node both parts vanish at once. The curve crosses itself
    // there, so it has two tangents rather than none, and a single quotient
    // cannot choose between them.
    var node = Math.abs(N) < 1e-12 && Math.abs(D) < 1e-12;
    var slope = (vertical || node) ? null : N/D;
    var meas  = vertical ? null : P.dy/P.dx;
    var out=
      '<div><span class="im-lab">point on the curve</span>('+fmt(P.x)+', '+fmt(P.y)+')</div>'+
      '<div><span class="im-lab">dy/dx = '+g.eq+'</span>'+
        fmt(N)+' / '+fmt(D)+' = '+
        (node?'<span class="im-flag">0/0. The curve crosses itself here, so there are two tangents rather than none</span>'
            :vertical?'<span class="im-flag">undefined, vertical tangent</span>':fmt(slope))+'</div>'+
      '<div><span class="im-lab">measured, dy &divide; dx</span>'+
        (vertical?'<span class="im-flag">undefined</span>':fmt(meas))+
        (node?'<span class="im-flag">, the branch this parametrization is on</span>':'')+'</div>';
    $('im-read').innerHTML=out;
  }
  $('im-t').addEventListener('input',draw);
  draw();
})();
</script>

The visualization shows several implicit relations without solving them for $$y$$. The point moves along the curve, and the tangent line is drawn from the slope predicted by the implicit derivative. The reported slope can also be checked by parametrizing the curve and computing $$\tfrac{dy}{dx} = \tfrac{dy/dt}{dx/dt}$$, and the two methods agree wherever the slope exists.

## When the denominator is zero

For the circle $$x^2+y^2=25$$, implicit differentiation gives $$\tfrac{dy}{dx}=-\tfrac{x}{y}$$. At $$(5,0)$$, the denominator is zero. That does not mean the curve itself is undefined there. It means the tangent is vertical, so its slope is not a finite number, and the algebra is reporting the geometry correctly.

This is also why critical points of an implicit relation include points where the derivative is zero and points where the derivative does not exist. A zero numerator may produce a horizontal tangent, and a zero denominator may produce a vertical tangent.

## Second derivatives stay implicit

Differentiating again often leaves $$x$$, $$y$$, and $$dy/dx$$ in the expression. For the circle, $$\tfrac{dy}{dx}=-\tfrac{x}{y}$$, and differentiating using the [quotient rule](/2026/07/30/derivative-rules-and-choosing.html) gives

$$\frac{d^2y}{dx^2} = -\frac{y-x\frac{dy}{dx}}{y^2}$$

Now substitute $$\tfrac{dy}{dx}=-\tfrac{x}{y}$$, so

$$\frac{d^2y}{dx^2} = -\frac{y+\frac{x^2}{y}}{y^2} = -\frac{x^2+y^2}{y^3}$$

Since the original relation gives $$x^2+y^2=25$$, we obtain $$\tfrac{d^2y}{dx^2} = -\tfrac{25}{y^3}$$. The original relation is often useful after the differentiation because it can simplify the result.

<div class="article-note" markdown="1">
A good final check is geometric. Substitute a point you know lies on the curve and ask whether the sign and size of the slope fit the graph.
</div>
