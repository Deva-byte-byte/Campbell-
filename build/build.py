import sys, re, html
from weasyprint import HTML
from pathlib import Path
def words(path):
    t=Path(path).read_text()
    t=re.sub(r'<head>.*?</head>','',t,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t))
    return len([w for w in t.split() if re.search(r'\w',w)])
for src,out in [a.split('=') for a in sys.argv[1:]]:
    doc=HTML(src).render()
    doc.write_pdf(out)
    print(f"{out}: pages={len(doc.pages)} words={words(src)}")
