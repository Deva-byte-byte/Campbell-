"""Render a chapter's two HTML sources to PDF with WeasyPrint and report delivery metrics.

Usage: python3 tools/render.py <chapter-dir> "<Chapter NN — Title>" <source-pages> [preview-dir]
"""
import re
import sys
from pathlib import Path

import pymupdf
from weasyprint import HTML

chapdir, stem, src_pages = Path(sys.argv[1]), sys.argv[2], int(sys.argv[3])
preview = Path(sys.argv[4]) if len(sys.argv) > 4 else None

jobs = [("sheet.html", f"{stem} — Numbers, Gold Standards and Traps.pdf"),
        ("notes.html", f"{stem} — Chapter Notes.pdf")]
for src, out in jobs:
    out_path = chapdir / out
    HTML(chapdir / src).write_pdf(out_path)
    doc = pymupdf.open(out_path)
    # Word count excludes running headers/footers: count body text from the HTML itself.
    text = re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<head>.*?</head>", "", (chapdir / src).read_text()))
    words = sum(1 for w in text.split() if re.search(r"\w", w))
    print(f"{out}: {doc.page_count} pages, {words} words")
    if src == "notes.html":
        print(f"  source pages {src_pages}; budget {450 * src_pages} words; "
              f"reading time ≈ {words / 150:.0f} min at 150 wpm")
    if preview:
        preview.mkdir(parents=True, exist_ok=True)
        for i in range(doc.page_count):
            doc[i].get_pixmap(dpi=80, colorspace=pymupdf.csGRAY).save(preview / f"{src[:-5]}-p{i + 1}.png")
