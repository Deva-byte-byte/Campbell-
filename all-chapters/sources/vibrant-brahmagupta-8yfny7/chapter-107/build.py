"""Build Chapter 107 deliverables: session record (Markdown) and two PDFs (WeasyPrint)."""
import re
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT
CH_NUM = "107"
CH_TITLE = "Urodynamic and Videourodynamic Evaluation of the Lower Urinary Tract"
FULL_TITLE = f"Chapter {CH_NUM} — {CH_TITLE}"
HEADER_TITLE = f"Chapter {CH_NUM} — Urodynamic and Videourodynamic Evaluation"
SHORT_A = {
    "CONDUCTING A URODYNAMIC STUDY: PATIENT AND TECHNICAL FACTORS": "Conducting a Urodynamic Study",
    "CLINICAL APPLICATIONS OF URODYNAMICS: EVIDENCE-BASED REVIEW AND GUIDELINES PERTAINING TO URODYNAMICS": "Clinical Applications of Urodynamics",
    "THE URODYNAMIC STUDY: ANALYSIS AND INTERPRETATION": "Analysis and Interpretation",
}


def tag_h2(html):
    def rep(m):
        t = m.group(1)
        short = SHORT_A.get(t, t.title().replace(" Of ", " of ").replace(" In ", " in ").replace(" And ", " and "))
        return f'<h2 data-short="{short}">{t}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", rep, html)
BODIES = [SRC / f"body{i}.md" for i in range(1, 6)]
MD_EXT = ["tables", "md_in_html", "sane_lists"]


def md(text):
    return markdown.markdown(text, extensions=MD_EXT)


def strip_session(text):
    """Remove instalment scaffolding comments."""
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)


def words(html):
    txt = re.sub(r"<[^>]+>", " ", html)
    return len(re.findall(r"[A-Za-z0-9][\w'’.\-/≥≤<>=+×%]*", txt))


FONT = "font-family: Carlito, 'DejaVu Sans', sans-serif;"

DOC2_CSS = f"""
@page {{
  size: A4; margin: 18mm 18mm 18mm 20mm;
  @top-left {{ content: "{HEADER_TITLE}"; width: 52%; {FONT} font-size: 8.5pt; color: #000;
              border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }}
  @top-right {{ content: string(sectionA); width: 48%; text-align: right; {FONT} font-size: 8.5pt; color: #000;
               border-bottom: 0.3pt solid #000; vertical-align: bottom; padding-bottom: 2pt; }}
  @bottom-center {{ content: "page " counter(page) " of " counter(pages); {FONT} font-size: 9pt; color: #000; }}
}}
html {{ {FONT} font-size: 11pt; line-height: 1.4; color: #000; }}
body {{ margin: 0; background: #fff; }}
* {{ color: #000; }}
p, li, td, th {{ text-align: left; hyphens: manual; orphans: 2; widows: 2; }}
h1 {{ font-size: 20pt; font-weight: bold; margin: 0 0 10pt; padding-bottom: 4pt;
      border-bottom: 1.5pt solid #000; line-height: 1.2; }}
h2 {{ font-size: 14pt; font-weight: bold; text-transform: uppercase; margin: 14pt 0 5pt;
      padding-bottom: 2pt; border-bottom: 1pt solid #000; string-set: sectionA attr(data-short); line-height: 1.25; }}
h3 {{ font-size: 12.5pt; font-weight: bold; margin: 10pt 0 3pt; }}
h4 {{ font-size: 11.5pt; font-weight: bold; margin: 8pt 0 2pt; }}
h1, h2, h3, h4, .tcap, .kptitle {{ break-after: avoid; page-break-after: avoid; }}
p {{ margin: 3pt 0; }}
ul, ol {{ margin: 2pt 0 4pt; padding-left: 16pt; }}
li {{ margin: 0 0 2.5pt; }}
li > ul {{ margin-top: 2pt; }}
em {{ font-style: italic; }}
p > em:first-child {{ font-size: 11pt; }}
table {{ width: 100%; border-collapse: collapse; margin: 4pt 0 6pt; font-size: 10pt; line-height: 1.3;
         border-top: 1pt solid #000; border-bottom: 1pt solid #000; }}
thead {{ display: table-header-group; }}
th {{ font-weight: bold; border-bottom: 0.5pt solid #000; padding: 3pt 5pt; vertical-align: bottom; }}
td {{ padding: 2.5pt 5pt; vertical-align: top; }}
tbody tr:nth-child(even) td {{ background: #f2f2f2; }}
tr {{ break-inside: avoid; }}
.tcap {{ font-weight: bold; text-transform: uppercase; margin: 9pt 0 1pt; font-size: 10.5pt; }}
.tsrc {{ font-size: 9.5pt; font-style: italic; margin: 0 0 4pt; }}
.keypoints {{ border: 0.75pt solid #000; padding: 6pt; margin: 8pt 0; }}
.keypoints ul {{ margin-bottom: 0; }}
.kptitle {{ font-weight: bold; text-transform: uppercase; margin: 0 0 3pt; }}
.concept {{ font-size: 11pt; margin: 6pt 0 8pt; break-before: avoid; page-break-before: avoid; }}
.concept em {{ font-style: italic; }}
"""

