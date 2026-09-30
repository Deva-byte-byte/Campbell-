import sys, re, html, subprocess, os
from weasyprint import HTML
B = os.path.dirname(os.path.abspath(__file__))
def wrap(body, css, title):
    return f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{title}</title><link rel="stylesheet" href="{css}"></head><body>{body}</body></html>'
def words(body):
    t = re.sub(r'<[^>]+>', ' ', body); t = html.unescape(t)
    return len(t.split())
def render(src, css, out):
    body = open(os.path.join(B, src), encoding='utf-8').read()
    doc = HTML(string=wrap(body, css, os.path.basename(out)), base_url=B).render()
    doc.write_pdf(out)
    return len(doc.pages), words(body)
if __name__ == '__main__':
    src, css, out = sys.argv[1:4]
    n, w = render(src, css, out)
    print(f'{out}: pages={n} words={w}')
