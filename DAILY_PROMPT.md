# Daily instruction to paste into a new Claude Code session

Start the session on the repository **Deva-byte-byte/Campbell-**, then paste this (attach the question paper PDF or paste the questions):

---

Use branch `claude/zen-cray-dt1fqe`. Read `CLAUDE.md` first and follow it exactly.

Today's task: compile model answers for the attached question paper(s) / the questions below.
- Source: my Campbell chapter notes in `reference/` first (use `reference/INDEX.md` and grep `reference/text/`), then the latest EAU/AUA/NCCN guidelines and landmark trials wherever needed. Accuracy is the top priority: no invented numbers.
- Format: half length (LAQ about 700 words, SAQ about 280), clear sentences where needed, all major subheadings, key concepts explained, acronyms spelled out at first use, key points after every answer, Rapid Revision Sheet at the end.
- Output: one A4 black-and-white PDF per paper, built with the tools in `tools/`. Send me the PDFs, commit and push.
- Before you start, tell me the number of questions, LAQ/SAQ split and estimated reading time, and flag any question whose meaning is unclear.

<paste questions here, or attach the paper>

---

To add more reference chapters, use this instead:

> Use branch `claude/zen-cray-dt1fqe`, read `CLAUDE.md`, and add the attached PDFs to the reference library with `tools/addref.sh`. Skip duplicates, then commit and push.
