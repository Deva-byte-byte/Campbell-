import sys, re, weasyprint, html
from pathlib import Path
here=Path(__file__).parent
out=here.parent
jobs={'notes.html':'Chapter 112 — Nocturia — Chapter Notes.pdf','sheet.html':'Chapter 112 — Nocturia — Numbers, Gold Standards and Traps.pdf'}
for src,dst in jobs.items():
    if len(sys.argv)>1 and src not in sys.argv[1:]: continue
    p=here/src
    if not p.exists(): continue
    doc=weasyprint.HTML(filename=str(p)).render()
    doc.write_pdf(str(out/dst))
    body=re.sub(r'<style.*?</style>|<head.*?</head>','',p.read_text(),flags=re.S)
    body=re.sub(r'<!--.*?-->','',body,flags=re.S)
    text=html.unescape(re.sub(r'<[^>]+>',' ',body))
    print(dst, 'pages:',len(doc.pages),'words:',len(text.split()))
