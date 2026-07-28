---
layout: page
title: Private Instruction
permalink: /private-instruction/
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&display=swap');
  /* ---- Scoped styling for the Private Instruction page ---- */
  .site-header .site-title { display:none; }
  .page-heading, .post-header { display:none; }
  body { font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; }

  .pi {
    --ink:#1f1f1f;
    --muted:#5c5c5c;
    --line:#e6e6e6;
    --accent:#2b2b2b;
    --accent-soft:#f0f0f0;
    --card:#fbfbfb;
    color:var(--ink);
    line-height:1.6;
  }
  .pi p { max-width:74ch; }
  .pi h1, .pi h2, .pi h3, .pi h4 { font-weight:700; }
  .pi b, .pi strong { font-weight:600; }

  .pi .label {
    text-transform:uppercase;
    letter-spacing:.14em;
    font-size:.72rem;
    font-weight:700;
    color:var(--accent);
    margin:0 0 .5rem;
  }

  .pi-hero { margin:0 0 2.5rem; }
  .pi-hero h1 { font-size:2.1rem; line-height:1.15; margin:0 0 .6rem; letter-spacing:-.02em; font-weight:700; }
  .pi-hero .tagline { font-size:1.12rem; color:var(--muted); max-width:64ch; margin:0; }

  .pi-section { margin:3.4rem 0; padding-top:2.8rem; border-top:1px solid var(--line); }
  .pi-section:first-of-type { border-top:none; padding-top:0; }
  .pi-section h2 { font-size:1.35rem; margin:0 0 1rem; letter-spacing:-.01em; }

  /* Course cards */
  .pi-courses { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:1.2rem; }
  .pi-course {
    border:1px solid var(--line); border-top:3px solid var(--accent);
    border-radius:3px 3px 14px 14px; padding:20px 20px 22px;
    background:var(--card);
  }
  .pi-course h3 { margin:0 0 .35rem; font-size:1.05rem; }
  .pi-course p { font-size:.94rem; color:var(--muted); margin:0; }

  /* Approach steps */
  .pi-steps { display:grid; grid-template-columns:repeat(2,1fr); gap:14px 28px; margin-top:1.1rem; }
  .pi-step { display:flex; gap:14px; align-items:flex-start; }
  .pi-step .num {
    flex:0 0 auto; min-width:1.5em; padding-top:.28rem;
    color:var(--muted); font-size:.92rem; font-weight:700;
  }
  .pi-step h4 { margin:.15rem 0 .2rem; font-size:1rem; }
  .pi-step p { margin:0; font-size:.92rem; color:var(--muted); }

  /* Testimonials */
  .pi-quotes { display:grid; grid-template-columns:repeat(2,1fr); gap:28px 40px; margin-top:1.3rem; }
  .pi-quote { border-left:1px solid var(--ink); padding:4px 0 4px 22px; }
  .pi-quote p { font-size:.96rem; margin:0 0 .9rem; }
  .pi-quote .who { font-size:.84rem; color:var(--muted); font-weight:600; letter-spacing:.02em; }

  /* Pricing */
  .pi-pricing { display:grid; grid-template-columns:repeat(2,1fr); gap:18px; margin-top:1.2rem; }
  .pi-price {
    position:relative; border:1px solid var(--line); border-radius:16px;
    padding:26px 24px; background:var(--card);
  }
  .pi-price.featured { border:1.5px solid var(--accent); background:#fff; }
  .pi-price .pill {
    position:absolute; top:-12px; left:24px; background:var(--accent); color:#fff;
    font-size:.68rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase;
    padding:5px 11px; border-radius:999px;
  }
  .pi-price h3 { margin:.2rem 0 .15rem; font-size:1.08rem; }
  .pi-price .amt { font-size:1.9rem; font-weight:700; letter-spacing:-.02em; }
  .pi-price .amt span { font-size:.95rem; font-weight:500; color:var(--muted); }
  .pi-price .note { font-size:.9rem; color:var(--muted); margin:.5rem 0 0; }

  /* Feature / tech lists */
  .pi-list { list-style:none; padding:0; margin:1rem 0 0; }
  .pi-list li { position:relative; padding:0 0 .55rem 1.4rem; font-size:.95rem; color:var(--ink); }
  .pi-list li::before {
    content:""; position:absolute; left:0; top:.55em;
    width:7px; height:7px; border-radius:50%; background:var(--accent);
  }
  .pi-list li b { font-weight:600; }

  /* CTA */
  .pi-cta { text-align:center; margin:2.6rem 0 1rem; padding:2.4rem 1rem; background:var(--accent-soft); border-radius:16px; }
  .pi-cta h2 { border:none; margin:0 0 .5rem; }
  .pi-cta p { margin:0 auto 1.3rem; color:var(--muted); max-width:52ch; }
  .pi-btn {
    display:inline-block; background:var(--accent); color:#fff !important;
    padding:13px 26px; border-radius:10px; text-decoration:none; font-weight:600;
    border:1px solid var(--accent); transition:opacity .15s ease;
  }
  .pi-btn:hover { opacity:.9; }
  .pi-btn-outline { background:transparent; color:var(--accent) !important; }
  .pi-btn-outline:hover { background:#fff; opacity:1; }
  .pi-cta-actions { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }
  .pi-cta .email { display:block; margin-top:1rem; font-size:.92rem; color:var(--muted); }

  .pi-fine { margin-top:2.4rem; padding-top:1.6rem; border-top:1px solid var(--line); }
  .pi-fine p { font-size:.9rem; color:var(--muted); }
  .pi-fine .label { color:var(--muted); }

  /* FAQ accordion */
  .pi-faq { margin-top:1.1rem; }
  .pi-faq details { border-bottom:1px solid var(--line); padding:15px 0; }
  .pi-faq details:first-of-type { border-top:1px solid var(--line); }
  .pi-faq summary {
    cursor:pointer; font-weight:600; font-size:1rem; list-style:none;
    display:flex; justify-content:space-between; align-items:center; gap:16px;
  }
  .pi-faq summary::-webkit-details-marker { display:none; }
  .pi-faq summary::after { content:"+"; color:var(--accent); font-weight:400; font-size:1.35rem; line-height:1; }
  .pi-faq details[open] summary::after { content:"\2212"; }
  .pi-faq details p { margin:.7rem 0 0; color:var(--muted); font-size:.95rem; max-width:70ch; }

  /* Highlight callout */
  .pi-callout {
    margin-top:1.2rem; padding:20px 24px; border:1px solid var(--line);
    border-left:3px solid var(--accent); border-radius:12px; background:var(--card);
  }
  .pi-callout p { margin:0; }

  /* Sample-lesson preview cards (static first-page images, not downloadable) */
  .pi-samples { display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-top:1.3rem; }
  .pi-sample {
    display:grid; grid-template-columns:124px 1fr; gap:20px; align-items:center;
    border:1px solid var(--line); border-radius:14px; padding:20px; background:var(--card);
  }
  .pi-sample-thumb {
    display:block; border:1px solid var(--line); border-radius:7px; overflow:hidden;
    box-shadow:0 5px 16px rgba(31,42,68,.12);
  }
  .pi-sample-thumb img { display:block; width:100%; height:auto; }
  .pi-sample-body .course { font-size:.74rem; color:var(--accent); font-weight:700; text-transform:uppercase; letter-spacing:.1em; margin:0 0 .3rem; }
  .pi-sample-body h4 { margin:0 0 .35rem; font-size:1.02rem; line-height:1.25; }
  .pi-sample-body p { margin:0 0 .7rem; font-size:.88rem; color:var(--muted); }
  .pi-sample-link { font-size:.9rem; font-weight:600; color:var(--accent); text-decoration:none; }
  .pi-sample-link:hover { text-decoration:underline; }

  @media (max-width:720px){
    .pi-courses, .pi-steps, .pi-quotes, .pi-pricing { grid-template-columns:1fr; }
    .pi-samples { grid-template-columns:1fr; }
    .pi-hero h1 { font-size:1.7rem; }
  }
</style>

<div class="pi" markdown="0">

  <div class="pi-hero">
    <h1>Private Mathematics &amp; Statistics Instruction</h1>
  </div>

  <style>
    .pi-jump{display:flex;gap:8px 24px;flex-wrap:wrap;margin:-1rem 0 .2rem}
    .pi-jump a{font-size:.76rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--muted);text-decoration:none}
    .pi-jump a:hover{color:var(--ink)}
    .pi-section{scroll-margin-top:24px}
  </style>
  <nav class="pi-jump" aria-label="Page sections">
    <a href="#approach">How I teach</a>
    <a href="#materials">Materials</a>
    <a href="#rates">Rates</a>
    <a href="#faq">FAQ</a>
    <a href="#start">Getting started</a>
  </nav>

  <!-- OVERVIEW -->
  <div class="pi-section">
    <p class="label">Overview</p>
    <p>I work privately with a small number of high school and college students, across the full arc of a mathematics or statistics course rather than the difficult night before a test. Instruction is live and one-on-one, planned around the student's actual class, its pacing, and whatever is specifically in the way. The standard throughout is the one the AP exam and good mathematics share: correct setup, precise notation, and reasoning a reader can follow. What follows is how that works in practice.</p>
  </div>

  <!-- COURSES -->
  <div class="pi-section">
    <p class="label">Courses</p>
    <style>
      .pi-courselist{margin:1.2rem 0 0}
      .pi-courselist .row{display:grid;grid-template-columns:200px 1fr;gap:24px;padding:16px 2px}
      .pi-courselist .row h3{margin:0;font-size:1.02rem}
      .pi-courselist .row p{margin:0;font-size:.95rem;color:var(--muted);max-width:60ch}
      @media (max-width:720px){.pi-courselist .row{grid-template-columns:1fr;gap:6px}}
    </style>
    <div class="pi-courselist">
      <div class="row">
        <h3>AP Statistics</h3>
        <p>The reasoning of uncertainty: study design, probability, and inference, together with the statistical writing the exam grades as strictly as the arithmetic. Named procedures, checked conditions, conclusions in context.</p>
      </div>
      <div class="row">
        <h3>AP Calculus AB &amp; BC</h3>
        <p>Limits, derivatives, integrals, and their applications, taught with the notation and justification that free-response scoring demands. For BC, the full second half as well: series, parametric and polar curves, and the further techniques of integration.</p>
      </div>
      <div class="row">
        <h3>AP Precalculus</h3>
        <p>The function families, trigonometry, and analytic groundwork on which calculus stands. Taught as genuine preparation for what follows, not merely as a prerequisite to pass through.</p>
      </div>
    </div>
  </div>

  <!-- WEBINARS -->
  <div class="pi-section">
    <p class="label">Free webinars</p>
    <h2>Two free sessions this August</h2>
    <p>Before the school year begins, I'm giving two free 45-minute sessions on how to start the year well. Everyone who registers receives my getting-started guide for their course, whether or not they attend live: the habits that make the year go well, the technical setup of calculator, notation, and how the course and exam are structured, and the early mistakes most worth avoiding.</p>
    <p style="margin-top:1.5rem;"><b>AP Statistics</b> &nbsp;&middot;&nbsp; Tuesday, August 25, 5:30 p.m. Pacific</p>
    <p style="margin-top:.45rem;"><b>AP Calculus AB &amp; BC</b> &nbsp;&middot;&nbsp; Thursday, August 27, 5:30 p.m. Pacific</p>
    <p style="margin-top:1.5rem;font-size:.93rem;color:var(--muted);">Students in AP Precalculus are welcome to register as well; I'll send the AP Precalculus guide, with a live session available by request.</p>
    <a href="https://forms.gle/PMQRaH75zCRBTLg3A" class="pi-btn" style="margin-top:1.3rem;" target="_blank" rel="noopener">Register for a webinar</a>
  </div>

  <!-- BACKGROUND -->
  <div class="pi-section">
    <p class="label">Background</p>
    <h2>Who you're working with</h2>
    <p>I hold an <b>M.S. in Statistics from the University of Washington</b> and a <b>B.S. in Mathematics from the University of Nevada, Reno</b>, with formal training in probability, statistical inference, regression, and the analytic foundations underlying calculus. My graduate training provides a rigorous theoretical foundation that carries through every session, from correct procedure selection to well-justified conclusions.</p>
    <p>I've taught in both structured university settings and one-on-one formats. As a graduate teaching assistant for large introductory statistics courses, I led weekly discussion sections, developed instructional materials, and helped students produce clear, defensible reasoning. I also mentored through UW's Directed Reading Program, designing and teaching a one-on-one short course in statistical learning. The complete record, degrees, coursework, and teaching history, is under <a href="/about/#training">academic training</a> on the about page.</p>
  </div>

  <!-- HOW I TEACH -->
  <div class="pi-section" id="approach">
    <p class="label">How I teach</p>
    <h2>The mistake behind the mistake</h2>
    <p>A wrong answer rarely tells the whole story. Two students can miss the same problem for completely different reasons, and the way a student sets a problem up often tells me more than the answer does. So while we work, I'm paying attention to more than whether the final number is right:</p>
    <ul class="pi-list">
      <li><b>How the problem gets set up</b>, and whether the student chose the right procedure for the right reason.</li>
      <li><b>Notation and justification</b>, where capable students quietly lose credit they have actually earned.</li>
      <li><b>Where the hesitation is</b>, which usually marks the line between what is secure and what only looks secure.</li>
      <li><b>Which errors repeat</b>, and whether a new mistake is really an old misconception resurfacing.</li>
      <li><b>What happens once the prompts stop</b>, the truest test of whether the learning has held.</li>
    </ul>
    <p style="margin-top:1.1rem;">From that, I can tell whether a difficulty is conceptual, procedural, organizational, or a matter of confidence, and each of those calls for a different response. A missed problem isn't a verdict; it's information about what we work on next.</p>

    <h3 style="margin:2.4rem 0 .5rem;font-size:1.08rem;">What a session looks like</h3>
    <p>Every session is built around the student, not a fixed script. Most of our time is spent solving problems together, and the teaching is calibrated to exactly what the student needs that day. Students are welcome to send specific problems, homework, or upcoming topics at least 24 hours in advance, and I'll build the session around them.</p>
    <div class="pi-steps">
      <div class="pi-step">
        <div class="num">1.</div>
        <div>
          <h4>Targeted teaching</h4>
          <p>First I decide how much teaching the student actually needs: a few minutes of review when it is just a refresher, or a full rebuild when a topic isn't sticking. Some things need a quick correction; others need to be retaught from the ground up.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">2.</div>
        <div>
          <h4>Guided problem-solving</h4>
          <p>Where most of the learning happens. Working through problems together is how the student builds real, durable skill, and it is also where I can follow the reasoning most closely. We take on AP-style problems and the student's own questions, and I coach in real time, correcting the setup rather than just the answer and adjusting the support as the work tells me to.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">3.</div>
        <div>
          <h4>Independent practice</h4>
          <p>Then I step back. The student works a few problems alone, because the goal isn't a solution that made sense while I was talking; it's reasoning the student can produce when the help is gone. We review together afterward.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">4.</div>
        <div>
          <h4>Notes &amp; solutions</h4>
          <p>A summary, worked problems, and solutions uploaded after each meeting, so the work is there to return to and each session builds on the last rather than starting from zero.</p>
        </div>
      </div>
    </div>
    <p style="margin-top:1.3rem;">I'm equally attentive to the learning environment. Many capable students lose points to uncertainty under time pressure, disorganized work, or inconsistent written communication. Sessions are calm and focused: questions are taken seriously, mistakes are handled constructively, and confidence is built alongside skill.</p>

    <h3 style="margin:2.4rem 0 .5rem;font-size:1.08rem;">Each session informs the next</h3>
    <p>Because I work with a small roster and keep detailed notes, I am not meeting your student fresh each week. I remember what caused trouble last month, notice when an old error resurfaces in a new topic, and can tell the difference between a student who is rushing and one who is genuinely confused.</p>
    <p>Over a term, I track what is becoming secure, what still needs attention, and whether the student is growing less dependent on prompting, and I shape the pacing, explanations, and practice around what I see. That accumulating picture of how a particular student works is the part of the instruction that can't be handed off or generated on demand.</p>
  </div>

  <!-- MATERIALS -->
  <div class="pi-section" id="materials">
    <p class="label">Materials</p>
    <h2>A full curriculum, ready before we start</h2>
    <p>Because I've already built the course, I don't have to choose between preparation and flexibility. Every topic already has clear explanations, worked examples, and practice ready to draw on, so we spend our time on what your student actually needs instead of building from scratch each week.</p>
    <p>The curriculum keeps us organized; the student's work decides where we spend our time. Most sessions don't move through a whole lesson; it's a resource to pull from, shaped around the gaps and recurring errors I see.</p>
    <p style="margin-top:1.1rem;">Whatever we use is shared with the student afterward. An optional <b>problem set</b>, assigned between sessions and submitted to me for written feedback, is also available as part of the between-session support add-on.</p>

    <div class="pi-callout" style="margin-top:1.4rem;">
      <p><b>Bring the problems you want to cover.</b> Alongside the prepared lesson, students are welcome to send me specific problems, homework questions, or upcoming topics at least 24 hours before a session, and I'll build them into that day's plan. Every session stays shaped around what the student needs and asks for.</p>
    </div>

  </div>

  <!-- AP EXAM PREP -->
  <div class="pi-section">
    <p class="label">AP exam preparation</p>
    <h2>A focused shift before the exam</h2>
    <p>Everything in the course is built with two ends in mind from the first session: succeeding in the AP class itself, and succeeding on the AP exam in May. The notation, the justification habits, and the rubric-aligned writing we practice all year are the exam's own standards, so exam preparation is never a separate project bolted on at the end.</p>
    <p>In the final one to two months, sessions then shift entirely to exam preparation: timed practice, full free-response and multiple-choice work, and targeted review of the content most likely to appear. The focus becomes transfer, performing accurately under timed, independent conditions, which is the real test of whether the learning holds. All exam-preparation materials are provided as part of this phase, at no cost beyond regular session time.</p>
  </div>

  <!-- TESTIMONIALS -->
  <div class="pi-section">
    <p class="label">Testimonials</p>
    <h2>What families say</h2>
    <div class="pi-quotes">
      <div class="pi-quote">
        <p>&ldquo;Katherine is an attentive, thoughtful, and highly effective tutor. She helped my daughter build both confidence and understanding in AP Statistics, making challenging material feel approachable. Her follow-up was exceptional; she regularly checked in and ensured nothing fell through the cracks. I highly recommend Katherine to any family looking for a knowledgeable, supportive, and dedicated tutor.&rdquo;</p>
        <span class="who">Parent of 2025 AP Statistics student</span>
      </div>
      <div class="pi-quote">
        <p>&ldquo;Katherine worked closely with us to understand our child's challenges and develop approaches for her specific needs. She was flexible and adaptive, and not only increased our child's understanding but helped her gain the self-confidence needed to really deepen her comprehension and growth.&rdquo;</p>
        <span class="who">Parent of 2025 AP Statistics student</span>
      </div>
    </div>
  </div>

  <!-- PRICING -->
  <div class="pi-section" id="rates">
    <p class="label">Pricing</p>
    <h2>Hourly, with one rate for every course</h2>
    <p>No packages or long-term commitment; you book the sessions you need. Sessions start at a 60-minute minimum and are booked in 30-minute increments, so we can size each meeting to the work at hand. I recommend a <b>weekly 90-minute session</b>: ninety minutes gives us enough time to teach the topic, practice it together, and leave room for an independent check.</p>
    <div class="pi-pricing">
      <div class="pi-price featured">
        <span class="pill">Recommended</span>
        <h3>90-minute session</h3>
        <div class="amt">$180<span> / session</span></div>
        <p class="note">Room to teach the topic, work through it together, and finish with an independent check. This is the cadence I recommend for steady weekly progress.</p>
      </div>
      <div class="pi-price">
        <h3>60-minute session</h3>
        <div class="amt">$130<span> / session</span></div>
        <p class="note">Best for targeted help, test review, or self-directed students who come with specific questions.</p>
      </div>
    </div>

    <p style="margin-top:1.5rem;">The rate reflects the preparation around each session as much as the hour itself: planning around your student's course, the materials, the notes and solutions afterward, and the continuity carried from one week to the next.</p>
    <p style="margin-top:1.1rem;font-weight:600;">Every session includes:</p>
    <ul class="pi-list">
      <li><b>Pre-planned, instructor-led teaching</b> aligned to your student's course and pacing.</li>
      <li><b>Session notes and full solutions</b> uploaded after each meeting for review.</li>
      <li><b>Calculator integration</b> (TI-84 Plus CE) so students avoid avoidable test-day mistakes.</li>
      <li><b>AP-aligned writing</b> focus on setup, justification, and interpretation.</li>
    </ul>

    <p style="margin-top:1.3rem;font-weight:600;">Optional add-on: between-session support &nbsp;<span style="color:var(--accent);">$200/month ($50/week)</span></p>
    <p style="margin-top:.5rem;font-size:.95rem;color:var(--muted);">For families who want the learning to stay active between meetings: continuity, accountability, and a feedback loop so a misunderstanding doesn't sit untouched for a week.</p>
    <ul class="pi-list">
      <li><b>Weekly assigned problem sets</b> with written feedback on method, setup, and communication, giving the student extra accountability to keep practicing between sessions.</li>
      <li><b>Generous between-session availability</b> on weekdays and weekends for questions and clarifications, so students never stay stuck for long and keep their momentum.</li>
      <li><b>Additional cheat sheets and study resources</b> to keep and reference throughout the year.</li>
      <li><b>Monthly parent check-ins</b> by email or call to review progress, strengths, and next steps.</li>
    </ul>

    <p style="margin-top:1.6rem;font-size:.93rem;color:var(--muted);"><b>Billing.</b> Sessions are billed monthly, with invoices sent on the 1st. I accept a limited number of students each academic year; once capacity is reached, I maintain a short waitlist.</p>
  </div>

  <!-- TECHNOLOGY -->
  <div class="pi-section">
    <p class="label">How it works</p>
    <h2>Technology &amp; setup</h2>
    <p>Sessions are built to feel like working side by side, with everything we write kept organized and easy to return to.</p>
    <ul class="pi-list">
      <li><b>Live Zoom sessions</b> with a shared digital whiteboard, where I write out each setup and every step of the reasoning by hand, just as we would on paper.</li>
      <li><b>Real-time annotation</b> on the student's own problems and homework, so they watch the work build up rather than passively following slides.</li>
      <li><b>Notes and full solutions</b> uploaded to a private shared folder (Dropbox) after each meeting, so nothing is lost and everything stays in one place; parents may be added on request.</li>
      <li><b>Calculator integration</b> (TI-84 Plus CE) walked through on screen, so the student learns the exact keystrokes that prevent avoidable test-day mistakes.</li>
      <li><b>Flexible across time zones:</b> I'm based in the Pacific time zone and regularly work with students elsewhere, and we'll find a weekly time that fits.</li>
      <li><b>A simple student setup:</b> a quiet space, stable internet, a graphing calculator (TI-84 Plus CE recommended), and a consistent way to take notes.</li>
    </ul>
  </div>

  <!-- FAQ -->
  <div class="pi-section" id="faq">
    <p class="label">Questions</p>
    <h2>Frequently asked</h2>
    <div class="pi-faq">
      <details>
        <summary>How is this different from homework help?</summary>
        <p>Homework help is organized around tonight's assignment; my work is organized around your student. Rather than walk through whatever problem is due, I watch how they reason, find what is actually getting in the way, teach to that, and make sure they can do it without me. The aim is a student who needs less help over time, not more.</p>
      </details>
      <details>
        <summary>What if my student understands an explanation but can't do the problems alone?</summary>
        <p>This is one of the most common reasons families reach out, and it is exactly what the structure is built for. Following an explanation and producing the reasoning yourself are different skills. Every session ends with the student working independently, so we find out what actually holds without prompts and rebuild whatever doesn't.</p>
      </details>
      <details>
        <summary>How do you know what my student needs to work on?</summary>
        <p>From watching them work. The setup, the notation, where they hesitate, and which errors repeat tell me whether a difficulty is conceptual, procedural, organizational, or a matter of confidence, and my notes carry that from week to week so the picture sharpens over time.</p>
      </details>
      <details>
        <summary>Why do you recommend a consistent weekly schedule?</summary>
        <p>Consistency is what lets the work compound. A steady weekly rhythm keeps us ahead of the class's pacing, lets me catch small gaps before they turn into costly ones, and means each session builds on the last instead of starting over.</p>
      </details>
      <details>
        <summary>Are sessions online or in person?</summary>
        <p>Sessions are conducted live over Zoom with a digital whiteboard for step-by-step work. This lets me support students wherever they are while keeping all notes and materials organized in one shared folder.</p>
      </details>
      <details>
        <summary>How do you align with my student's class?</summary>
        <p>I follow your student's course pacing and build each session around their current topics, assignments, and the specific errors I observe, so our work reinforces what is happening in the classroom rather than running parallel to it.</p>
      </details>
      <details>
        <summary>Do you teach courses beyond the three listed?</summary>
        <p>Yes. AP coursework is the center of the practice, but I also work with students in non-AP and college-level mathematics and statistics. If your course is not listed, write and we will discuss fit.</p>
      </details>
      <details>
        <summary>What happens before the AP exam?</summary>
        <p>In the final one to two months, sessions shift into focused exam preparation with timed practice, full free-response and multiple-choice work, and targeted review. All preparation materials are included.</p>
      </details>
      <details>
        <summary>What if we need to reschedule?</summary>
        <p>Occasional schedule changes are normal. I ask for reasonable notice when possible and do my best to accommodate.</p>
      </details>
      <details>
        <summary>Is the between-session support required?</summary>
        <p>No. It is an optional monthly add-on for families who want assigned practice, written feedback, and weekday support between sessions. Many students do well with the weekly session alone.</p>
      </details>
      <details>
        <summary>What does my student need to get started?</summary>
        <p>A quiet space, stable internet, a graphing calculator (TI-84 Plus CE recommended), and a consistent note-taking method.</p>
      </details>
    </div>
  </div>

  <!-- AVAILABILITY -->
  <div class="pi-section" id="start">
    <p class="label">Availability</p>
    <h2>Scheduling and getting started</h2>
    <p>I'm based in the Pacific time zone and regularly work with students in other time zones; we will find a weekly slot that fits your schedule.</p>
    <p>Weekly slots are limited and tend to fill quickly, so it is best to secure a place on the roster early. I take only a small number of students each academic year, and once the roster is full I keep a short waitlist.</p>
    <p><b>The strongest results start at the beginning of the course.</b> The ideal time to begin is the first weeks of the term, while each topic can be built correctly the first time, before small gaps quietly compound into the ones that cost points later. Students who join mid-semester are very welcome and can make real gains; we simply spend our early sessions closing those gaps before we get ahead of new material. Reserving a spot before the term begins lets us prepare, stay ahead of your class's pacing, and settle into a steady weekly rhythm from the very first week.</p>
  </div>

  <!-- CTA -->
  <div class="pi-cta">
    <h2>Getting started</h2>
    <p>Write to me with your question, or book a free 15-minute introduction. After we speak, I will suggest the arrangement that fits your student.</p>
    <link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
    <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
    <div class="pi-cta-actions">
      <a href="mailto:hi@katherinedelno.com" class="pi-btn">Email me</a>
      <a href="https://calendly.com/katherinedelno" class="pi-btn pi-btn-outline"
         onclick="Calendly.initPopupWidget({url:'https://calendly.com/katherinedelno'});return false;">Book a meet-and-greet</a>
    </div>
    <span class="email">or email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a></span>
  </div>

  <!-- DISCLAIMER -->
  <div class="pi-fine">
    <p class="label">Academic progress &amp; no guaranteed outcomes</p>
    <p>My goal is to help students build durable understanding, stronger problem-solving habits, and clearer written communication through structured instruction, targeted practice, and actionable feedback aligned with AP expectations.</p>
    <p>I cannot and do not guarantee any specific grade, test score, class placement, or AP exam result. Outcomes depend on factors outside my control, including the student's consistency between sessions, completion of assigned work, attendance, classroom instruction and grading policies, assessment difficulty, and test-day conditions. By enrolling, families are purchasing instructional time and academic coaching, not a promised outcome.</p>
    <p class="label" style="margin-top:1.4rem;">Accessibility</p>
    <p>I want this website and my instruction to be usable by everyone. I aim to follow recognized web accessibility guidelines (WCAG 2.1 Level AA) and make ongoing improvements. If you have any difficulty accessing content on this site, or if you need materials in an alternative format or an accommodation for sessions, please email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a> and I will work with you promptly to provide the information or assistance you need.</p>
    <p><small>AP&reg; is a registered trademark owned by the College Board, which is not affiliated with and does not endorse this private instruction service.</small></p>
  </div>

</div>
