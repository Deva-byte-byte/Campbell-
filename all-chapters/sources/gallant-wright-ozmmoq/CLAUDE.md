# Campbell-Walsh-Wein chapter notes

- Follow `INSTRUCTIONS.md` for every summary and compile. It is the standing instruction set.
- One folder per chapter under `chapters/NNN/`, holding:
  - `notes.html` (Document 2)
  - `sheet.html` (Document 1)
  - `session-log.md` (flags, coverage, delivery report — never printed)
  - the two rendered PDFs
- Shared print CSS lives in `tools/notes.css` and `tools/sheet.css`.
- Render with `python3 tools/render.py chapters/NNN "Chapter NN — Title" <source-pages> [preview-dir]`.
  - Needs WeasyPrint, PyMuPDF and the Carlito font (`fonts-crosextra-carlito`).
