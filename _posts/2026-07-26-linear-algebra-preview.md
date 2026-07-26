---
layout: post
title: "Linear algebra, the second pillar"
date: 2026-07-26
description: "Matrices as motions of space, determinants as area, eigenvectors as the directions that matter. The college course beneath nearly everything quantitative."
course: "All courses"
courses: [AP Calculus BC, AP Precalculus, AP Statistics]
read_time: "8 min read"
math: true
---

Ask a mathematician, a statistician, and a machine-learning engineer which college course they use most, and you will get one answer three times: linear algebra. It is the mathematics of many things at once, of data with thousands of columns, images with millions of pixels, systems with dozens of interlocking equations. Calculus studies change; linear algebra studies structure, and the modern world runs on both.

If you took AP Precalculus, you have already met the main character. A matrix there was a small grid that transformed points. That idea, taken seriously, is the whole course.

## A matrix is a motion of space

The matrix $$\begin{bmatrix} a & b \\ c & d \end{bmatrix}$$ moves every point of the plane at once: the point $$(x, y)$$ goes to $$(ax + by,\ cx + dy)$$. The best way to understand a particular matrix is to watch what it does to the whole grid. Try it.

<div class="viz" markdown="0">
  <canvas id="la-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="la-a">a</label><input type="range" id="la-a" min="-20" max="20" step="1" value="10" style="min-width:80px">
    <label for="la-b">b</label><input type="range" id="la-b" min="-20" max="20" step="1" value="0" style="min-width:80px">
    <label for="la-c">c</label><input type="range" id="la-c" min="-20" max="20" step="1" value="0" style="min-width:80px">
    <label for="la-d">d</label><input type="range" id="la-d" min="-20" max="20" step="1" value="10" style="min-width:80px">
  </div>
  <div class="viz-controls"><span class="viz-value" id="la-read" style="min-width:100%"></span></div>
  <p class="viz-caption">The light grid is the plane before; the dark grid is the plane after the matrix acts; the shaded region is the image of the unit square. Experiments: make the matrix double both diagonal entries and the square scales; set b nonzero and it shears; try a = 0, b = −1, c = 1, d = 0 for a rotation. Then watch the determinant readout: it is exactly the area of the shaded region, with a sign for orientation. Slide the entries until the determinant hits zero and the whole plane collapses onto a line, which is precisely when a matrix has no inverse, and the visual reason behind every determinant fact you memorized.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('la-cv'), c = cv.getContext('2d');
  var sa = document.getElementById('la-a'), sb = document.getElementById('la-b');
  var sc = document.getElementById('la-c'), sd = document.getElementById('la-d');
  var read = document.getElementById('la-read');
  var W = cv.width, H = cv.height, S = 46;
  function px(x){ return W/2 + x*S; }
  function py(y){ return H/2 - y*S; }
  function draw(){
    var a = sa.value/10, b = sb.value/10, cc = sc.value/10, d = sd.value/10;
    c.clearRect(0, 0, W, H);
    function T(x, y){ return [a*x + b*y, cc*x + d*y]; }
    function gridLines(fn, color, wdt){
      c.strokeStyle = color; c.lineWidth = wdt;
      for(var k = -6; k <= 6; k++){
        c.beginPath();
        for(var t = -6; t <= 6; t += 0.25){
          var p = fn(k, t); var X = px(p[0]), Y = py(p[1]);
          t === -6 ? c.moveTo(X, Y) : c.lineTo(X, Y);
        }
        c.stroke();
        c.beginPath();
        for(t = -6; t <= 6; t += 0.25){
          var q = fn(t, k); X = px(q[0]); Y = py(q[1]);
          t === -6 ? c.moveTo(X, Y) : c.lineTo(X, Y);
        }
        c.stroke();
      }
    }
    gridLines(function(x, y){ return [x, y]; }, '#ececea', 1);
    gridLines(T, '#b5b5b2', 1);
    // image of unit square
    var p0 = T(0,0), p1 = T(1,0), p2 = T(1,1), p3 = T(0,1);
    c.fillStyle = 'rgba(31,31,31,0.18)';
    c.beginPath();
    c.moveTo(px(p0[0]), py(p0[1])); c.lineTo(px(p1[0]), py(p1[1]));
    c.lineTo(px(p2[0]), py(p2[1])); c.lineTo(px(p3[0]), py(p3[1]));
    c.closePath(); c.fill();
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2; c.stroke();
    var det = a*d - b*cc;
    read.textContent = 'matrix [ ' + a.toFixed(1) + '  ' + b.toFixed(1) + ' ; ' + cc.toFixed(1) + '  ' + d.toFixed(1) + ' ]    det = ad − bc = ' + det.toFixed(2) + '  (area of the shaded image)';
  }
  [sa, sb, sc, sd].forEach(function(s){ s.addEventListener('input', draw); });
  draw();
})();
</script>

