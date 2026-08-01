#!/usr/bin/env python3
"""Find bare pipes that kramdown will turn into a table.

Kramdown starts a table when a paragraph's first line contains an unescaped '|'.
A line like  `The function $$|x| \cdot 1$$ ...`  therefore renders as table cells
and the mathematics never reaches MathJax. Nothing warns you.

Safe regions, which this script skips: <script> blocks, elements carrying
markdown="0" (every viz block), and Liquid tags {%- ... -%}.

Usage:  python3 _style/check-pipes.py            # whole site
        python3 _style/check-pipes.py FILE ...   # named files
Exit status is 1 if anything was found.
"""
import re, sys, glob, os

def offending(path):
    src = open(path, encoding='utf-8').read()
    out, in_script, in_md0 = [], False, False
    for n, line in enumerate(src.split('\n'), 1):
        if re.search(r'<script[ >]', line):      in_script = True
        if re.search(r'markdown="0"', line):     in_md0 = True
        blocked = in_script or in_md0
        if '</script>' in line:                  in_script = False
        if in_md0 and line.strip() == '</div>':  in_md0 = False
        if blocked or '|' not in line:           continue
        s = line.strip()
        if re.match(r'^\|', s):                  continue   # deliberate table row
        if re.match(r'^\|?[\s:|-]+$', s):        continue   # table separator
        if re.sub(r'\{%-?.*?-?%\}', '', s).find('|') < 0:   continue   # Liquid only
        out.append((n, s))
    return out

paths = sys.argv[1:] or sorted(glob.glob('_posts/*.md')) + ['resources.md', 'index.md']
found = 0
for p in paths:
    if not os.path.exists(p): continue
    for n, s in offending(p):
        print('%s:%d  %s' % (p, n, s[:110]))
        found += 1
print('%d bare pipe%s found. Use \\vert for absolute value.'
      % (found, '' if found == 1 else 's'))
sys.exit(1 if found else 0)
