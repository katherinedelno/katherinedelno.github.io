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
  .pi-reg-row { display:flex; gap:12px; flex-wrap:wrap; margin-top:1.3rem; }
  @media (max-width:560px){
    .pi-reg-row { flex-direction:column; align-items:stretch; }
    .pi-reg-row .pi-btn { text-align:center; }
  }

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
    <p>I work privately with a small number of high school and college students, usually across the full arc of a mathematics or statistics course. Instruction is live and one-on-one. Each session is planned around the student's class, its pacing, and the specific difficulties I see in their work.</p>
    <p>I bring a rigorous mathematical and statistical background to my teaching, with particular attention to theory, notation, and reasoning. At the same time, I try to make those ideas clear and approachable for students. The standard throughout is careful work that a reader can follow.</p>
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
        <p>AP Statistics asks students to reason carefully about uncertainty. We work through study design, probability, sampling distributions, and inference, with close attention to the written reasoning the exam requires. Students learn to choose procedures for the right reasons, check conditions, and state conclusions clearly in context.</p>
      </div>
      <div class="row">
        <h3>AP Calculus AB &amp; BC</h3>
        <div>
          <p>Limits, derivatives, integrals, and their applications are taught alongside the notation and justification expected on free-response work. For BC, this also includes series, parametric and polar curves, and additional techniques of integration.</p>
          <p style="margin-top:.6rem;">My aim is for the major ideas of calculus to feel connected rather than like a collection of separate procedures.</p>
        </div>
      </div>
      <div class="row">
        <h3>AP Precalculus</h3>
        <p>AP Precalculus develops the function families, trigonometry, and analytic groundwork that calculus depends on. I teach it as mathematics worth understanding in its own right, while keeping the transition to calculus in view.</p>
      </div>
    </div>
  </div>

  <!-- WEBINARS -->
  <div class="pi-section">
    <p class="label">Free webinars</p>
    <h2>Two free sessions this August</h2>
    <p>Whether your student's year begins in August or after Labor Day, I am offering two free 45-minute sessions on how to begin the course well.</p>
    <p>Everyone who registers receives my getting-started guide for the course within a day, whether or not they attend live. The guide covers useful early habits, calculator and notation setup, the structure of the course and exam, and common mistakes worth avoiding.</p>
    <p style="margin-top:1.5rem;"><b>AP Statistics</b> &nbsp;&middot;&nbsp; Tuesday, August 25, 5:30 p.m. Pacific</p>
    <p style="margin-top:.45rem;"><b>AP Calculus AB &amp; BC</b> &nbsp;&middot;&nbsp; Thursday, August 27, 5:30 p.m. Pacific</p>
    <div class="pi-reg-row">
      <a href="https://us06web.zoom.us/meeting/register/IeqFGjh3Q7OnCN5nYqqrtw" class="pi-btn" target="_blank" rel="noopener">Register for AP Statistics, Aug 25</a>
      <a href="https://us06web.zoom.us/meeting/register/vAjK5wd5S4edqx6cp6egKQ" class="pi-btn" target="_blank" rel="noopener">Register for AP Calculus, Aug 27</a>
    </div>

    {% include subscribe.html
       heading="Or just take the guide"
       blurb="The guide does not depend on attending a session. There is one for each of the three courses, including AP Precalculus. Choose a course and I will send it."
       button="Send the guide"
       done="Thank you. I'll send the guide to that address shortly."
       choose="true" %}
  </div>

  <!-- BACKGROUND -->
  <div class="pi-section">
    <p class="label">Background</p>
    <h2>Who you're working with</h2>
    <p>I hold an <b>M.S. in Statistics from the University of Washington</b> and a <b>B.S. in Mathematics from the University of Nevada, Reno</b>. My formal training includes probability, statistical inference, regression, and the mathematical foundations underlying calculus.</p>
    <p>That training shapes how I teach. I care about correct procedure, but also about why a method applies, what the notation means, and whether a conclusion is actually justified.</p>
    <p>I have taught in both university and one-on-one settings. As a graduate teaching assistant for introductory statistics courses, I led weekly discussion sections, developed instructional materials, and worked with students on clear statistical reasoning. I also mentored through the University of Washington's Directed Reading Program, where I designed and taught a one-on-one short course in statistical learning.</p>
    <p>My degrees, coursework, statistical work, and teaching history are listed under <a href="/about/#training">academic training</a> on the About page.</p>
  </div>

  <!-- HOW I TEACH -->
  <div class="pi-section" id="approach">
    <p class="label">How I teach</p>
    <h2>The mistake behind the mistake</h2>
    <p>A wrong answer rarely tells me enough on its own. Two students can miss the same problem for completely different reasons. The setup often tells me more than the final answer.</p>
    <p>While a student works, I pay attention to:</p>
    <ul class="pi-list">
      <li><b>how the problem is set up</b> and why a procedure was chosen</li>
      <li><b>notation and justification</b></li>
      <li><b>where the student hesitates</b></li>
      <li><b>which errors repeat</b></li>
      <li><b>what happens once the prompts stop</b></li>
    </ul>
    <p style="margin-top:1.1rem;">Those details help me determine whether the difficulty is conceptual, procedural, organizational, or simply a matter of execution. The response should depend on the cause.</p>
    <p>A missed problem is useful information. It tells us what to work on next.</p>

    <h3 style="margin:2.4rem 0 .5rem;font-size:1.08rem;">What a session looks like</h3>
    <p>Every session is built around the student rather than a fixed script. Most of our time is spent solving problems. Students are welcome to send homework, specific questions, or upcoming topics at least 24 hours in advance so I can include them in the session plan.</p>
    <div class="pi-steps">
      <div class="pi-step">
        <div class="num">1.</div>
        <div>
          <h4>Targeted teaching</h4>
          <p>First I decide how much direct teaching is actually needed. Sometimes a student needs only a brief review. Other topics need to be rebuilt from the beginning.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">2.</div>
        <div>
          <h4>Guided problem-solving</h4>
          <p>Most of the session is spent working through problems together. This is where I can follow the student's reasoning closely and correct a problem at the point where it begins.</p>
          <p style="margin-top:.5rem;">We use AP-style problems as well as questions from the student's own course. I adjust the amount of support as we work.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">3.</div>
        <div>
          <h4>Independent practice</h4>
          <p>Then I step back. The student works independently so we can see what remains once the explanation and prompting are gone.</p>
          <p style="margin-top:.5rem;">We review the work together afterward.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">4.</div>
        <div>
          <h4>Notes &amp; solutions</h4>
          <p>After each meeting, I upload a summary, worked problems, and solutions. The student has a record of the work to return to, and the next session begins with the context of the last one already in place.</p>
        </div>
      </div>
    </div>
    <p style="margin-top:1.3rem;">I also pay attention to the conditions under which students work well. Capable students can lose points through rushed setup, disorganized work, or uncertainty under time pressure. Sessions are calm and focused. Questions are taken seriously, and mistakes are treated as part of the information we use.</p>

    <h3 style="margin:2.4rem 0 .5rem;font-size:1.08rem;">Each session informs the next</h3>
    <p>I keep detailed notes for every student. I am not meeting them fresh each week.</p>
    <p>I know what caused difficulty several weeks earlier. I can notice when the same misconception returns in a new form. I can also distinguish between an isolated mistake and a pattern that needs more attention.</p>
    <p>Over a term, I track what is becoming secure, what still needs work, and how much prompting a student requires. The pacing and practice become more specific as that picture develops.</p>
  </div>

  <!-- MATERIALS -->
  <div class="pi-section" id="materials">
    <p class="label">Materials</p>
    <h2>A full curriculum, ready before we start</h2>
    <p>I have built a complete curriculum for each course I teach. Every major topic has explanations, worked examples, and practice ready to use.</p>
    <p>That preparation gives us structure without forcing every student through the same lesson. The curriculum keeps the course organized. The student's work determines where we spend our time.</p>
    <p style="margin-top:1.1rem;">Most sessions do not move through a full prepared lesson from beginning to end. I draw from the materials based on the student's current course, questions, and recurring difficulties.</p>
    <p>Anything we use is shared afterward.</p>

    <div class="pi-callout" style="margin-top:1.4rem;">
      <p>Students may also send specific problems, homework questions, or upcoming topics at least 24 hours before a session so I can build them into that day's plan.</p>
    </div>

    <p style="margin-top:1.4rem;">An optional between-session support plan is available for students who would benefit from additional assigned practice and written feedback.</p>

  </div>

  <!-- AP EXAM PREP -->
  <div class="pi-section">
    <p class="label">AP exam preparation</p>
    <h2>A focused shift before the AP exam</h2>
    <p>The course is taught with both the class and the AP exam in mind from the beginning. The notation, justification, and written reasoning we practice throughout the year are the same habits students need in May.</p>
    <p>During the final one to two months, sessions shift toward focused exam preparation. We use timed practice, full free-response and multiple-choice work, and targeted review of weaker content.</p>
    <p>At that stage, I am looking closely at whether the student can transfer what they know to unfamiliar problems and work accurately under independent, timed conditions.</p>
    <p>All exam-preparation materials are included in regular session time.</p>
  </div>

  <!-- TESTIMONIALS -->
  <div class="pi-section">
    <p class="label">Testimonials</p>
    <h2>What families say</h2>
    <div class="pi-quotes">
      <div class="pi-quote">
        <p>&ldquo;Katherine is an attentive, thoughtful, and highly effective tutor. Her thoroughness and genuine care are evident in every interaction. She helped my daughter build both confidence and understanding in AP Statistics, making challenging material feel approachable and manageable.</p>
        <p>Communication was consistently easy and her follow-up was exceptional; Katherine regularly checked in, provided helpful feedback, and ensured that nothing fell through the cracks. Most importantly, my daughter felt comfortable and connected, which made learning more engaging and productive.</p>
        <p>I highly recommend Katherine to any family looking for a knowledgeable, supportive, and dedicated tutor.&rdquo;</p>
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
    <p>There are no packages or long-term commitments. Sessions have a 60-minute minimum and can be booked in 30-minute increments.</p>
    <p>For most students, I recommend a <b>weekly 90-minute session</b>. This gives us enough time to teach, work through problems together, and finish with independent practice.</p>
    <div class="pi-pricing">
      <div class="pi-price featured">
        <span class="pill">Recommended</span>
        <h3>90-minute session</h3>
        <div class="amt">$210<span> / session</span></div>
        <p class="note">Recommended for regular weekly instruction. Ninety minutes gives us enough time to develop a topic carefully without rushing the independent work at the end.</p>
      </div>
      <div class="pi-price">
        <h3>60-minute session</h3>
        <div class="amt">$140<span> / session</span></div>
        <p class="note">A good fit for targeted questions, test review, or students who arrive with a specific set of problems to work through.</p>
      </div>
    </div>

    <p style="margin-top:1.5rem;">The rate reflects the work around each session as well as the meeting itself. This includes preparation around the student's course, the materials we use, notes and solutions afterward, and the continuity from one week to the next.</p>
    <p style="margin-top:1.1rem;font-weight:600;">Every session includes:</p>
    <ul class="pi-list">
      <li><b>teaching planned around the student's course and pacing</b></li>
      <li><b>session notes and full solutions</b> uploaded after each meeting</li>
      <li><b>TI-84 Plus CE instruction</b> when calculator work is relevant</li>
      <li><b>close attention to setup, notation, justification, and interpretation</b></li>
    </ul>

    <p style="margin-top:1.3rem;font-weight:600;">Optional between-session support &nbsp;<span style="color:var(--accent);">$200/month ($50/week)</span></p>
    <p style="margin-top:.5rem;font-size:.95rem;color:var(--muted);">This option is for students who would benefit from more structured work between meetings.</p>
    <p style="margin-top:.5rem;font-size:.95rem;color:var(--muted);">It includes:</p>
    <ul class="pi-list">
      <li><b>weekly assigned problem sets</b> with written feedback on method, setup, and communication</li>
      <li><b>between-session availability</b> for questions and clarification on weekdays and weekends</li>
      <li><b>additional reference sheets and study materials</b></li>
      <li><b>monthly parent check-ins</b> by email or phone to discuss progress and next steps</li>
    </ul>

    <p style="margin-top:1.6rem;font-size:.93rem;color:var(--muted);"><b>Billing.</b> Sessions are billed after they occur, never in advance. On the first business day of each month, I send one invoice for the previous month's sessions. Payment is due within seven days.</p>
    <p style="font-size:.93rem;color:var(--muted);">Rates are held for the full academic year for enrolled families.</p>
    <p style="font-size:.93rem;color:var(--muted);">I accept a limited number of students each academic year. Once the roster is full, I maintain a short waitlist.</p>
    <p style="font-size:.93rem;color:var(--muted);">Full billing, attendance, and cancellation terms are available under <a href="/policies/">Policies</a>.</p>
  </div>

  <!-- REFERRALS -->
  <div class="pi-section" id="referrals">
    <p class="label">Referrals</p>
    <h2>Most new students come through families I already work with</h2>
    <p>If you refer a family and their student enrolls, I will credit one 60-minute session to your next invoice after the new student completes a first month of instruction. If you are no longer enrolled when the credit comes due, I will send an Amazon gift card for the same amount instead.</p>
    <p style="margin-top:1.1rem;">There is no limit on referrals. I ask only that they be genuine recommendations for families you think would be a good fit for the practice.</p>
    <p style="margin-top:1.1rem;">Families considering instruction are welcome to write to me at <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a> or <a href="https://calendly.com/katherinedelno" target="_blank" rel="noopener">book a free 15-minute introduction</a>.</p>
  </div>

  <!-- TECHNOLOGY -->
  <div class="pi-section">
    <p class="label">How it works</p>
    <h2>Technology &amp; setup</h2>
    <p>Sessions are designed to feel as close as possible to working side by side while keeping the student's work organized and easy to revisit.</p>
    <ul class="pi-list">
      <li>Live Zoom sessions use a shared digital whiteboard for step-by-step work.</li>
      <li>I can annotate the student's own problems and homework in real time.</li>
      <li>Notes and full solutions are uploaded to a private shared Dropbox folder after each meeting. Parents may be added on request.</li>
      <li>TI-84 Plus CE work can be demonstrated on screen when relevant.</li>
      <li>I am based in the Pacific time zone and work with students in other time zones.</li>
      <li>Students need a quiet space, stable internet, a graphing calculator when required, and a consistent way to take notes.</li>
    </ul>
  </div>

  <!-- FAQ -->
  <div class="pi-section" id="faq">
    <p class="label">Questions</p>
    <h2>Frequently asked</h2>
    <div class="pi-faq">
      {%- for item in site.data.faq %}
      <details>
        <summary>{{ item.q }}</summary>
        {%- for para in item.a %}
        <p>{{ para }}</p>
        {%- endfor %}
      </details>
      {%- endfor %}
    </div>

    {%- comment -%}
      FAQPage structured data, generated from the same _data/faq.yml the list
      above renders. Google shows these as expandable results; keeping both
      outputs on one source is what stops the markup and the page disagreeing.
    {%- endcomment -%}
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {%- for item in site.data.faq %}
        {
          "@type": "Question",
          "name": {{ item.q | strip_html | jsonify }},
          "acceptedAnswer": { "@type": "Answer", "text": {{ item.a | join: " " | strip_html | jsonify }} }
        }{% unless forloop.last %},{% endunless %}
        {%- endfor %}
      ]
    }
    </script>
  </div>

  <!-- AVAILABILITY -->
  <div class="pi-section" id="start">
    <p class="label">Availability</p>
    <h2>Scheduling and getting started</h2>
    <p>I am based in the Pacific time zone and regularly work with students elsewhere. We will find a weekly time that fits your schedule when availability allows.</p>
    <p>I keep the academic-year roster small. Weekly slots are limited, and once the roster is full I maintain a short waitlist.</p>
    <p><b>The beginning of a course is usually the best time to start.</b> It gives us a chance to establish strong habits early and address misunderstandings before later material depends on them.</p>
    <p>Students who begin mid-semester are also welcome. In that case, the first sessions often involve identifying and closing earlier gaps while we keep pace with new material.</p>
  </div>

  <!-- CTA -->
  <div class="pi-cta">
    <h2>Getting started</h2>
    <p>Write to me with your question, or book a free 15-minute introduction. After we speak, I will suggest the arrangement that makes sense for your student.</p>
    <link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
    <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
    <div class="pi-cta-actions">
      <a href="mailto:hi@katherinedelno.com" class="pi-btn">Email me</a>
      <a href="https://calendly.com/katherinedelno" class="pi-btn pi-btn-outline"
         onclick="Calendly.initPopupWidget({url:'https://calendly.com/katherinedelno'});return false;">Book a meet-and-greet</a>
    </div>
    <p style="margin:1.4rem auto 0;font-size:.9rem;">Before instruction begins, please read the <a href="/policies/">Policies</a> and <a href="/privacy/">Privacy notice</a>. I send both by email during intake and ask for a short reply confirming that you have read them.</p>
  </div>

  <!-- DISCLAIMER -->
  <div class="pi-fine">
    <p class="label">Academic progress &amp; no guaranteed outcomes</p>
    <p>My role is to provide careful instruction, appropriate practice, and clear feedback. I cannot guarantee a particular grade, test score, class placement, or AP exam result.</p>
    <p>Outcomes also depend on factors outside my control, including attendance, work between sessions, classroom instruction, grading policies, assessment difficulty, and test-day conditions.</p>
    <p>Families are purchasing instructional time and academic support, not a promised outcome.</p>
    <p>The standards I hold myself to are set out in full under <a href="/policies/">Policies</a>.</p>
    <p class="label" style="margin-top:1.4rem;">Accessibility</p>
    <p>I want this website and my instruction to be usable by everyone. I aim to follow recognized web accessibility guidelines (WCAG 2.1 Level AA) and make ongoing improvements.</p>
    <p>If you have difficulty accessing content on this site, or need materials in an alternative format or an accommodation for sessions, please email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a>. I will work with you to provide the information or assistance you need.</p>
  </div>

</div>
