#!/usr/bin/env python3
"""Compute and set read_time for the articles in _posts.

    python3 _style/read-time.py            # report only
    python3 _style/read-time.py --write    # rewrite front matter

The formula, and why each term is there:

    minutes = words/130 + 0.30*display_equations + 1.0*has_interactive
                        + 0.05*table_rows
    read_time = max(5, round(minutes))

  words/130     130 wpm, not the 200-250 of ordinary prose. These articles
                are read slowly and often re-read; a student following a
                worked example is not skimming.
  0.30/equation 18 seconds to parse a display equation and connect it to
                the sentence that introduced it. Inline math is left inside
                the word count, where it behaves like a word.
  1.0/interactive  The prose instructs the reader to operate the thing
                ("Drag the slider and watch"), so the time is real.
  0.05/table row  Three seconds a row.
  floor of 5    Below five minutes the label stops carrying information.

Word counting strips, in this order: front matter, <script> and <style>
blocks, then $$...$$ mathematics, then HTML tags. The order matters -
stripping tags first lets a "<" inside mathematics (L < 1, p > 1) swallow
everything up to the next ">".
"""
import re
import sys
import glob
import os

WPM = 130
MIN_PER_EQUATION = 0.30
MIN_PER_INTERACTIVE = 1.0
MIN_PER_TABLE_ROW = 0.05
FLOOR = 5


def measure(path):
    src = open(path, encoding='utf-8').read()
    front, body = src.split('---\n', 2)[1], src.split('---\n', 2)[2]
    body = re.sub(r'<script\b.*?</script>', ' ', body, flags=re.S | re.I)
    body = re.sub(r'<style\b.*?</style>', ' ', body, flags=re.S | re.I)

    equations = len(re.findall(r'(?m)^\$\$', body))
    table_rows = len(re.findall(r'(?m)^\|', body))
    interactive = bool(re.search(r'<div class="viz[ "]|interactive-regression', body))

    text = re.sub(r'\$\$.*?\$\$', ' ', body, flags=re.S)   # mathematics first
    text = re.sub(r'<[^>]+>', ' ', text)                   # then tags
    words = len(re.findall(r"[A-Za-z][A-Za-z'’-]*", text))

    minutes = (words / WPM
               + equations * MIN_PER_EQUATION
               + (MIN_PER_INTERACTIVE if interactive else 0)
               + table_rows * MIN_PER_TABLE_ROW)
    current = re.search(r'read_time: "(\d+)', front)
    return dict(words=words, equations=equations, tables=table_rows,
                interactive=interactive, minutes=minutes,
                read_time=max(FLOOR, round(minutes)),
                current=int(current.group(1)) if current else None)


def main():
    write = '--write' in sys.argv
    paths = sorted(glob.glob(os.path.join(os.path.dirname(__file__) or '.',
                                          '..', '_posts', '*.md')))
    paths = [p for p in paths if 'welcome-to-jekyll' not in p]
    changed = 0
    print('%-46s %5s %3s %4s %3s   %3s -> %-3s' %
          ('article', 'words', 'eq', 'viz', 'tbl', 'now', 'new'))
    for p in paths:
        m = measure(p)
        mark = '' if m['read_time'] == m['current'] else '   %+d' % (m['read_time'] - m['current'])
        if m['read_time'] != m['current']:
            changed += 1
        print('%-46s %5d %3d %4s %3d   %3s    %-3d%s' %
              (os.path.basename(p)[5:-3][:46], m['words'], m['equations'],
               'yes' if m['interactive'] else '-', m['tables'],
               m['current'], m['read_time'], mark))
        if write and m['read_time'] != m['current']:
            src = open(p, encoding='utf-8').read()
            src = re.sub(r'read_time: "\d+ min read"',
                         'read_time: "%d min read"' % m['read_time'], src, count=1)
            open(p, 'w', encoding='utf-8').write(src)
    print('\n%d of %d differ from the value in front matter.' % (changed, len(paths)))
    if not write:
        print('Re-run with --write to apply.')


if __name__ == '__main__':
    main()
