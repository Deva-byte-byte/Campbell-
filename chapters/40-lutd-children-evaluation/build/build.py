import re, sys, markdown
from weasyprint import HTML

TITLE = "Chapter 40 — Clinical and Urodynamic Evaluation of Lower Urinary Tract Dysfunction in Children"
OUT = "/home/user/Campbell-/chapters/40-lutd-children-evaluation/"

def md(path):
    h = markdown.markdown(open(path).read(), extensions=["tables", "md_in_html"])
    # table / comparison / figure titles → caps title class
    h = re.sub(r'<p><strong>([A-Z][A-Z0-9.\-]{2,}[^<]*)</strong>(.*?)</p>',
               lambda m: f'<p class="tt"><strong>{m.group(1)}</strong>{m.group(2)}</p>', h, flags=re.M)
    return h

BASE = """
@font-face{}
*{box-sizing:border-box}
html{font-family:Carlito,'DejaVu Sans',sans-serif;color:#000;hyphens:manual}
body{margin:0;text-align:left}
strong,b{font-weight:700}
h1,h2,h3,h4{break-after:avoid;page-break-after:avoid;color:#000}
p,li{orphans:2;widows:2}
"""

CSS2 = BASE + """
@page{size:A4;margin:18mm 18mm 18mm 20mm;
  @top-left{content:"Chapter 40 — Evaluation of Lower Urinary Tract Dysfunction in Children";font:8.5pt Carlito,'DejaVu Sans';color:#000;vertical-align:bottom;padding-bottom:1.5mm;border-bottom:0.3pt solid #000}
  @top-right{content:string(sec);font:8.5pt Carlito,'DejaVu Sans';color:#000;vertical-align:bottom;padding-bottom:1.5mm;border-bottom:0.3pt solid #000}
  @bottom-center{content:"page " counter(page) " of " counter(pages);font:9pt Carlito,'DejaVu Sans';color:#000}}
@page:first{@top-left{content:none;border:none}@top-right{content:none;border:none}}
body{font-size:11pt;line-height:1.4}
h1{font-size:20pt;line-height:1.2;margin:0 0 8pt;padding-bottom:5pt;border-bottom:1.5pt solid #000}
h2{font-size:14pt;text-transform:uppercase;margin:14pt 0 5pt;padding-bottom:2pt;border-bottom:1pt solid #000;string-set:sec content()}
h3{font-size:12.5pt;margin:10pt 0 3pt}
h4{font-size:11.5pt;margin:8pt 0 2pt}
p{margin:3pt 0}
ul,ol{margin:2pt 0 4pt;padding-left:5mm}
li{margin:0 0 2.5pt}
li>ul,li>ol{margin-top:2.5pt}
i.d{font-style:italic;font-weight:400}
.src{font-weight:400;text-transform:none;font-size:10pt}
p.tt{margin:9pt 0 2pt;text-transform:uppercase;break-after:avoid;font-size:10.5pt}
table{width:100%;border-collapse:collapse;font-size:10pt;line-height:1.3;margin:2pt 0 5pt;border-top:1pt solid #000;border-bottom:1pt solid #000}
thead{display:table-header-group}
th{text-align:left;vertical-align:bottom;border-bottom:0.5pt solid #000;padding:2.5pt 4pt;font-weight:700}
td{vertical-align:top;padding:2.5pt 4pt}
tbody tr:nth-child(even){background:#f2f2f2}
tr{break-inside:avoid}
p.concept{font-style:italic;margin:5pt 0 7pt;break-before:avoid;page-break-before:avoid}
p.concept b{font-style:italic}
.kp{border:0.75pt solid #000;padding:6pt;margin:8pt 0}
.kp ul{margin:0}
.kpt{font-weight:700;text-transform:uppercase;margin:0 0 3pt}
"""

CSS1 = BASE + """
@page{size:A4;margin:12mm 13mm;
  @bottom-center{content:counter(page);font:8pt Carlito,'DejaVu Sans';color:#000}}
body{font-size:9.4pt;line-height:1.25}
.cols{column-count:2;column-gap:7mm;column-fill:balance}
h1{font-size:14pt;margin:0 0 5pt;padding-bottom:3pt;border-bottom:1pt solid #000;column-span:all}
h2{font-size:10.4pt;text-transform:uppercase;margin:6pt 0 2pt;padding-bottom:1pt;border-bottom:0.5pt solid #000}
ul,ol{margin:0;padding-left:4mm}
li{margin:0 0 1pt}
p{margin:0}
.box{border:1pt solid #000;padding:4pt 6pt;margin:0 0 6pt;column-span:all}
.box ol{columns:2;column-gap:7mm}
.boxt{font-weight:700;text-transform:uppercase;margin-bottom:2pt}
.traps{background:#ececec;border-left:5pt double #000;padding:4pt 6pt;margin:6pt 0 0}
.traps ul{padding-left:3.5mm}
"""

def page(body, css, title):
    return f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{body}</body></html>'

b2 = md("doc2.md")
HTML(string=page(b2, CSS2, TITLE)).write_pdf(OUT + "Chapter 40 — Clinical and Urodynamic Evaluation of Lower Urinary Tract Dysfunction in Children — Chapter Notes.pdf")

b1 = md("doc1.md")
h1, rest = b1.split("</h1>", 1)
b1 = f'<div class="cols">{h1}</h1>{rest}</div>'
HTML(string=page(b1, CSS1, TITLE)).write_pdf(OUT + "Chapter 40 — Clinical and Urodynamic Evaluation of Lower Urinary Tract Dysfunction in Children — Numbers, Gold Standards and Traps.pdf")
open("doc2.html","w").write(page(b2, CSS2, TITLE)); open("doc1.html","w").write(page(b1, CSS1, TITLE))
