#!/usr/bin/env python3
"""Render chapter notes (Document 2) and cheat sheet (Document 1) to PDF with WeasyPrint.

Usage: build.py <chapter-dir> "<Chapter NN — Title>" <source-pages>
Expects <chapter-dir>/notes.md and <chapter-dir>/cheatsheet.md.
"""
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

TOOLS = Path(__file__).resolve().parent
EXTS = ["tables", "attr_list", "md_in_html", "sane_lists"]


def render(md_text):
    # Notes are written with 2-space list nesting; Python-Markdown needs 4.
    md_text = re.sub(r"(?m)^( +)(?=[-*] |\d+\. )", lambda m: m.group(1) * 2, md_text)
    html = markdown.markdown(md_text, extensions=EXTS)
    # Conceptual takeaway: "<em>Concept —</em> ..." paragraph -> bold label, italic body.
    html = re.sub(
        r'<p class="concept"><em>Concept —</em>\s*(.*?)</p>',
        lambda m: '<p class="concept"><b>Concept —</b> <i>' + m.group(1) + "</i></p>",
        html,
        flags=re.S,
    )
    # Table caption paragraph directly before a table becomes its caption.
    html = re.sub(
        r'<p class="tcap">(.*?)</p>\s*<table>',
        r'<table><caption>\1</caption>',
        html,
        flags=re.S,
    )
    return html


def words(md_text):
    """Count words a reader reads: rendered text, excluding markup."""
    from html.parser import HTMLParser

    class Text(HTMLParser):
        def __init__(self):
            super().__init__()
            self.parts = []

        def handle_data(self, data):
            self.parts.append(data)

    parser = Text()
    parser.feed(render(md_text))
    return len(re.findall(r"\S*[A-Za-z0-9]\S*", " ".join(parser.parts)))


def build(chapter_dir, title, kind):
    src = chapter_dir / ("notes.md" if kind == "notes" else "cheatsheet.md")
    md_text = src.read_text(encoding="utf-8")
    body = render(md_text)
    css = (TOOLS / f"{kind}.css").read_text(encoding="utf-8")
    css = css.replace("__CHAPTER__", title.replace('"', '\\"'))
    doc = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{title}</title><style>{css}</style></head><body>{body}</body></html>"""
    suffix = "Chapter Notes" if kind == "notes" else "Numbers, Gold Standards and Traps"
    out = chapter_dir / f"{title} — {suffix}.pdf"
    (chapter_dir / f"{kind}.html").write_text(doc, encoding="utf-8")
    pdf = HTML(string=doc, base_url=str(chapter_dir)).write_pdf()
    out.write_bytes(pdf)
    return out, words(md_text)


if __name__ == "__main__":
    d = Path(sys.argv[1]).resolve()
    title = sys.argv[2]
    pages = int(sys.argv[3])
    kinds = sys.argv[4:] or ["notes", "cheatsheet"]
    for kind in kinds:
        if kind == "cheatsheet" and not (d / "cheatsheet.md").exists():
            continue
        out, n = build(d, title, kind)
        print(f"{kind}: {out.name}  words={n}", end="")
        if kind == "notes":
            print(f"  source_pages={pages}  cap={pages*360}  read_min={n/120:.0f}", end="")
        print()
