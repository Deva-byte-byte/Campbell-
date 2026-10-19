#!/usr/bin/env python3
"""Assign whole chapters (20-162) to 20 mixed sets, balancing ledger items and mixing book areas."""
import json, os
from collections import Counter
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
L = json.load(open(os.path.join(ROOT, 'ledger.json'))); M = json.load(open(os.path.join(ROOT, 'chapters.json')))
cnt = Counter(i["ch"] for i in L if i["ch"] >= 20)
def area(c):
    for lo, hi, a in [(15,19,'Surgical basics'),(20,54,'Paediatrics'),(55,62,'Infection, inflammation, biology'),(63,74,'Reproductive and sexual'),
                      (75,83,'Genital tumours and surgery'),(84,104,'Kidney, obstruction, stones, renal tumours'),(105,107,'Adrenal'),
                      (108,132,'LUT function and incontinence'),(133,142,'Trauma, bladder cancer, diversion'),(143,162,'Prostate')]:
        if lo <= c <= hi: return a
N = 20; sets = [dict(n=k+1, ch=[], items=0, areas=set()) for k in range(N)]
for c in sorted(cnt, key=lambda c: -cnt[c]):
    a = area(c)
    cand = [s for s in sets if a not in s['areas']] or sets
    s = min(cand, key=lambda s: s['items'])
    s['ch'].append(c); s['items'] += cnt[c]; s['areas'].add(a)
for s in sets: s['ch'].sort()
sets.sort(key=lambda s: s['ch'][0])
for k, s in enumerate(sets): s['n'] = k + 1
plan = [dict(set=s['n'], chapters=s['ch'], items=s['items'], status='todo') for s in sets]
json.dump(plan, open(os.path.join(ROOT, 'sets_plan.json'), 'w'), indent=1)
md = ['# 20 mixed MCQ sets of 65: coverage plan (chapters 20–162)', '',
      'Each set mixes chapters from different areas. Every book answer and Chapter Review point (items in `ledger.json`) is assigned to one set and must be covered by a question or explanation there. `tools/coverage.py` checks this.', '',
      '| Set | Chapters | Items | Status |', '|---|---|---|---|']
for p in plan:
    md.append(f"| {p['set']} | " + '; '.join(f"{c} {M[str(c)]['title']}" for c in p['chapters']) + f" | {p['items']} | {p['status']} |")
open(os.path.join(ROOT, 'SETS.md'), 'w').write('\n'.join(md) + '\n')
print(min(p['items'] for p in plan), max(p['items'] for p in plan), sum(p['items'] for p in plan))
for p in plan[:6]: print(p['set'], p['chapters'], p['items'])
