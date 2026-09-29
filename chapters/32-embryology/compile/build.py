"""Render Chapter 32 Document 1 (cheat sheet) and Document 2 (chapter notes) with WeasyPrint."""
import pathlib
import markdown
from weasyprint import HTML

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent
CHAPTER = "Chapter 32 — Embryology of the Human Genitourinary Tract"
FONT = "'Carlito', 'DejaVu Sans', sans-serif"

COMMON = f"""
html {{ font-family: {FONT}; color: #000; hyphens: manual; }}
body {{ margin: 0; text-align: left; }}
h1, h2, h3, h4, .tcap, .lvd, .kpt, .boxt {{ break-after: avoid; }}
p, li {{ orphans: 2; widows: 2; }}
strong {{ font-weight: bold; }}
"""

DOC2_CSS = COMMON + f"""
@page {{
  size: A4; margin: 18mm 18mm 18mm 20mm;
  @top-left {{ width: 50%; content: "{CHAPTER}"; font-size: 8.5pt; color: #000; border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }}
  @top-right {{ width: 50%; text-align: right; content: string(section, start); font-size: 8.5pt; color: #000; border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }}
  @bottom-center {{ content: "page " counter(page) " of " counter(pages); font-size: 9pt; color: #000; }}
}}
body {{ font-size: 11pt; line-height: 1.4; }}
h1 {{ font-size: 20pt; font-weight: bold; margin: 0 0 8pt; padding-bottom: 4pt; border-bottom: 1.5pt solid #000; line-height: 1.2; }}
h2 {{ string-set: section content(); font-size: 14pt; font-weight: bold; text-transform: uppercase; margin: 14pt 0 5pt; padding-bottom: 2pt; border-bottom: 1pt solid #000; line-height: 1.2; }}
h3 {{ font-size: 12.5pt; font-weight: bold; margin: 9pt 0 3pt; line-height: 1.25; }}
h4 {{ font-size: 11.5pt; font-weight: bold; margin: 6pt 0 2pt; }}
.lvd {{ font-size: 11pt; font-style: italic; margin: 6pt 0 1pt; }}
p {{ margin: 3pt 0; }}
ul, ol {{ margin: 2pt 0 4pt; padding-left: 14pt; }}
li {{ margin: 0 0 2.5pt; }}
li > ul, li > ol {{ margin: 2pt 0 0; }}
.concept {{ font-size: 11pt; margin: 5pt 0 6pt; break-before: avoid; }}
.kp {{ border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }}
.kpt {{ font-weight: bold; text-transform: uppercase; margin: 0 0 3pt; }}
.kp ul {{ margin-bottom: 0; }}
.tcap {{ font-weight: bold; text-transform: uppercase; font-size: 10pt; margin: 8pt 0 2pt; }}
.tsrc {{ font-size: 10pt; margin: 1pt 0 4pt; }}
table {{ width: 100%; border-collapse: collapse; font-size: 10pt; line-height: 1.3; border-top: 1pt solid #000; border-bottom: 1pt solid #000; margin: 2pt 0 5pt; }}
thead {{ display: table-header-group; }}
th {{ text-align: left; font-weight: bold; border-bottom: 0.5pt solid #000; padding: 2.5pt 4pt; vertical-align: bottom; }}
td {{ padding: 2.5pt 4pt; vertical-align: top; }}
tbody tr:nth-child(even) td {{ background: #f2f2f2; }}
tr {{ break-inside: avoid; }}
"""

DOC1_CSS = COMMON + """
@page {
  size: A4; margin: 12mm 13mm 12mm 13mm;
  @bottom-center { content: counter(page); font-size: 8pt; color: #000; }
}
body { font-size: 9.4pt; line-height: 1.25; }
.cols { column-count: 2; column-gap: 7mm; }
h1 { column-span: all; font-size: 14pt; font-weight: bold; margin: 0 0 5pt; padding-bottom: 3pt; border-bottom: 1pt solid #000; }
h2 { font-size: 10.4pt; font-weight: bold; text-transform: uppercase; margin: 7pt 0 3pt; padding-bottom: 1pt; border-bottom: 0.5pt solid #000; line-height: 1.2; }
p { margin: 0; }
ul { margin: 0; padding-left: 10pt; }
li { margin: 0 0 1pt; }
.box { column-span: all; border: 1pt solid #000; padding: 4pt 6pt; margin: 0 0 6pt; }
.box ul { column-count: 2; column-gap: 7mm; }
.boxt { font-weight: bold; text-transform: uppercase; margin: 0 0 2pt; }
.traps { background: #ececec; border-left: 5pt double #000; padding: 4pt 6pt; margin: 8pt 0 0; }
"""


def md(text):
    return markdown.markdown(text, extensions=["tables", "md_in_html"])


def render(src, css, out, wrap_cols=False):
    body = md((HERE / src).read_text())
    if wrap_cols:
        # title spans; everything else flows in two columns
        h1_end = body.index("</h1>") + 5
        body = body[:h1_end] + '<div class="cols">' + body[h1_end:] + "</div>"
    html = f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{CHAPTER}</title><style>{css}</style></head><body>{body}</body></html>"
    doc = HTML(string=html).render()
    doc.write_pdf(OUT / out)
    return len(doc.pages)


if __name__ == "__main__":
    n1 = render("doc1.md", DOC1_CSS, f"{CHAPTER} — Numbers, Gold Standards and Traps.pdf", wrap_cols=True)
    n2 = render("doc2.md", DOC2_CSS, f"{CHAPTER} — Chapter Notes.pdf")
    print("doc1 pages", n1, "doc2 pages", n2)
