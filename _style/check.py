#!/usr/bin/env python3
"""One command that checks every published article against the style sheet.

    python3 _style/check.py            # whole site
    python3 _style/check.py FILE ...   # named files

Exit status is 1 if anything is reported. Nothing here is a matter of taste;
every check corresponds to a rule in STYLE-SHEET.md, which lives in the
private site-notes repository, or to a way the page can render wrongly
without any warning.

The three checks that catch silent rendering failures are the pipe check, the
math-delimiter check, and the \\left/\\right check. The rest are style.
"""
import re, sys, glob, os, collections

try:
    import yaml
except ImportError:
    yaml = None

# ---------------------------------------------------------------- helpers

def split_fm(src):
    parts = src.split('---\n', 2)
    return (parts[1], parts[2]) if len(parts) == 3 else ('', src)

def strip_scripts(t):
    return re.sub(r'<script.*?</script>', '', t, flags=re.S)

def kramdown_lines(body):
    """(lineno, line) for lines kramdown actually parses: outside <script>
    and outside anything carrying markdown="0" (which is every viz block)."""
    out, in_script, in_md0 = [], False, False
    for i, L in enumerate(body.split('\n'), 1):
        if re.search(r'<script[ >]', L):   in_script = True
        if re.search(r'markdown="0"', L):  in_md0 = True
        blocked = in_script or in_md0
        if '</script>' in L:                       in_script = False
        if in_md0 and L.strip() == '</div>':       in_md0 = False
        if not blocked:
            out.append((i, L))
    return out

def math_spans(text):
    return [m.group(0) for m in re.finditer(r'\$\$(?:(?!\$\$).)+\$\$', text, re.S)]

def prose_only(body):
    t = strip_scripts(body)
    t = re.sub(r'\$\$(?:(?!\$\$).)+\$\$', '', t, flags=re.S)
    return re.sub(r'<[^>]+>', '', t)

# ---------------------------------------------------------------- checks

