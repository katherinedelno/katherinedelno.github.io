---
layout: page
title: Are you ready for AP Calculus?
permalink: /ap-calculus-readiness/
description: "Sixteen questions covering the algebra, functions, trigonometry, and logarithms that AP Calculus assumes. Results are organized by area so you can see which skills are secure and which are worth reviewing before the course begins."
math: true
image: "/assets/og/readiness-calculus.png"
---

<style>
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;--faint:#9a9a97;color:var(--ink);line-height:1.6}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .7rem}

  .dg-hero{max-width:62ch;margin:0 0 2.2rem}
  .dg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .7rem;letter-spacing:-.02em;font-weight:700}
  .dg-hero p{font-size:1.06rem;color:var(--muted);line-height:1.6;margin:0 0 1rem}

  .dg-panel{border:1px solid var(--line);border-radius:12px;padding:28px 30px;max-width:70ch;background:#fff}
  .dg-panel h2{font-size:1.2rem;font-weight:700;letter-spacing:-.015em;margin:0 0 .9rem}
  .dg-facts{list-style:none;margin:0 0 1.4rem;padding:0}
  .dg-facts li{font-size:.94rem;color:var(--muted);padding:7px 0;border-bottom:1px solid var(--line);display:flex;gap:14px}
  .dg-facts li:last-child{border-bottom:none}
  .dg-facts b{color:var(--ink);font-weight:700;flex:0 0 8.5rem}

  .dg-btn{font:inherit;font-size:.9rem;font-weight:700;letter-spacing:.03em;padding:12px 24px;border:1px solid var(--ink);border-radius:8px;background:var(--ink);color:#fff;cursor:pointer}
  .dg-btn:hover{background:#000;border-color:#000}
  .dg-btn:disabled{background:#c9c9c9;border-color:#c9c9c9;cursor:not-allowed}
  .dg-btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .dg-btn-outline{font:inherit;font-size:.88rem;font-weight:700;padding:11px 20px;border:1px solid var(--line);border-radius:8px;background:none;color:var(--ink);cursor:pointer}
  .dg-btn-outline:hover{border-color:var(--ink)}

  .dg-quiz{display:none;max-width:70ch}
  .dg-quiz.is-on{display:block}

  .dg-bar{height:2px;background:var(--line);border-radius:2px;overflow:hidden;margin:0 0 1.5rem}
  .dg-bar i{display:block;height:100%;background:var(--ink);width:0;transition:width .25s ease}
  .dg-status{display:flex;justify-content:space-between;align-items:baseline;font-size:.72rem;text-transform:uppercase;letter-spacing:.13em;font-weight:700;color:var(--faint);margin:0 0 .6rem}
  .dg-status .dg-part{color:var(--accent)}

  .dg-q{font-size:1.2rem;line-height:1.5;font-weight:600;margin:0 0 1.5rem;letter-spacing:-.01em}
  .dg-opts{list-style:none;margin:0 0 1.5rem;padding:0;display:grid;gap:9px}
  .dg-opt{width:100%;text-align:left;font:inherit;font-size:1rem;line-height:1.5;padding:14px 17px;border:1px solid var(--line);border-radius:9px;background:#fff;color:var(--ink);cursor:pointer;transition:border-color .12s ease}
  .dg-opt:hover{border-color:var(--accent)}
  .dg-opt:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .dg-opt.is-picked{border-color:var(--ink);background:var(--accent-soft)}
  .dg-nav{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
  .dg-skip{font:inherit;font-size:.86rem;color:var(--muted);background:none;border:none;text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--faint);cursor:pointer;padding:6px 2px}
  .dg-skip:hover{color:var(--ink)}

  .dg-res{display:none;max-width:72ch}
  .dg-res.is-on{display:block}
  .dg-score{border-top:1px solid var(--ink);border-bottom:1px solid var(--line);padding:26px 0 24px;margin:0 0 2rem}
  .dg-score .dg-num{font-size:3.1rem;font-weight:700;letter-spacing:-.03em;line-height:1;margin:0 0 .5rem}
  .dg-score .dg-num small{font-size:1.3rem;font-weight:600;color:var(--faint);letter-spacing:0}
  .dg-score h2{font-size:1.35rem;font-weight:700;letter-spacing:-.02em;margin:0 0 .5rem}
  .dg-score p{font-size:1rem;color:var(--muted);margin:0;max-width:62ch;line-height:1.6}

  .dg-part-row{border-bottom:1px solid var(--line);padding:20px 0}
  .dg-part-row:last-of-type{border-bottom:none}
  .dg-part-head{display:flex;justify-content:space-between;align-items:baseline;gap:16px;margin:0 0 .5rem}
  .dg-part-head h3{font-size:1.03rem;font-weight:700;margin:0;letter-spacing:-.01em}
  .dg-part-head span{font-size:.78rem;font-weight:700;color:var(--faint);letter-spacing:.06em;white-space:nowrap}
  .dg-meter{height:6px;background:var(--accent-soft);border-radius:3px;overflow:hidden;margin:0 0 .7rem}
  .dg-meter i{display:block;height:100%;background:var(--ink)}
  .dg-part-row p{font-size:.92rem;color:var(--muted);line-height:1.6;margin:0 0 .5rem;max-width:62ch}
  .dg-part-row .dg-links{font-size:.88rem;margin:0}
  .dg-part-row .dg-links a{color:var(--ink);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;text-decoration-color:var(--faint)}
  .dg-part-row .dg-links a:hover{text-decoration-color:var(--ink)}

  .dg-review{margin-top:2.4rem}
  .dg-review h2{font-size:1.2rem;font-weight:700;letter-spacing:-.015em;margin:0 0 .3rem}
  .dg-review>p{font-size:.93rem;color:var(--muted);margin:0 0 1.2rem;max-width:62ch}
  .dg-item{border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:0 0 10px}
  .dg-item.is-right{background:var(--card)}
  .dg-item .dg-item-q{font-size:.98rem;font-weight:600;margin:0 0 .6rem;line-height:1.5}
  .dg-item .dg-item-v{font-size:.9rem;color:var(--muted);margin:0 0 .35rem;line-height:1.55}
  .dg-item .dg-item-v b{color:var(--ink);font-weight:700}
  .dg-item .dg-why{font-size:.9rem;color:var(--muted);line-height:1.6;margin:.55rem 0 0;padding-top:.55rem;border-top:1px solid var(--line)}
  .dg-tag{display:inline-block;font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--faint);margin:0 0 .5rem}

  .dg-actions{margin-top:2rem;display:flex;gap:10px;flex-wrap:wrap}
  .dg-note{margin-top:2.6rem;padding:22px 24px;background:var(--card);border:1px solid var(--line);border-radius:12px;font-size:.95rem;line-height:1.6;max-width:70ch}
  .dg-note p{margin:0 0 .7rem}
  .dg-note p:last-child{margin:0}
  .dg-note a{color:var(--ink);text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--faint)}

  @media (max-width:640px){
    .dg-hero h1{font-size:1.7rem}
    .dg-panel{padding:20px 18px}
    .dg-facts li{flex-direction:column;gap:2px}
    .dg-facts b{flex:none}
    .dg-q{font-size:1.08rem}
    .dg-score .dg-num{font-size:2.4rem}
  }
  @media (prefers-reduced-motion:reduce){.dg-bar i,.dg-opt{transition:none}}
</style>

<div class="pg" markdown="0">

  <div class="dg-hero">
    <p class="label">Diagnostic</p>
    <h1>Are you ready for AP Calculus?</h1>
    <p>Calculus depends on a large amount of algebra, function work, trigonometry, and logarithms that the course generally assumes are already familiar.</p>
    <p>This diagnostic contains sixteen questions in those prerequisite skills. It is designed to identify specific areas that may be worth reviewing before the course begins.</p>
    <p>There is no grade.</p>
  </div>

  <div class="dg-panel" id="dg-start">
    <h2>Before you begin</h2>
    <ul class="dg-facts">
      <li><b>Length</b> <span>16 questions, four in each topic area. About 15 minutes.</span></li>
      <li><b>Calculator</b> <span>None. Every answer is exact.</span></li>
      <li><b>Skipping</b> <span>Allowed. A skipped question is treated as useful information rather than forced into a guess.</span></li>
      <li><b>Results</b> <span>Immediate, with a breakdown by area and an explanation for every question.</span></li>
      <li><b>Privacy</b> <span>Everything runs in your browser. Nothing from the diagnostic is recorded or sent anywhere.</span></li>
    </ul>
    <button type="button" class="dg-btn" id="dg-begin">Begin the diagnostic</button>
  </div>

  <div class="dg-quiz" id="dg-quiz">
    <div class="dg-bar"><i id="dg-fill"></i></div>
    <p class="dg-status"><span id="dg-count"></span><span class="dg-part" id="dg-partname"></span></p>
    <p class="dg-q" id="dg-prompt"></p>
    <ul class="dg-opts" id="dg-opts"></ul>
    <div class="dg-nav">
      <button type="button" class="dg-btn" id="dg-next" disabled>Next</button>
      <button type="button" class="dg-skip" id="dg-skip">Skip this one</button>
    </div>
  </div>

  <div class="dg-res" id="dg-res">
    <div class="dg-score">
      <p class="dg-num" id="dg-num"></p>
      <h2 id="dg-band"></h2>
      <p id="dg-verdict"></p>
    </div>

    <div id="dg-parts"></div>

    <div class="dg-review">
      <h2>Every question, and what each answer meant</h2>
      <p>The incorrect choices are deliberate. Each corresponds to a mistake that commonly appears in this material.</p>
      <p>Reviewing the answer choices can therefore tell you more than the total score alone. It can show whether the issue came from algebra, notation, a remembered rule, or the way the problem was interpreted.</p>
      <div id="dg-items"></div>
    </div>

    <div class="dg-actions">
      <button type="button" class="dg-btn-outline" id="dg-again">Take it again</button>
    </div>

    {% include subscribe.html
       heading="A review plan for what you missed"
       blurb="This is the shorter version of the readiness diagnostic I use with my own students. Each topic area has additional review material behind it. || If you would like the AP Calculus getting-started guide, leave an email address below. It covers course setup, notation, and several early habits that are useful before the term begins."
       button="Send the guide"
       done="Thank you. I'll send the AP Calculus getting-started guide to that address shortly." 
       course="AP Calculus" %}

    <div class="dg-note">
      <p>Sixteen questions cannot measure every prerequisite skill. A low score in one area is not a conclusion about whether you can succeed in calculus.</p>
      <p>The useful part of the result is its specificity. If several missed questions point to the same algebraic or trigonometric skill, that gives you something concrete to review before the course begins.</p>
      <p>If you would like help working through what the diagnostic found, you can read about <a href="{{ "/private-instruction/" | relative_url }}">private instruction &amp; rates</a> or write to <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>.</p>
    </div>
  </div>

</div>

<script>
(function(){
  "use strict";

  // Each item carries the misconception behind every wrong option. The review
  // screen shows the explanation for the option actually chosen, so the feedback
  // names the specific error rather than restating the correct method.
  var PARTS = {
    A: {
      name: "Algebra fluency",
      why: "Factoring and rational simplification are what limit evaluation and derivative cleanup are made of. A limit that looks like 0/0 is almost always asking you to factor and cancel; if that step is slow or uncertain, every limit problem in the first unit costs you time you don't have.",
      links: [
        ["Indeterminate forms and the algebra that resolves them", "/2026/07/30/indeterminate-forms.html"],
        ["The derivative as a limit", "/2026/07/30/derivative-as-a-limit.html"]
      ]
    },
    B: {
      name: "Functions",
      why: "Composition is the Chain Rule wearing a different hat, and the difference quotient is the definition of the derivative. Students who cannot see which function sits inside another will meet that same difficulty again in every chain rule, every related rate, and every substitution.",
      links: [
        ["Functions inside functions", "/2026/07/30/functions-inside-functions.html"],
        ["The chain rule, layer by layer", "/2026/07/30/chain-rule-reading-the-layers.html"]
      ]
    },
    C: {
      name: "Trigonometry",
      why: "Unit-circle values are never the point of a calculus problem and are never awarded credit, which is exactly why they are dangerous: they appear inside trig derivatives, motion problems, and integrals as unremarked-on arithmetic, and a wrong value quietly ruins a problem you otherwise did correctly.",
      links: [
        ["The unit circle and the sine curve", "/2026/07/25/unit-circle-unrolled.html"]
      ]
    },
    D: {
      name: "Exponentials, logarithms, and lines",
      why: "Log and exponential algebra runs every growth and decay model, point-slope form is the tangent line, and average rate of change is the seed of the Mean Value Theorem. These look like leftovers from precalculus right up until the moment they are the whole problem.",
      links: [
        ["Logarithms undo exponentials", "/2026/07/30/logarithms-undo-exponentials.html"],
        ["Two existence theorems, and what they refuse to tell you", "/2026/07/30/mean-value-and-extreme-value-theorems.html"]
      ]
    }
  };

  var Q = [
    { part:"A", prompt:"Factor completely: \\(2x^{3}-8x\\)",
      opts:[
        ["\\(2x(x-2)(x+2)\\)", "Correct. Greatest common factor first, then the difference of squares. Stopping one step early is the most common way to lose this one."],
        ["\\(2x(x^{2}-4)\\)", "You pulled out the GCF correctly and then stopped. \\(x^{2}-4\\) is a difference of squares and still factors, and \"completely\" means going until nothing else will."],
        ["\\(2x(x-2)^{2}\\)", "This is the perfect-square pattern, not the difference of squares. \\(x^{2}-4\\) factors as \\((x-2)(x+2)\\); \\((x-2)^{2}\\) would expand to \\(x^{2}-4x+4\\)."],
        ["\\((2x-4)(x+2)\\)", "Check by expanding: this gives \\(2x^{2}-8\\), not \\(2x^{3}-8x\\). The factor of \\(x\\) in the GCF got absorbed incorrectly."]
      ], ans:0 },

    { part:"A", prompt:"Simplify: \\(\\dfrac{\\tfrac{1}{x}-\\tfrac{1}{3}}{x-3}\\)",
      opts:[
        ["\\(-\\dfrac{1}{3x}\\)", "Correct, and the sign is the whole difficulty. The numerator becomes \\(\\frac{3-x}{3x}\\), and \\(3-x=-(x-3)\\) is what lets the cancellation happen."],
        ["\\(\\dfrac{1}{3x}\\)", "Everything but the sign. \\(\\frac{1}{x}-\\frac{1}{3}=\\frac{3-x}{3x}\\), and \\(3-x\\) is the negative of \\(x-3\\), so cancelling leaves a factor of \\(-1\\) behind."],
        ["\\(\\dfrac{3-x}{3x(x-3)}\\)", "This is correct algebra, stopped before the simplification. Rewriting \\(3-x\\) as \\(-(x-3)\\) lets the \\((x-3)\\) cancel, which is the entire point of the problem."],
        ["\\(\\dfrac{1}{x-3}\\)", "Something was cancelled that isn't a factor of the whole numerator. Complex fractions have to be combined into a single fraction before anything can cancel."]
      ], ans:0 },

    { part:"A", prompt:"Rewrite as a single power of \\(x\\): \\(\\dfrac{1}{x^{2}\\sqrt{x}}\\)",
      opts:[
        ["\\(x^{-5/2}\\)", "Correct. \\(x^{2}\\cdot x^{1/2}=x^{5/2}\\), and the reciprocal negates the exponent. This rewriting comes before every Power Rule derivative."],
        ["\\(x^{5/2}\\)", "The exponent arithmetic is right, but the expression is a reciprocal. Moving \\(x^{5/2}\\) from the denominator to the numerator changes the sign of the exponent."],
        ["\\(x^{-3/2}\\)", "The exponents were subtracted rather than added. \\(x^{2}\\cdot x^{1/2}\\) adds them: \\(2+\\frac12=\\frac52\\)."],
        ["\\(x^{-2}\\sqrt{x}\\)", "Half converted. The radical also needs to become a power, and it is in the denominator, so it contributes \\(-\\frac12\\) rather than \\(+\\frac12\\)."]
      ], ans:0 },

    { part:"A", prompt:"Solve, writing the answer as an interval: \\(\\lvert 2x-1\\rvert<5\\)",
      opts:[
        ["\\((-2,\\,3)\\)", "Correct. The inequality becomes \\(-5<2x-1<5\\), and isolating \\(x\\) gives \\(-2<x<3\\)."],
        ["\\((-3,\\,2)\\)", "The endpoints are swapped in sign. From \\(-5<2x-1<5\\), adding 1 gives \\(-4<2x<6\\), then dividing by 2 gives \\(-2<x<3\\)."],
        ["\\((-\\infty,-2)\\cup(3,\\infty)\\)", "This is the solution to \\(\\lvert 2x-1\\rvert>5\\). A \"less than\" absolute value gives one interval between two bounds; \"greater than\" gives two pieces going outward."],
        ["\\([-2,\\,3]\\)", "The endpoints are right but the brackets are not. The inequality is strict, so neither endpoint is included."]
      ], ans:0 },

    { part:"B", prompt:"If \\(f(x)=x^{2}-3x\\), find and simplify \\(f(a+1)\\).",
      opts:[
        ["\\(a^{2}-a-2\\)", "Correct. \\((a+1)^{2}-3(a+1)=a^{2}+2a+1-3a-3\\), which collects to \\(a^{2}-a-2\\)."],
        ["\\(a^{2}-3a-2\\)", "\\((a+1)^{2}\\) was expanded as \\(a^{2}+1\\). Squaring a binomial produces a middle term: \\((a+1)^{2}=a^{2}+2a+1\\)."],
        ["\\(a^{2}-a+4\\)", "The \\(-3\\) was not distributed across both terms. \\(-3(a+1)=-3a-3\\), so the constant is \\(1-3=-2\\)."],
        ["\\(a^{2}+2a-2\\)", "The \\(-3a\\) never made it into the collection. After expanding, the \\(a\\) terms are \\(2a\\) and \\(-3a\\), which combine to \\(-a\\)."]
      ], ans:0 },

    { part:"B", prompt:"If \\(f(x)=2x+1\\) and \\(g(x)=x^{2}\\), find \\(f\\big(g(x)\\big)\\) and \\(g\\big(f(x)\\big)\\).",
      opts:[
        ["\\(2x^{2}+1\\) and \\((2x+1)^{2}\\)", "Correct. Work outside-in: \\(f\\) acts on \\(x^{2}\\), and \\(g\\) squares all of \\(2x+1\\). Recognising which function sits inside is the whole Chain Rule."],
        ["\\((2x+1)^{2}\\) and \\(2x^{2}+1\\)", "The two are reversed. In \\(f(g(x))\\), \\(g\\) is the inside function, so \\(x^{2}\\) is what gets substituted into \\(f\\)."],
        ["\\(2x^{2}+1\\) for both", "Composition is not commutative. \\(f(g(x))\\) and \\(g(f(x))\\) are different functions except in special cases, and telling them apart is exactly what the Chain Rule requires."],
        ["\\(2x^{3}+x^{2}\\)", "This is the product \\(f(x)\\cdot g(x)\\). Composition substitutes one function into the other rather than multiplying them."]
      ], ans:0 },

    { part:"B", prompt:"Give the domain of \\(f(x)=\\dfrac{\\sqrt{6-2x}}{x-1}\\).",
      opts:[
        ["\\((-\\infty,1)\\cup(1,3]\\)", "Correct. The radicand needs \\(6-2x\\ge 0\\), so \\(x\\le 3\\), and the denominator needs \\(x\\ne 1\\)."],
        ["\\((-\\infty,\\,3]\\)", "The radical was handled correctly and the denominator was forgotten. \\(x=1\\) makes the denominator zero and has to be removed."],
        ["\\((-\\infty,1)\\cup(1,3)\\)", "The excluded point is right but the endpoint is not. At \\(x=3\\) the radicand is exactly 0, which is allowed; \\(\\sqrt{0}=0\\)."],
        ["\\((1,\\,3]\\)", "Only the piece to the right of 1 was kept. Nothing rules out negative \\(x\\) here; \\(6-2x\\) only grows as \\(x\\) decreases."]
      ], ans:0 },

    { part:"B", prompt:"For \\(f(x)=x^{2}\\), simplify \\(\\dfrac{f(x+h)-f(x)}{h}\\) completely.",
      opts:[
        ["\\(2x+h\\)", "Correct. \\((x+h)^{2}-x^{2}=2xh+h^{2}\\), and dividing by \\(h\\) leaves \\(2x+h\\). This is the difference quotient behind the definition of the derivative."],
        ["\\(2x\\)", "That is the limit as \\(h\\to 0\\), not the simplification. The question asks for the expression before the limit is taken, and the leftover \\(h\\) is what makes the limit interesting."],
        ["\\(2x+h^{2}\\)", "The \\(h^{2}\\) term was not divided. Every term in the numerator is divided by \\(h\\), so \\(h^{2}/h=h\\)."],
        ["\\(h\\)", "The \\(2xh\\) term went missing. Expanding \\((x+h)^{2}\\) gives \\(x^{2}+2xh+h^{2}\\); the \\(x^{2}\\) cancels but the \\(2xh\\) does not."]
      ], ans:0 },

    { part:"C", prompt:"Give exact values: \\(\\sin\\dfrac{\\pi}{3}\\) and \\(\\cos\\dfrac{3\\pi}{4}\\).",
      opts:[
        ["\\(\\dfrac{\\sqrt3}{2}\\) and \\(-\\dfrac{\\sqrt2}{2}\\)", "Correct. \\(\\frac{3\\pi}{4}\\) is in the second quadrant, where cosine is negative."],
        ["\\(\\dfrac{\\sqrt3}{2}\\) and \\(\\dfrac{\\sqrt2}{2}\\)", "The magnitude is right and the sign is not. \\(\\frac{3\\pi}{4}\\) sits in the second quadrant, where \\(x\\)-coordinates, and therefore cosines, are negative."],
        ["\\(\\dfrac{1}{2}\\) and \\(-\\dfrac{\\sqrt2}{2}\\)", "Sine and cosine are swapped at \\(\\frac{\\pi}{3}\\). \\(\\sin\\frac{\\pi}{3}=\\frac{\\sqrt3}{2}\\) and \\(\\cos\\frac{\\pi}{3}=\\frac12\\)."],
        ["\\(\\dfrac{\\sqrt3}{2}\\) and \\(-\\dfrac{1}{2}\\)", "The reference angle for \\(\\frac{3\\pi}{4}\\) is \\(\\frac{\\pi}{4}\\), not \\(\\frac{\\pi}{3}\\), so the value is \\(\\frac{\\sqrt2}{2}\\) in magnitude."]
      ], ans:0 },

    { part:"C", prompt:"Solve on \\([0,2\\pi)\\): \\(\\cos x=-\\dfrac12\\)",
      opts:[
        ["\\(x=\\dfrac{2\\pi}{3},\\ \\dfrac{4\\pi}{3}\\)", "Correct. Cosine is negative in the second and third quadrants, and the reference angle is \\(\\frac{\\pi}{3}\\)."],
        ["\\(x=\\dfrac{\\pi}{3},\\ \\dfrac{5\\pi}{3}\\)", "These are the solutions to \\(\\cos x=+\\frac12\\). The negative sign moves the answers to the quadrants where cosine is negative."],
        ["\\(x=\\dfrac{2\\pi}{3},\\ \\dfrac{5\\pi}{3}\\)", "The first is right and the second is not. Both solutions must have cosine negative, and \\(\\frac{5\\pi}{3}\\) is in the fourth quadrant, where cosine is positive."],
        ["\\(x=\\dfrac{5\\pi}{6},\\ \\dfrac{7\\pi}{6}\\)", "The right quadrants, the wrong reference angle. These are the solutions to \\(\\cos x=-\\frac{\\sqrt3}{2}\\); for \\(-\\frac12\\) the reference angle is \\(\\frac{\\pi}{3}\\)."]
      ], ans:0 },

    { part:"C", prompt:"Simplify to a single trig function: \\(1+\\tan^{2}\\theta\\)",
      opts:[
        ["\\(\\sec^{2}\\theta\\)", "Correct. Divide \\(\\sin^{2}\\theta+\\cos^{2}\\theta=1\\) through by \\(\\cos^{2}\\theta\\). This identity is the derivative of \\(\\tan x\\) in disguise."],
        ["\\(\\csc^{2}\\theta\\)", "That is \\(1+\\cot^{2}\\theta\\). The two companion identities are easy to swap: tangent pairs with secant, cotangent with cosecant."],
        ["\\(\\sec\\theta\\)", "The exponent went missing. Dividing \\(\\sin^{2}\\theta+\\cos^{2}\\theta=1\\) by \\(\\cos^{2}\\theta\\) leaves squares throughout."],
        ["\\(1+\\cot^{2}\\theta\\)", "This is a different identity, equal to \\(\\csc^{2}\\theta\\), not to \\(1+\\tan^{2}\\theta\\)."]
      ], ans:0 },

    { part:"C", prompt:"The acute angle \\(\\theta\\) has \\(\\sin\\theta=\\dfrac35\\). Find \\(\\cos\\theta\\) and \\(\\tan\\theta\\).",
      opts:[
        ["\\(\\cos\\theta=\\dfrac45,\\ \\tan\\theta=\\dfrac34\\)", "Correct. Opposite 3, hypotenuse 5, so the adjacent side is 4. This build-the-triangle move is how related rates and inverse-trig derivatives get evaluated."],
        ["\\(\\cos\\theta=\\dfrac45,\\ \\tan\\theta=\\dfrac43\\)", "The cosine is right and the tangent is inverted. Tangent is opposite over adjacent, so \\(\\frac{3}{4}\\)."],
        ["\\(\\cos\\theta=\\dfrac54,\\ \\tan\\theta=\\dfrac34\\)", "The cosine is inverted. Cosine is adjacent over hypotenuse, and the hypotenuse is the largest side, so cosine of an acute angle can never exceed 1."],
        ["\\(\\cos\\theta=\\dfrac53,\\ \\tan\\theta=\\dfrac34\\)", "The 5 and the 3 were read as adjacent and hypotenuse. Here 3 is opposite and 5 is the hypotenuse, so the missing adjacent side is 4."]
      ], ans:0 },

    { part:"D", prompt:"Write as a single logarithm: \\(2\\ln x-\\ln y\\)",
      opts:[
        ["\\(\\ln\\dfrac{x^{2}}{y}\\)", "Correct. The coefficient becomes an exponent, and a difference of logs becomes a quotient."],
        ["\\(\\ln\\dfrac{2x}{y}\\)", "The coefficient was treated as a factor. A number in front of a log becomes an exponent inside it: \\(2\\ln x=\\ln x^{2}\\)."],
        ["\\(\\ln(x^{2}y)\\)", "Subtraction became multiplication. A difference of logs is the log of a quotient; a sum would be the product."],
        ["\\(2\\ln\\dfrac{x}{y}\\)", "The coefficient cannot be factored out across the subtraction, because it only multiplies the first term."]
      ], ans:0 },

    { part:"D", prompt:"Solve exactly: \\(e^{2x}=7\\)",
      opts:[
        ["\\(x=\\dfrac{\\ln 7}{2}\\)", "Correct. Taking the natural log of both sides gives \\(2x=\\ln 7\\). Leave it exact; this is the standard form in exponential-model problems."],
        ["\\(x=\\ln\\dfrac{7}{2}\\)", "The division happened inside the logarithm. \\(2x=\\ln 7\\) is divided by 2 outside: \\(\\frac{\\ln 7}{2}\\), which is not \\(\\ln\\frac72\\)."],
        ["\\(x=2\\ln 7\\)", "Multiplied where you needed to divide. From \\(2x=\\ln 7\\), dividing both sides by 2 isolates \\(x\\)."],
        ["\\(x=\\ln 7-\\ln 2\\)", "This equals \\(\\ln\\frac72\\), which comes from treating the 2 as inside the log rather than as a coefficient of \\(x\\)."]
      ], ans:0 },

    { part:"D", prompt:"Solve: \\(\\log_{2}(x-1)=3\\)",
      opts:[
        ["\\(x=9\\)", "Correct. In exponential form, \\(x-1=2^{3}=8\\), so \\(x=9\\)."],
        ["\\(x=7\\)", "Right up to the last step: \\(x-1=8\\) gives \\(x=8+1=9\\), not \\(8-1\\)."],
        ["\\(x=6\\)", "The base and the exponent were multiplied rather than raised. \\(\\log_{2}(x-1)=3\\) means \\(2^{3}=x-1\\), not \\(2\\cdot 3\\)."],
        ["\\(x=4\\)", "The logarithm was never undone. Converting to exponential form is the move: \\(\\log_b A=c\\) means \\(b^{c}=A\\)."]
      ], ans:0 },

    { part:"D", prompt:"Find the average rate of change of \\(f(x)=x^{2}\\) on \\([1,4]\\).",
      opts:[
        ["\\(5\\)", "Correct. \\(\\frac{f(4)-f(1)}{4-1}=\\frac{16-1}{3}=5\\). This is the slope of the secant line, and the seed of the Mean Value Theorem."],
        ["\\(15\\)", "The numerator without the denominator. Average rate of change is a slope, so the change in \\(f\\) is divided by the change in \\(x\\)."],
        ["\\(\\dfrac{17}{3}\\)", "The function values were added rather than subtracted. The numerator is \\(f(4)-f(1)\\)."],
        ["\\(\\dfrac{1}{5}\\)", "The fraction is inverted: \\(\\frac{\\Delta x}{\\Delta f}\\) rather than \\(\\frac{\\Delta f}{\\Delta x}\\). Rate of change is always output over input."]
      ], ans:0 }
  ];

  // Shuffle each item's options once at load, keeping track of where the correct
  // one lands, so the answer is never sitting in the same position every time.
  Q.forEach(function(q){
    var tagged = q.opts.map(function(o, i){ return {o:o, right: i === q.ans}; });
    for (var i = tagged.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = tagged[i]; tagged[i] = tagged[j]; tagged[j] = t;
    }
    q.opts = tagged.map(function(t){ return t.o; });
    q.ans = tagged.findIndex(function(t){ return t.right; });
  });

  var el = function(id){ return document.getElementById(id); };
  var start = el("dg-start"), quiz = el("dg-quiz"), res = el("dg-res");
  var picks = new Array(Q.length).fill(null);
  var at = 0, chosen = null;

  function typeset(node){
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([node]).catch(function(){});
    }
  }

  function render(){
    var q = Q[at];
    el("dg-fill").style.width = ((at / Q.length) * 100) + "%";
    el("dg-count").textContent = "Question " + (at + 1) + " of " + Q.length;
    el("dg-partname").textContent = PARTS[q.part].name;
    el("dg-prompt").innerHTML = q.prompt;

    var list = el("dg-opts");
    list.innerHTML = "";
    q.opts.forEach(function(opt, i){
      var li = document.createElement("li");
      var b = document.createElement("button");
      b.type = "button";
      b.className = "dg-opt";
      b.innerHTML = opt[0];
      b.setAttribute("aria-pressed", "false");
      b.addEventListener("click", function(){
        chosen = i;
        Array.prototype.forEach.call(list.querySelectorAll(".dg-opt"), function(x){
          x.classList.remove("is-picked");
          x.setAttribute("aria-pressed", "false");
        });
        b.classList.add("is-picked");
        b.setAttribute("aria-pressed", "true");
        el("dg-next").disabled = false;
      });
      li.appendChild(b);
      list.appendChild(li);
    });

    chosen = null;
    el("dg-next").disabled = true;
    el("dg-next").textContent = (at === Q.length - 1) ? "See results" : "Next";
    typeset(quiz);
  }

  function advance(){
    picks[at] = chosen;
    if (at === Q.length - 1) { finish(); return; }
    at++;
    render();
    quiz.scrollIntoView({behavior:"smooth", block:"start"});
  }

  function finish(){
    quiz.classList.remove("is-on");
    res.classList.add("is-on");

    var right = 0, byPart = {A:[0,0], B:[0,0], C:[0,0], D:[0,0]};
    Q.forEach(function(q, i){
      byPart[q.part][1]++;
      if (picks[i] !== null && picks[i] === q.ans) { right++; byPart[q.part][0]++; }
    });

    el("dg-num").innerHTML = right + " <small>of " + Q.length + "</small>";

    // Bands scaled from the thirty-item version of this diagnostic.
    var band, verdict;
    if (right >= 14) {
      band = "Ready";
      verdict = "The prerequisites are in place. Start the course on schedule, and treat anything you missed below as a warm-up rather than a project.";
    } else if (right >= 11) {
      band = "Ready, with specific gaps";
      verdict = "Enough is secure to start on time. The areas scoring lowest below are worth a few focused hours before the course reaches them, which it will do within weeks.";
    } else if (right >= 8) {
      band = "Review first";
      verdict = "There is real ground to make up, and it is much cheaper to make it up now than during the term. Two or three sessions on the weakest areas below would change how the first unit goes.";
    } else {
      band = "Structured review";
      verdict = "The gaps here are broad enough that starting calculus without closing them would make the course harder than it needs to be. This is common, it is not a verdict about ability, and a structured review over a few weeks addresses most of it.";
    }
    el("dg-band").textContent = band;
    el("dg-verdict").textContent = verdict;

    var wrap = el("dg-parts");
    wrap.innerHTML = "";
    ["A","B","C","D"].forEach(function(k){
      var got = byPart[k][0], tot = byPart[k][1], p = PARTS[k];
      var row = document.createElement("div");
      row.className = "dg-part-row";
      row.innerHTML =
        '<div class="dg-part-head"><h3>' + p.name + '</h3><span>' + got + ' / ' + tot + '</span></div>' +
        '<div class="dg-meter"><i style="width:' + ((got / tot) * 100) + '%"></i></div>' +
        '<p>' + p.why + '</p>' +
        (got < tot
          ? '<p class="dg-links">Worth reading: ' + p.links.map(function(l){
              return '<a href="' + l[1] + '">' + l[0] + '</a>';
            }).join(", ") + '.</p>'
          : '');
      wrap.appendChild(row);
    });

    var items = el("dg-items");
    items.innerHTML = "";
    Q.forEach(function(q, i){
      var pick = picks[i];
      var ok = pick !== null && pick === q.ans;
      var d = document.createElement("div");
      d.className = "dg-item" + (ok ? " is-right" : "");
      var yours = pick === null
        ? '<p class="dg-item-v"><b>Skipped.</b> The answer is ' + q.opts[q.ans][0] + '.</p>'
        : '<p class="dg-item-v"><b>' + (ok ? "Correct" : "You chose") + ':</b> ' + q.opts[pick][0] +
          (ok ? '' : '<br><b>Answer:</b> ' + q.opts[q.ans][0]) + '</p>';
      d.innerHTML =
        '<p class="dg-tag">' + PARTS[q.part].name + ' &middot; Question ' + (i + 1) + '</p>' +
        '<p class="dg-item-q">' + q.prompt + '</p>' + yours +
        '<p class="dg-why">' + (pick === null ? q.opts[q.ans][1] : q.opts[pick][1]) + '</p>';
      items.appendChild(d);
    });

    typeset(res);
    res.scrollIntoView({behavior:"smooth", block:"start"});
  }

  el("dg-begin").addEventListener("click", function(){
    start.style.display = "none";
    quiz.classList.add("is-on");
    render();
  });
  el("dg-next").addEventListener("click", advance);
  el("dg-skip").addEventListener("click", function(){ chosen = null; advance(); });
  el("dg-again").addEventListener("click", function(){
    picks = new Array(Q.length).fill(null);
    at = 0;
    res.classList.remove("is-on");
    quiz.classList.add("is-on");
    render();
    document.querySelector(".dg-hero").scrollIntoView({behavior:"smooth", block:"start"});
  });
})();
</script>
