#!/usr/bin/env python3
"""Check reading notes review/notes/setNN.md: every ledger id of the set's chapters must appear in an
<!-- ids --> comment. Prints missing/unknown ids and word count. Usage: notescheck.py N"""
import json, os, re, sys
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
n = int(sys.argv[1]); P = json.load(open(os.path.join(R, 'sets_plan.json')))[n-1]
want = {x['id'] for x in json.load(open(os.path.join(R, 'ledger.json'))) if x['ch'] in P['chapters']}
t = open(os.path.join(R, 'notes', f'set{n:02d}.md')).read()
got = set(re.findall(r'c\d{3}-[ar]\d{2}', ' '.join(re.findall(r'<!--(.*?)-->', t, re.S))))
words = len(re.sub(r'<!--.*?-->', '', t, flags=re.S).split())
print(f'set {n}: {len(want)} items, {len(want & got)} covered, missing {sorted(want - got)}, unknown {sorted(got - want)}, {words} words (~{words/43:.0f} min)')
