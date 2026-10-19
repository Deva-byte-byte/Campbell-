#!/usr/bin/env python3
"""Add Campbell-Walsh-Wein Review PDFs to review/: copy PDF, split text by chapter, rebuild INDEX.md.
Usage: python3 tools/addreview.py file1.pdf [file2.pdf ...]"""
import re, sys, os, shutil, subprocess, json, hashlib
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
PDF, TXT = os.path.join(ROOT, 'pdf'), os.path.join(ROOT, 'text')
META = os.path.join(ROOT, 'chapters.json')
os.makedirs(PDF, exist_ok=True); os.makedirs(TXT, exist_ok=True)
meta = json.load(open(META)) if os.path.exists(META) else {}

def starts(lines):
    out = []
    for i, l in enumerate(lines):
        m = re.match(r'^\s*(\d)\s?(\d)?\s?(\d)?\s*$', l)
        if not m: continue
        num = int(''.join(g for g in m.groups() if g))
        nxt = [x.strip() for x in lines[i+1:i+18] if x.strip()]
        if nxt and nxt[0][0].isupper() and not re.match(r'^[a-e]\.', nxt[0]) and len(nxt[0]) >= 6 \
           and any(x.lower().replace(' ','').startswith('keyword') for x in nxt):
            out.append((i, num))
    return out

def stats(t):
    a = r = 0; sec = None; title = []
    for x in t.split('\n')[1:]:
        s = x.strip()
        if not title and not s: continue
        if len(title) < 4 and s and not s.lower().startswith('keyword') and sec is None and not re.search(r'[A-Z]\.,? [A-Z]|, and ', s):
            title.append(s); continue
        if re.match(r'^Answers', s): sec = 'A'
        elif re.match(r'^Questions', s): sec = 'Q'
        elif re.match(r'^Chapter [Rr]eview', s): sec = 'R'
        elif sec == 'A' and re.match(r'^\d{1,2}\.? ?[a-f]\.', s): a += 1
        elif sec == 'R' and re.match(r'^\d{1,2}\. ', s): r += 1
        if s and title and sec is None and (s.lower().startswith('keyword') or re.search(r', and |[A-Z]\. [A-Z]', s)):
            sec = 'H'
    return ' '.join(title), a, r, len(t.split())

seen = {hashlib.md5(open(os.path.join(PDF, f), 'rb').read()).hexdigest() for f in os.listdir(PDF)}
for f in sys.argv[1:]:
    h = hashlib.md5(open(f, 'rb').read()).hexdigest()
    if h in seen: print('skip duplicate', f); continue
    seen.add(h)
    lines = subprocess.run(['pdftotext', '-layout', f, '-'], capture_output=True, text=True).stdout.split('\n')
    st = starts(lines)
    if not st: print('no chapters found in', f); continue
    nums = [n for _, n in st]
    shutil.copy(f, os.path.join(PDF, f'ch{nums[0]:03d}-{nums[-1]:03d}.pdf'))
    for k, (i, n) in enumerate(st):
        end = st[k+1][0] if k + 1 < len(st) else len(lines)
        t = '\n'.join(lines[i:end]); path = os.path.join(TXT, f'ch{n:03d}.txt')
        if os.path.exists(path) and len(open(path).read()) >= len(t): continue
        open(path, 'w').write(t)
        title, a, r, w = stats(t)
        meta[str(n)] = dict(title=meta.get(str(n), {}).get('title') or title, q=a, r=r, w=w)
        print(f'ch {n}: {title} | book Qs {a} | review pts {r}')
json.dump(meta, open(META, 'w'), indent=1, sort_keys=True)
have = sorted(int(k) for k in meta)
missing = [n for n in range(15, max(have) + 1) if n not in have]
def ranges(xs):
    out = []; 
    for x in xs:
        if out and x == out[-1][1] + 1: out[-1][1] = x
        else: out.append([x, x])
    return ', '.join(f'{a}' if a == b else f'{a}–{b}' for a, b in out)
R = 0.35; scope = [n for n in have if n >= 15]
md = ['# Campbell-Walsh-Wein Review (12th ed., Review 3rd ed., 2020): chapter repository', '',
      '- `pdf/`: uploaded PDFs, named by chapter range. `text/chNNN.txt`: one text file per chapter.',
      '- MCQ scope: chapters 15 onward (1–14 already solved). Est. MCQs ≈ 0.35 × (book Qs + review points).', '',
      '| Ch | Title | Book Qs | Review pts | Est. MCQs |', '|---|---|---|---|---|']
for n in have:
    m = meta[str(n)]; md.append(f"| {n} | {m['title']} | {m['q']} | {m['r']} | {max(3, round((m['q']+m['r'])*R))} |")
tq = sum(meta[str(n)]['q'] for n in scope); tr = sum(meta[str(n)]['r'] for n in scope)
md += ['', f'**Chapters held:** {len(have)}. **In MCQ scope (15+):** {len(scope)} chapters, {tq} book Qs, {tr} review points, about {round((tq+tr)*R)} MCQs for full coverage.',
       '', f'**Missing (15 onward):** {ranges(missing)} (and anything after {max(have)}).']
open(os.path.join(ROOT, 'INDEX.md'), 'w').write('\n'.join(md) + '\n')
print('missing:', ranges(missing))
