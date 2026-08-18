---
layout: practice
title: "Related rates"
date: 2026-08-18
description: "Ten multiple-choice items and two free-response questions on related rates, with full solutions, named distractors, and the rubric points each part carries."
blurb: "Ten multiple-choice items and two free-response questions, split the way Section I is split, with the rubric points each part carries"
course: "AP Calculus AB & BC"
kind: mechanics
sequence: 4
unit: "Unit 4, Contextual Applications of Differentiation"
archetype: "Related Rates"
ced_topics: ["4.4", "4.5"]
ced_weight: "Unit 4 is 10 to 15 percent of the exam"
exam_form: "May 2027"
mcq_no_calc: 6
mcq_calc: 4
frq_count: 2
frq_points: 18
essay: /2026/07/20/related-rates-translation-problem.html
read_time: "37 min read"
work_time: "55 min timed"
math: true
image: "/assets/og/practice-related-rates.png"
---

Related rates questions are mostly translation. The calculus in them is one application of the chain rule.

Almost every point lost on this archetype is lost before any differentiation happens. It is lost in the equation relating the quantities, or in the moment a value that is true only at one instant gets substituted too early.

The ten multiple-choice items below are split the way Section I is split, six without a calculator and four with one. The two free-response questions carry the rubric points a reader would apply.

Work the set cold and timed. The solutions are worth more after an honest attempt than before one.

If the setup itself is the difficulty rather than the arithmetic, read [A procedure for related rates](/2026/07/20/related-rates-translation-problem.html) first and come back.

## Section I, Part A

Six items, no calculator. Allow about thirteen minutes, which is the per-question budget of the real Part A.

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 1</span><span class="pr-nocalc">No calculator</span><span>CED 4.5</span></p>

A spherical balloon is inflated so that its radius increases at a constant rate of 0.5 centimeter per second. At the instant the radius is 4 centimeters, what is the rate of change of the volume of the balloon, in cubic centimeters per second?

- (A) $$8\pi$$
- (B) $$32\pi$$
- (C) $$64\pi$$
- (D) $$\tfrac{256\pi}{3}$$

<div class="pr-sol" markdown="1">

**Answer: (B).**

The volume of a sphere in terms of its radius is

$$ V=\frac{4}{3}\pi r^3 . $$

Both $$V$$ and $$r$$ are functions of time, so differentiating with respect to $$t$$ requires the chain rule:

$$ \frac{dV}{dt}=4\pi r^2\,\frac{dr}{dt}. $$

The instant is described by $$r=4$$ and $$dr/dt=0.5$$, and both values are substituted only now, after the differentiation:

$$ \frac{dV}{dt}=4\pi(4)^2(0.5)=32\pi \ \text{cm}^3\!/\text{s}. $$

**Where the other options come from.**

- **(A)** differentiates $$r^3$$ as though the exponent were 2, producing $$4\pi r$$ in place of $$4\pi r^2$$.
- **(C)** differentiates correctly and then omits $$dr/dt$$. That omission is the chain rule itself, and it is the single most common error in this archetype.
- **(D)** substitutes $$r=4$$ before differentiating. The number that results is the volume at that instant, not a rate, and its units give it away.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 2</span><span class="pr-nocalc">No calculator</span><span>CED 4.5</span></p>

Two vehicles leave the same intersection at the same time. One travels north at a constant 40 miles per hour and the other travels east at a constant 30 miles per hour. Two hours after they leave, at what rate is the distance between them increasing, in miles per hour?

- (A) 35
- (B) 40
- (C) 48
- (D) 50

<div class="pr-sol" markdown="1">

**Answer: (D).**

Let $$x$$ be the eastward distance, $$y$$ the northward distance, and $$z$$ the distance between the vehicles. The paths are perpendicular, so

$$ z^2=x^2+y^2 . $$

Differentiating with respect to $$t$$ gives

$$ 2z\,\frac{dz}{dt}=2x\,\frac{dx}{dt}+2y\,\frac{dy}{dt}. $$

