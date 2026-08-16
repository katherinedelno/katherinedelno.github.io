---
layout: post
title: "A preview of linear algebra"
date: 2026-07-26
description: "Linear algebra studies vectors, matrices, transformations, and systems. Its geometry underlies regression, machine learning, differential equations, and much of modern applied mathematics."
course: "All courses"
courses: [AP Calculus BC, AP Precalculus, AP Statistics]
section: beyond
read_time: "8 min read"
math: true
kind: beyond
sequence: 8
interactive: true
blurb: "Linear algebra studies vectors, matrices, transformations, and systems. Its geometry underlies regression, machine learning, differential equations, and much of modern applied mathematics"
image: "/assets/og/linear-algebra-preview.png"
---

Linear algebra studies systems of quantities at once.

Its basic objects are vectors, matrices, and linear transformations.

The subject appears throughout mathematics, statistics, engineering, physics, computer science, and machine learning because many problems can be organized around these structures.

A matrix is more than a rectangular table of numbers.

It can be understood as a rule that transforms space.

## A matrix as a transformation

Consider

$$A = \begin{bmatrix} a & b\\ c & d \end{bmatrix}.$$

Applied to a point

$$\begin{bmatrix} x\\y \end{bmatrix},$$

the matrix produces

$$A \begin{bmatrix} x\\y \end{bmatrix} = \begin{bmatrix} ax+by\\ cx+dy \end{bmatrix}.$$

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
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
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

The light grid shows the original plane.

The dark grid shows the result after the matrix acts.

The shaded parallelogram is the image of the unit square.

Try changing the diagonal entries.

Then introduce a nonzero off-diagonal entry to create a shear.

The same matrix acts on every point of the plane at once.

That viewpoint makes many matrix rules geometric.

## The determinant as area scale

For a two-dimensional matrix,

$$\det(A)=ad-bc.$$

Geometrically, the absolute value of the determinant is the factor by which the transformation scales area.

If

$$\vert \det(A)\vert =2,$$

the area of the unit square becomes 2.

If

$$\det(A)=0,$$

the transformed square collapses to zero area.

The plane has been flattened into a line or point.

Such a transformation cannot be inverted because distinct input points are sent to the same output.

The sign of the determinant records orientation.

A negative determinant means the transformation reverses orientation, as a reflection does.

This geometric interpretation explains why the determinant is much more than a formula for checking invertibility.

## Eigenvectors and eigenvalues

Some directions have a special relationship with a matrix.

An eigenvector $$v$$ satisfies

$$Av=\lambda v.$$

The matrix may stretch, shrink, or reverse the vector, but it does not rotate it away from its line.

The scalar $$\lambda$$ is the corresponding eigenvalue.

Eigenvectors identify directions along which a complicated transformation becomes simple multiplication.

This makes them useful for understanding repeated transformations and systems that evolve over time.

## Repeated transformations

Suppose the same matrix is applied again and again.

Directly computing

$$A^n$$

can become cumbersome.

If the matrix can be expressed in a basis of eigenvectors, repeated application becomes much easier because each eigenvector direction is simply multiplied by its eigenvalue at every step.

This idea appears in population models, Markov chains, differential equations, numerical algorithms, and many other settings.

## Least squares becomes geometry

Linear regression can also be written in matrix form.

With several predictors,

$$X\beta\approx y.$$

Usually there is no coefficient vector $$\beta$$ that makes every prediction equal the observed response exactly.

Least squares chooses the vector that makes the residual vector as small as possible in squared Euclidean distance.

Geometrically, the fitted response is the projection of $$y$$ onto the space of possible predictions generated by the columns of $$X$$.

The familiar [least-squares line](/2026/07/30/least-squares-regression-influence.html) from introductory statistics is the simplest version of this projection problem.

Multiple regression uses the same geometry in higher dimensions.

## Principal components

A dataset with many variables can be viewed as a cloud of points in a high-dimensional space.

The covariance matrix records how those variables vary together.

Its eigenvectors identify principal directions of variation.

Principal component analysis uses these directions to create new coordinates that capture as much variation as possible with fewer dimensions.

This is one example of how linear algebra becomes a natural language for statistics and data analysis.

## Connections to calculus

Linear algebra and multivariable calculus meet constantly.

The derivative of a function of several variables is naturally represented by a linear map.

Jacobian matrices describe local changes of coordinates.

Determinants measure how those transformations scale area and volume.

Systems of differential equations can be studied using eigenvalues and eigenvectors.

The subjects are taught separately, but they increasingly overlap as the mathematics becomes more advanced.

## What the course feels like

A first linear algebra course often contains fewer long symbolic computations than calculus and more attention to structure.

The early topics may include:

- systems of linear equations
- matrices and matrix operations
- vector spaces
- linear independence
- bases and dimension
- linear transformations
- determinants
- eigenvalues and eigenvectors
- orthogonality and least squares

Proof may also become more prominent, depending on the course.

<div class="article-note" markdown="1">
The central shift is to stop treating a matrix as a collection of entries and begin treating it as an object that acts on a space.

The sliders above are a good place to begin.
</div>
