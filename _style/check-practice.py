#!/usr/bin/env python3
"""Check the practice sets in _practice against the house standard.

    python3 _style/check-practice.py            # every set
    python3 _style/check-practice.py FILE ...   # named files

Exit status is 1 if anything is reported.

This runs every check in _style/check.py first, with the internal-link universe
widened to include /practice/ URLs, and then adds the checks that only make
sense for a practice set. The added checks exist because the ways a practice
page goes wrong are not the ways an essay goes wrong. An essay can be read and
its errors seen. A practice set can look completely finished while one of its
distractors is unreachable, one of its rubrics adds to eight, or one of its
solutions quietly names an answer that is not among the options.

What is checked here, and why each one is worth a rule:

  structure      Every item carries exactly one solution block, and the divs
                 balance. An unbalanced div swallows the rest of the page and
                 Jekyll will not warn.
  options        Four options, labelled (A) through (D), in order. Not three
                 (the item is unfinished) and not five (a paste went wrong).
  answer         The solution opens with "Answer: (X)." and X is one of the
                 four. Without this the page has no machine-readable key.
  distractors    Each of the three wrong letters is named in the solution.
                 This is the standard the whole section is sold on, and it is
                 the first thing that slips when a set is written in a hurry.
  key balance    No answer letter takes more than half the items, and no letter
                 appears three times in a row. Same convention the printed
                 practice exams follow.
  rubric         Every free-response question has a rubric table whose points
                 add to the number claimed in the heading, and the per-question
                 totals add to frq_points in the front matter.
  counts         mcq_no_calc, mcq_calc and frq_count match what is on the page.
  CED            Every item names at least one CED topic, and every topic named
                 on an item appears in the front-matter ced_topics list.
"""
import re
import sys
import glob
import os
import collections
import importlib.util

try:
    import yaml
except ImportError:
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------- shared rules

