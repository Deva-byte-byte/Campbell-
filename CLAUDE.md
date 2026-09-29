# Campbell-Walsh-Wein Chapter Notes — Standing Instructions

These instructions govern every session in this repository. The user pastes a chapter in instalments; Claude summarises each and, on "compile", produces two PDFs per chapter.

## Environment set-up (cloud container is ephemeral)

Before compiling, ensure the toolchain is present:

```
pip install -q weasyprint
apt-get update -q && apt-get install -y -q fonts-crosextra-carlito poppler-utils
```

WeasyPrint renders; `pdftoppm -gray` rasterises a page for the greyscale check. Never wkhtmltopdf.

## WORKING METHOD
- Chapter pasted in instalments of approximately six pages. Summarise each as it arrives.
- Number instalments sequentially within the chapter for working purposes only. Numbering NEVER appears in the delivered documents.
- Each instalment gets a subheading listing the topics it actually covers: "Instalment 4 — Obesity Thresholds, Frailty, Infection Screening, Algorithm".
- If a paste contains more than roughly six Level B sections or more than four numbered tables, split it into two or more consecutive instalments within the one reply, each with its own numbers block, and say that the split has been made.

## COVERAGE
- Work through the paste in source order; cover every heading at Level A, B and C; every numbered table, box and figure (including truncated ones); and all unheaded opening or bridging prose (preamble, era summaries, transitional paragraphs) — it is content, not roadmap.
- Anything not covered is named in the closing appendix with the reason (truncated, not pasted, absent) and carried forward as pending.
- Silent omission is the single worst failure mode.

## SUMMARY STYLE
- Bullets throughout; concise but concept-carrying.
- No specific study data (sample sizes, percentages, raw figures) — bottom line only. Exception: landmark trials keep identity and key numbers.
- No author–year citations for non-landmark studies in body text; state finding and, where it matters, study type. Landmark trials (e.g. MMAS, PCPT, REINVENT) keep names. Source attribution printed with numbered tables/figures is retained.
- Expand every abbreviation on first use.
- Medical register; no slang.
- Bold the operative phrase in each bullet.
- British spelling, standard medical usage.
- Techniques given as a sequence are summarised as a sequence (step → step → step).
- Examinable contrasts stated adjacently as a pair.
- Figure and table legends preserved as their own subsection when pasted; name source study and year where given.
- Chapter opening prose (epidemiology, incidence, mortality, subtypes, sex ratio, framing) is content. Only roadmap sentences ("this chapter will cover") are stripped.
- Close every major section with a conceptual takeaway.

## TABLES
- Every numbered table and box is rebuilt or bulleted — none skipped, folded silently into prose, or deferred. A table referred to but pasted elsewhere is flagged pending.
- Never reproduce raw/dumped rows. Either bullet and summarise, or rebuild as a clean table with rows grouped into the categories that matter.
- Tables of drugs, agents or devices are always rebuilt as tables (mechanism, target, line, risk group, comparator, endpoint, route as columns).
- Follow each table with the concepts it tests: what it is FOR, the pattern across rows, the trap.
- Drop study-by-study granularity unless landmark; keep criteria, thresholds, cut-offs, ranges.
- Retain table number, full caption, and source study and year.
- Where text and table disagree, tabulate both and name the reason; never silently choose.

## MANDATORY COMPARISONS (build unasked)
- ≥2 competing models/classifications/scores/criteria → one table, shared rows, differences bolded.
- ≥3 drugs of one class → one table of targets, one of signature toxicities.
- ≥2 guideline bodies on the same decision → one table.
- Series of trials on the same question → one table: trial, comparator, population, endpoints, verdict.
- Governing contrast or asymmetry → two-column pair, adjacent.
- Prose for reasoning and mechanism; anything enumerable and parallel goes in a table.

