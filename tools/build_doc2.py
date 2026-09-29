"""Build Document 2 (Chapter Notes) from session instalment files.

Strips instalment scaffolding, numbers-to-lock-in blocks and source-flag
appendices; restores the chapter's own heading hierarchy; renders with WeasyPrint.
Usage: python3 build_doc2.py <chapter-dir> <chapter title> <output.pdf> <source pages> [compile-source.md ...]
"""
import re, sys, glob, markdown
from weasyprint import HTML

chdir, title, out, src_pages = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])

def body_of(text):
    lines, keep, seen_a, out_lines = text.splitlines(), False, set(), []
    for ln in lines:
        if ln.startswith('## Instalment'):
            keep = True; continue
        if ln.startswith('## The numbers to lock in') or ln.startswith('## Source flags'):
            keep = False; continue
        if not keep or ln.strip() == '---':
            continue
        out_lines.append(ln)
    return out_lines

lines = []
if len(sys.argv) > 5:
    # Pre-tightened compile source (already stripped of session scaffolding)
    for f in sys.argv[5:]:
        lines += open(f).read().splitlines()
else:
    for f in sorted(glob.glob(f'{chdir}/session-instalments-*.md')):
        lines += body_of(open(f).read())

# Merge duplicate Level A heads (a Level A section can span instalment files)
res, seen = [], set()
for ln in lines:
    if ln.startswith('### '):
        if ln in seen: continue
        seen.add(ln)
    res.append(ln)
lines = res

# Session-only cross-references never print
lines = [re.sub(r'\s*\(see the source flags\)', '', l) for l in lines]

# python-markdown: 4-space nesting, blank line before lists
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

words = len(re.findall(r"[A-Za-z0-9µ°%–\-']+", re.sub(r'[*|#<>]', ' ', md)))

html = markdown.markdown(md, extensions=['tables', 'md_in_html', 'sane_lists'])
html = re.sub(r'<p><strong>([^<]+)</strong></p>\s*<table>', r'<table><caption>\1</caption>', html)
html = re.sub(r'<p><em>Concept —</em>\s*', r'<p class="concept"><strong>Concept —</strong> ', html)
html = re.sub(r'<div class="keypoints">\s*<p><strong>([^<]+)</strong></p>',
              r'<div class="keypoints"><p class="kptitle">\1</p>', html)
html = re.sub(r'<p><strong>(FIG\. [^<]+)</strong>', r'<p class="fig"><strong>\1</strong>', html)

css = open(f'{chdir}/../tools/doc2.css').read()
doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body><h1>{title}</h1>{html}</body></html>'''
open(out.replace('.pdf', '.html'), 'w').write(doc)
pdf = HTML(string=doc).write_pdf()
open(out, 'wb').write(pdf)
print(f'words={words} per_page={words/src_pages:.0f} minutes={words/120:.1f}')
