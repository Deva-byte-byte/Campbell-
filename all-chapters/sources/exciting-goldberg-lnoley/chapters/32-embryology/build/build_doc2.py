"""Build Document 2 (Chapter Notes) for Chapter 32 from the compiled source doc2.md.
doc2.md is the compile-time restructure of instalments 01-05 (scaffolding, numbers blocks
and source-flag appendices removed; chapter heading hierarchy restored).
Usage: python3 build_doc2.py <output.pdf>
"""
import re, sys, os, markdown
from weasyprint import HTML
here = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1]
SRC_PAGES = 24  # pp. 584-607
lines = open(f'{here}/doc2.md').read().splitlines()
fixed, prev = [], ''
for ln in lines:
    m = re.match(r'^( +)([-*] |\d+\. )', ln)
    if m:
        ln = ' ' * (len(m.group(1)) * 2) + ln[len(m.group(1)):]
    is_item = bool(re.match(r'^\s*([-*] |\d+\. )', ln))
    prev_item = bool(re.match(r'^\s*([-*] |\d+\. )', prev))
    if is_item and prev.strip() and not prev_item and not prev.startswith('<'):
        fixed.append('')
    fixed.append(ln); prev = ln
md = '\n'.join(fixed)
plain = re.sub(r'<[^>]+>', ' ', md)
words = len(re.findall(r"[A-Za-z0-9µ°%–\-'’αβ]+", re.sub(r'[*|#<>]', ' ', plain)))
html = markdown.markdown(md, extensions=['tables', 'md_in_html', 'sane_lists'])
def _blk(m):
    rows = m.group(2).count('<tr>')
    cls = 'tblock long' if rows > 9 else 'tblock'
    return f'<div class="{cls}"><p class="tcap">{m.group(1)}</p><table>{m.group(2)}</table></div>'
html = re.sub(r'<p><strong>([^<]+)</strong></p>\s*<table>(.*?)</table>', _blk, html, flags=re.S)
html = re.sub(r'<p><em>Concept —</em>\s*', r'<p class="concept"><strong>Concept —</strong> ', html)
html = re.sub(r'<div class="keypoints">\s*<p><strong>([^<]+)</strong></p>', r'<div class="keypoints"><p class="kptitle">\1</p>', html)
css = open(f'{here}/doc2.css').read()
title = 'Chapter 32 — Embryology of the Human Genitourinary Tract'
doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>{title} — Chapter Notes</title>
<style>{css}</style></head><body><h1>{title}<span class="sub">Chapter Notes — source pp. 584–607 (partial coverage)</span></h1>{html}</body></html>'''
open(f'{here}/doc2.html', 'w').write(doc)
HTML(string=doc).write_pdf(out)
print(f'words={words} per_page={words/SRC_PAGES:.0f} minutes={words/120:.1f}')
