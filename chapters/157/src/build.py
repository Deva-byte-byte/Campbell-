"""Build Chapter 157 session record (Markdown) and the two print PDFs (WeasyPrint)."""
from pathlib import Path
import markdown
from weasyprint import HTML

SRC = Path(__file__).parent
OUT = SRC.parent
TITLE = "Chapter 157 — Diagnosis and Staging of Prostate Cancer"
read = lambda n: (SRC / n).read_text()


def md(text):
    return markdown.markdown(text, extensions=["tables", "md_in_html"])


# Markdown inside HTML blocks needs markdown="1"
def prep(text):
    return (text.replace('<div class="kp">', '<div class="kp" markdown="1">')
                .replace('<div class="top">', '<div class="top" markdown="1">')
                .replace('<div class="traps">', '<div class="traps" markdown="1">'))


# ---------- Session record ----------
a, b = read("a_diagnosis.md"), read("b_staging.md")
session = "\n\n".join([
    f"# {TITLE} — Session Record",
    "## Instalment 1 — Presentation, Screening Concepts, ERSPC and PLCO, Guideline Recommendations, "
    "Digital Rectal Examination, Factors Influencing PSA, 5α-Reductase Inhibitors, Table 157.1, "
    "Biopsy Triggers, PSA Density, Velocity, Free and Complexed PSA, Isoforms, hK2, Multiplex Tests, Other Markers",
    a,
    read("n1.md"),
    "## Instalment 2 — Clinical vs Pathological Staging, TNM (Table 157.2), PSA and DRE for Extent, "
    "Needle Biopsy and Grade Groups, D'Amico and CAPRA, MRI, Staging Imaging, PSMA PET, "
    "Molecular Staging, Pelvic Lymphadenectomy, Key Points",
    b,
    read("n2.md"),
    read("flags.md"),
])
(OUT / f"{TITLE} — Session Record.md").write_text(session)

# ---------- Shared CSS ----------
BASE = """
@font-face{font-family:C;src:local('Carlito')}
*{color:#000}
body{font-family:Carlito,'DejaVu Sans',sans-serif;hyphens:none;text-align:left}
h1,h2,h3,h4,h5,.tt,.bt,.kpt{break-after:avoid}
p,li{orphans:2;widows:2}
ul{margin:0;padding-left:1.1em}
strong{font-weight:700}
"""

DOC2_CSS = BASE + """
@page{size:A4;margin:18mm 18mm 18mm 20mm;
  @top-left{content:string(chap);font:8.5pt Carlito;vertical-align:bottom;padding-bottom:1.5mm;border-bottom:0.3pt solid #000}
  @top-right{content:string(sec);font:8.5pt Carlito;vertical-align:bottom;padding-bottom:1.5mm;border-bottom:0.3pt solid #000}
  @bottom-center{content:"page " counter(page) " of " counter(pages);font:9pt Carlito}}
body{font-size:11pt;line-height:1.4}
h1{font-size:20pt;font-weight:700;margin:0 0 8pt;padding-bottom:4pt;border-bottom:1.5pt solid #000;string-set:chap content()}
h2{font-size:14pt;font-weight:700;text-transform:uppercase;margin:14pt 0 5pt;padding-bottom:2pt;border-bottom:1pt solid #000;string-set:sec content()}
h3{font-size:12.5pt;font-weight:700;margin:9pt 0 3pt}
h4{font-size:11.5pt;font-weight:700;margin:7pt 0 2pt}
h5{font-size:11pt;font-style:italic;font-weight:400;margin:5pt 0 1pt}
li{margin:0 0 2.5pt}
p{margin:0 0 4pt}
table{width:100%;border-collapse:collapse;border-top:1pt solid #000;border-bottom:1pt solid #000;font-size:10pt;line-height:1.3;margin:2pt 0 5pt}
thead th{border-bottom:0.5pt solid #000;text-align:left;font-weight:700;padding:2pt 4pt;vertical-align:bottom}
td{padding:2pt 4pt;vertical-align:top}
tbody tr:nth-child(even){background:#f2f2f2}
thead{display:table-header-group}
.tt{font-weight:700;text-transform:uppercase;font-size:10pt;margin:7pt 0 2pt}
.src{font-size:10pt;margin:0 0 4pt}
.concept{font-style:italic;break-before:avoid;margin:4pt 0 6pt}
.concept strong{font-style:normal}
.kp{border:0.75pt solid #000;padding:6pt;margin-top:12pt}
.kpt{font-weight:700;text-transform:uppercase;margin:0 0 3pt}
"""

DOC1_CSS = BASE + """
@page{size:A4;margin:12mm 13mm;@bottom-center{content:counter(page);font:8pt Carlito}}
body{font-size:9.4pt;line-height:1.25;columns:2;column-gap:7mm}
h1{column-span:all;font-size:14pt;font-weight:700;margin:0 0 5pt;padding-bottom:3pt;border-bottom:1pt solid #000}
h2{font-size:10.4pt;font-weight:700;text-transform:uppercase;margin:6pt 0 3pt;border-bottom:0.5pt solid #000}
li{margin:0 0 1pt}
p{margin:0}
.bt{font-weight:700;text-transform:uppercase;margin:0 0 2pt}
.top{column-span:all;border:1pt solid #000;padding:4pt 6pt;margin:0 0 6pt}
.traps{background:#ececec;border-left:5pt double #000;padding:4pt 6pt;margin-top:8pt}
"""


def render(body_md, css, out, title):
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{css}</style></head><body>{md(prep(body_md))}</body></html>"
    HTML(string=html).write_pdf(out)


doc2_md = f"# {TITLE}\n\n{a}\n\n{b}"
render(doc2_md, DOC2_CSS, OUT / f"{TITLE} — Chapter Notes.pdf", TITLE)
render(read("doc1.md"), DOC1_CSS, OUT / f"{TITLE} — Numbers, Gold Standards and Traps.pdf", TITLE)
print("built")
