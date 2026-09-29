# Campbell-Walsh-Wein chapter notes

- Follow `INSTRUCTIONS.md` for every chapter session: instalment summaries, "The numbers to lock in", source-flag appendix, and the two-PDF compile.
- Keep each chapter's session notes in `chapters/NN-short-title/` (one markdown file per instalment) and commit them as they are written, so a compile can run from a fresh container.
- Rendering toolchain (not preinstalled in a fresh container): `pip install weasyprint pypdfium2` and `apt-get install fonts-crosextra-carlito`. Use pypdfium2 for the greyscale rasterisation check.
