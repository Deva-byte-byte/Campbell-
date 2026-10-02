# MCh Urology exam answer compilation – standing instructions

This repository is the user's MCh Urology exam-preparation workspace. The user is an Indian MCh Urology candidate. The exam is 3 hours: 2 LAQs (long answer questions, 25 marks each) and 5 SAQs (short answer questions, 10 marks each). The user sends question papers or question lists and wants model answers compiled as printable PDFs. Follow these instructions in every session unless the user says otherwise.

## Working branch
- Work on branch `claude/zen-cray-dt1fqe` (or the branch the session tells you to use). Commit and push finished work.

## Sources, in priority order
1. **`reference/`**: the user's Campbell-Walsh-Wein chapter notes (163+ PDFs). Search the text copies in `reference/text/*.txt` (grep) and use `reference/INDEX.md` to find the right chapter. These are the primary source.
2. **Guidelines**: EAU, AUA, NCCN, AUA/SMSNA, KDIGO and Indian law (THOA) where relevant. Use the latest version you can verify; name the guideline and year only when sure.
3. **Landmark trials and studies**: name, year and a one-line result. Only cite trials you are certain exist with correct results.
- Add from 2 and 3 wherever the chapter notes are incomplete or outdated. If the notes and a newer guideline disagree, state both briefly.
- **Accuracy is the top priority.** Never invent numbers, doses, cut-offs, dates, trials or names. If unsure, give the accepted range or omit it.

## Answer format (user-approved)
Each question is answered in this structure:

```
## <Paper/Set>-<Q no>. <Question text exactly as given>
**Type:** LAQ (25 marks)   or   **Type:** SAQ (10 marks)

### <Major exam subheadings: Definition/Introduction, Classification, Pathophysiology,
     Clinical features, Evaluation/Investigations, Management, Complications,
     Follow-up, Recent advances, as fits the topic>
- bullets; tables for classifications/comparisons; short ASCII flowcharts for algorithms
**Diagram to draw:** one short line

> **Key points to remember:**
> - 3–4 short one-line points (numbers, eponyms, trials)
```

- **Length: "half length".** Body (excluding key points box): **LAQ ≈ 650–750 words, SAQ ≈ 260–300 words.** The user reads at about 40–45 words a minute, so keep to these budgets.
- **Clear sentences where needed.** Use short, plain sentences wherever a bare bullet would be cryptic. No chains of arrows/slashes/symbols. Arrows only in flowcharts or simple cause → effect.
- **Keep all major subheadings** an examiner expects for the topic.
- **Keep the concepts.** Briefly explain mechanisms, principles and rationale (why/how), so the candidate can write from understanding. Cut trivia (minor history dates, brand names, secondary trials, rare causes), not concepts.
- **Exam-oriented content only**: what a candidate would write and an examiner would mark: definitions, classifications/grading, key cut-offs and doses, indications/contraindications, management steps, main complications, 1–3 landmark trials, current guideline position, 2–3 recent advances.
- **Acronyms**: spell out every acronym in full at its first use in EACH answer, e.g. "GFR (glomerular filtration rate)". Common units (mL, mg, mmHg, Fr, °C) need no expansion.
- Separate questions with `---`. Start each paper file with `# <Paper title>` and a numbered contents list.
- If a question looks like a typo (e.g. "HSG in neonates"), state the assumed meaning in one italic line at the top of that answer.
- A question repeated across papers: answer it once and cross-reference it in the other paper.

## Output: one A4 black-and-white PDF per paper
1. Write the draft paper as Markdown in `answers/<set-name>/drafts/<Paper-name>.md` (one file per paper).
2. Build the final file (answers + key points after each answer + Rapid Revision Sheet at the end):
   `python3 tools/build_paper.py answers/<set>/drafts/<Paper>.md answers/<set>/<Paper>.md`
3. Make the PDF: `tools/md2pdf.sh answers/<set>/<Paper>.md pdf/<set>/<Paper>.pdf`
   (A4, black and white, page numbers, each question on a new page; tools auto-install the `markdown` Python package and find Chromium).
4. Render 1–2 pages to PNG (`pdftoppm -r 45 -png -f N -l N file.pdf out`) and look at them to check that lists, tables and key points boxes render properly.
5. Send the PDFs to the user (SendUserFile, display "attach"), commit and push.
- The user prints with A4 and "Actual size". Keep the stylesheet black and white (`tools/style.css`).

## Quality checks before delivering
- Re-read every answer for factual errors: doses, cut-offs, trial results, dates, eponyms. Cross-check numbers against the matching `reference/text` chapter.
- `python3 tools/numcheck.py <source.md> <condensed.md>` lists numbers in a condensed file that are not in its source (use when shortening an existing answer).
- Report word counts and approximate reading time (total words ÷ ~43 words a minute) to the user.
- Tell the user plainly about anything uncertain, any assumption about a question's meaning, and anything left out.

## Adding new reference PDFs
- `tools/addref.sh /path/to/upload1.pdf /path/to/upload2.pdf ...` copies them into `reference/`, extracts text into `reference/text/`, and rebuilds `reference/INDEX.md`. Check for byte-identical duplicates (`cmp`) first and skip them. Commit and push.
- Tell the user which existing or likely exam answers each new chapter relates to.

## Existing work in this repository
- **Current:** `answers/2015-summer/` and `pdf/2015-summer/`: MCh Urology Summer 2015 Papers I–IV, chapter-sourced half-length versions (drafts in `answers/2015-summer/drafts/`). Use this folder layout (`answers/<set>/`, `pdf/<set>/`) for every new set.
- Older versions: `answers/Paper-*.md` / `pdf/Paper-*.pdf` (pre-chapter half-length) and `answers/concise/`.
- `answers/full/` and `pdf/full/`: the earlier full-length versions (reference only).
- Missing chapters in `reference/`: 89 only. Chapter 119 is only 2 pages. Chapter 56 (hypospadias) has a full version and a "short version"; Chapter 110 (OAB) has two versions.
