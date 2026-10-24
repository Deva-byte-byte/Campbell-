#!/usr/bin/env python3
"""Combine built sets (review/sets/setNN.json) into one exam page: all questions first, answers after submit.
Usage: buildexam.py out.html N [N ...]"""
import json, os, sys
T = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(T, '..', 'review')
out, ns = sys.argv[1], [int(x) for x in sys.argv[2:]]
P = json.load(open(os.path.join(ROOT, 'sets_plan.json'))); M = json.load(open(os.path.join(ROOT, 'chapters.json')))
sets = []
for n in ns:
    q = [{k: v for k, v in x.items() if k != 'c'} for x in json.load(open(os.path.join(ROOT, 'sets', f'set{n:02d}.json')))]
    sets.append({"n": n, "ch": '; '.join(f"{c} {M[str(c)]['title']}" for c in P[n-1]['chapters']), "q": q})
tot = sum(len(s['q']) for s in sets); lab = ', '.join(map(str, ns[:-1])) + ' and ' + str(ns[-1])
html = open(os.path.join(T, 'exam_template.html')).read() \
    .replace('__TITLE__', f'MCQ Exam Sets {"–".join(map(str, (ns[0], ns[-1])))}').replace('__STORE__', 'mch-exam-' + '-'.join(map(str, ns))) \
    .replace('__H1__', f'Mixed sets {lab}: {tot}-question exam') \
    .replace('__EYEBROW__', 'MCh Urology · Campbell-Walsh-Wein Review · exam mode') \
    .replace('__SUB__', 'Answer every question first; you can change answers until you submit. Then the score and all answers with explanations appear together. Each set covers every book question and Chapter Review point of its chapters.') \
    .replace('__SETS__', json.dumps(sets, ensure_ascii=False))
open(out, 'w').write(html); print('wrote', out, tot, 'questions')