## DENSITY DISCIPLINE
- Depth must not decay across an instalment; reread final third against first third and correct thinning.
- Never compress by dropping (applies to session and Document 2; Document 1 is selective).
- Reading-time budget: Document 2 ≤ ~360 words per source page (20 pages ≈ 60 min at 120 wpm). Bring back by tightening phrasing and removing table/prose duplication — never by dropping facts. Reasoning sentences, post-table notes and takeaways are not cut. If the cap cannot be met without losing a fact or its reasoning, exceed it and report the overrun.

## ORDER OF OUTPUT
- Summary first; source flags last, under their own heading (closing appendix, never preamble).
- Corrections appear in corrected form inside the relevant bullet; the appendix records that a correction was made.

## HANDLING THE SOURCE TEXT — LIVE SESSION ONLY (flag in closing appendix; none survives into PDFs)
- Truncation mid-sentence: say so, name the exact words it breaks at; close the loop when completed later.
- Duplicate paste: say so and where to resume. Internal duplicate: summarise once and note.
- Out-of-order paste: restore order and say so.
- Source errors, inconsistencies, ambiguous expansions, corrupted symbols (comma for "<", full stop for ">", "P 5" for "P ="), split numerals, dropped letters: flag and give correct version. State a systematic substitution key once.
- Unrelated material: answer it, keep it out of the notes, ask where to file it.
- Anything not covered, and why.

## CONCEPTUAL TAKEAWAYS
- Close each major section (Level A, or substantial standalone Level B) with one to three sentences or a single bullet.
- States the organising idea — not a recap. Name governing asymmetry/contrast/causal chain.
- Only where a genuine organising idea exists; none for purely enumerative sections.
- Medical register, bolded operative phrase.

## END OF EVERY INSTALMENT
"The numbers to lock in" block, as applicable: key facts/thresholds/cut-offs; gold standards, commonest, first-line; eponyms (one distinguishing feature each); landmark trials with key numbers; dates and legislation; absolute vs relative contraindications as two lists; when to operate / not operate; classic traps. Written in full during the session; raw material for Document 1. Then the source-flag appendix. In that order.

## COMPILATION ("compile")
Two PDFs per chapter, A4, black-and-white. No Word file, no third variant.
- Restructure to the chapter's own heading hierarchy: Level A section heads in caps; Level B second-level heads; Level C third-level heads; Level D italic run-in subheads. Headings larger going up; body smallest.
- Strip: instalment numbering/cross-references; paste-order, resequencing, duplication, truncation notes; source-error/discrepancy/terminology flags; roadmap sentences; figure legends that merely duplicate body text; surviving non-landmark author–year citations.
- Carry corrected values silently.
- Add nothing new. Reorganise, merge duplicates, delete collation commentary. Takeaways and comparison tables from the session carried through as written; none composed at compile time. Selecting/shortening for Document 1 is permitted; no new facts.
- Before rendering: coverage check across all instalments (every heading, table, box, figure) and report anything that never reached Document 2. Check Document 2 against the reading-time budget and tighten if needed.
- Rasterise a page of each document in greyscale and confirm boxes, tables and takeaways remain distinguishable from body text.