At $$t=2$$ the distances are $$x=60$$ and $$y=80$$, so $$z=100$$. Substituting now,

$$ \frac{dz}{dt}=\frac{60(30)+80(40)}{100}=\frac{5000}{100}=50 \ \text{mi/h}. $$

Note that 50 exceeds both speeds. It has to: each vehicle contributes to the separation, so the distance grows faster than either one travels. Adding the speeds to get 70 would be correct only for two vehicles moving in opposite directions along one line, where the geometry collapses to a subtraction of coordinates.

**Where the other options come from.**

- **(A)** averages the two speeds. Averaging would answer a question about a single vehicle, not about a distance built from two.
- **(B)** reports the speed of the faster vehicle, on the reasoning that the separation grows at least that fast. The reasoning is sound and the conclusion is a lower bound, not the rate.
- **(C)** pairs each distance with the other vehicle's speed. The arithmetic is otherwise identical, which is exactly why the bookkeeping deserves the care.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 3</span><span class="pr-nocalc">No calculator</span><span>CED 4.5</span></p>

Water is pumped into an inverted right circular cone at a constant rate of 2 cubic meters per minute. The cone has height 6 meters and radius 3 meters at the top. At the instant the water is 4 meters deep, at what rate is the depth increasing, in meters per minute?

- (A) $$\tfrac{1}{8\pi}$$
- (B) $$\tfrac{1}{6\pi}$$
- (C) $$\tfrac{1}{2\pi}$$
- (D) $$\tfrac{2}{3\pi}$$

<div class="pr-sol" markdown="1">

**Answer: (C).**

The water forms a cone similar to the tank, so its radius and depth stay in a fixed ratio:

$$ \frac{r}{h}=\frac{3}{6}=\frac{1}{2}\qquad\Longrightarrow\qquad r=\frac{h}{2}. $$

That relation holds at every instant, so it may be used before differentiating. Eliminating $$r$$ first leaves one variable:

$$ V=\frac{1}{3}\pi r^2 h=\frac{1}{3}\pi\left(\frac{h}{2}\right)^{2}h=\frac{\pi h^3}{12}. $$

Now differentiate and substitute the snapshot values $$dV/dt=2$$ and $$h=4$$:

$$ \frac{dV}{dt}=\frac{\pi h^2}{4}\,\frac{dh}{dt}\qquad\Longrightarrow\qquad 2=4\pi\,\frac{dh}{dt}\qquad\Longrightarrow\qquad \frac{dh}{dt}=\frac{1}{2\pi}. $$

**Where the other options come from.**

- **(A)** uses $$r=h$$, dropping the similar-triangle relation entirely.
- **(B)** omits the factor $$\tfrac13$$ in the volume of a cone.
- **(D)** holds the radius fixed at 3. A vessel whose radius does not change with depth is a cylinder, and the whole difficulty of the item disappears with it.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 4</span><span class="pr-nocalc">No calculator</span><span>CED 4.5</span></p>

A street lamp is mounted 15 feet above level ground. A person 6 feet tall walks away from the base of the lamp along a straight path at 4 feet per second. At what rate is the tip of the person's shadow moving along the ground, in feet per second?

- (A) $$\tfrac{8}{5}$$
- (B) $$\tfrac{8}{3}$$
- (C) 4
- (D) $$\tfrac{20}{3}$$

<div class="pr-sol" markdown="1">

**Answer: (D).**

Let $$x$$ be the distance from the base of the lamp to the person and $$s$$ the length of the shadow. The lamp and the person cut off similar right triangles, so

$$ \frac{6}{s}=\frac{15}{x+s}. $$

Cross-multiplying and collecting,

$$ 6(x+s)=15s\qquad\Longrightarrow\qquad 6x=9s\qquad\Longrightarrow\qquad s=\frac{2}{3}x. $$

The tip of the shadow sits at distance $$x+s$$ from the base, so

