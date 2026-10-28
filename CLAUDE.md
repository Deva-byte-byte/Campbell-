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
## Q<no>. <Question text exactly as given>   (e.g. Q1, Q2, Q3a–Q3f; the paper label is in the title)
**Type:** LAQ (25 marks)   or   **Type:** SAQ (10 marks)

### <Major exam subheadings: Definition/Introduction, Classification, Pathophysiology,
     Clinical features, Evaluation/Investigations, Management, Complications,
     Follow-up, Recent advances, as fits the topic>
- bullets; tables for classifications/comparisons; short ASCII flowcharts for algorithms
**Diagram to draw:** one short line

> **Key points to remember:**
> - 3–4 short one-line points (numbers, eponyms, trials)
```

- **Length: "half length".** Whole answer including heading and key points box: **LAQ ≈ 700–750 words, SAQ ≈ 300–330 words**; a 4-paper set ≈ 3,400–3,600 words per paper. The user accepted ~6 hours of reading for a full 4-paper set (answers ≈5½ h + revision sheets ≈30 min) in exchange for complete core content. The user reads at about 40–45 words a minute, so keep to these budgets.
- **Clear sentences where needed.** Use short, plain sentences wherever a bare bullet would be cryptic. No chains of arrows/slashes/symbols. Arrows only in flowcharts or simple cause → effect.
- **Keep all major subheadings** an examiner expects for the topic.
- **Keep the concepts.** Briefly explain mechanisms, principles and rationale (why/how), so the candidate can write from understanding. Cut trivia (minor history dates, brand names, secondary trials, rare causes), not concepts.
- **Touch on everything relevant (user requirement).** For each question, every subtopic in the matching reference chapter(s) that is relevant to the question must appear at least as a brief mention. Core items get a short explanation; secondary items get a one-phrase mention (e.g. an "**Also know:** a; b; c" line). Only pure trivia may be omitted.
- **Never reduce a core item to bare names.** Classification/grading tables, tests with their method, lists whose details carry marks (e.g. brainstem reflexes with method and cranial nerves), operative or algorithm steps and key mechanisms must stay written out, even if the topic is thin in the reference chapters. Shorten secondary material instead.
- **Exam-oriented content only**: what a candidate would write and an examiner would mark: definitions, classifications/grading, key cut-offs and doses, indications/contraindications, management steps, main complications, 1–3 landmark trials, current guideline position, 2–3 recent advances.
- **Acronyms**: spell out every acronym in full at its first use in EACH answer, e.g. "GFR (glomerular filtration rate)". Common units (mL, mg, mmHg, Fr, °C) need no expansion.
- Separate questions with `---`. Start each paper file with `# <Year-Season> Paper <n> – <subject>` and a numbered contents list.
- If a question looks like a typo (e.g. "HSG in neonates"), state the assumed meaning in one italic line at the top of that answer.
- A question repeated across papers: answer it once and cross-reference it in the other paper.

## Output: one A4 black-and-white PDF per paper
0. **Naming (user requirement):** label every paper as `<year>-<season> Paper <n>` with Arabic numerals, e.g. "2018-Summer Paper 1". Files: `answers/<set>/drafts/<set>-paper-<n>.md`, `answers/<set>/<set>-paper-<n>.md`, `pdf/<set>/<set>-paper-<n>.pdf` (e.g. `pdf/2018-summer/2018-summer-paper-1.pdf`). The first line of each draft is `# 2018-Summer Paper 1 – Basic Sciences in Urology` (subject after the dash); the revision sheet heading is built from it. Cross-references read "See 2018-Summer Paper 3, Q3a".
1. Write the draft paper as Markdown in `answers/<set>/drafts/<set>-paper-<n>.md` (one file per paper).
2. Build the final file (answers + key points after each answer + Rapid Revision Sheet at the end):
   `python3 tools/build_paper.py answers/<set>/drafts/<set>-paper-<n>.md answers/<set>/<set>-paper-<n>.md`