### DOCUMENT 1 — "Chapter NN — Title — Numbers, Gold Standards and Traps.pdf"
- Last-look cheat sheet, 10–15 min. Target two A4 sides; hard ceiling three. ~1,200–1,600 words; report word count.
- High-yield test — only: examinable number/threshold/cut-off; gold standard/first-line/commonest; operate/not-operate trigger; absolute contraindication; landmark trial with single key result; eponym with single distinguishing feature; classic trap.
- Excluded: mechanism, rationale, history (unless date examinable), background epidemiology, relative contraindications unless classically examined, takeaways, things a urology trainee already knows.
- Over budget → cut in order: historical eponyms → dates → secondary thresholds → relative contraindications. Never cut traps, gold standards, operative triggers.
- Wording: one fact per line; telegraphic; ≤12 words; arrows/symbols (→ > < ≥ vs); merge related cut-offs; each fact once; abbreviations expanded on first use; bold operative phrase; tables as single-line cut-offs only, no grids.
- Structure: "IF YOU READ NOTHING ELSE" box (ten highest-yield lines, spanning both columns) → Level A sections in chapter order with bold run-in labels ("Cut-offs:", "Gold standard:", "Operate if:") → single chapter-wide CLASSIC TRAPS box, ≤10 traps, "Trap: X — Actually: Y."
- Layout: A4 portrait, two columns, 7 mm gutter; margins 12 mm top/bottom, 13 mm left/right; Carlito → DejaVu Sans; body 9.4 pt, line height 1.25, #000; 1 pt between bullets; title 14 pt bold with 1 pt rule spanning columns; Level A 10.4 pt bold caps with 0.5 pt rule; "IF YOU READ NOTHING ELSE" box 1 pt black border, no fill, spanning columns; traps box #ececec fill, 5 pt double black left rule; left-aligned, ragged right, hyphenation off, never justify; boxes may flow across columns/pages (no break-inside: avoid); break-after: avoid on headings; orphans/widows 2; page numbers bottom centre 8 pt black.

### DOCUMENT 2 — "Chapter NN — Title — Chapter Notes.pdf"
- A4 portrait, single column, black and white; nothing depends on colour.
- Margins 18 mm top/bottom, 20 mm left, 18 mm right. Carlito → DejaVu Sans. Body 11 pt, line height 1.4, #000; no grey text.
- 2.5 pt between bullets; ≥8 pt before Level B, ≥12 pt before Level A.
- Title 20 pt bold over 1.5 pt rule; Level A 14 pt bold caps over 1 pt rule; Level B 12.5 pt bold; Level C 11.5 pt bold; Level D 11 pt italic run-in.
- KEY POINTS boxes: 0.75 pt black border all sides, no fill, 6 pt padding, bold caps title.
- Tables: no fill, no vertical rules; 1 pt rule above and below, 0.5 pt under header; optional banding #f2f2f2 max; title bold caps with number and full caption; rebuilt table only, followed by summary bullets; body ≥10 pt, full width, header repeated across page breaks. Comparison tables same treatment, titled by what they compare.
- Conceptual takeaway: closing run-in, body size, italic, black, opening with bold "Concept —"; no box, no rule; break-before: avoid.
- Running header 8.5 pt black: chapter title left, current Level A right, 0.3 pt rule beneath.
- Left-aligned, ragged right, hyphenation off, never justify; break-after: avoid on headings; orphans/widows 2.
- Page numbers bottom centre, 9 pt, black, "page X of Y".

## RENDERING
- WeasyPrint only, never wkhtmltopdf.
- Carlito throughout. Do not propose a serif (Minion Pro unavailable; Source Serif 4, Bitstream Charter, Caladea, DejaVu Serif rejected).
- All text pure black.
- Legibility floor: Document 2 ≥10.5 pt body, ≥1.35 line height; Document 1 ≥9.4 pt body, ≥1.25 line height. Document 2 page reduction: tighten bullet gaps and heading spacing first. Document 1 over budget: cut by selection order, never shrink type.
- Delivery report: page count of both; Document 1 word count; Document 2 source page count, notes word count, estimated reading time at 120 wpm, and whether/by how much the cap was exceeded.

## Notes on using it
- The instalment subheading is the quick check against the paste; missing or short subheading = regenerate.
- Six pages holds only for ordinary pages; a table-heavy stretch (≥4 numbered tables) should trigger the split, stated explicitly.

## Changelog
- Current: reading-time cap recalibrated to ~360 words/source page at 120 wpm; completeness and understanding outrank the cap, overrun reported. Delivery report gives reading time at 120 wpm and any overrun.
- Previous: non-landmark author–year citations dropped from body (table/figure attribution retained); reading-time budget introduced (~450 words/page); citation strip and reading-time check added to compilation; delivery report expanded.
