# Brief for a chapter agent

You are producing compiled revision notes for ONE chapter of Campbell-Walsh-Wein Urology (12th ed.), from a PDF the user uploaded. The user asked "compress and compile": summarise the chapter per their standing instructions and produce both compiled documents.

## Read first
1. `/home/user/Campbell-/CLAUDE.md` — the user's standing instructions. Follow them exactly. They are the spec. Read ALL of it.
2. Your chapter's source text (path given in your task). Page markers `=====PDF PAGE n=====` give the PDF page number; the printed book page number is usually the first token on the page. Text was machine-extracted, so: column order may be interleaved, tables are flattened, figure images are missing (legends are present), ligatures/symbols may be corrupted (e.g. `/H11001` = "+", `/H11349` etc. are glyph codes — decode from context and flag the substitution key).
3. For EVERY page that holds a numbered table or box, and wherever the text is garbled, open the page image with the Read tool: `/tmp/claude-0/-home-user-Campbell-/6c570746-a24e-5ac5-b4ed-f259d01ec677/scratchpad/pages/p-NN.png` (NN = two-digit PDF page number, e.g. p-07.png). Rebuild tables from the image, not from the flattened text.
4. Skip the reference list at the chapter end (it is bibliography, not content — note in the flags file that it was deliberately excluded). Skip "Suggested readings" too, same note. KEY POINTS boxes in the chapter ARE content.

## What to produce (write these files; do not print them in your reply)
In `/home/user/Campbell-/build/`:

A. `chNN_notes.html` — Document 2 body fragment (no <html>/<head>/<body>; the build script wraps it). Structure:
   - `<h1>Chapter NN — Title</h1>` (the textbook's own chapter title, as printed)
   - Level A → `<h2>` (write in normal case; CSS uppercases it), Level B → `<h3>`, Level C → `<h4>`, Level D → `<p><span class="d">Run-in.</span> text</p>` or a `<li>` starting with `<span class="d">…</span>`.
   - Follow the CHAPTER'S OWN heading hierarchy and wording. Unheaded opening prose goes under the h1 before the first h2 (as bullets).
   - Bullets `<ul><li>` with `<b>operative phrase</b>` bolded in each bullet. Sequences as "step → step → step".
   - Numbered tables: `<p class="tabletitle">TABLE 34.2 Full Caption…</p>` then `<table><thead>…</thead><tbody>…</tbody></table>`, then `<p class="tablesource">Source attribution if the book gives one (e.g. "Data from X et al., 2014").</p>` if any, then the post-table concept bullets (what the table is for / pattern / trap). A table may instead be bulleted if that serves better — but drug/agent/device tables are always tables.
   - Boxes (numbered "BOX 35.1 …") → same treatment as tables (tabletitle + table or bullets).
   - The chapter's KEY POINTS boxes → `<div class="keypoints"><div class="kptitle">Key points</div><ul>…</ul></div>`.
   - Figures: legends with teaching content → bullets under a Level D run-in "Figure 34.3 — …" (name source/year if the legend gives it). Legends that merely duplicate body text are dropped (compile strip rule).
   - Mandatory comparison tables, titled for what they compare: `<p class="tabletitle">Comparison — X vs Y</p>` + table.
   - Conceptual takeaways at the end of each Level A (and substantial Level B) section: `<p class="concept"><b>Concept —</b> …</p>`. Only where a genuine organising idea exists.
   - British spelling throughout (paediatric, haematuria, oedema, anaemia, oestrogen, tumour, catheterisation, etc.). Expand each abbreviation on first use.
   - No author–year citations in body text except landmark studies/trials/guideline bodies (e.g. RIVUR, Society for Fetal Urology, AAP, NICE are named as bodies, not as citations).
   - No instalment numbers, no source-error/truncation flags, no roadmap sentences. Where the source is wrong, carry the corrected value silently.
   - Budget: ≤ ~360 words per source page (content pages, excluding reference-only pages). If completeness/reasoning cannot fit, exceed the cap — facts and reasoning outrank the cap. Tighten phrasing and remove table/prose duplication first.
   - Use HTML entities or literal Unicode for ≥ ≤ → × µ etc. Escape `<` and `>` in text as `&lt;` `&gt;`.

B. `chNN_cheat.html` — Document 1 body fragment, following the DOCUMENT 1 rules exactly:
   ```
   <h1>Chapter NN — Title — Numbers, Gold Standards and Traps</h1>
   <div class="nothingelse"><div class="boxtitle">If you read nothing else</div><ul>…10 lines…</ul></div>
   <div class="cols">
     <h2>Level A section</h2><ul><li><b>Cut-offs:</b> …</li>…</ul>
     …
     <div class="traps"><div class="boxtitle">Classic traps</div><ul><li>Trap: X — Actually: Y.</li>… ≤10</ul></div>
   </div>
   ```
   1,200–1,600 words; target 2 sides, ceiling 3. Telegraphic, ≤12 words per bullet, arrows/symbols, bold operative phrase, abbreviations expanded on first use. Nothing in Doc 1 that is not also in Doc 2.

C. `chNN_session.md` — the live-session record (this is what the user would have seen during instalments; it is NOT printed):
   - The instalment scaffold: split the chapter into instalments of ~6 source pages (split further where a stretch has >6 Level B sections or >4 numbered tables, and say so), each with its subheading "Instalment n — Topic, Topic, Topic" listing the topics it actually covers.
   - For each instalment, the full "The numbers to lock in" block (all applicable categories per CLAUDE.md, contraindications as two separate lists).
   - Then the SOURCE-FLAG APPENDIX for the whole chapter: truncations (exact break words), duplicates, resequencing (column/page-order fixes you made), source errors/inconsistencies with corrected values, substitution key for corrupted symbols, text/table discrepancies, anything not covered and why (e.g. figure images not reproducible; reference list excluded).
   - Then the COVERAGE CHECK: list every heading (A/B/C), every numbered table, box and figure in the chapter, each marked as covered in Doc 2 (or not, with reason).

## Build and self-check
Run: `cd /home/user/Campbell-/build && python3 build.py NN "Exact Chapter Title" SOURCE_PAGES`
(SOURCE_PAGES = number of content pages in your chapter excluding pages that are only references.)
It writes the PDFs to `/home/user/Campbell-/output/` and greyscale PNGs `chNN_notes_grey-1.png` / `chNN_cheat_grey-1.png` in build/. Read both PNGs and confirm boxes, tables and takeaways are distinguishable from body text. Also check Doc 1 is ≤3 sides (target 2) and within 1,200–1,600 words; if over, cut per the selection order (never shrink type). Check Doc 2 against the cap; tighten phrasing if over, but never drop facts or reasoning. Before finishing, reread the final third of your notes against the first third and correct any thinning (density discipline). Do not edit the CSS or build.py; if you believe they need a change, say so in your reply.

Do NOT commit or push; the coordinator will.

## Your final reply (short)
Report: Doc 1 pages and word count; Doc 2 pages, word count, source pages, reading time at 120 wpm, cap and overrun if any; number of instalments and any splits; a 5–10 line digest of the most important source flags (errors corrected, truncations, items not covered); any coverage-check gaps.
