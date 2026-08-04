---
layout: post
title: "Implicit differentiation"
date: 2026-07-30
description: "When a relation between x and y cannot be solved for y, the derivative can still be found. The method is the chain rule applied to a variable rather than to an expression, and the result depends on both coordinates."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 11
interactive: true
blurb: "The slope on an implicit curve needs both coordinates, not just x"
image: "/assets/og/implicit-differentiation.png"
---

A relation like $$x^2 + xy + y^2 = 7$$ describes a perfectly good curve, and it has a tangent line at almost every point of it. What it does not have is a formula for $$y$$ in terms of $$x$$ that anyone wants to differentiate.

Implicit differentiation gets the slope without solving. The framework's statement of it is one sentence: the chain rule is the basis for implicit differentiation. That is not a hint about where the method came from. It is the method.

## The chain rule, applied to a variable

Differentiating $$y^2$$ with respect to $$x$$ gives $$2y \cdot \tfrac{dy}{dx}$$, not $$2y$$. The extra factor is the [inner derivative](/2026/07/30/chain-rule-reading-the-layers.html) — $$y$$ is a function of $$x$$, so $$y^2$$ is a composition, and the chain rule attaches the derivative of what is inside. The course's exam guidance says exactly this: in an expression like $$\tfrac{y}{3y^2 - x}$$, students must recognize that the chain rule applies to $$y$$ because $$y$$ depends on $$x$$.

Everything else is ordinary differentiation. Take $$x^2 + xy + y^2 = 7$$ and differentiate both sides with respect to $$x$$, using the product rule on $$xy$$:

$$2x + \left(y + x\frac{dy}{dx}\right) + 2y\frac{dy}{dx} = 0.$$

Collect the $$\tfrac{dy}{dx}$$ terms and solve:

$$\frac{dy}{dx} = -\,\frac{2x + y}{x + 2y}.$$

## The slope needs both coordinates

That formula is the structural difference. An explicit derivative is a function of $$x$$ alone; an implicit one takes $$x$$ and $$y$$ both, and it has to, because a vertical line usually meets the curve more than once.

On this curve, setting $$x = 1$$ gives $$y^2 + y - 6 = 0$$, so $$y = 2$$ or $$y = -3$$. Both points are on the curve. At $$(1, 2)$$ the slope is $$-\tfrac45$$, and at $$(1, -3)$$ it is $$-\tfrac15$$. Same $$x$$, same relation, different tangents. An answer of the form "$$\tfrac{dy}{dx}$$ at $$x = 1$$" is not a well-posed question here, and that is worth noticing before an exam asks for a tangent line and supplies a point rather than a coordinate.

<div class="viz" markdown="0">
  <div class="viz-controls" id="im-curves"></div>
  <canvas id="im-cv" width="700" height="380"></canvas>
  <div class="viz-controls">
    <label for="im-t">Point on the curve</label>
    <input type="range" id="im-t" min="0" max="1000" step="1" value="120">
  </div>
  <div class="im-read" id="im-read"></div>
  <p class="viz-caption">Four relations, none of them solved for y. The point slides along the curve and the line drawn through it is the tangent whose slope the implicit formula predicts. Below, that formula is shown with its numerator and denominator separated, then checked against a slope obtained a completely different way — by parametrizing the curve and dividing dy by dx. The two agree everywhere, including where they both fail: when the denominator reaches zero the tangent is vertical and there is no slope to report, which is a point the course calls critical rather than an accident of the algebra.</p>
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
        (node?'<span class="im-flag">0/0 &mdash; the curve crosses itself here, so there are two tangents rather than none</span>'
            :vertical?'<span class="im-flag">undefined &mdash; vertical tangent</span>':fmt(slope))+'</div>'+
      '<div><span class="im-lab">measured, dy &divide; dx</span>'+
        (vertical?'<span class="im-flag">undefined</span>':fmt(meas))+
        (node?'<span class="im-flag">&nbsp;&mdash; the branch this parametrization is on</span>':'')+'</div>';
    $('im-read').innerHTML=out;
  }
  $('im-t').addEventListener('input',draw);
  draw();
})();
</script>

Slide along the circle and the two coordinates trade roles: near the top and bottom the curve is flat and the slope is near zero, near the left and right edges it is steep. The formula $$-\tfrac{x}{y}$$ says both of those at once, and it says them without ever mentioning $$\sqrt{25 - x^2}$$.

## When the denominator is zero

At $$(5, 0)$$ on the circle the formula gives $$-\tfrac50$$, which is not a number. The curve is not misbehaving — it has a vertical tangent there, and a vertical line has no slope. The algebra reports the geometry accurately by refusing to produce a value.

This is course content rather than a footnote. Unit 5 defines a critical point of an implicit relation as a point where the first derivative equals zero *or does not exist*, so the vanishing denominator is one of the two cases you are expected to find. On the folium $$x^3 + y^3 = 6xy$$ the denominator $$y^2 - 2x$$ vanishes at $$\big(2^{5/3},\, 2^{4/3}\big) \approx (3.1748,\, 2.5198)$$, and by the curve's symmetry in $$x$$ and $$y$$ the numerator vanishes at the mirror point, where the tangent is horizontal instead. The slider does not land exactly on either, and watching it approach is the more useful view: the reported slope climbs past 500 rounding one end of the loop and falls below two thousandths at the other. On the circle it does land exactly, and there the readout stops giving numbers and says why.

## The second derivative keeps the first one inside it

Differentiating again does not escape the situation. The course says so directly: second derivatives involving implicit differentiation may be relations of $$x$$, $$y$$, and $$\tfrac{dy}{dx}$$. On the circle, applying the [quotient rule](/2026/07/30/derivative-rules-and-choosing.html) to $$-\tfrac{x}{y}$$,

$$\frac{d^2y}{dx^2} = -\,\frac{y - x\tfrac{dy}{dx}}{y^2} = -\,\frac{y + \tfrac{x^2}{y}}{y^2} = -\,\frac{x^2 + y^2}{y^3},$$

where the middle step substitutes the first derivative back in. Only now does the relation itself help: $$x^2 + y^2 = 25$$, so the whole thing collapses to $$-\tfrac{25}{y^3}$$. Substituting the constraint is the last step, not the first, and doing it early is how the algebra usually goes wrong.

<div class="article-note" markdown="1">
A check worth running on every implicit answer: substitute a point you know is on the curve and ask whether the number is plausible from the picture. The folium at $$(3, 3)$$ gives $$\tfrac{6 - 9}{9 - 6} = -1$$, and the curve is symmetric about $$y = x$$ there, so a slope of $$-1$$ is the only answer the symmetry allows. Most sign errors in implicit differentiation die at that test.
</div>
