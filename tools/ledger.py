#!/usr/bin/env python3
"""Build review/ledger.json: one item per book answer and per Chapter Review point (chapters 15-162)."""
import re, os, json
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
items = []
for f in sorted(os.listdir(os.path.join(ROOT, 'text'))):
    ch = int(f[2:5])
    if ch < 15: continue
    L = open(os.path.join(ROOT, 'text', f)).read().split('\n')
    sec = None; cur = None; na = nr = 0
    def flush():
        global cur
        if cur:
            cur['text'] = re.sub(r'\s+', ' ', cur['text']).strip()
            if len(cur['text']) > 8: items.append(cur)
        cur = None
    for l in L:
        s = l.strip()
        if re.match(r'^Answers?$', s, re.I) or re.match(r'^Answers\b', s, re.I): flush(); sec = 'A'; continue
        if re.match(r'^Questions\b', s): flush(); sec = 'Q'; continue
        if re.match(r'^Chapter [Rr]eview', s): flush(); sec = 'R'; continue
        if sec in ('A', 'R') and re.match(r'^(Pathology|Imaging)$', s): flush(); continue
        if sec == 'A' and na > 5 and re.match(r'^1\.\s', s) and not re.match(r'^1\.\s?[a-f]\.', s):
            flush(); sec = 'R'
        if sec == 'A' and re.match(r'^\d{1,2}\.?\s?[a-f]\.', s):
            flush(); na += 1; cur = dict(id=f'c{ch:03d}-a{na:02d}', ch=ch, kind='answer', text=s); continue
        if sec == 'R' and re.match(r'^\d{1,2}\.\s', s):
            flush(); nr += 1; cur = dict(id=f'c{ch:03d}-r{nr:02d}', ch=ch, kind='review', text=s); continue
        if sec == 'A' and re.match(r'^\d{1,2}\.?\s?[a-f]\.', s) is None and cur and s and not re.match(r'^(FIG|TABLE|Table|From )', s):
            cur['text'] += ' ' + s
        elif sec == 'R' and cur and s and not re.match(r'^\d{1,3}$', s):
            cur['text'] += ' ' + s
    flush()
json.dump(items, open(os.path.join(ROOT, 'ledger.json'), 'w'), indent=0, ensure_ascii=False)
from collections import Counter
c = Counter(i['ch'] for i in items)
print(len(items), 'items;', len(c), 'chapters; min', min(c.values()), 'max', max(c.values()))
print([ch for ch in range(15, 163) if ch not in c])