$$ x+s=\frac{5}{3}x\qquad\Longrightarrow\qquad \frac{d}{dt}(x+s)=\frac{5}{3}\,\frac{dx}{dt}=\frac{5}{3}(4)=\frac{20}{3}\ \text{ft/s}. $$

Notice that $$x$$ never appears in the answer. The tip moves at the same rate wherever the person is, which is worth knowing because a question that supplies a distance is often supplying a number the solution does not need.

**Where the other options come from.**

- **(A)** inverts the ratio, multiplying by $$\tfrac{6}{15}$$ rather than by the $$\tfrac53$$ the similar triangles produce. An answer smaller than the person's own speed should end this option before the arithmetic is checked.
- **(B)** gives $$ds/dt$$, the rate at which the shadow lengthens. The tip carries the person's own motion as well, so the two rates differ by exactly $$dx/dt$$.
- **(C)** reports the person's speed.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 5</span><span class="pr-nocalc">No calculator</span><span>CED 4.4</span></p>

For a fixed quantity of gas held at constant temperature, the pressure $$P$$ in atmospheres and the volume $$V$$ in liters satisfy $$PV=200$$. At the instant $$V=20$$, the volume is increasing at 4 liters per minute. What is $$dP/dt$$ at that instant, in atmospheres per minute?

- (A) $$-40$$
- (B) $$-2$$
- (C) $$-\tfrac{1}{2}$$
- (D) 2

<div class="pr-sol" markdown="1">

**Answer: (B).**

The relation is already given, so no geometry is needed. Differentiate it as a product, since both factors vary with time:

$$ P\,\frac{dV}{dt}+V\,\frac{dP}{dt}=0. $$

The instant supplies $$V=20$$ and $$dV/dt=4$$. It does not supply $$P$$, which has to be recovered from the relation itself:

$$ P=\frac{200}{20}=10. $$

Substituting all three values,

$$ 10(4)+20\,\frac{dP}{dt}=0\qquad\Longrightarrow\qquad \frac{dP}{dt}=-2\ \text{atm/min}. $$

**Where the other options come from.**

- **(A)** uses 200 in place of $$P$$. The constant on the right side of the relation is the product of the two quantities, not one of them, and a missing value has to be recovered before it can be substituted.
- **(C)** inverts the last division.
- **(D)** drops the sign. A relation of the form $$PV=c$$ forces the two quantities to move in opposite directions, so a positive answer here is wrong before any arithmetic is checked.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 6</span><span class="pr-nocalc">No calculator</span><span>CED 4.5</span></p>

The length and the width of a rectangle are both functions of time. At a certain instant the length is 10 centimeters and increasing at 3 centimeters per second, while the width is 6 centimeters and decreasing at 2 centimeters per second. What is the rate of change of the area at that instant, in square centimeters per second?

- (A) $$-20$$
- (B) $$-6$$
- (C) $$-2$$
- (D) 38

<div class="pr-sol" markdown="1">

**Answer: (C).**

Write the length as $$f(t)$$ and the width as $$g(t)$$, so the area is the product $$A=fg$$ and

$$ \frac{dA}{dt}=f'g+fg'. $$

The instant gives $$f=10$$, $$f'=3$$, $$g=6$$, and $$g'=-2$$. The word *decreasing* is what makes $$g'$$ negative, and carrying that sign is the whole content of the item:

$$ \frac{dA}{dt}=3(6)+10(-2)=18-20=-2\ \text{cm}^2\!/\text{s}. $$

The area is shrinking even though the length is growing faster than the width is shrinking, because each rate is weighted by the *other* dimension.

**Where the other options come from.**

- **(A)** keeps only the second term, differentiating the width and holding the length fixed.
- **(B)** multiplies the two rates. The product rule adds two terms, each of which holds one factor fixed, and never multiplies the derivatives.
- **(D)** ignores the sign on the width, so the two effects reinforce each other instead of opposing.

</div>
</div>

## Section I, Part B

Four items, graphing calculator required. Allow about twelve minutes. Answers are given to three decimal places, which is the convention the exam expects.

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 7</span><span>Calculator</span><span>CED 4.5</span></p>

