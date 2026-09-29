import markdown, sys, re
from weasyprint import HTML
TITLE="Chapter 46 — Neuromuscular Dysfunction of the Lower Urinary Tract in Children"
def conv(p):
    src=re.sub(r'(?m)^  (?=- )','    ',open(p).read())
    return markdown.markdown(src, extensions=['tables','md_in_html'])
COMMON="""
@font-face{}
*{color:#000}
body{font-family:Carlito,'DejaVu Sans',sans-serif;color:#000;background:#fff;hyphens:manual;text-align:left}
h1,h2,h3,h4,h5,p.tcap{break-after:avoid;page-break-after:avoid}
p,li{orphans:2;widows:2}
b,strong{font-weight:bold}
"""
CSS2=COMMON+"""
@page{size:A4;margin:18mm 18mm 18mm 20mm;
 @top-left{content:"%s";font:8.5pt Carlito,'DejaVu Sans';color:#000;border-bottom:0.3pt solid #000;vertical-align:bottom;padding-bottom:2pt}
 @top-right{content:string(sec);font:8.5pt Carlito,'DejaVu Sans';color:#000;border-bottom:0.3pt solid #000;vertical-align:bottom;padding-bottom:2pt}
 @bottom-center{content:"page " counter(page) " of " counter(pages);font:9pt Carlito,'DejaVu Sans';color:#000}}
body{font-size:11pt;line-height:1.4}
h1{font-size:20pt;font-weight:bold;border-bottom:1.5pt solid #000;padding-bottom:4pt;margin:0 0 10pt;line-height:1.2}
h2{font-size:14pt;font-weight:bold;text-transform:uppercase;border-bottom:1pt solid #000;padding-bottom:2pt;margin:13pt 0 5pt;string-set:sec content();line-height:1.25}
h3{font-size:12.5pt;font-weight:bold;margin:8pt 0 3pt}
h4{font-size:11.5pt;font-weight:bold;margin:8pt 0 3pt}
p{margin:3pt 0}
p em:only-child{font-style:italic}
ul{margin:2pt 0 4pt;padding-left:14pt}
li{margin:0 0 2.5pt}
li>ul{margin-top:2.5pt}
table{width:100%%;border-collapse:collapse;font-size:10pt;line-height:1.3;border-top:1pt solid #000;border-bottom:1pt solid #000;margin:3pt 0 6pt}
thead{display:table-header-group}
th{text-align:left;font-weight:bold;border-bottom:0.5pt solid #000;padding:3pt 4pt;vertical-align:bottom}
td{padding:2.5pt 4pt;vertical-align:top}
tbody tr:nth-child(even){background:#f2f2f2}
tr{break-inside:auto}
p.tcap{font-weight:bold;text-transform:uppercase;margin:7pt 0 2pt;font-size:10.5pt}
p.tnote{font-size:10pt;margin:0 0 5pt}
div.kp,div.figs{border:0.75pt solid #000;padding:6pt;margin:8pt 0}
p.kpt{font-weight:bold;text-transform:uppercase;margin:0 0 3pt}
p.concept{font-style:italic;margin:6pt 0 4pt;break-before:avoid;page-break-before:avoid}
p.concept b{font-style:italic}
"""%TITLE
CSS1=COMMON+"""
@page{size:A4;margin:12mm 13mm;@bottom-center{content:counter(page);font:8pt Carlito,'DejaVu Sans';color:#000}}
body{font-size:9.4pt;line-height:1.25;columns:2;column-gap:7mm;column-fill:auto}
h1{column-span:all;font-size:14pt;font-weight:bold;border-bottom:1pt solid #000;padding-bottom:3pt;margin:0 0 6pt}
h2{font-size:10.4pt;font-weight:bold;text-transform:uppercase;border-bottom:0.5pt solid #000;margin:7pt 0 3pt;padding-bottom:1pt}
ul{margin:0;padding-left:10pt}
li{margin:0 0 1pt}
li>ul{margin-top:1pt}
p{margin:0}
div.top{column-span:all;border:1pt solid #000;padding:5pt 7pt;margin:0 0 6pt}
div.top ul{columns:2;column-gap:7mm}
div.traps{background:#ececec;border-left:5pt double #000;padding:5pt 6pt;margin:7pt 0 0}
p.boxt{font-weight:bold;text-transform:uppercase;margin:0 0 3pt}
"""
def build(md,css,out):
    html=f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>{css}</style></head><body>{conv(md)}</body></html>'
    open(md.replace('.md','.html'),'w').write(html)
    doc=HTML(string=html).render(); doc.write_pdf(out); print(out,len(doc.pages),'pages')
build('doc2.md',CSS2,'../Chapter 46 — Neuromuscular Dysfunction of the Lower Urinary Tract in Children — Chapter Notes.pdf')
build('doc1.md',CSS1,'../Chapter 46 — Neuromuscular Dysfunction of the Lower Urinary Tract in Children — Numbers, Gold Standards and Traps.pdf')
