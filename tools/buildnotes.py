#!/usr/bin/env python3
"""Render review/notes/setNN.md files into one reading page (ids stripped, contents, Update lines highlighted).
Usage: buildnotes.py out.html N [N ...]"""
import os, re, sys, markdown
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review')
out, ns = sys.argv[1], [int(x) for x in sys.argv[2:]]
toc, body, words = [], [], 0
for n in ns:
    t = re.sub(r'\s*<!--.*?-->', '', open(os.path.join(R, 'notes', f'set{n:02d}.md')).read(), flags=re.S)
    words += len(t.split())
    t = re.sub(r'^# .*$', '', t, count=1, flags=re.M)
    chs = []
    def h2(m):
        i = f's{n}c{len(chs)}'; chs.append((i, m.group(1).strip())); return f'## {m.group(1).strip()} {{#{i}}}'
    t = re.sub(r'^## (.*)$', h2, t, flags=re.M)
    html = markdown.markdown(t, extensions=['tables', 'attr_list', 'sane_lists'])
    html = html.replace('<strong>Update:</strong>', '<strong class="upd">Update:</strong>')
    body.append(f'<section class="set" id="set{n}"><h1 class="seth">Set {n}</h1>{html}</section>')
    toc.append(f'<li><a href="#set{n}">Set {n}</a><ul>' + ''.join(f'<li><a href="#{i}">{h}</a></li>' for i, h in chs) + '</ul></li>')
lab = ', '.join(map(str, ns[:-1])) + ' and ' + str(ns[-1])
page = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes_template.html')).read() \
    .replace('__TITLE__', 'Reading Notes Sets') \
    .replace('__H1__', f'Reading notes: sets {lab}') \
    .replace('__SUB__', f'Every book answer and Chapter Review point of these sets, grouped by chapter and topic. About {words:,} words, roughly {words/43/60:.1f} hours at 43 words a minute. Lines marked Update correct the book against current guidelines.') \
    .replace('__TOC__', '<ol class="toc">' + ''.join(toc) + '</ol>').replace('__BODY__', ''.join(body))
open(out, 'w').write(page); print('wrote', out, words, 'words')
