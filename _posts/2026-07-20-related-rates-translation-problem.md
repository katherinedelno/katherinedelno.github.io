---
layout: post
title: "A procedure for related rates"
date: 2026-07-20
description: "Related-rates problems are mostly translation. Name the changing quantities, relate them, differentiate with respect to time, and only then use the snapshot values."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "11 min read"
math: true
kind: mechanics
sequence: 14
interactive: true
blurb: "Related-rates problems are mostly translation. Name the changing quantities, relate them, differentiate with respect to time, and only then use the snapshot values"
image: "/assets/og/related-rates-translation-problem.png"
---

The calculus in a related-rates problem is usually straightforward.

The harder part is translating the situation into an equation that connects the changing quantities.

Once that equation is correct, the rest follows a stable procedure.

## A five-step routine

1. Draw the situation and name the changing quantities.
2. Write the rates you know and the rate you want.
3. Find an equation relating the variables.
4. Differentiate the equation with respect to time.
5. Substitute the values that describe the particular instant and solve.

The order matters.

A value that is true only at one instant should usually be substituted after the differentiation.

A relationship that is true for all time may be used before differentiating.

## The most common mistake

Suppose the area of a circle is

$$ A=\pi r^2. $$

If a problem asks about the instant when $$r=5$$, substituting 5 before differentiating gives

$$ A=25\pi. $$

Now $$r$$ is gone. The expression no longer records that the radius is changing.

Instead, differentiate first:

$$ \frac{dA}{dt} = 2\pi r\frac{dr}{dt}. $$

Then substitute $$r=5$$ and the relevant value of $$dr/dt$$.

The snapshot value belongs after the derivative because it is true only at that instant.

## Example 1: a sliding ladder

A 13-foot ladder leans against a wall. Its base moves away from the wall at 2 feet per second. How fast is the top moving when the base is 5 feet from the wall?

Let $$x$$ be the distance from the wall to the base and $$y$$ the height of the top.

We know

$$ \frac{dx}{dt}=2, $$

and we want $$dy/dt$$.

The ladder length is constant, so

$$ x^2+y^2=169. $$

Differentiate with respect to $$t$$:

$$ 2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0. $$

At the instant when $$x=5$$, the Pythagorean theorem gives $$y=12$$.

Now substitute:

$$ 2(5)(2) + 2(12)\frac{dy}{dt} = 0. $$

Therefore

$$ \frac{dy}{dt} = -\frac56. $$

The top is moving downward at

$$ \frac56 $$

foot per second.

The negative sign records the direction.

