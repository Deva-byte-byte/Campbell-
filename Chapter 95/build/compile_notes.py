"""Compile the live-session instalment files into Document 2 (Chapter Notes).

Strips instalment scaffolding, numbers blocks, source-flag appendices,
continuation headings, duplicative figure legends and non-landmark
citations, then renders to PDF with WeasyPrint.
"""
import glob
import os
import re
import sys

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
CHAP = os.path.dirname(HERE)
SESSION = os.path.join(CHAP, "session")

TITLE = "Chapter 95 — Urinary Lithiasis: Etiology, Epidemiology, and Pathogenesis"
OUT = os.path.join(
    CHAP,
    "Chapter 95 — Urinary Lithiasis (Etiology, Epidemiology, and Pathogenesis) — Chapter Notes.pdf",
)

# Non-landmark attributions to delete from body text (landmark trials,
# eponyms and table/figure source lines are kept).
CITATION_STRIPS = [
    (" (Pak and Chu, 1973)", ""),
    ("**Weight-based / sex-based** (Parks and Coe)", "**Weight-based / sex-based**"),
    ("**EQUIL 2** (Finlayson) —", "**EQUIL 2** —"),
    (" (Dent and Senior, 1955)", ""),
]


def strip_session(text: str) -> str:
    out = []
    skipping = False
    for line in text.splitlines():
        if line.startswith("# Instalment"):
            skipping = False
            continue
        if line.startswith("## ▸"):
            skipping = True
            continue
        if skipping:
            continue
        if line.startswith("*Split notice") or line.startswith("*Second half of the split"):
            continue
        if re.match(r"^#{2,6} .*\(continued\)\s*$", line):
            continue
        if line.startswith("## URINARY LITHIASIS — CHAPTER OPENING"):
            continue
        if "<!-- dup -->" in line:
            continue
        out.append(line)
    text = "\n".join(out)
    # Selected references section (bibliography) — drop heading and its bullet(s)
    text = re.sub(r"### Selected References.*?(?=\n#|\Z)", "", text, flags=re.S)
    # Figure-legend headings left with no legends beneath them
    text = re.sub(r"###### Figure legends\s*\n(?=\s*(#|<div|\Z))", "", text)
    # Python-Markdown needs 4-space nesting; session files use 2-space
    text = re.sub(r"(?m)^( +)(?=[-*]|\d+\.|\*\*)", lambda m: " " * (len(m.group(1)) * 2), text)
    for a, b in CITATION_STRIPS:
        text = text.replace(a, b)
    return text


def main():
    parts = [open(p, encoding="utf-8").read() for p in sorted(glob.glob(os.path.join(SESSION, "i*.md")))]
    md_text = strip_session("\n\n".join(parts))
    open(os.path.join(HERE, "notes_compiled.md"), "w", encoding="utf-8").write(md_text)

    body = markdown.markdown(md_text, extensions=["tables", "md_in_html", "attr_list", "sane_lists"])
    body = re.sub(r"<p><strong>Concept —</strong>", '<p class="concept"><strong>Concept —</strong>', body)
    # First table row: mark as header (markdown already emits thead)
    css = open(os.path.join(HERE, "notes.css"), encoding="utf-8").read()
    html = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{TITLE} — Chapter Notes</title><style>{css}</style></head>
<body><h1 class="chaptitle">{TITLE}</h1>{body}</body></html>"""
    open(os.path.join(HERE, "notes.html"), "w", encoding="utf-8").write(html)
    HTML(string=html, base_url=HERE).write_pdf(OUT)

    import html as _h
    plain = _h.unescape(re.sub(r"<[^>]+>", " ", body))
    words = sum(1 for w in plain.split() if re.search(r"[A-Za-z0-9]", w))
    print("OUT", OUT)
    print("WORDS", words)


if __name__ == "__main__":
    sys.exit(main())
