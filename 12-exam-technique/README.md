# Module 12 — Exam technique: the 150-minute protocol

**Time: revision weeks.** You now own every skill family. This module is about spending
them efficiently: time allocation, evidence discipline, recovery plans, and a mock
schedule using the papers in `9626-topical-questions\9618 Past Papers\`.

## 1. Time budget (75 marks / 150 minutes)

Work in marks-per-minute (≈2 marks/minute) but front-load the formulaic parts:

| Phase | Time | What |
|---|---|---|
| Setup | 5 min | Evidence document: name/centre/candidate number; save as `evidence_zz999_9999`. Read all three questions. |
| First pass — Q1 | ~35 min | Q1 is usually the most mechanical (ADT skeleton). Bank it fully, screenshots included. |
| Second pass — Q2/Q3 | ~45 min each | Usually OOP+files and one algorithm-heavy question. Do the formulaic parts of *both* before the hardest sub-parts. |
| Hardest parts | flexible | The 6–8-mark single parts (tree insert, AddItem, hash insert). Attempt — no negative marking. |
| Final 15 min | 15 min | Evidence audit (checklist below). Non-negotiable. |

Do not sink 30 minutes into one 6-mark part while unsaved 15-mark parts sit in your editor.

## 2. The evidence checklist (final 15 minutes)

Cambridge's rule: **not in the evidence document = no marks.** Before stopping:

- [ ] Every part's **code** is pasted at the correct part label.
- [ ] Every screenshot part has an image showing the **paper's exact test data** being run
      (including the deliberate overflow/invalid tests — e.g. the 11th push into a full
      stack, the invalid check-digit string).
- [ ] Program files saved with the exact names given (`Question1_J22` etc.).
- [ ] Screenshot content matches what the part demands (e.g. N25/42 Q3(e)(ii): the new
      file's contents *and* its filename visible).
- [ ] No part left blank — wrong-but-attempted code can still collect mark points; blank
      collects none.

## 3. Reading the question (the 30-second scan)

For every part, extract and jot at the margin:

1. **Procedure or function?** ("write program code for the function Push()") — header
   marks follow the wording; functions must return in all branches.
2. **Parameters and return type** — often printed explicitly; copy them verbatim.
3. **Sentinels and messages** — `−1`, `"Empty"`, `"Stack is full"`: use the exact strings.
4. **Bans** — "no inbuilt sorting functions", "without using an inbuilt split function",
   "inbuilt length allowed". Circle them.
5. **Global or local?** — "declared globally" changes your `global` declarations.
6. **Validation demanded or explicitly waived** — N23/42 Q1 says "You do not need to
   validate the parameters"; others demand validation loops. Both appear; read.

## 4. When pseudocode is printed — translate, don't rewrite

The most under-rated instruction in the paper: where pseudocode is given (complete or with
blanks), your answer is marked against *that* algorithm. Translate line by line — same
bounds, same comparison direction, same parameter names. J22/42's binary search computes
mid as `(Lower + (Upper − 1)) DIV 2`; candidates who "fixed" it to their own preferred form
still worked, but translated versions match mark points exactly and cost nothing.

## 5. Recovery plans

- **Syntax error you can't find** → comment the block; rebuild it in 5 lines from the
  skeleton. Never leave broken code pasted in the evidence document if you can paste a
  partial-but-running version instead.
- **Logic bug with no time** → paste the best version, add a comment showing intended
  behaviour; mark points for structure (header, checks, updates) can still score.
- **Screenshot missed earlier** → re-run the saved program with the printed test data and
  capture it; the program file is still on disk.
- **Blank mind on a hard ADT** → draw the array on paper and trace ONE operation by hand
  (Module 9's advice); 90 seconds that usually unblocks the whole part.

## 6. The mock schedule (use your own PDF collection)

Six full mocks before the exam — 2h30 each, closed book, evidence document discipline,
then self-mark against the published mark schemes (same folder):

| Mock | Paper | Why this one |
|---|---|---|
| 1 | June 2023 P42 | OOP inheritance + variable-length files (hardest file format) |
| 2 | June 2024 P42 | Recursion everywhere + two-class tree |
| 3 | June 2025 P41 | Circular queue + six-file write + object tree |
| 4 | June 2025 P42 | Stack calculator + hash table + inheritance |
| 5 | June 2026 P42 | No-builtin string limits + free-list linked list |
| 6 | Nov 2025 P43 | Composition grid + run-length + array-slice recursion |

Keep the remaining unique papers (see `question-bank.md`) as module practice and
fallback mocks. Self-marking rules: award mark points ruthlessly — no "it basically does
that". Log every lost mark into three buckets: *syntax slip*, *misread question*,
*didn't know* — the buckets tell you what to revise. Aim for 60+/75 (an A** boundary is
typically around 55–65 depending on session).

## 7. Final week

- Rebuild the canonical skeleton from memory: class template, try/except file patterns,
  stack/queue skeletons, bubble/insertion sorts, binary search both forms, recursive
  in-order traversal. (All are in `pseudocode-cheatsheet.md` and module READMEs.)
- Re-read the pitfalls sections of every module — they are all real mark losses observed in
  the mark schemes.
- Sleep. Paper 4 rewards a steady hand and a patient evidence workflow, not last-minute
  cramming.

## Checkpoint

- [ ] I can state my time budget per question and what happens in the final 15 minutes.
- [ ] I have a written recovery plan for syntax errors and missing screenshots.
- [ ] Six mocks are scheduled with self-marking dates.
- [ ] I can rebuild every canonical skeleton from memory.
