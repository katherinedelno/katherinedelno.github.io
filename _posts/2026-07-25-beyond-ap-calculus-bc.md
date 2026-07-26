---
layout: post
title: "Beyond BC: a preview of multivariable calculus"
date: 2026-07-25
description: "Everything in BC lives on a curve. Add one more variable and functions become landscapes, derivatives become compass directions, and integrals fill volumes. A tour of what waits in Calculus 3, with a surface you can spin."
course: "AP Calculus BC"
read_time: "8 min read"
math: true
---

Every function in AP Calculus takes one number in and puts one number out, so its graph is a curve, and the whole course happens on that curve: slopes along it, areas under it. Calculus 3 asks a single innocent question. What if a function takes two numbers in?

The answer is that the graph becomes a surface, a landscape floating over the plane, and every idea you learned this year grows a new dimension. None of the BC machinery is wasted; it all reappears, upgraded.

## Functions become landscapes

The function $$f(x,y) = \sin x \cos y$$ takes a point of the plane and returns a height. Its graph is the rolling terrain below. Drag the slider to walk around it.

<div class="viz" markdown="0">
  <canvas id="s3-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="s3-rot">Rotate</label>
    <input type="range" id="s3-rot" min="0" max="1000" value="140">
  </div>
  <p class="viz-caption">The graph of z = sin x cos y, a function of two variables. Peaks, valleys, and mountain passes replace the maxima and minima of BC. Walking east-west changes the height at one rate, walking north-south at another, and that observation is the whole idea of partial derivatives.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('s3-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('s3-rot');
  var W = cv.width, H = cv.height;
  var N = 28, LO = -3.6, HI = 3.6;
  function f(x, y){ return Math.sin(x)*Math.cos(y); }
  function draw(){
    var th = (slider.value/1000)*2*Math.PI, tilt = 0.42;
    var ct = Math.cos(th), st = Math.sin(th);
    c.clearRect(0, 0, W, H);
    function proj(x, y, z){
      var X = x*ct - y*st, Y = x*st + y*ct;
      return [W/2 + X*62, H/2 + 26 - z*74 + Y*62*tilt];
    }
    var i, j;
    c.lineWidth = 1;
    for(i = 0; i <= N; i++){
      var x = LO + (HI - LO)*i/N;
      c.strokeStyle = '#9a9a97'; c.beginPath();
      for(j = 0; j <= N; j++){
        var y = LO + (HI - LO)*j/N, p = proj(x, y, f(x, y));
        j ? c.lineTo(p[0], p[1]) : c.moveTo(p[0], p[1]);
      }
      c.stroke();
    }
    for(j = 0; j <= N; j++){
      var y2 = LO + (HI - LO)*j/N;
      c.strokeStyle = '#c9c9c6'; c.beginPath();
      for(i = 0; i <= N; i++){
        var x2 = LO + (HI - LO)*i/N, p2 = proj(x2, y2, f(x2, y2));
        i ? c.lineTo(p2[0], p2[1]) : c.moveTo(p2[0], p2[1]);
      }
      c.stroke();
    }
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

## Derivatives become directions

On a curve there is only one way to move, so one derivative suffices. On a landscape you can set off in any direction, and each direction has its own rate of change. Calculus 3 tames the infinity of choices with two special ones: the **partial derivatives** $$\tfrac{\partial f}{\partial x}$$ and $$\tfrac{\partial f}{\partial y}$$, the rates of change walking due east and due north. They are computed with the rules you already know, holding the other variable still, so if $$f(x,y) = x^2 y$$, then $$\tfrac{\partial f}{\partial x} = 2xy$$, treating $$y$$ like the constant it momentarily is.

Then comes the first genuinely new object of the course. Package the two partials into a vector,

$$\nabla f = \left\langle \frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y} \right\rangle,$$

called the **gradient**, and something remarkable is true: at every point of the landscape, this vector points in the direction of steepest ascent, and its length is the steepness. A ball released on the surface rolls exactly opposite the gradient. Hikers, heat-seeking particles, and the machine-learning algorithms that train neural networks all follow gradients; "gradient descent," the phrase behind much of modern AI, means rolling downhill on a landscape with millions of input variables instead of two.

Optimization upgrades the same way. Maxima and minima still occur where the derivative vanishes, but now that means the whole gradient is zero, and a new character appears alongside peaks and valleys: the **saddle point**, a mountain pass that is a maximum along one direction and a minimum along another. The second-derivative test grows into a determinant computation for exactly this reason; one number can no longer distinguish a peak from a pass. You can spot saddles in the surface above, sitting between neighboring peaks.

## Integrals fill volumes

In BC, $$\int_a^b f\,dx$$ adds up values along an interval. The **double integral** $$\iint_R f\,dA$$ adds up values over a whole region of the plane, and where the single integral computed area under a curve, the double integral computes volume under a surface. The mechanics are pleasantly familiar: integrate in $$x$$ treating $$y$$ as constant, then integrate the result in $$y$$, two BC integrals stacked. Riemann sums return too, now as grids of rectangular columns filling a solid, which is exactly the picture the wireframe above suggests.

Polar coordinates, which BC introduced for curves, become a workhorse here. Regions with circular symmetry are miserable in $$x$$ and $$y$$ and effortless in $$r$$ and $$\theta$$, and the polar area element $$dA = r\,dr\,d\theta$$ explains, at last, exactly why the polar area formula you memorized carries its factor of $$\tfrac12 r^2$$. And one of the first triumphs of the course is a BC white whale: $$\int_{-\infty}^{\infty} e^{-x^2} dx$$, which has no elementary antiderivative, falls in three lines once you square it and switch to polar coordinates. The answer is $$\sqrt{\pi}$$, and it is the reason the normal distribution in statistics has a $$\sqrt{2\pi}$$ in its formula.

## Curves fight back: vector fields and line integrals

The last third of the course flips the picture. Instead of a landscape of heights, imagine a plane where every point carries an arrow: wind velocity, water current, gravitational pull. That is a **vector field**, and the natural question becomes: how much does the field help or hinder you as you travel along a curve through it? The answer is a **line integral**, and it is precisely the physicist's definition of work.

Here your parametric training pays its full dividend. Curves are traced by $$\big(x(t), y(t)\big)$$ exactly as in BC Unit 9, and the arc-length integrand $$\sqrt{x'(t)^2 + y'(t)^2}$$ you learned there is the backbone of every line integral.

The finale is a family of theorems, with **Green's theorem** first among them, that relate what a field does along the boundary of a region to what happens inside it. If that sounds familiar, it should: the Fundamental Theorem of Calculus says the accumulation inside an interval is controlled by values at the two boundary points. Green's theorem is the same statement one dimension up, and Stokes' theorem, at the end of the road, is the version for surfaces in space. The FTC you learned this year is the first rung of a ladder that climbs through every dimension.

## What carries over, and what to keep sharp

Students sometimes assume Calculus 3 requires new superpowers. It mostly requires BC skills executed cleanly in a richer setting: the chain rule (which becomes a beautiful tree-diagram bookkeeping system), integration technique, parametric curves and vectors, polar coordinates, and comfort with limits. The series unit takes a rest and returns in differential equations and analysis courses.

If you want the honest preview in one sentence: BC taught you calculus on a wire; Calculus 3 teaches it on a sheet, and the sheet is where physics, economics, data science, and machine learning actually live.

<div class="article-note" markdown="1">
A question to carry with you into the course: on the spinning surface above, where would a drop of water land if it started at a mountain pass, exactly on the saddle? The answer depends on the direction of the smallest nudge, which is why saddle points, not peaks, turn out to be the interesting places, in mountain ranges and in neural networks alike.
</div>