DOC1_CSS = f"""
@page {{
  size: A4; margin: 12mm 13mm 12mm 13mm;
  @bottom-center {{ content: counter(page); {FONT} font-size: 8pt; color: #000; }}
}}
html {{ {FONT} font-size: 9.4pt; line-height: 1.25; color: #000; }}
body {{ margin: 0; background: #fff; }}
* {{ color: #000; }}
p, li {{ text-align: left; hyphens: manual; orphans: 2; widows: 2; }}
h1 {{ font-size: 14pt; font-weight: bold; margin: 0 0 5pt; padding-bottom: 3pt; border-bottom: 1pt solid #000;
      line-height: 1.2; }}
.cols {{ column-count: 2; column-gap: 7mm; }}
h2 {{ font-size: 10.4pt; font-weight: bold; text-transform: uppercase; margin: 6pt 0 2pt;
      padding-bottom: 1pt; border-bottom: 0.5pt solid #000; break-after: avoid; page-break-after: avoid; }}
ul {{ margin: 0; padding-left: 10pt; }}
li {{ margin: 0 0 1pt; }}
p {{ margin: 0; }}
.nothing {{ border: 1pt solid #000; padding: 4pt 6pt; margin: 0 0 6pt; column-count: 2; column-gap: 7mm; }}
.boxtitle {{ font-weight: bold; text-transform: uppercase; margin-bottom: 2pt; column-span: all; }}
.traps {{ background: #ececec; border-left: 5pt double #000; padding: 4pt 6pt; margin-top: 6pt; }}
"""


def html_doc(title, css, body):
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>{body}</body></html>"""


def build_doc2():
    text = "\n\n".join(strip_session(p.read_text()) for p in BODIES)
    body = f"<h1>{FULL_TITLE}</h1>\n" + tag_h2(md(text))
    html = html_doc(f"{FULL_TITLE} — Chapter Notes", DOC2_CSS, body)
    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build" / "doc2.html").write_text(html)
    out = OUT / f"Chapter {CH_NUM} — {CH_TITLE} — Chapter Notes.pdf"
    doc = HTML(string=html, base_url=str(ROOT)).render()
    doc.write_pdf(out)
    return out, len(doc.pages), words(md(text))


def build_doc1():
    text = (SRC / "doc1.md").read_text()
    # split: the 'nothing' box spans both columns; sections and traps flow in two columns
    first_end = text.index("</div>") + len("</div>")
    box, rest = text[:first_end], text[first_end:]
    body = f"<h1>{FULL_TITLE} — Numbers, Gold Standards and Traps</h1>\n{md(box)}\n<div class=\"cols\">{md(rest)}</div>"
    html = html_doc(f"{FULL_TITLE} — Numbers, Gold Standards and Traps", DOC1_CSS, body)
    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build" / "doc1.html").write_text(html)
    out = OUT / f"Chapter {CH_NUM} — {CH_TITLE} — Numbers, Gold Standards and Traps.pdf"
    doc = HTML(string=html, base_url=str(ROOT)).render()
    doc.write_pdf(out)
    return out, len(doc.pages), words(md(text))


def build_session_record():
    """Instalment-ordered session record: notes, numbers block, then flags appendix."""
    nums = (SRC / "numbers.md").read_text()
    blocks = dict(re.findall(r"<!-- NUM (\d) -->\s*(.*?)(?=<!-- NUM|\Z)", nums, flags=re.S))
    parts = [f"# {FULL_TITLE} — Session Record\n"]
    for i, p in enumerate(BODIES, 1):
        t = p.read_text()
        head = re.search(r"<!-- INST \d \| (.*?) -->", t).group(1)
        parts.append(f"\n---\n\n# {head}\n\n{strip_session(t)}\n\n{blocks[str(i)].strip()}\n")
    parts.append("\n---\n\n" + (SRC / "flags.md").read_text())
    out = ROOT / f"Chapter {CH_NUM} — Session Record.md"
    out.write_text("".join(parts))
    return out


if __name__ == "__main__":
    rec = build_session_record()
    p2, n2, w2 = build_doc2()
    p1, n1, w1 = build_doc1()
    print(f"session record: {rec.name}")
    print(f"doc1: {n1} pages, {w1} words")
    print(f"doc2: {n2} pages, {w2} words, {w2/120:.0f} min at 120 wpm")
