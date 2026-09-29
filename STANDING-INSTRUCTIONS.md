# Campbell-Walsh-Wein Chapter Notes — Standing Instructions

The full standing instructions (working method, coverage, summary style, tables, mandatory comparisons, density discipline, order of output, source handling, conceptual takeaways, end-of-instalment block, compilation, Document 1 and Document 2 specifications, rendering) were supplied at the start of the Chapter 31 session on 2026-09-29 and govern all files in this repository.

Key operating constraints recorded here for continuity across sessions:

- Instalments of about six source pages; split when > ~6 Level B sections or > 4 numbered tables.
- Session files (`chNN/session-*.md`) hold instalment notes, "The numbers to lock in" blocks and source-flag appendices.
- On "compile": two PDFs per chapter, rendered with WeasyPrint in Carlito (fallback DejaVu Sans), A4, black and white:
  - `Chapter NN — Title — Numbers, Gold Standards and Traps.pdf` (two sides, 1,200–1,600 words, two columns, 9.4 pt)
  - `Chapter NN — Title — Chapter Notes.pdf` (single column, 11 pt, ≤ ~360 words per source page, page X of Y)
- Rendering toolchain in a fresh container: `pip install weasyprint` and `apt-get install fonts-crosextra-carlito`.
- Source PDFs are not committed to the repository (copyright); they stay in the session scratchpad.
