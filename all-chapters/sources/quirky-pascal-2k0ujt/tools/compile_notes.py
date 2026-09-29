"""Compile a session-notes file into Document 2 (Chapter Notes PDF).

Strips session scaffolding (@@INST, @@NUMBERS, @@FLAGS, @@LEGEND-DROP blocks),
renders the chapter hierarchy with WeasyPrint, and reports word count and pages.

Usage: python3 compile_notes.py session-notes.md "Out.pdf" SOURCE_PAGES
"""
import re
import sys

import markdown
from weasyprint import HTML

CSS = r"""
@page {
  size: A4; margin: 18mm 18mm 18mm 20mm;
  @top-left { content: string(chtitle); font: 8.5pt Carlito, 'DejaVu Sans'; color:#000;
              border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }
  @top-right { content: string(section, start); font: 8.5pt Carlito, 'DejaVu Sans'; color:#000;
               border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }
  @bottom-center { content: "page " counter(page) " of " counter(pages);
                   font: 9pt Carlito, 'DejaVu Sans'; color:#000; }
}
html { font-family: Carlito, 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.4;
       color: #000; text-align: left; hyphens: manual; orphans: 2; widows: 2; }
body { margin: 0; }
h1, h2, h3, h4 { color:#000; break-after: avoid; page-break-after: avoid; line-height: 1.2; }
h1 { font-size: 20pt; font-weight: bold; margin: 0 0 8pt; padding-bottom: 4pt;
     border-bottom: 1.5pt solid #000; }
h2 { font-size: 14pt; font-weight: bold; text-transform: uppercase; margin: 14pt 0 5pt;
     padding-bottom: 2pt; border-bottom: 1pt solid #000; string-set: section content(); }
h3 { font-size: 12.5pt; font-weight: bold; margin: 9pt 0 3pt; }
h4 { font-size: 11.5pt; font-weight: bold; margin: 7pt 0 2pt; }
p { margin: 3pt 0; }
ul, ol { margin: 2pt 0 4pt; padding-left: 15pt; }
li { margin: 0 0 2.5pt; }
li > ul, li > ol { margin-top: 2.5pt; }
em { font-style: italic; }
p.lvd { margin: 6pt 0 2pt; break-after: avoid; }
p.lvd em { font-style: italic; font-size: 11pt; }
p.concept { font-style: italic; margin: 6pt 0 4pt; break-before: avoid; page-break-before: avoid; }
p.concept em { font-style: italic; }
p.concept strong:first-child { font-style: normal; }
p.tcap { font-weight: bold; text-transform: uppercase; font-size: 10pt; margin: 9pt 0 2pt;
         break-after: avoid; page-break-after: avoid; letter-spacing: 0.2pt; }
table { width: 100%; border-collapse: collapse; font-size: 10pt; line-height: 1.3;
        border-top: 1pt solid #000; border-bottom: 1pt solid #000; margin: 0 0 5pt; }
thead { display: table-header-group; }
th { text-align: left; font-weight: bold; border-bottom: 0.5pt solid #000; padding: 3pt 4pt; vertical-align: bottom; }
td { padding: 2.5pt 4pt; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f2f2f2; }
tr { break-inside: avoid; }
div.kp { border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }
div.kp p.kp-title { font-weight: bold; text-transform: uppercase; margin: 0 0 3pt; }
div.kp ul { margin-bottom: 0; }
"""


def strip_session(src: str) -> tuple[str, str]:
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    src = re.sub(r"^@@(NUMBERS|FLAGS|LEGEND-DROP)\s*$.*?^@@END\s*$", "", src, flags=re.S | re.M)
    src = re.sub(r"^@@INST .*$", "", src, flags=re.M)
    m = re.search(r"^@@TITLE (.*)$", src, flags=re.M)
    title = m.group(1).strip()
    src = src.replace(m.group(0), "")
    assert "@@" not in src, "unstripped scaffolding"
    return title, src


def build_html(title: str, body_md: str) -> str:
    body = markdown.markdown(body_md, extensions=["tables", "md_in_html", "sane_lists"])
    body = re.sub(r"<p><strong>Concept —</strong>", r'<p class="concept"><strong>Concept —</strong>', body)
    body = re.sub(r'(<div class="kp">\s*)<p><strong>KEY POINTS</strong></p>',
                  r'\1<p class="kp-title">Key points</p>', body)
    body = re.sub(r"<p><em>([^<]*\.)</em></p>", r'<p class="lvd"><em>\1</em></p>', body)
    short = title.split(":")[0]
    return (f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{short}</title>"
            f"<style>{CSS} h1 {{ string-set: chtitle '{short}'; }}</style></head><body>"
            f"<h1>{title}</h1>{body}</body></html>")


def main():
    src_path, out_pdf, src_pages = sys.argv[1], sys.argv[2], int(sys.argv[3])
    title, body_md = strip_session(open(src_path, encoding="utf-8").read())
    html = build_html(title, body_md)
    open(out_pdf.replace(".pdf", ".html"), "w", encoding="utf-8").write(html)
    doc = HTML(string=html).render()
    doc.write_pdf(out_pdf)
    text = re.sub(r"<style>.*?</style>|<[^>]+>", " ", html, flags=re.S)
    words = len(re.findall(r"[A-Za-z0-9][\w'’.,%/–-]*", text))
    cap = 360 * src_pages
    print(f"pages={len(doc.pages)} words={words} cap={cap} "
          f"read_min={words/120:.0f} over={max(0, words-cap)}")


if __name__ == "__main__":
    main()
