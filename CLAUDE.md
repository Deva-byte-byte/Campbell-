# Campbell-Walsh-Wein chapter notes

This repository holds chapter notes built from Campbell-Walsh-Wein Urology.

- Standing instructions for every session: `STANDING-INSTRUCTIONS.md`. Follow them exactly.
- Compiled PDFs go in `chapters/`, one folder per chapter.
- Toolchain for compiling: WeasyPrint (`pip install weasyprint`), the Carlito font
  (`apt-get install fonts-crosextra-carlito`) and poppler-utils (`pdftoppm`, for the
  greyscale check). A fresh container may not have them, so install them first.

## Layout

- `chapters/chNN/notes.md` — Document 2 source (chapter heading order). `cheatsheet.md` — Document 1 source.
- `chapters/chNN/session.md` — instalment subheadings, "numbers to lock in" blocks, source flags, coverage check. Never printed.
- Build both PDFs: `python3 tools/build.py chapters/chNN "Chapter NN — Title" <source-pages>`
  (prints word counts and the 360-words-per-page cap). Styles: `tools/notes.css`, `tools/cheatsheet.css`.
- Markdown conventions: `##` Level A, `###` Level B, `####` Level C; `<p class="tcap">…</p>` + blank line before a
  table gives its caption; `<div class="kp" markdown="1">` for KEY POINTS; a paragraph starting `*Concept —*`
  followed by `{: .concept}` is a conceptual takeaway.