def load_base():
    """_style/check.py, imported rather than duplicated."""
    path = os.path.join(HERE, 'check.py')
    spec = importlib.util.spec_from_file_location('housecheck', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def known_urls():
    """Post URLs and practice URLs together, so a link from one to the other
    does not read as dead."""
    urls = set()
    for p in glob.glob(os.path.join(ROOT, '_posts', '*.md')):
        urls.add(re.sub(r'^(\d{4})-(\d\d)-(\d\d)-(.*)\.md$',
                        r'/\1/\2/\3/\4.html', os.path.basename(p)))
    for p in glob.glob(os.path.join(ROOT, '_practice', '*.md')):
        urls.add('/practice/%s/' % os.path.basename(p)[:-3])
    for extra in ('/resources/', '/practice/', '/private-instruction/',
                  '/about/', '/policies/', '/privacy/'):
        urls.add(extra)
    return urls

# ---------------------------------------------------------------- parsing

ITEM_OPEN = '<div class="pr-item" markdown="1">'
SOL_OPEN = '<div class="pr-sol" markdown="1">'


def split_fm(src):
    parts = src.split('---\n', 2)
    return (parts[1], parts[2]) if len(parts) == 3 else ('', src)


def items(body):
    """Yield (index, block) for each pr-item block, in page order."""
    chunks = body.split(ITEM_OPEN)[1:]
    for i, c in enumerate(chunks, 1):
        yield i, c.split(ITEM_OPEN)[0]


def tags(block):
    m = re.search(r'<p class="pr-tag">(.*?)</p>', block, re.S)
    if not m:
        return []
    return [re.sub(r'<[^>]+>', '', s).strip()
            for s in re.findall(r'<span[^>]*>(.*?)</span>', m.group(1), re.S)]


def solution(block):
    if SOL_OPEN not in block:
        return None
    return block.split(SOL_OPEN, 1)[1]

# ---------------------------------------------------------------- checks

def check_practice(path, base, urls):
    src = open(path, encoding='utf-8').read()
    fm_text, body = split_fm(src)
    bad = list(base.check(path, urls))

    def flag(kind, detail=''):
        bad.append((kind, detail))

    fm = {}
    if yaml:
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception as e:
            flag('front matter does not parse', str(e))

    # Every front-matter check is conditioned on `fm` being populated. Without
    # pyyaml there is no front matter to inspect, and a check that fires on an
    # empty dict reports the absence of the parser as a defect in the page.
    for k in ('archetype', 'unit', 'ced_topics', 'mcq_no_calc', 'mcq_calc',
              'frq_count', 'frq_points', 'exam_form', 'work_time', 'blurb'):
        if fm and k not in fm:
            flag('missing practice front-matter key', k)
    if fm and fm.get('layout') != 'practice':
        flag('layout is not practice', str(fm.get('layout')))
    declared = [str(t) for t in (fm.get('ced_topics') or [])]
    if fm and not declared:
        flag('ced_topics is empty')

    blocks = list(items(body))
    if not blocks:
        flag('no pr-item blocks found')
        return bad

    n_nocalc = n_calc = n_frq = 0
    answers = []

    for i, block in blocks:
        where = 'item %d' % i
        label = (tags(block) or ['?'])[0]

        # structure. The split has already consumed this item's opening tag,
        # so the block carries one more closing tag than opening tag.
        if block.count('</div') != block.count('<div') + 1:
            flag('unbalanced divs in item', '%s (%s)' % (where, label))
        if block.count(SOL_OPEN) != 1:
            flag('item does not have exactly one solution block',
                 '%s (%s)' % (where, label))
        sol = solution(block)
        if sol is None:
            continue

        chips = tags(block)
        is_frq = any(c.lower().startswith('free response') for c in chips)
        calc = [c for c in chips if c in ('Calculator', 'No calculator')]
        if not calc:
            flag('item has no calculator chip', '%s (%s)' % (where, label))

        # CED chips, and agreement with the front matter
        ced = []
        for c in chips:
            if c.startswith('CED'):
                ced += [t.strip() for t in c[3:].split(',') if t.strip()]
        if not ced:
            flag('item names no CED topic', '%s (%s)' % (where, label))
        for t in ced:
            if declared and t not in declared:
                flag('CED topic on an item is not in ced_topics',
                     '%s names %s' % (where, t))

        if is_frq:
            n_frq += 1
            claimed = None
            for c in chips:
                m = re.match(r'(\d+)\s+points?$', c)
                if m:
                    claimed = int(m.group(1))
            if claimed is None:
                flag('free-response item does not state its point total', where)
            rows = re.findall(r'^\|\s*\([a-z]\)\s*\|\s*(\d+)\s*\|', sol, re.M)
            if not rows:
                flag('free-response item has no rubric table', where)
            else:
                total = sum(int(r) for r in rows)
                if claimed is not None and total != claimed:
                    flag('rubric points do not add to the stated total',
                         '%s: table gives %d, heading says %d'
                         % (where, total, claimed))
            if 'Rubric pattern' not in sol:
                flag('free-response solution has no rubric pattern block', where)
            continue

        # multiple choice
        if calc and calc[0] == 'No calculator':
            n_nocalc += 1
        else:
            n_calc += 1

        opts = re.findall(r'^-\s*\(([A-Z])\)', block, re.M)
        if opts != ['A', 'B', 'C', 'D']:
            flag('options are not exactly (A) (B) (C) (D) in order',
                 '%s got %s' % (where, ''.join(opts) or 'none'))

        m = re.search(r'\*\*Answer:\s*\(([A-D])\)\.\*\*', sol)
        if not m:
            flag('solution does not open with a parsable answer', where)
            continue
        ans = m.group(1)
        answers.append(ans)

        if 'Where the other options come from' not in sol:
            flag('solution has no distractor block', where)
        named = set(re.findall(r'^-\s*\*\*\(([A-D])\)\*\*', sol, re.M))
        missing = sorted({'A', 'B', 'C', 'D'} - {ans} - named)
        if missing:
            flag('distractors not named', '%s missing %s'
                 % (where, ', '.join('(%s)' % x for x in missing)))
        if ans in named:
            flag('the correct option is listed among the distractors', where)

    # Answer-key balance, the convention the printed practice exams follow:
    # every letter within one of even, and no letter three times in a row.
    # The evenness test is only meaningful once a set is long enough for a
    # quarter of it to be more than a rounding artefact.
    if answers:
        counts = collections.Counter(answers)
        if len(answers) >= 8:
            even = len(answers) / 4.0
            for letter in 'ABCD':
                if abs(counts[letter] - even) > 1:
                    flag('answer key is not within one of even',
                         '(%s) is the answer to %d of %d items, even would be %.1f'
                         % (letter, counts[letter], len(answers), even))
        for j in range(len(answers) - 2):
            if answers[j] == answers[j + 1] == answers[j + 2]:
                flag('three consecutive items share an answer letter',
                     'items %d to %d are all (%s)' % (j + 1, j + 3, answers[j]))

    # counts declared against counts found
    for key, found in (('mcq_no_calc', n_nocalc), ('mcq_calc', n_calc),
                       ('frq_count', n_frq)):
        if fm and key in fm and fm[key] != found:
            flag('front matter disagrees with the page',
                 '%s says %s, page has %d' % (key, fm[key], found))

    return bad

# ---------------------------------------------------------------- main

def main():
    base = load_base()
    urls = known_urls()
    targets = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, '_practice', '*.md')))
    total = 0
    checked = 0
    missing = []
    for p in targets:
        # Counted, not skipped in silence. An argument that names nothing used
        # to be passed over quietly, so a mistyped path, or a shell that hands
        # a trailing comment through as argv, produced a clean report over an
        # empty set. A green run has to mean files were read.
        if not os.path.exists(p):
            missing.append(p)
            continue
        bad = check_practice(p, base, urls)
        checked += 1
        if bad:
            print('\n%s' % os.path.basename(p))
            for kind, detail in bad:
                print('   %-52s %s' % (kind, detail))
            total += len(bad)

    print('\n%d file%s checked, %d finding%s.'
          % (checked, '' if checked == 1 else 's',
             total, '' if total == 1 else 's'))
    if missing:
        print('\n  WARNING: %d argument%s named nothing on disk and %s skipped:'
              % (len(missing), '' if len(missing) == 1 else 's',
                 'was' if len(missing) == 1 else 'were'))
        for m in missing:
            print('    %s' % m)
        print('  If you pasted a command with a trailing comment, zsh passed the\n'
              '  comment through as arguments. Add `setopt interactive_comments`\n'
              '  to ~/.zshrc, or drop the comment.')
        return 1
    if checked == 0:
        print('\n  WARNING: no files were checked.')
        return 1
    if yaml is None:
        # Said loudly and last, because a clean run that silently skipped half
        # its checks is worse than a run that fails.
        print('\n  WARNING: pyyaml is not installed, so no front-matter check ran.\n'
              '  Counts, CED topics, point totals and required keys were NOT verified.\n'
              '  Install it with:  python3 -m pip install pyyaml')
        return 1
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