A hot-air balloon rises vertically from a point on level ground 150 feet from an observer. At the instant the balloon is 200 feet above the ground it is rising at 12 feet per second. At what rate is the angle of elevation from the observer to the balloon increasing, in radians per second?

- (A) 0.029
- (B) 0.051
- (C) 0.080
- (D) 1.650

<div class="pr-sol" markdown="1">

**Answer: (A).**

Let $$\theta$$ be the angle of elevation and $$h$$ the height of the balloon. The horizontal distance is fixed at 150, so

$$ \tan\theta=\frac{h}{150}. $$

Differentiating with respect to $$t$$,

$$ \sec^2\theta\,\frac{d\theta}{dt}=\frac{1}{150}\,\frac{dh}{dt}. $$

At the instant in question $$h=200$$, so $$\tan\theta=\tfrac43$$ and

$$ \sec^2\theta=1+\tan^2\theta=1+\frac{16}{9}=\frac{25}{9}. $$

Therefore

$$ \frac{d\theta}{dt}=\frac{12}{150}\cdot\frac{9}{25}=0.0288\ \text{rad/s}. $$

**Where the other options come from.**

- **(B)** uses $$\sin^2\theta$$ where $$\cos^2\theta$$ belongs. The reciprocal of $$\sec^2\theta$$ is $$\cos^2\theta$$, and here $$\cos\theta=0.6$$ rather than $$\sin\theta=0.8$$.
- **(C)** omits $$\sec^2\theta$$ entirely, differentiating $$\tan\theta$$ as though it were $$\theta$$.
- **(D)** is the correct rate reported in degrees per second. The question asks for radians, and a calculator left in degree mode produces this without any warning.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 8</span><span>Calculator</span><span>CED 4.5</span></p>

A trough is 10 feet long. Its vertical cross-sections are isosceles triangles with the vertex down, 3 feet across the top and 2 feet deep. Water is pumped in at 5 cubic feet per minute. At what rate is the water level rising when the water is 1.2 feet deep, in feet per minute?

- (A) 0.139
- (B) 0.167
- (C) 0.278
- (D) 0.333

<div class="pr-sol" markdown="1">

**Answer: (C).**

The surface of the water narrows as the level falls, so the width $$w$$ at depth $$h$$ is not constant. Similar triangles give

$$ \frac{w}{h}=\frac{3}{2}\qquad\Longrightarrow\qquad w=\frac{3}{2}h. $$

The cross-section is a triangle of width $$w$$ and height $$h$$, and the trough is a prism of length 10, so

$$ V=10\cdot\frac{1}{2}wh=10\cdot\frac{1}{2}\left(\frac{3}{2}h\right)h=\frac{15}{2}h^2 . $$

Differentiating and substituting $$dV/dt=5$$ and $$h=1.2$$,

$$ \frac{dV}{dt}=15h\,\frac{dh}{dt}\qquad\Longrightarrow\qquad 5=15(1.2)\,\frac{dh}{dt}\qquad\Longrightarrow\qquad \frac{dh}{dt}=\frac{5}{18}=0.278\ \text{ft/min}. $$

**Where the other options come from.**

- **(A)** omits the factor $$\tfrac12$$ in the area of a triangle.
- **(B)** treats the cross-section as a rectangle of fixed width 3.
- **(D)** keeps the triangle but fixes the width at 3, so the surface never narrows toward the vertex.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 9</span><span>Calculator</span><span>CED 4.5</span></p>

A particle moves along the curve $$y=\sqrt{x}$$. At the instant the particle is at the point $$(4,2)$$, its $$x$$-coordinate is increasing at 3 units per second. At what rate is the distance from the particle to the origin changing at that instant, in units per second?

- (A) 3.019
- (B) 3.750
- (C) 6.037
- (D) 27.000

<div class="pr-sol" markdown="1">

**Answer: (A).**

