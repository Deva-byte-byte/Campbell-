"""Render Chapter 165 notes and cheat sheet to PDF with WeasyPrint."""
import re
import sys

import markdown
from weasyprint import HTML

TITLE = "Chapter 165 — Management of Recurrent and Newly Metastatic Prostate Cancer"

NOTES_CSS = """
@page {
  size: A4; margin: 18mm 18mm 18mm 20mm;
  @top-left { content: "%(title)s"; font: 8.5pt Carlito, 'DejaVu Sans'; color: #000;
              border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }
  @top-right { content: string(sect); font: 8.5pt Carlito, 'DejaVu Sans'; color: #000;
               border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }
  @bottom-center { content: "page " counter(page) " of " counter(pages);
                   font: 9pt Carlito, 'DejaVu Sans'; color: #000; }
}
html { font-family: Carlito, 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.4;
       color: #000; hyphens: manual; text-align: left; }
body { margin: 0; }
h1, h2, h3, h4, h5, h6 { break-after: avoid; color: #000; }
h1 { font-size: 20pt; font-weight: bold; margin: 0 0 10pt; padding-bottom: 4pt;
     border-bottom: 1.5pt solid #000; line-height: 1.2; }
h2 { font-size: 14pt; font-weight: bold; text-transform: uppercase; margin: 16pt 0 6pt;
     padding-bottom: 2pt; border-bottom: 1pt solid #000; string-set: sect content(); line-height: 1.25; }
h3 { font-size: 12.5pt; font-weight: bold; margin: 10pt 0 4pt; }
h4 { font-size: 11.5pt; font-weight: bold; margin: 8pt 0 3pt; }
h5 { font-size: 11pt; font-style: italic; font-weight: normal; margin: 6pt 0 2pt; }
p { margin: 3pt 0; orphans: 2; widows: 2; }
ul, ol { margin: 2pt 0 4pt; padding-left: 14pt; }
li { margin: 0 0 2.5pt; orphans: 2; widows: 2; }
li > ul, li > ol { margin-top: 2.5pt; }
table { width: 100%%; border-collapse: collapse; margin: 6pt 0 5pt; font-size: 10pt; line-height: 1.3;
        border-top: 1pt solid #000; border-bottom: 1pt solid #000; }
thead { display: table-header-group; }
th { text-align: left; vertical-align: bottom; font-weight: bold; border-bottom: 0.5pt solid #000;
     padding: 3pt 4pt; }
td { text-align: left; vertical-align: top; padding: 2.5pt 4pt; }
tbody tr:nth-child(even) td { background: #f2f2f2; }
p.tt { font-weight: bold; text-transform: uppercase; margin: 10pt 0 0; break-after: avoid; }
p.src { font-size: 10pt; margin: 0 0 4pt; }
div.kp { border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }
div.kp > p:first-child { font-weight: bold; text-transform: uppercase; margin-top: 0; }
p.concept { font-style: italic; margin: 6pt 0 4pt; break-before: avoid; }
p.concept b { font-style: normal; }
""" % {"title": TITLE}

SHEET_CSS = """
@page {
  size: A4; margin: 12mm 13mm;
  @bottom-center { content: counter(page); font: 8pt Carlito, 'DejaVu Sans'; color: #000; }
}
html { font-family: Carlito, 'DejaVu Sans', sans-serif; font-size: 9.4pt; line-height: 1.25;
       color: #000; hyphens: manual; text-align: left; }
body { margin: 0; }
h1 { font-size: 14pt; font-weight: bold; margin: 0 0 5pt; padding-bottom: 2pt;
     border-bottom: 1pt solid #000; break-after: avoid; }
.cols { column-count: 2; column-gap: 7mm; }
h2 { font-size: 10.4pt; font-weight: bold; text-transform: uppercase; margin: 6pt 0 2pt;
     padding-bottom: 1pt; border-bottom: 0.5pt solid #000; break-after: avoid; }
p { margin: 1pt 0; orphans: 2; widows: 2; }
ul { margin: 0; padding-left: 10pt; }
li { margin: 0 0 1pt; orphans: 2; widows: 2; }
div.top { border: 1pt solid #000; padding: 4pt 6pt; margin: 0 0 6pt; column-count: 2; column-gap: 7mm; }
div.top > p:first-child { column-span: all; font-weight: bold; margin: 0 0 2pt; }
div.traps { background: #ececec; border-left: 5pt double #000; padding: 4pt 6pt; margin: 6pt 0 0; }
div.traps > p:first-child { font-weight: bold; margin: 0 0 2pt; }
"""


def md_to_html(text):
    return markdown.markdown(text, extensions=["tables", "md_in_html", "sane_lists"])


def notes_html(md):
    # Standalone bold caps lines immediately before a table become table titles.
    md = re.sub(r"^\*\*((?:TABLE|COMPARISON|PAIR|IMAGING|NON-CURATIVE|GENETIC)[^\n]*)\*\*$",
                r'<p class="tt">\1</p>', md, flags=re.M)
    md = re.sub(r"^\*(Data from [^\n]*)\*$", r'<p class="src">\1</p>', md, flags=re.M)
    md = re.sub(r"^\*(Abbreviations:[^\n]*)\*$", r'<p class="src">\1</p>', md, flags=re.M)
    body = md_to_html(md)
    return f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{TITLE}</title>" \
           f"<style>{NOTES_CSS}</style></head><body>{body}</body></html>"


def sheet_html(md):
    title, rest = md.split("\n", 1)
    top_start = rest.index('<div class="top"')
    top_end = rest.index("</div>", top_start) + len("</div>")
    top = rest[top_start:top_end]
    cols = rest[top_end:]
    body = md_to_html(title) + md_to_html(top) + '<div class="cols">' + md_to_html(cols) + "</div>"
    return f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{TITLE}</title>" \
           f"<style>{SHEET_CSS}</style></head><body>{body}</body></html>"


def words(md):
    t = re.sub(r"</?[a-zA-Z][^>]*>", " ", md)
    t = re.sub(r"[|*#]+|^\s*-\s|^-{3,}", " ", t, flags=re.M)
    return len([w for w in t.split() if re.search(r"\w", w)])


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    notes_md = open("ch165_notes.md", encoding="utf-8").read()
    sheet_md = open("ch165_sheet.md", encoding="utf-8").read()
    n_pdf = f"{out}/Chapter 165 — Management of Recurrent and Newly Metastatic Prostate Cancer — Chapter Notes.pdf"
    s_pdf = f"{out}/Chapter 165 — Management of Recurrent and Newly Metastatic Prostate Cancer — Numbers, Gold Standards and Traps.pdf"
    nd = HTML(string=notes_html(notes_md)).render()
    nd.write_pdf(n_pdf)
    sd = HTML(string=sheet_html(sheet_md)).render()
    sd.write_pdf(s_pdf)
    print("notes pages", len(nd.pages), "words", words(notes_md))
    print("sheet pages", len(sd.pages), "words", words(sheet_md))
