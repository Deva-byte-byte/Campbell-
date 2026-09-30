#!/usr/bin/env python3
"""Render chapter body fragments into the two print PDFs and report counts.

Usage: build.py NN "Chapter Title" SOURCE_PAGES
Reads build/chNN_notes.html and build/chNN_cheat.html (body fragments only) and
writes the two PDFs to output/, plus a greyscale PNG of page 1 of each to build/.
"""
import re, subprocess, sys
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
B, OUT = ROOT / "build", ROOT / "output"


def words(html):
    text = re.sub(r"<[^>]+>", " ", html)
    return len(re.findall(r"[A-Za-z0-9≥≤<>→%]+[^\s]*", text))


def render(fragment, css, title, pdf):
    doc = f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{title}</title></head><body>{fragment}</body></html>'
    r = HTML(string=doc, base_url=str(B)).render(stylesheets=[str(B / css)])
    r.write_pdf(pdf)
    return len(r.pages)


def main():
    nn, title, src_pages = sys.argv[1], sys.argv[2], int(sys.argv[3])
    OUT.mkdir(exist_ok=True)
    notes = (B / f"ch{nn}_notes.html").read_text()
    cheat = (B / f"ch{nn}_cheat.html").read_text()
    p2 = OUT / f"Chapter {nn} — {title} — Chapter Notes.pdf"
    p1 = OUT / f"Chapter {nn} — {title} — Numbers, Gold Standards and Traps.pdf"
    n2 = render(notes, "notes.css", f"Chapter {nn} — {title}", p2)
    n1 = render(cheat, "cheat.css", f"Chapter {nn} — {title}", p1)
    w2, w1 = words(notes), words(cheat)
    cap = 360 * src_pages
    for pdf, tag in ((p2, "notes"), (p1, "cheat")):
        page = "2" if (tag == "notes" and n2 > 1) else "1"
        subprocess.run(["pdftoppm", "-gray", "-r", "80", "-f", page, "-l", page, "-png", str(pdf),
                        str(B / f"ch{nn}_{tag}_grey")], check=True)
    print(f"Doc 1 (cheat): {n1} pages ({n1} sides), {w1} words")
    print(f"Doc 2 (notes): {n2} pages, {w2} words; source {src_pages} pp; cap {cap} words; "
          f"reading time {w2/120:.0f} min at 120 wpm; "
          + ("within cap" if w2 <= cap else f"OVER cap by {w2-cap} words ({(w2-cap)/120:.0f} min)"))


if __name__ == "__main__":
    main()