def check(path, known_urls):
    src = open(path, encoding='utf-8').read()
    fm_text, body = split_fm(src)
    name = os.path.basename(path)
    bad = []
    def flag(kind, detail=''): bad.append((kind, detail))

    # --- front matter
    if yaml:
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception as e:
            flag('front matter does not parse', str(e)); fm = {}
    else:
        fm = {}
    for k in ('layout', 'title', 'date', 'description', 'course',
              'read_time', 'kind', 'sequence'):
        if fm and k not in fm:
            flag('missing front-matter key', k)
    if fm.get('kind') not in (None, 'foundations', 'mechanics', 'beyond'):
        flag('unknown kind', str(fm.get('kind')))

    # --- silent rendering failures
    for i, L in kramdown_lines(body):
        if '|' not in L:
            continue
        s = L.strip()
        if re.match(r'^\|', s) or re.match(r'^\|?[\s:|-]+$', s):
            continue                                   # deliberate table
        if '|' not in re.sub(r'\{%-?.*?-?%\}', '', s):
            continue                                   # Liquid only
        flag('bare pipe: kramdown will render this line as a table',
             'line %d  %s' % (i, s[:70]))
    if body.count('$$') % 2:
        flag('odd number of $$ delimiters')
    for s in math_spans(body):
        if len(re.findall(r'\\left', s)) != len(re.findall(r'\\right', s)):
            flag('unbalanced \\left/\\right', s[:60])
        if s.count('{') != s.count('}'):
            flag('unbalanced braces in math', s[:60])

    # --- style sheet rules
    prose = prose_only(body)
    # 's is ambiguous — "the framework's" is a possessive and stays — so the
    # general check uses only the unambiguous suffixes, plus a short list of
    # 's forms that are never possessive.
    for c in re.findall(r"\b\w+['’](?:t|re|ve|ll|d|m)\b", prose):
        flag('contraction', c)
    for c in re.findall(r"\b(?:it|that|what|here|there|let|he|she|who|"
                        r"nothing|everything|something)['’]s\b",
                        prose, flags=re.I):
        flag('contraction', c)
    if '!' in prose:
        flag('exclamation mark')
    if re.search(r'^### ', body, flags=re.M):
        flag('### heading (the corpus uses ## only)')
    for h in re.findall(r'^## (.+)$', body, flags=re.M):
        if h.rstrip().endswith(('.', '!', '?', ':')):
            flag('heading ends with punctuation', h)
    for L in body.split('\n'):
        if re.match(r'^\s*(?:[-*+]|\d+\.|\|)\s*\*\*', L):
            continue                                   # run-in label: allowed
        for m in re.finditer(r'(?<=\S)[ ]\*\*[^*\n]+\*\*', L):
            flag('mid-sentence bold (use italics)', m.group(0)[:40])

    # inline mathematics must not carry display-size constructs
    for L in strip_scripts(body).split('\n'):
        s = L.strip()
        if s.startswith('$$') and s.endswith('$$') and s.count('$$') == 2:
            continue                                   # display equation
        for m in re.finditer(r'\$\$(.+?)\$\$', L):
            g = m.group(1)
            if r'\dfrac' in g:
                flag('\\dfrac inline', g[:50])
            if re.search(r'\\frac(?![\d])', g):
                flag('\\frac inline (use \\tfrac)', g[:50])
            # Two traps here. \b is no good after \int, because the next
            # character is usually an underscore and regex counts that as a
            # word character. And \textstyle is a *declaration*: it applies to
            # the rest of the group, so it need only appear somewhere earlier
            # in the span, not immediately before the symbol.
            for cmd in (r'\int', r'\sum', r'\prod'):
                m2 = re.search(re.escape(cmd) + r'(?![A-Za-z])', g)
                if m2 and r'\textstyle' not in g[:m2.start()]:
                    flag('%s inline without \\textstyle' % cmd, g[:50])

    # --- structural
    for txt, url in re.findall(r'\[([^\]]+)\]\((/[^)#]+)\)', prose):
        if url not in known_urls:
            flag('dead internal link', url)
    ids = re.findall(r'\bid="([^"]+)"', src)
    for k, v in collections.Counter(ids).items():
        if v > 1:
            flag('duplicate element id', k)
    prefixes = {i.split('-')[0] for i in ids if '-' in i}
    if len(prefixes) > 1:
        flag('more than one id prefix in one article', str(sorted(prefixes)))
    for m in re.finditer(r'<div class="article-note"([^>]*)>', body):
        if 'markdown="1"' not in m.group(1):
            flag('article-note without markdown="1"')
    if '<canvas' in body and 'devicePixelRatio' in body and \
       'Math.min(window.devicePixelRatio' not in body:
        flag('canvas without a device-pixel-ratio cap')
    # The backing store must be resized exactly once per canvas. If the resize
    # sits in a helper that is itself called from inside another function, it
    # re-reads a width it already scaled and doubles it again, so the canvas
    # grows without bound on every slider event. Nothing warns; the page simply
    # falls apart after a few interactions.
    #
    # A resize at the top level of the IIFE is fine. A resize inside a helper is
    # fine too, provided that helper is only ever called during setup — so the
    # test is whether any call to the enclosing helper happens while already
    # inside another function body.
    for js in re.findall(r'<script>(.*?)</script>', body, flags=re.S):
        for m in re.finditer(r'^[ \t]*\w+\.width\s*=\s*\w+\s*\*\s*d__', js, flags=re.M):
            before = js[:m.start()]
            if before.count('{') - before.count('}') <= 1:
                continue                      # top level of the IIFE: correct
            fn = None
            for d in re.finditer(r'function\s+(\w+)\s*\(', before):
                fn = d.group(1)               # nearest enclosing named function
            if not fn:
                flag('device-pixel-ratio resize inside an anonymous nested function',
                     m.group(0).strip())
                continue
            for call in re.finditer(r'\b%s\s*\(' % re.escape(fn), js):
                if re.match(r'\s*function', js[call.end() - len(fn) - 8:]):
                    continue
                head = js[:call.start()]
                if head.count('{') - head.count('}') > 1:
                    flag('device-pixel-ratio resize reachable from a redrawn function '
                         '(canvas doubles on every call)', '%s() called inside another function' % fn)
                    break
    has_viz = 'class="viz' in body or 'interactive-regression' in body
    if fm and bool(fm.get('interactive')) != has_viz:
        flag('interactive: flag disagrees with the body',
             'flag=%s body=%s' % (bool(fm.get('interactive')), has_viz))
    return bad

# ---------------------------------------------------------------- main

def main():
    posts = sorted(glob.glob('_posts/*.md'))
    urls = {re.sub(r'^(\d{4})-(\d\d)-(\d\d)-(.*)\.md$', r'/\1/\2/\3/\4.html',
                   os.path.basename(p)) for p in posts}
    targets = sys.argv[1:] or posts
    total = 0
    for p in targets:
        if not os.path.exists(p):
            continue
        bad = check(p, urls)
        if bad:
            print('\n%s' % os.path.basename(p))
            for kind, detail in bad:
                print('   %-52s %s' % (kind, detail))
            total += len(bad)
    print('\n%d file%s checked, %d finding%s.'
          % (len(targets), '' if len(targets) == 1 else 's',
             total, '' if total == 1 else 's'))
    return 1 if total else 0

if __name__ == '__main__':
    sys.exit(main())
