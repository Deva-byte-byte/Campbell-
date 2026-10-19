#!/usr/bin/env python3
"""Check a set's questions cover all ledger items assigned to it. Usage: coverage.py SETNO path/to/setNN.json"""
import json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
L = {i['id']: i for i in json.load(open(os.path.join(ROOT, 'ledger.json')))}
plan = json.load(open(os.path.join(ROOT, 'sets_plan.json')))
n = int(sys.argv[1]); qs = json.load(open(sys.argv[2]))
want = {i for i, it in L.items() if it['ch'] in plan[n-1]['chapters']}
got = {c for q in qs for c in q.get('c', [])}
bad = got - set(L); miss = sorted(want - got); extra = sorted(got & set(L) - want)
print(f'set {n}: {len(qs)} questions, {len(want)} items assigned, {len(want & got)} covered, {len(miss)} missing')
if bad: print('unknown ids:', sorted(bad))
if miss: print('missing:', ' '.join(miss))
if extra: print('also covers (other sets):', ' '.join(extra))
sys.exit(1 if miss or bad else 0)
