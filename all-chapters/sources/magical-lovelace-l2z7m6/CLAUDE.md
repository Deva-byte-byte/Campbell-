# Campbell-Walsh-Wein chapter notes

This repository holds chapter-by-chapter study notes built from Campbell-Walsh-Wein pastes.

- Standing instructions (working method, style, tables, compile and rendering rules) are in `STANDING-INSTRUCTIONS.md`. Follow them in every session.
- Each chapter lives in `chapters/NN-short-title/`:
  - `session-notes.md` — the live-session instalment summaries, numbers blocks and source-flag appendices (working material; instalment numbering and flags never reach the PDFs).
  - The two compiled PDFs, when the user says "compile".
- Rendering: WeasyPrint only (`pip install weasyprint`); font Carlito (`apt-get install fonts-crosextra-carlito`), falling back to DejaVu Sans.
