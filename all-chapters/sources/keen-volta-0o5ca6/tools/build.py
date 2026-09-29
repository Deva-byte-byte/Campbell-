#!/usr/bin/env python3
"""Render a chapter's notes.md and cheatsheet.md to the two print PDFs.

Usage: build.py <chapter-dir> "<Chapter NN — Title>"
"""
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

FONT = "Carlito, 'DejaVu Sans', sans-serif"

NOTES_CSS = """
@page {
  size: A4;
  margin: 18mm 18mm 18mm 20mm;
  @top-left {
    content: "%(title)s"; font: 8.5pt %(font)s; color: #000;
    vertical-align: bottom; padding-bottom: 2pt; border-bottom: 0.3pt solid #000;
  }
  @top-right {
    content: string(section); font: 8.5pt %(font)s; color: #000;
    vertical-align: bottom; padding-bottom: 2pt; border-bottom: 0.3pt solid #000;
  }
  @bottom-center {
    content: "page " counter(page) " of " counter(pages);
    font: 9pt %(font)s; color: #000;
  }
}
html { font-family: %(font)s; font-size: 11pt; line-height: 1.4; color: #000; background: #fff; }
body { margin: 0; text-align: left; hyphens: manual; orphans: 2; widows: 2; }
h1, h2, h3, h4 { color: #000; break-after: avoid; line-height: 1.2; }
h1 { font-size: 20pt; font-weight: bold; border-bottom: 1.5pt solid #000; padding-bottom: 4pt; margin: 0 0 8pt; }
h2 { font-size: 14pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #000;
     padding-bottom: 2pt; margin: 14pt 0 5pt; string-set: section content(); }
h3 { font-size: 12.5pt; font-weight: bold; margin: 10pt 0 3pt; }
h4 { font-size: 11.5pt; font-weight: bold; margin: 8pt 0 3pt; }
p { margin: 3pt 0; }
p > em:first-child { font-style: italic; }
ul, ol { margin: 2pt 0 4pt; padding-left: 14pt; }
li { margin: 0 0 2.5pt; }
li > ul, li > ol { margin-top: 2.5pt; margin-bottom: 0; }
.concept { font-style: italic; break-before: avoid; margin: 5pt 0 4pt; }
.concept b { font-style: italic; }
.kp { border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }
.kp ul { margin-bottom: 0; }
.kpt { font-weight: bold; text-transform: uppercase; margin: 0 0 3pt; }
.tcap { font-weight: bold; text-transform: uppercase; margin: 9pt 0 3pt; break-after: avoid; font-size: 10.5pt; }
.tsrc { font-size: 9pt; margin: 2pt 0 5pt; }
table { width: 100%%; border-collapse: collapse; border-top: 1pt solid #000; border-bottom: 1pt solid #000;
        font-size: 10pt; line-height: 1.3; margin: 0 0 5pt; }
thead { display: table-header-group; }
th { text-align: left; vertical-align: bottom; border-bottom: 0.5pt solid #000; padding: 3pt 4pt; font-weight: bold; }
td { text-align: left; vertical-align: top; padding: 3pt 4pt; }
tbody tr:nth-child(even) { background: #f2f2f2; }
tr { break-inside: avoid; }
"""

SHEET_CSS = """
@page {
  size: A4;
  margin: 12mm 13mm;
  @bottom-center { content: counter(page); font: 8pt %(font)s; color: #000; }
}
html { font-family: %(font)s; font-size: 9.4pt; line-height: 1.25; color: #000; background: #fff; }
body { margin: 0; text-align: left; hyphens: manual; orphans: 2; widows: 2; }
h1 { font-size: 14pt; font-weight: bold; border-bottom: 1pt solid #000; padding-bottom: 2pt; margin: 0 0 5pt; break-after: avoid; }
.cols { column-count: 2; column-gap: 7mm; }
h2 { font-size: 10.4pt; font-weight: bold; text-transform: uppercase; border-bottom: 0.5pt solid #000;
     margin: 6pt 0 2pt; padding-bottom: 1pt; break-after: avoid; }
h2:first-child { margin-top: 0; }
p { margin: 2pt 0; break-after: avoid; }
ul { margin: 0 0 2pt; padding-left: 10pt; }
li { margin: 0 0 1pt; }
.top { border: 1pt solid #000; padding: 4pt 6pt; margin: 0 0 6pt; }
.top ul { column-count: 2; column-gap: 7mm; }
.traps { background: #ececec; border-left: 5pt double #000; padding: 4pt 6pt; margin: 6pt 0 0; }
.boxt { font-weight: bold; text-transform: uppercase; margin: 0 0 2pt; }
"""


def md(text):
    return markdown.markdown(text, extensions=["tables", "md_in_html", "sane_lists"])


def page(title, css, body):
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{title}</title><style>{css}</style></head><body>{body}</body></html>"""


def build(chapter_dir, title):
    d = Path(chapter_dir)
    fill = {"title": title.replace('"', '\\"'), "font": FONT}

    notes = page(title, NOTES_CSS % fill, md((d / "notes.md").read_text()))
    (d / "notes.html").write_text(notes)
    HTML(string=notes, base_url=str(d)).write_pdf(d / f"{title} — Chapter Notes.pdf")

    # Cheat sheet: title and top box span both columns; the rest flows in two.
    src = (d / "cheatsheet.md").read_text()
    head, rest = src.split("\n## ", 1)
    body = md(head) + '<div class="cols">' + md("## " + rest) + "</div>"
    sheet = page(title, SHEET_CSS % fill, body)
    (d / "cheatsheet.html").write_text(sheet)
    HTML(string=sheet, base_url=str(d)).write_pdf(
        d / f"{title} — Numbers, Gold Standards and Traps.pdf")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
