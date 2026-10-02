# Re-render both Chapter 53 PDFs with WeasyPrint (Carlito font required).
import weasyprint
weasyprint.HTML('notes.html').write_pdf('notes.pdf')
weasyprint.HTML('sheet.html').write_pdf('sheet.pdf')
