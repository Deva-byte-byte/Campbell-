# Campbell-Walsh-Wein Chapter Notes — Standing Instructions

This is the governing specification for every chapter-notes session in this repository.
The full text is maintained by the user and pasted at the start of each session; the
pasted version always takes precedence over this copy.

## Toolchain (verified in the cloud container)

- WeasyPrint (`pip install weasyprint`) — never wkhtmltopdf.
- Carlito (`apt-get install fonts-crosextra-carlito`), DejaVu Sans fallback.
- poppler-utils (`pdftoppm -gray`) for the greyscale rasterisation check.
- Set `font-family` explicitly inside `@page` margin boxes (`@bottom-center`, `@top-left`,
  `@top-right`); otherwise WeasyPrint renders page numbers and running headers in DejaVu Serif.

## Output layout

- `chapters/NN-title/` — per-chapter working files (session notes, HTML sources).
- Delivered PDFs:
  - `Chapter NN — Title — Numbers, Gold Standards and Traps.pdf` (Document 1)
  - `Chapter NN — Title — Chapter Notes.pdf` (Document 2)
