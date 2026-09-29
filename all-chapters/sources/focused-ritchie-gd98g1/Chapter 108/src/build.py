"""Render Chapter 108 PDFs with WeasyPrint."""
from pathlib import Path
import weasyprint
here = Path(__file__).parent
base = "Chapter 108 — Urinary Incontinence and Pelvic Prolapse, Epidemiology and Pathophysiology"
weasyprint.HTML(here / "notes.html").write_pdf(here.parent / f"{base} — Chapter Notes.pdf")
weasyprint.HTML(here / "sheet.html").write_pdf(here.parent / f"{base} — Numbers, Gold Standards and Traps.pdf")
