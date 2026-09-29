"""Render chapter HTML to PDF with WeasyPrint and report page and word counts.

Usage: python3 tools/render.py <in.html> <out.pdf>
"""
import re
import sys
from html import unescape

from weasyprint import HTML


def words(html_path):
    text = open(html_path, encoding="utf-8").read()
    text = re.sub(r"(?s)<head>.*?</head>", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(unescape(text).split())


if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    doc = HTML(src).render()
    doc.write_pdf(out)
    print(f"{out}: {len(doc.pages)} pages, {words(src)} words")
