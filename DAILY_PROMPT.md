# Daily prompt (final)

Start a new Claude Code session on the repository **Deva-byte-byte/Campbell-**, attach the question paper (or paste the questions at the end), and paste this:

---

Use branch `claude/zen-cray-dt1fqe`. Read `CLAUDE.md` first and follow it exactly.

**Task:** compile model answers for the attached MCh Urology question paper(s). Call this set `<set-name>` (e.g. 2016-winter) and use `answers/<set-name>/` and `pdf/<set-name>/`.

**Before writing:** tell me the number of papers and questions, the LAQ/SAQ split, any repeated questions (answer once, cross-reference), any question whose meaning is unclear (state your assumption), and the estimated reading time. Then go ahead without waiting.

**Sources:**
1. My Campbell chapter notes in `reference/` first. Find the right chapters with `reference/INDEX.md` and grep `reference/text/`.
2. Then the latest EAU/AUA/NCCN (and other relevant) guidelines and landmark trials wherever the notes are thin or outdated. If they disagree with my notes, give both.
3. Accuracy is the top priority: no invented numbers, doses, dates or trials.

**Content rules:**
- Touch on **every relevant subtopic** in the matching chapters: core points explained briefly, secondary points mentioned in a phrase ("Also know:" line). Leave out only pure trivia.
- **Never reduce a core item to bare names**: classification tables, tests with their method, details that carry marks (e.g. brainstem reflexes with method and cranial nerves), operative/algorithm steps and key mechanisms must be written out.
- Keep all major exam subheadings, explain key concepts (why/how), clear short sentences where bullets would be cryptic, acronyms spelled out at first use in each answer.
- Length: LAQ about 700–750 words, SAQ about 300–330 words (including key points).
- Each answer ends with a "Key points to remember" box (3–4 points); each paper ends with a Rapid Revision Sheet.

**Process:**
1. Draft each paper in `answers/<set-name>/drafts/`.
2. Check every answer against its chapters (correct anything that disagrees).
3. Check coverage: every relevant chapter subtopic is at least mentioned.
4. Check core items: no table, test, steps or mechanism reduced to bare names.
5. Build with `tools/build_paper.py` and `tools/md2pdf.sh`: one A4 black-and-white PDF per paper. Render a page or two to check the layout.

**Deliver:** send me the PDFs, commit and push. Then tell me the reading time, which facts are not from my chapters, any chapter-vs-guideline differences, and any assumptions you made.

<paste questions here, or attach the paper>

---

## To add more reference chapters

> Use branch `claude/zen-cray-dt1fqe`, read `CLAUDE.md`, and add the attached PDFs to the reference library with `tools/addref.sh`. Skip byte-identical duplicates, keep both versions if a chapter differs from one already saved, then commit and push. Tell me which existing or likely exam answers each chapter relates to.

## To fix or improve an existing set

> Use branch `claude/zen-cray-dt1fqe` and read `CLAUDE.md`. In set `<set-name>`, fix the following: <describe>. Rebuild the PDFs, send them to me, commit and push.
