#!/usr/bin/env python3
"""Build set N: review/sets/setNN.py (list R of [topic, stem, options, key, explanation, source, ledger_ids]) ->
review/sets/setNN.json + HTML quiz. Runs coverage and option-length audits. Usage: buildset.py N [seed] [out.html]"""
import json, os, sys, random, re, collections, runpy, subprocess
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
n = int(sys.argv[1]); seed = int(sys.argv[2]) if len(sys.argv) > 2 else n
R = runpy.run_path(os.path.join(ROOT, 'sets', f'set{n:02d}.py'))['R']
random.seed(seed); out = []
for t, q, o, a, e, s, c in R:
    idx = list(range(4)); random.shuffle(idx)
    out.append({"f": "mcq", "t": t, "q": q, "o": [o[j] for j in idx], "a": idx.index(a), "e": [e], "s": s, "c": c})
js = os.path.join(ROOT, 'sets', f'set{n:02d}.json'); json.dump(out, open(js, 'w'), ensure_ascii=False, indent=0)
rank = collections.Counter(); big = []; bad = []
for x in out:
    L = [len(o) for o in x['o']]; k = L[x['a']]; oth = sorted(l for j, l in enumerate(L) if j != x['a'])
    rank[sorted(L, reverse=True).index(k)] += 1
    if k >= oth[-1] + 3: big.append(x['t'])
    if re.search(r'FALSE|NOT|EXCEPT', x['q']) and re.search(r'\b(always|never|only|all|every|no role)\b', x['o'][x['a']], re.I): bad.append(x['t'])
print(f'{len(out)} questions | key length rank (0=longest): {sorted(rank.items())} | positions: {sorted(collections.Counter(x["a"] for x in out).items())}')
print('key clearly longest:', big); print('absolute words in keyed negatives:', bad)
subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'coverage.py'), str(n), js])
if len(sys.argv) > 3:
    tpl = open(os.path.join(os.path.dirname(__file__), 'quiz_template.html')).read()
    plan = json.load(open(os.path.join(ROOT, 'sets_plan.json')))[n-1]; M = json.load(open(os.path.join(ROOT, 'chapters.json')))
    chs = ', '.join(str(c) for c in plan['chapters'])
    html = tpl.replace('__TITLE__', f'Mixed MCQ Set {n}').replace('__STORE__', f'mch-mixed-set-{n}') \
              .replace('__H1__', f'Mixed set {n} of 41: {len(out)} MCQs').replace('__EYEBROW__', f'MCh Urology · Campbell-Walsh-Wein Review · chapters {chs}') \
              .replace('__SUB__', 'Part of a 41-set series covering every book question and Chapter Review point of chapters 15–162. Topics are mixed. All four options are similar in length. Read every explanation: it carries the remaining facts.') \
              .replace('__Q__', json.dumps([{k: v for k, v in x.items() if k != 'c'} for x in out], ensure_ascii=False))
    open(sys.argv[3], 'w').write(html); print('wrote', sys.argv[3])