<div class="viz" markdown="0">
  <canvas id="lad-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="lad-x">Base distance</label>
    <input type="range" id="lad-x" min="10" max="125" step="1" value="50">
    <span class="viz-value" id="lad-read"></span>
  </div>
  <p class="viz-caption">The base moves at a steady 2 ft/s, yet the top's speed changes with position: gentle when the ladder is steep, violent as it flattens out. That is the whole point of related rates. The relationship between the rates depends on where you are, which is why the snapshot values must wait until after the differentiation. Note what happens to dy/dt as x approaches 13: the formula sends the top's speed toward infinity, a sign the model (a top that never leaves the wall) is breaking down, and a good example of interrogating a model's domain.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('lad-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('lad-x'), read = document.getElementById('lad-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var SC = 17, OX = 60, OY = H - 40;
  function draw(){
    var x = slider.value/10, y = Math.sqrt(169 - x*x);
    var dydt = -(x*2)/y;
    c.clearRect(0, 0, W, H);
    // wall and ground
    c.strokeStyle = '#9a9a97'; c.lineWidth = 2;
    c.beginPath(); c.moveTo(OX, OY); c.lineTo(OX + 15*SC, OY); c.stroke();
    c.beginPath(); c.moveTo(OX, OY); c.lineTo(OX, OY - 14*SC); c.stroke();
    // ladder
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 4; c.lineCap = 'round';
    c.beginPath(); c.moveTo(OX + x*SC, OY); c.lineTo(OX, OY - y*SC); c.stroke();
    c.lineCap = 'butt';
    // base arrow (constant)
    c.strokeStyle = '#6b6b6b'; c.lineWidth = 2;
    c.beginPath(); c.moveTo(OX + x*SC, OY + 16); c.lineTo(OX + x*SC + 34, OY + 16); c.stroke();
    c.beginPath(); c.moveTo(OX + x*SC + 34, OY + 16); c.lineTo(OX + x*SC + 27, OY + 12); c.moveTo(OX + x*SC + 34, OY + 16); c.lineTo(OX + x*SC + 27, OY + 20); c.stroke();
    // top arrow (scaled by |dy/dt|)
    var alen = Math.min(Math.abs(dydt)*16, 90);
    c.beginPath(); c.moveTo(OX - 16, OY - y*SC); c.lineTo(OX - 16, OY - y*SC + alen); c.stroke();
    c.beginPath(); c.moveTo(OX - 16, OY - y*SC + alen); c.lineTo(OX - 20, OY - y*SC + alen - 7); c.moveTo(OX - 16, OY - y*SC + alen); c.lineTo(OX - 12, OY - y*SC + alen - 7); c.stroke();
    c.fillStyle = '#5c5c5c'; c.font = '700 13px Hanken Grotesk, sans-serif';
    c.fillText('2 ft/s (constant)', OX + x*SC + 42, OY + 20);
    read.textContent = 'x = ' + x.toFixed(1) + ' ft,  y = ' + y.toFixed(2) + ' ft,  dy/dt = ' + dydt.toFixed(2) + ' ft/s';
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The base moves at a constant rate, but the top does not.

As the ladder becomes flatter, the magnitude of $$dy/dt$$ increases. The relationship between the two rates depends on the geometry at that instant.

This is why the position values cannot be inserted before differentiating.

## Example 2: a draining cone

An inverted conical tank has radius 6 meters and height 12 meters. Water drains at 3 cubic meters per minute. How fast is the water level falling when the water is 4 meters deep?

Let $$h$$ be the water depth, $$r$$ the radius of the water surface, and $$V$$ the volume.

Both $$r$$ and $$h$$ change, but the shape of the tank gives a relationship that is true at every instant.

Similar triangles give

$$ \frac{r}{h} = \frac{6}{12}, $$

so

$$ r=\frac{h}{2}. $$

Because this relationship is always true, it can be substituted before differentiation.

The volume is

$$ V = \frac13\pi r^2h = \frac13\pi\left(\frac h2\right)^2h = \frac{\pi h^3}{12}. $$

Differentiate:

$$ \frac{dV}{dt} = \frac{\pi h^2}{4}\frac{dh}{dt}. $$

At the instant in question,

$$ \frac{dV}{dt}=-3 $$

and

$$ h=4. $$

So

$$ -3 = 4\pi\frac{dh}{dt}, $$

which gives

$$ \frac{dh}{dt} = -\frac{3}{4\pi}. $$

The water level is falling at

$$ \frac{3}{4\pi} \approx0.239 $$

meter per minute.

Notice the two kinds of substitution.

The relationship $$r=h/2$$ is structural and holds for all time. The value $$h=4$$ is a snapshot and waits until after differentiation.

## Example 3: a camera tracking a rocket

A camera is 100 meters from a launch pad. A rocket rises vertically at 50 meters per second. How fast is the camera's angle of elevation increasing when the rocket is 100 meters high?

Let $$y$$ be the rocket's height and $$\theta$$ the angle of elevation.

The horizontal distance is constant, so

$$ \tan\theta = \frac{y}{100}. $$

Differentiate with respect to time:

$$ \sec^2\theta\frac{d\theta}{dt} = \frac{1}{100}\frac{dy}{dt}. $$

When $$y=100$$,

$$ \theta=\frac{\pi}{4}, $$

so

$$ \sec^2\theta=2. $$

Using

$$ \frac{dy}{dt}=50, $$

we get

$$ 2\frac{d\theta}{dt} = \frac{50}{100}. $$

Therefore

$$ \frac{d\theta}{dt} = \frac14. $$

The angle is increasing at one quarter radian per second.

Radians matter here because the standard trigonometric derivative formulas assume radian measure.

## A final check

Before finishing a related-rates problem, check four things.

- Does the sign agree with the story?
- Do the units work?
- Did every changing variable receive its own rate during differentiation?
- Does [the final sentence](/2026/07/08/notation-that-costs-ap-calculus-points.html) state the value, units, and direction?

If the tank is draining, $$dV/dt$$ should be negative.

If a term such as $$y^2$$ was differentiated with respect to time, the result should contain $$dy/dt$$.

If the units do not balance across the differentiated equation, something in the setup is wrong.

<div class="article-note" markdown="1">
The calculus is usually not the fragile part. The translation is.
</div>