## Determinants stop being formulas

In Precalculus, $$ad - bc$$ was a rule. In linear algebra it becomes a picture: the determinant is the factor by which a matrix scales area (in three dimensions, volume), and its sign records whether the transformation flips orientation. Every mysterious determinant property becomes obvious at once. Why does a zero determinant mean no inverse? Because the matrix has flattened the plane onto a line, and a flattening cannot be undone: two different points now share an image, and no function can send one output back to two inputs. Why do determinants multiply when matrices compose? Because scaling area by 2 and then by 3 scales it by 6.

If you have seen the polar area element $$r\,dr\,d\theta$$ or wondered why substitution in integrals carries that extra factor, this is the same idea: the factor is a determinant, tracking how a change of variables distorts area. Calculus 3 and linear algebra are the two halves of one story.

## Eigenvectors: the directions a matrix cannot hide

Here is the course's central discovery. Almost every matrix, however it churns the plane, has a few special directions that it does not turn: vectors it merely stretches. Those are its **eigenvectors**, and the stretch factors are its **eigenvalues**. They are the matrix's true personality, and finding them turns impossible problems into easy ones, because along those directions a complicated transformation acts like simple multiplication.

Two examples show the reach. First, Google. Rank every webpage by the principle that a page is important if important pages link to it. That sounds circular, but write the link structure as a giant matrix and the circularity resolves: the ranking is the eigenvector of the web. PageRank, the algorithm that built Google, is an eigenvector computation on a matrix with billions of rows.

Second, your statistics course. A dataset with dozens of correlated variables is a cloud in high-dimensional space. Its covariance structure is a matrix, and that matrix's eigenvectors point along the directions where the data genuinely varies. Keeping only the biggest few, a technique called principal component analysis, compresses hundreds of variables into a handful with minimal loss, and it is a daily tool across genetics, finance, and image processing.

## Least squares, revisited from above

There is a moment in the course when AP Statistics students feel the floor connect. The least-squares regression line of Unit 5 is recomputed in one line of linear algebra: the data form a matrix equation $$X\beta \approx y$$ with no exact solution, and the least-squares fit is the *projection* of $$y$$ onto the space of predictions the model can reach, the geometric shadow of the data onto the model. The normal equations, the $$r^2$$ decomposition, multiple regression with twenty predictors: all of it is one projection picture. Statistics majors take linear algebra early for exactly this reason; regression is linear algebra wearing a lab coat.

## Where it sits in a college path

Linear algebra typically comes right after the calculus sequence, sometimes alongside it, and it is deliberately different in flavor: more ideas and structures, fewer long computations, and, in many versions, a first serious encounter with proof. Students who liked the why questions in AP courses often find it their favorite. It is prerequisite territory for machine learning, computer graphics, quantum mechanics, economics, cryptography, and essentially all of modern statistics. If calculus is the language of change, linear algebra is the language of data, and the two together are the working vocabulary of every quantitative field.

<div class="article-note" markdown="1">
A puzzle at the sliders: find a matrix whose determinant is negative and watch what happened to the shaded square's corners; the plane has been flipped over like a page. Then try to build a rotation with a negative determinant. You cannot, and proving why not, in any number of dimensions, is a one-line argument in the course. Rotations preserve orientation; reflections reverse it; the determinant's sign knows which is which.
</div>
