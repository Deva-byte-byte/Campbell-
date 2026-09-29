# CAMPBELL-WALSH-WEIN CHAPTER NOTES — STANDING INSTRUCTIONS

These instructions govern every session in this repository. The authoritative
full text is the user's standing-instructions message; this file preserves it
so each new session starts under the same rules.

## Session environment
- Render with **WeasyPrint** (never wkhtmltopdf). If missing: `pip install weasyprint`.
- Font **Carlito** (fallback DejaVu Sans). If missing: `apt-get install -y fonts-crosextra-carlito`.
- Delivered PDFs go in `chapters/Chapter NN — Title/` and are committed and pushed.

## WORKING METHOD
- The user pastes a chapter in instalments, approximately six pages at a time. Summarise each as it arrives.
- Number the instalments sequentially within the chapter for working purposes only. Instalment numbering is a scaffold for the live session — it NEVER appears in the delivered documents.
- Give each instalment a subheading listing the topics it actually covers: "Instalment 4 — Obesity Thresholds, Frailty, Infection Screening, Algorithm".
- If a paste contains more than roughly six Level B sections or more than four numbered tables, split it: summarise it as two or more consecutive instalments within the one reply, each with its own numbers block, rather than as one compressed pass. Say that the split has been made.

## COVERAGE
- Work through the paste in source order and cover everything in it: every heading at Level A, B and C; every numbered table, box and figure, including any whose number or caption is truncated; and any unheaded opening or bridging prose — chapter preamble, era summaries, transitional paragraphs. Unheaded prose carries epidemiology and framing; it is content, not roadmap.
- Anything in the paste that is not covered is named explicitly in the closing appendix, with the reason — truncated, not pasted, absent from the paste — and carried forward as pending until it arrives.
- Silent omission is the single worst failure mode. An acknowledged gap is acceptable; an unacknowledged one is not.

## SUMMARY STYLE
- Bullet points throughout. Concise but concept-carrying — keep the reasoning, drop the padding.
- Omit specific study data: no sample sizes, percentages, or raw figures. Give only the bottom line of what a study showed. Exception: landmark trials important enough to know by name — those keep their identity and key numbers.
- Omit author–year citations for studies that are not landmark ("Stacey, 2014", "Capogrosso, 2013", "Quam, 1989"): state the finding and, where it matters, the study type ("meta-analysis of randomised trials"), without the citation. Only landmark trials keep their names — e.g. MMAS, PCPT, REINVENT. This governs body text only; the source attribution printed with a numbered table or figure ("Data from Francis et al., 2007") is retained under the TABLES rule.
- Expand every abbreviation in full on first use, then abbreviate.
- No slang, no informal register. Medical language throughout.
- Bold the operative phrase in each bullet.
- British spelling and standard medical usage, even where the source is American.
- Where the source gives a technique as a sequence, summarise it as a sequence (step → step → step).
- Where two facts are the examinable contrast (rigid vs flexible, active vs passive deflection), state them adjacently as a pair.
- Preserve figure and table legends as their own subsection when pasted; name the source study and year where the legend gives it.
- Chapter opening prose is content. Epidemiology, incidence, mortality, subtype proportions, sex ratio and the framing of why a disease is treated as it is are all summarised. Only roadmap sentences ("this chapter will cover") are stripped.
- Close every major section with a conceptual takeaway.

## TABLES
- Every numbered table and box in the paste is rebuilt or bulleted. None is skipped, folded silently into prose, or deferred. A table referred to in the text but pasted elsewhere is flagged as pending and picked up when it arrives.
- NEVER reproduce a source table as raw or dumped rows. Either bullet and summarise, or rebuild as a clean table with rows collapsed and grouped into the categories that matter (sex, age band, setting, criterion), not one row per study.
- Tables of drugs, agents or devices are always rebuilt as tables. Mechanism, target, line of therapy, risk group, comparator, endpoint and route are columns, not sentences.
- Follow every table with the concepts it tests: what it is FOR, the pattern across rows, and the trap it sets.
- Drop study-by-study granularity unless landmark. Keep criteria, thresholds, cut-offs and ranges.
- Retain table number, full caption and source study and year.
- Where body text and a table give different values for the same endpoint, tabulate both and name the reason (independent vs investigator review, data cut, denominator). Do not silently select one.