3. Make the PDF: `tools/md2pdf.sh answers/<set>/<set>-paper-<n>.md pdf/<set>/<set>-paper-<n>.pdf`
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
- `answers/2016-summer/` and `pdf/2016-summer/`: MCh Urology Summer 2016 Papers I–IV (question paper PDF saved in `answers/2016-summer/`).
- `answers/2017-summer/` and `pdf/2017-summer/`: MCh Urology Summer 2017 Papers I–IV (Paper III is a question-bank practice paper).
- `answers/2017-winter/` and `pdf/2017-winter/`: MCh Urology Winter 2017 Papers I–IV (SNM and Botox answered in Paper III, cross-referenced in Paper IV).
- `answers/2018-summer/` and `pdf/2018-summer/`: MCh Urology Summer 2018 Papers I–IV.
- `answers/2019-summer/` and `pdf/2019-summer/`: 2019-Summer Papers 1–4 (question paper PDF saved in `answers/2019-summer/`).
- `answers/2020-summer/` and `pdf/2020-summer/`: 2020-Summer Papers 1–4 (question paper PDF saved in `answers/2020-summer/`; VUJ embryology in Paper 1 Q2, cross-referenced in Paper 3 Q2; rejection in Paper 1 Q3d, cross-referenced in Paper 4 Q1).
- `answers/2021-summer/` and `pdf/2021-summer/`: 2021-Summer Papers 1–4 (Paper 1 is a question-bank practice paper; question paper PDF saved in `answers/2021-summer/`).
- `answers/2022-summer/` and `pdf/2022-summer/`: 2022-Summer Papers 1–4 (mini-PCNL answered in Paper 1 Q1, cross-referenced in Paper 3 Q3c; question paper PDF saved in `answers/2022-summer/`).
- `answers/2023-winter/` and `pdf/2023-winter/`: 2023-Winter Papers 1–4 (question paper PDF saved in `answers/2023-winter/`).
- `answers/2024-winter/` and `pdf/2024-winter/`: 2024-Winter Papers 1–4 (immunotherapy for mRCC in Paper 2 Q3e, cross-referenced from Paper 3 Q3b; question paper PDF saved in `answers/2024-winter/`).
- `answers/2025-winter/` and `pdf/2025-winter/`: 2025-Winter Papers 1–4 (RPLND answered in Paper 3 Q3f, cross-referenced in Paper 4 Q3e; RCC immunotherapy in Paper 4 Q3a; question paper PDF saved in `answers/2025-winter/`).
- `answers/practice-set-01/` and `pdf/practice-set-01/`: Practice Set 1 Papers 1–4, compiled from the question bank (files `practice-set-01-paper-<n>`; titles `# Practice Set 1 Paper <n> – <subject>`; ANH in Paper 3 Q3a cross-referenced to Paper 3 Q2; fURS full answer in Paper 2 Q3b).
- `answers/practice-set-02/` and `pdf/practice-set-02/`: Practice Set 2 Papers 1–4, compiled from the question bank (b/l VUR full answer in Paper 3 Q2, cross-referenced in Paper 3 Q3d; lap donor nephrectomy in Paper 4 Q3a, cross-referenced in Paper 4 Q3d).
- `answers/practice-set-03/` … `practice-set-06/` (and matching `pdf/` folders): Practice Sets 3–6, Papers 1–4 each, compiled from the question bank; many questions are exact repeats of earlier actual papers (cross-referenced). The user re-issued Sets 3–6 and 8 with new last-paper SAQs (handwritten-list topics); the answers were rewritten accordingly. Set 6 stone analysis is now the full answer in Paper 3 Q3c.
- `answers/practice-set-07/` … `practice-set-17/`: question-bank practice sets (7–8: Papers 1–3; 9–14: Papers 1–2; 15–17: Paper 2 only). `answers/practice-set-18/` … `practice-set-22/`: 6-SAQ short-answer sheets (files `practice-set-<n>-saq.md`, titles `# Practice Set <n> SAQ Sheet – Short Answer Practice`).
- `archive/2015-summer-older/`: earlier 2015 versions (old half-length, old full-length, concise drafts), reference only.
- Missing chapters in `reference/`: 89 only. Chapter 119 is only 2 pages. Chapter 56 (hypospadias) has a full version and a "short version"; Chapter 110 (OAB) has two versions.