Let $$D$$ be the distance from the particle to the origin. Squaring first avoids differentiating a square root:

$$ D^2=x^2+y^2=x^2+x, $$

using $$y^2=x$$, which holds along the whole curve and so may be substituted before differentiating.

Differentiate with respect to $$t$$:

$$ 2D\,\frac{dD}{dt}=(2x+1)\,\frac{dx}{dt}. $$

At the given instant $$x=4$$, so $$D=\sqrt{20}$$, and $$dx/dt=3$$:

$$ \frac{dD}{dt}=\frac{(2(4)+1)(3)}{2\sqrt{20}}=\frac{27}{2\sqrt{20}}=3.019\ \text{units/s}. $$

**Where the other options come from.**

- **(B)** adds $$dx/dt$$ and $$dy/dt$$. A distance is not the sum of the coordinates, and its rate is not the sum of their rates.
- **(C)** divides by $$D$$ rather than by $$2D$$, dropping the factor the power rule puts in front of $$D^2$$.
- **(D)** reports $$d(D^2)/dt=27$$, the rate at which the *square* of the distance changes. Squaring to avoid the radical is the right move, and undoing it at the end is the step it costs.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Question 10</span><span>Calculator</span><span>CED 4.5</span></p>

A lighthouse stands 3 kilometers from a long straight shoreline. Its beacon rotates at a constant 4 revolutions per minute. At what rate is the beam moving along the shoreline at the point 4 kilometers from the point on the shore nearest the lighthouse, in kilometers per minute?

- (A) 33.333
- (B) 75.398
- (C) 125.664
- (D) 209.439

<div class="pr-sol" markdown="1">

**Answer: (D).**

Let $$\theta$$ be the angle between the beam and the perpendicular from the lighthouse to the shore, and let $$x$$ be the distance along the shore from that perpendicular foot to the beam. Then

$$ x=3\tan\theta . $$

The rotation rate is given in revolutions, and every derivative of a trigonometric function assumes radians, so convert first:

$$ \frac{d\theta}{dt}=4\ \text{rev/min}=8\pi\ \text{rad/min}. $$

Differentiating and using $$\tan\theta=\tfrac43$$ at $$x=4$$, so that $$\sec^2\theta=\tfrac{25}{9}$$,

$$ \frac{dx}{dt}=3\sec^2\theta\,\frac{d\theta}{dt}=3\cdot\frac{25}{9}\cdot 8\pi=\frac{200\pi}{3}=209.439\ \text{km/min}. $$

**Where the other options come from.**

- **(A)** uses 4 as a rate in radians per minute. One revolution is $$2\pi$$ radians, and the factor of $$2\pi$$ is the most common oversight on any rotating-beam item.
- **(B)** omits $$\sec^2\theta$$.
- **(C)** uses $$\sec\theta$$ where $$\sec^2\theta$$ belongs.

</div>
</div>

## Section II

Two free-response questions, nine rubric points each. Allow about fifteen minutes per question, the same budget the exam gives.

Show the setup. On this archetype the setup is where most of the credit lives, and a correct final number written without a visible relation and a visible differentiation earns very little of it.

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Free response 1</span><span>Calculator</span><span>9 points</span><span>CED 4.4, 4.5</span></p>

A water tank has the shape of an inverted right circular cone with height 12 feet and radius 4 feet at the top. Water is pumped into the tank at a constant rate of 6 cubic feet per minute, and water leaks out through a hole at the bottom at a rate of $$L(t)=0.4\sqrt{t}$$ cubic feet per minute, where $$t$$ is measured in minutes. Let $$h(t)$$ be the depth of the water in the tank, in feet, at time $$t$$.

1. Show that the volume of water in the tank at the moment the depth is $$h$$ feet is $$V=\tfrac{\pi h^3}{27}$$.
2. At time $$t=9$$ minutes the depth of the water is 5 feet. Find the rate at which the depth is changing at that instant. Indicate units of measure.
3. Is the depth of the water increasing or decreasing at $$t=9$$? Give a reason for your answer.
4. Find the time $$t>0$$ at which the water level stops rising. Show the equation that leads to your answer.