## MANDATORY COMPARISONS
Build a comparison table, unasked, wherever the source presents parallel entities:
- Two or more competing models, classifications, scores or criteria → one table, shared rows, differences bolded.
- Three or more drugs of one class → one table of targets, one of signature toxicities.
- Two or more guideline bodies on the same decision → one table.
- A series of trials answering the same question → one table: trial, comparator, population, endpoints, verdict.
- A governing contrast or asymmetry (normoxia vs hypoxia, hereditary vs sporadic, immediate vs deferred) → a two-column pair, adjacent.
Prose is for reasoning and mechanism. Anything enumerable and parallel goes in a table.

## DENSITY DISCIPLINE
- Depth must not decay across an instalment. Before closing, reread the final third against the first third and correct any thinning.
- Never compress by dropping. Tighten phrasing; the set of facts does not shrink. (Applies to the session and Document 2; Document 1 is deliberately selective.)
- Reading-time budget: Document 2 runs to no more than ~360 words per source page (20 pages ≈ 60 min at 120 wpm). Bring an overrun back by tightening phrasing and removing table/prose duplication — never by dropping facts. Reasoning sentences, post-table notes and conceptual takeaways are not cut. Completeness and understanding outrank the cap: if it cannot be met without losing a fact or its reasoning, exceed it and report the overrun.

## ORDER OF OUTPUT
- Summary first, source flags last. Flags are a closing appendix, never a preamble.
- Corrections appear inside the relevant bullet, in corrected form; the appendix records that a correction was made.

## HANDLING THE SOURCE TEXT — LIVE SESSION ONLY (closing appendix; never in PDFs)
- Truncation mid-sentence: say so and name the exact words it breaks at; close the loop when completed later.
- Duplicate paste: say so and where to resume. Internal duplicate: summarise once and note it.
- Out-of-order paste: restore correct order and say so.
- Source errors, inconsistencies, ambiguous expansions: flag and give the correct version — never silently reproduce or fix. Includes corrupted symbols (comma for "<", full stop for ">", "P 5" for "P ="), split numerals, dropped letters.
- Systematic character substitution: state the key once.
- Unrelated material: answer it, keep it out of the notes, ask where to file it.
- Anything not covered, and why.

## CONCEPTUAL TAKEAWAYS
- Close each major section (Level A, or a substantial standalone Level B) with one to three sentences or a single bullet — never a paragraph.
- States the organising idea, not a recap. Name the governing asymmetry, contrast or causal chain where one exists.
- Only where a genuine organising idea exists; purely enumerative sections get none.
- Medical register, bolded operative phrase.

## END OF EVERY INSTALMENT
Block titled "The numbers to lock in", as applicable:
- Key facts, figures, thresholds and cut-offs
- Gold standards, commonest, first-line options
- Eponyms, each with its single distinguishing feature
- Landmark trials by name, with key numbers
- Dates and legislation, each with its single distinguishing feature
- Absolute vs relative contraindications, as two separate lists
- When to operate / when not to operate
- Classic traps
Written in full in session; raw material for Document 1, not printed as they stand.
Then the source-flag appendix. In that order.

## COMPILATION ("COMPILE")
Two PDFs per chapter, black-and-white A4. No Word file, no third variant.
- Restructure to the chapter's own heading hierarchy: Level A section heads in caps; Level B second-level heads; Level C third-level heads; Level D italic run-in subheads. Headings larger going up; body smallest.
- Strip from both: instalment numbering/cross-references; paste-order, resequencing, duplication and truncation notes; source-error, discrepancy and terminology flags; roadmap sentences; figure legends that merely duplicate body text; surviving non-landmark author–year citations.
- Carry corrected values silently.
- Add nothing new. Reorganise, merge duplicates, delete collation commentary. Session takeaways and comparison tables carried through as written; none composed at compile time. Selecting/shortening for Document 1 permitted; no new facts.
- Before rendering: coverage check across all instalments (every heading, table, box, figure) — report anything that never reached Document 2. Check Document 2 against the reading-time budget and tighten if over.
- Rasterise a page of each document in greyscale and confirm every box, table and takeaway is distinguishable from body text.

