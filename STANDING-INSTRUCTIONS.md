# Campbell-Walsh-Wein Chapter Notes — Standing Instructions

Standing instructions for the chapter-notes workflow, as given at the start of the session (current revision: 120 words-per-minute reading budget, cap about 360 words per source page).

Summary of the pipeline:

1. Chapters are pasted in instalments of about six pages. Each instalment is summarised in source order, with a topic subheading, a "The numbers to lock in" block, and then a closing source-flag appendix.
2. When the user says **"compile"**, two A4 black-and-white PDFs are produced per chapter with WeasyPrint in Carlito:
   - `Chapter NN — Title — Numbers, Gold Standards and Traps.pdf` (two-column cheat sheet, 1,200–1,600 words)
   - `Chapter NN — Title — Chapter Notes.pdf` (single-column study notes, ≤ ~360 words per source page)
3. Delivery report: page counts, Document 1 word count, and for Document 2 the source pages, word count, reading time at 120 wpm and any overrun of the cap.

Toolchain the cloud container needs (not pre-installed):

```
pip install weasyprint pymupdf
apt-get install -y fonts-crosextra-carlito
```

The full instruction text lives in the session transcript. Paste it again at the start of any new session.