<div class="pr-sol" markdown="1">

**Part (a).**

The water in the tank forms a cone similar to the tank itself, so its radius and depth hold a fixed ratio:

$$ \frac{r}{h}=\frac{4}{12}=\frac{1}{3}\qquad\Longrightarrow\qquad r=\frac{h}{3}. $$

Substituting into the volume of a cone,

$$ V=\frac{1}{3}\pi r^2h=\frac{1}{3}\pi\left(\frac{h}{3}\right)^{2}h=\frac{\pi h^3}{27}. $$

**Part (b).**

The volume changes at the rate water enters minus the rate it leaves:

$$ \frac{dV}{dt}=6-0.4\sqrt{t}. $$

At $$t=9$$,

$$ \frac{dV}{dt}=6-0.4(3)=4.8\ \text{ft}^3\!/\text{min}. $$

Differentiating the result of part (a) connects that to the depth:

$$ \frac{dV}{dt}=\frac{\pi h^2}{9}\,\frac{dh}{dt}. $$

At the given instant $$h=5$$, so

$$ 4.8=\frac{25\pi}{9}\,\frac{dh}{dt}\qquad\Longrightarrow\qquad \frac{dh}{dt}=\frac{43.2}{25\pi}=0.550\ \text{ft/min}. $$

**Part (c).**

The depth is increasing. At $$t=9$$ water enters at 6 cubic feet per minute and leaves at 1.2, so $$dV/dt=4.8>0$$. Since $$dh/dt$$ is a positive multiple of $$dV/dt$$, the depth is increasing as well.

**Part (d).**

The level stops rising at the instant the two rates balance:

$$ 6=0.4\sqrt{t}\qquad\Longrightarrow\qquad \sqrt{t}=15\qquad\Longrightarrow\qquad t=225\ \text{minutes}. $$

**Rubric pattern.**

| Part | Points | Earned for |
|---|---|---|
| (a) | 1 | similar triangles giving $$r=h/3$$ |
| (a) | 1 | substitution and simplification to $$\pi h^3/27$$ |
| (b) | 1 | $$dV/dt=6-0.4\sqrt{t}$$, or the value 4.8 |
| (b) | 1 | chain rule: $$dV/dt=\tfrac{\pi h^2}{9}\,dh/dt$$ |
| (b) | 1 | answer 0.550 |
| (b) | 1 | units, feet per minute |
| (c) | 1 | increasing, with a reason resting on the sign of $$dV/dt$$ |
| (d) | 1 | the equation $$6=0.4\sqrt{t}$$ |
| (d) | 1 | $$t=225$$ minutes |

**Where the points go.**

- Reporting 4.8 as the answer to part (b) is the most common loss. It is a rate of volume, and the question asks for a rate of depth.
- The units point in part (b) is free and is lost more often than any computational point on the paper.
- In part (c), *because water is being pumped in* does not earn the point. The tank is also leaking, so the reason has to compare the two rates or cite the sign of their difference.
- Part (d) does not require solving a differential equation. The level stops rising when the net rate is zero, which is an algebraic condition on $$t$$ alone.

</div>
</div>

<div class="pr-item" markdown="1">

<p class="pr-tag"><span>Free response 2</span><span class="pr-nocalc">No calculator</span><span>9 points</span><span>CED 4.5</span></p>

A street lamp is mounted at the top of a pole 18 feet tall. A person 6 feet tall walks away from the base of the pole along a straight path at a constant rate of 5 feet per second. Let $$x$$ be the distance from the base of the pole to the person and let $$s$$ be the length of the person's shadow, both measured in feet at time $$t$$ seconds.

1. Write a proportion relating $$x$$ and $$s$$, and use it to show that $$s=\tfrac{x}{2}$$.
2. Find $$ds/dt$$. Is the shadow lengthening at a constant rate? Give a reason for your answer.
3. Find the rate at which the tip of the shadow moves away from the base of the pole.
4. At the instant $$x=24$$, the person slows to 3 feet per second. Find the rate at which the distance between the person and the top of the pole is changing at that instant.