### DOCUMENT 1 — "Chapter NN — Title — Numbers, Gold Standards and Traps.pdf"
Last-look cheat sheet, 10–15 minutes.
- Length: one A4 sheet both sides; hard ceiling three sides. ~1,200–1,600 words; report word count.
- Selection — only: examinable number/threshold/cut-off; gold standard, first-line or commonest; operate / don't-operate trigger; absolute contraindication; landmark trial with single key result; eponym with distinguishing feature; classic trap.
- Excluded: mechanism, rationale, history (unless date examinable), background epidemiology, relative contraindications unless classically examined, conceptual takeaways, what a trainee already knows.
- Over budget → cut in order: historical eponyms → dates → secondary thresholds → relative contraindications. Never cut traps, gold standards or operative triggers.
- Wording: one fact per line; telegraphic, ≤12 words; arrows/symbols (→ > < ≥ vs); merge related cut-offs; collapse duplicates; abbreviations expanded on first use; bold operative phrase; tables as single-line cut-offs only, no grids.
- Structure: "IF YOU READ NOTHING ELSE" box (ten highest-yield lines, spanning both columns) → Level A sections in chapter order with bold run-in labels ("Cut-offs:", "Gold standard:", "Operate if:") → single CLASSIC TRAPS box, max ten, "Trap: X — Actually: Y."
- Layout: A4 portrait, two columns, 7 mm gutter, B&W. Margins 12 mm top/bottom, 13 mm left/right. Carlito → DejaVu Sans. Body 9.4 pt, line height 1.25, #000. 1 pt between bullets. Title 14 pt bold, 1 pt rule, spanning columns. Level A 10.4 pt bold caps, 0.5 pt rule. Nothing-else box: 1 pt black border, no fill, spanning. Traps box: #ececec fill, 5 pt double black left rule. Left-aligned ragged right, no hyphenation, never justify. Boxes may flow across columns/pages (no break-inside: avoid). break-after: avoid on headings. Orphans/widows 2. Page numbers bottom centre, 8 pt.

### DOCUMENT 2 — "Chapter NN — Title — Chapter Notes.pdf"
- A4 portrait, single column, B&W; nothing depends on colour.
- Margins 18 mm top/bottom, 20 mm left, 18 mm right.
- Carlito → DejaVu Sans. Body 11 pt, line height 1.4, #000. No grey text.
- 2.5 pt between bullets. ≥8 pt before Level B heads, ≥12 pt before Level A heads.
- Headings: title 20 pt bold over 1.5 pt rule; Level A 14 pt bold caps over 1 pt rule; Level B 12.5 pt bold; Level C 11.5 pt bold; Level D 11 pt italic run-in.
- KEY POINTS boxes: 0.75 pt black border all sides, no fill, 6 pt padding, bold caps title.
- Tables: no fill, no vertical rules; 1 pt rule above and below, 0.5 pt under header; optional banding #f2f2f2. Bold caps title with number and full caption. Rebuilt table, never raw rows, followed by summary bullets. Body ≥10 pt, full width, header repeated across breaks.
- Comparison tables: same treatment, titled for what they compare.
- Conceptual takeaway: closing run-in, body size, italic, black, opening with bold "Concept —". No box, no rule. break-before: avoid.
- Running header 8.5 pt: chapter title left, current Level A right, 0.3 pt rule beneath.
- Left-aligned ragged right, no hyphenation, never justify. break-after: avoid on headings. Orphans/widows 2.
- Page numbers bottom centre, 9 pt, "page X of Y".

## RENDERING
- WeasyPrint, never wkhtmltopdf.
- Carlito throughout. Do not propose a serif again (Minion Pro unavailable; Source Serif 4, Bitstream Charter, Caladea, DejaVu Serif rejected).
- All text pure black.
- Legibility floor: Document 2 ≥10.5 pt body, ≥1.35 line height; Document 1 ≥9.4 pt, ≥1.25. Document 2 page count comes down by tightening bullet gaps and heading spacing first. Document 1 over budget → cut by selection order, never shrink type.
- Report on delivery: page count of both; Document 1 word count; for Document 2 the source page count, notes word count, estimated reading time at 120 wpm, and whether/by how much the cap was exceeded.

## Notes on using it
- The instalment subheading is the quick check: if missing, or naming fewer topics than the paste contains, the reply should be regenerated.
- Six pages holds only for ordinary pages. A six-page paste with four or more numbered tables should be split; say so if it is not.
