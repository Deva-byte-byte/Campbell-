"""Compile Chapter 110 session notes into the two print PDFs (WeasyPrint)."""
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

HERE = Path(__file__).parent
TITLE = "Chapter 110 — Overactive Bladder"

DOC2_CSS = """
@page {
  size: A4; margin: 18mm 18mm 18mm 20mm;
  @top-left { content: "Chapter 110 — Overactive Bladder"; font: 8.5pt Carlito, 'DejaVu Sans'; color: #000;
              border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }
  @top-right { content: string(sect); font: 8.5pt Carlito, 'DejaVu Sans'; color: #000;
               border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }
  @bottom-center { content: "page " counter(page) " of " counter(pages); font: 9pt Carlito, 'DejaVu Sans'; color: #000; }
}
html { font-family: Carlito, 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.4; color: #000; }
body { margin: 0; text-align: left; hyphens: manual; orphans: 2; widows: 2; }
h1, h2, h3, h4 { break-after: avoid; color: #000; line-height: 1.2; }
h1 { font-size: 20pt; font-weight: bold; margin: 0 0 10pt; padding-bottom: 4pt; border-bottom: 1.5pt solid #000; }
h2 { font-size: 14pt; font-weight: bold; text-transform: uppercase; margin: 14pt 0 5pt; padding-bottom: 2pt;
     border-bottom: 1pt solid #000; string-set: sect content(); }
h3 { font-size: 12.5pt; font-weight: bold; margin: 10pt 0 3pt; }
h4 { font-size: 11.5pt; font-weight: bold; margin: 8pt 0 2pt; }
p { margin: 3pt 0; }
ul, ol { margin: 2pt 0 4pt; padding-left: 14pt; }
li { margin: 0 0 2.5pt; }
li > ul { margin-top: 2.5pt; }
em { font-style: italic; }
p > em:first-child { font-weight: normal; }
.tt { font-weight: bold; text-transform: uppercase; margin: 9pt 0 2pt; break-after: avoid; font-size: 10.5pt; }
.src { font-size: 10pt; margin: 1pt 0 5pt; }
table { width: 100%; border-collapse: collapse; font-size: 10pt; line-height: 1.3; margin: 2pt 0 5pt;
        border-top: 1pt solid #000; border-bottom: 1pt solid #000; }
thead { display: table-header-group; }
th { text-align: left; vertical-align: bottom; border-bottom: 0.5pt solid #000; padding: 3pt 4pt; font-weight: bold; }
td { vertical-align: top; padding: 2.5pt 4pt; }
tbody tr:nth-child(even) td { background: #f2f2f2; }
tr { break-inside: avoid; }
.kp { border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }
.kp ul { margin-bottom: 0; }
.kpt { font-weight: bold; text-transform: uppercase; margin: 0 0 3pt; }
.concept { font-style: italic; margin: 5pt 0 6pt; break-before: avoid; }
.concept b { font-style: normal; }
"""


def strip_session(md: str) -> str:
    return re.sub(r"<!--S-->.*?<!--/S-->", "", md, flags=re.S)


def build_doc2() -> Path:
    md = strip_session((HERE / "session-notes.md").read_text())
    body = markdown.markdown(md, extensions=["tables", "md_in_html"])
    html = f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{TITLE} — Chapter Notes</title>" \
           f"<style>{DOC2_CSS}</style></head><body>{body}</body></html>"
    (HERE / "doc2.html").write_text(html)
    out = HERE / f"{TITLE} — Chapter Notes.pdf"
    HTML(string=html, base_url=str(HERE)).write_pdf(out)
    return out


def build_doc1() -> Path:
    html = (HERE / "doc1.html").read_text()
    out = HERE / f"{TITLE} — Numbers, Gold Standards and Traps.pdf"
    HTML(string=html, base_url=str(HERE)).write_pdf(out)
    return out


if __name__ == "__main__":
    which = sys.argv[1:] or ["1", "2"]
    if "2" in which:
        print(build_doc2())
    if "1" in which:
        print(build_doc1())
