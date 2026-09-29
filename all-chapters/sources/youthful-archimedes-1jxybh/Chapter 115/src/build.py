"""Render Chapter 115 notes and cheat sheet to A4 PDFs with WeasyPrint."""
import pathlib, re, html
from weasyprint import HTML

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent
TITLE = "Chapter 115 — Electrical Stimulation and Neuromodulation in Storage and Emptying Failure"
SHORT = "Chapter 115 — Electrical Stimulation and Neuromodulation"

BASE = """
html { font-family: Carlito, 'DejaVu Sans', sans-serif; color: #000; hyphens: manual; }
body { margin: 0; color: #000; text-align: left; orphans: 2; widows: 2; }
h1, h2, h3, h4, .lvd, .tcap, .boxt, .kpt { break-after: avoid; page-break-after: avoid; color: #000; }
ul { margin: 0; padding-left: 1.1em; }
b, strong { font-weight: 700; }
"""

NOTES_CSS = BASE + f"""
@page {{
  size: A4; margin: 18mm 18mm 18mm 20mm;
  @top-left {{ content: "{SHORT}"; font-size: 8.5pt; width: 55%; border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }}
  @top-right {{ content: string(section); font-size: 8.5pt; width: 45%; text-align: right; border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }}
  @bottom-center {{ content: "page " counter(page) " of " counter(pages); font-size: 9pt; }}
}}
body {{ font-size: 11pt; line-height: 1.4; }}
h1 {{ font-size: 20pt; font-weight: 700; line-height: 1.2; margin: 0 0 10pt; padding-bottom: 5pt; border-bottom: 1.5pt solid #000; }}
h2 {{ font-size: 14pt; font-weight: 700; text-transform: uppercase; margin: 14pt 0 5pt; padding-bottom: 2pt; border-bottom: 1pt solid #000; string-set: section content(text); line-height: 1.2; }}
h3 {{ font-size: 12.5pt; font-weight: 700; margin: 9pt 0 3pt; line-height: 1.25; }}
h4 {{ font-size: 11.5pt; font-weight: 700; margin: 6pt 0 2pt; }}
.lvd {{ font-size: 11pt; font-style: italic; margin: 5pt 0 1pt; }}
li {{ margin-bottom: 2.5pt; }}
.concept {{ font-size: 11pt; margin: 5pt 0 4pt; break-before: avoid; page-break-before: avoid; }}
.tcap {{ font-weight: 700; text-transform: uppercase; font-size: 10pt; margin: 8pt 0 2pt; }}
table {{ width: 100%; border-collapse: collapse; font-size: 10pt; line-height: 1.3; border-top: 1pt solid #000; border-bottom: 1pt solid #000; margin: 0 0 5pt; }}
thead {{ display: table-header-group; }}
th {{ text-align: left; font-weight: 700; border-bottom: 0.5pt solid #000; padding: 3pt 4pt; vertical-align: bottom; }}
td {{ padding: 2.5pt 4pt; vertical-align: top; }}
tbody tr:nth-child(even) td {{ background: #f2f2f2; }}
tr {{ break-inside: avoid; }}
.kp {{ border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }}
.kpt {{ font-weight: 700; text-transform: uppercase; margin: 0 0 3pt; }}
"""

SHEET_CSS = BASE + """
@page { size: A4; margin: 12mm 13mm 12mm 13mm;
  @bottom-center { content: counter(page); font-size: 8pt; } }
body { font-size: 9.4pt; line-height: 1.25; column-count: 2; column-gap: 7mm; }
h1 { column-span: all; font-size: 14pt; font-weight: 700; margin: 0 0 5pt; padding-bottom: 3pt; border-bottom: 1pt solid #000; line-height: 1.15; }
h2 { font-size: 10.4pt; font-weight: 700; text-transform: uppercase; margin: 6pt 0 2pt; padding-bottom: 1pt; border-bottom: 0.5pt solid #000; line-height: 1.15; }
li { margin-bottom: 1pt; }
.box { column-span: all; border: 1pt solid #000; padding: 4pt 6pt; margin: 0 0 4pt; }
.box ul { columns: 2; column-gap: 7mm; }
.boxt { font-weight: 700; text-transform: uppercase; margin: 0 0 2pt; }
.traps { background: #ececec; border-left: 5pt double #000; padding: 4pt 6pt; margin: 6pt 0 0; }
"""

def page(body, css, title):
    return f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{title}</title><style>{css}</style></head><body>{body}</body></html>"

def words(src):
    return len(html.unescape(re.sub(r"<[^>]+>", " ", src)).split())

notes = (HERE / "notes.html").read_text()
sheet = (HERE / "cheatsheet.html").read_text()
n_pdf = OUT / f"{TITLE} — Chapter Notes.pdf"
s_pdf = OUT / f"{TITLE} — Numbers, Gold Standards and Traps.pdf"
nd = HTML(string=page(notes, NOTES_CSS, "Chapter 115 Notes")).render()
sd = HTML(string=page(sheet, SHEET_CSS, "Chapter 115 Cheat Sheet")).render()
nd.write_pdf(n_pdf); sd.write_pdf(s_pdf)
nw, sw = words(notes), words(sheet)
print(f"Notes: {len(nd.pages)} pages, {nw} words, {nw/120:.0f} min at 120 wpm")
print(f"Cheat sheet: {len(sd.pages)} sides, {sw} words")
