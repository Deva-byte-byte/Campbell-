"""Render chapter notes (Document 2) and cheat sheets (Document 1) to PDF with WeasyPrint.

Usage: python3 build/build.py <source.md> <doc1|doc2> <output.pdf> "<running title>"
"""
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

HERE = Path(__file__).parent


def render(src, kind, out, title):
    text = Path(src).read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "md_in_html", "attr_list"])
    if kind == "doc1":
        # Everything after the title flows in two columns; boxes marked .span break out.
        body = re.sub(r"(</h1>)", r'\1<div class="cols">', body, count=1) + "</div>"
    css = (HERE / f"{kind}.css").read_text(encoding="utf-8").replace("__TITLE__", title)
    html = f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{body}</body></html>'
    HTML(string=html, base_url=str(HERE)).write_pdf(out)


if __name__ == "__main__":
    render(*sys.argv[1:5])