<div class="pr-sol" markdown="1">

**Part (a).**

The pole and the person are both vertical, and the light travels in a straight line from the top of the pole past the person's head to the tip of the shadow. The two right triangles that result are similar, so corresponding sides are proportional:

$$ \frac{6}{s}=\frac{18}{x+s}. $$

Cross-multiplying and collecting terms,

$$ 6(x+s)=18s\qquad\Longrightarrow\qquad 6x=12s\qquad\Longrightarrow\qquad s=\frac{x}{2}. $$

**Part (b).**

Differentiating the relation from part (a),

$$ \frac{ds}{dt}=\frac{1}{2}\,\frac{dx}{dt}=\frac{1}{2}(5)=\frac{5}{2}\ \text{ft/s}. $$

The shadow lengthens at a constant rate. The relation between $$s$$ and $$x$$ is linear, so $$ds/dt$$ is a fixed multiple of $$dx/dt$$, and $$dx/dt$$ is constant by hypothesis.

**Part (c).**

The tip of the shadow sits at distance $$x+s$$ from the base of the pole, and part (a) gives

$$ x+s=x+\frac{x}{2}=\frac{3}{2}x. $$

Therefore

$$ \frac{d}{dt}(x+s)=\frac{3}{2}\,\frac{dx}{dt}=\frac{3}{2}(5)=\frac{15}{2}\ \text{ft/s}. $$

**Part (d).**

Let $$D$$ be the distance from the person to the top of the pole. The person stands on the ground at horizontal distance $$x$$, and the top of the pole is 18 feet up, so

$$ D^2=x^2+18^2=x^2+324. $$

Differentiating with respect to $$t$$,

$$ 2D\,\frac{dD}{dt}=2x\,\frac{dx}{dt}. $$

At the instant $$x=24$$,

$$ D=\sqrt{576+324}=\sqrt{900}=30, $$

and the speed at that instant is $$dx/dt=3$$, so

$$ \frac{dD}{dt}=\frac{x}{D}\,\frac{dx}{dt}=\frac{24(3)}{30}=\frac{12}{5}\ \text{ft/s}. $$

**Rubric pattern.**

| Part | Points | Earned for |
|---|---|---|
| (a) | 1 | a correct proportion from similar triangles |
| (a) | 1 | algebra reaching $$s=x/2$$ |
| (b) | 1 | $$ds/dt=5/2$$ feet per second |
| (b) | 1 | constant, with a reason naming the linear relation |
| (c) | 1 | identifying the tip as $$x+s$$ |
| (c) | 1 | answer $$15/2$$ feet per second |
| (d) | 1 | $$D^2=x^2+324$$ |
| (d) | 1 | implicit differentiation with respect to $$t$$ |
| (d) | 1 | answer $$12/5$$ feet per second |

**Where the points go.**

- Part (c) answered with $$ds/dt$$ earns nothing. The shadow lengthens at $$5/2$$ while its tip moves at $$15/2$$, and the difference is exactly the person's own speed. Reading the question for *which* quantity is moving is the whole task.
- In part (d), 18 is a constant, not a variable. Differentiating it as though the pole were growing is a fast way to lose the second point.
- Part (b) asks two things, a value and a judgment with a reason. A number alone earns one point of the two.
- The change of speed in part (d) applies only to that instant. Nothing computed in parts (b) and (c) needs revisiting, and a solution that recomputes them has misread the question rather than made an error.

</div>
</div>

<div class="article-note" markdown="1">

Every value on this page was recomputed independently before publication, including each incorrect option, so that the error named beneath a distractor is the error that actually produces it.

Related rates appear on the free-response section roughly every other year and in Part A of Section I most years. When the archetype does appear on Section II it usually carries the tank or the similar-triangle geometry above, and it almost always includes a units point and a justification point.

</div>
