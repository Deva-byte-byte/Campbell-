"""Verify every numeric token in the original survives in the tightened file."""
import re, sys
from collections import Counter
def nums(t):
    t = t.replace(' ', ' ')
    return Counter(re.findall(r'\d+(?:[.,]\d+)*', t))
a, b = open(sys.argv[1]).read(), open(sys.argv[2]).read()
na, nb = nums(a), nums(b)
missing = sorted(k for k in na if k not in nb)
heads_a = [l for l in a.splitlines() if l.startswith('#')]
heads_b = [l for l in b.splitlines() if l.startswith('#')]
tabs_a = sum(1 for l in a.splitlines() if re.match(r'\|[-| ]+\|$', l.strip()))
tabs_b = sum(1 for l in b.splitlines() if re.match(r'\|[-| ]+\|$', l.strip()))
conc_a = [l for l in a.splitlines() if l.startswith('*Concept')]
conc_b = [l for l in b.splitlines() if l.startswith('*Concept')]
print('words', len(a.split()), '->', len(b.split()))
print('missing numbers:', missing)
print('headings equal:', heads_a == heads_b, len(heads_a), len(heads_b))
print('tables:', tabs_a, tabs_b)
print('concepts verbatim:', conc_a == conc_b, len(conc_a), len(conc_b))
print('keypoints:', a.count('keypoints'), b.count('keypoints'))
