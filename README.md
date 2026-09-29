# Python for Cambridge 9618 Paper 4 — A Complete Preparation Course

A skill-by-skill course that prepares A Level students for **9618 Paper 4 (Practical)**
using Python 3 (console mode), built directly on the past papers in
`C:\Users\mali\Desktop\cs\9626-topical-questions\9618 Past Papers\` (June & November
2021–2026).

Every worked example and practice task cites a real paper question (session, variant,
question part, marks). Students attempt the questions from the original PDFs in that
folder; this course supplies the teaching, the Python–pseudocode bridge, model solutions,
and mark-scheme-guided commentary.

## Web course (recommended way to study)

The whole course also builds into a self-contained static website:

```bash
python build_site.py          # regenerates ./site (42 pages)
```

Serve it with any static server, e.g.:

```bash
cd site
python -m http.server 8123    # then open http://127.0.0.1:8123/
```

(Opening `site/index.html` directly from disk also works.) The site adds: sidebar
navigation with previous/next paging, client-side full-text search (press `/`),
syntax-highlighted code with copy buttons, a viewer for all 24 model solutions plus the
sample data files, per-module **checkpoint progress** and a course-wide progress bar
(saved in the browser), and a light/dark theme. No external dependencies — works fully
offline, so it can be shared with students as a folder or zipped.

## Start here

1. **[pseudocode-cheatsheet.md](pseudocode-cheatsheet.md)** — the translation table the
   whole course leans on. Print it for every student.
2. **[00-exam-orientation](00-exam-orientation/README.md)** — how the exam works, the
   evidence-document rules that decide real marks, and how the mark schemes treat Python.
3. **[question-bank.md](question-bank.md)** — every unique paper question catalogued by
   topic and marks, with a skill→question index.

## The modules

| # | Module | Core skill | Typical exam weight |
|---|---|---|---|
| 0 | [Exam orientation](00-exam-orientation/README.md) | Format, evidence discipline, setup | — |
| 1 | [Python foundations](01-python-foundations/README.md) | Pseudocode→Python translation, validation loops | background in every paper |
| 2 | [Modular programming](02-modular-programming/README.md) | Procedures/functions, parameters, `global` | every paper |
| 3 | [Arrays & records](03-arrays-and-records/README.md) | 1D/2D arrays, parallel arrays, records | ~20–30 marks |
| 4 | [Strings & validation](04-strings-and-validation/README.md) | No-builtin string algorithms, validation | 10–20 marks |
| 5 | [Files & exceptions](05-files-and-exceptions/README.md) | Read/write patterns, try/except marks | 5–25 marks |
| 6 | [OOP foundations](06-oop-foundations/README.md) | Classes, `__init__`, getters, arrays of objects | ~20–30 marks |
| 7 | [OOP advanced](07-oop-inheritance/README.md) | Composition, inheritance, overriding, `super()` | 15–30 marks |
| 8 | [Stacks & queues](08-stacks-and-queues/README.md) | Array-based ADTs with pointer conventions | 20–29 marks |
| 9 | [Lists, trees, hashes](09-lists-trees-hashes/README.md) | Linked lists, binary trees, hash tables | 20–30 marks |
| 10 | [Searching & sorting](10-searching-and-sorting/README.md) | Linear/binary search, bubble/insertion sort | 10–20 marks |
| 11 | [Recursion](11-recursion/README.md) | Trace, translate, iterative↔recursive | 6–17 marks |
| 12 | [Exam technique](12-exam-technique/README.md) | 150-minute protocol, evidence audit, mock plan | all of it |

Each module follows the same shape: **objectives → teaching notes → worked example(s)
from real papers with model solutions → practice set citing original PDFs → common
pitfalls → checkpoint**.

## Solutions and data files

- [`solutions/`](solutions/) — 24 runnable Python model solutions (m01–m10...), one or
  more per module. Each file's docstring states the reference question, the run command
  and any test input. All verified to run cleanly.
- [`data-files/`](data-files/) — sample data files in the formats the papers describe
  (`CardValues.txt`, `Employees.txt`, `TheData.txt`, ...), with synthetic content. The
  original exam data files are not published, so these are recreations — students should
  also make their own.

Run a solution from the `solutions/` folder, e.g.:

```bash
cd solutions
python m01_unknown_function.py
echo 7 | python m01_data_linear_search.py          # with test input
seq 1 11 | python m08_queue_j26.py                 # overflow test data
```

## Suggested pathway

- **Full course (12–14 weeks):** Modules 0–1, then 2–5, then 6–7, then 8–11, one module
  per week, each ending with its practice set. Module 12's six mocks fill the final
  revision weeks (see the schedule in [12-exam-technique](12-exam-technique/README.md)).
- **Intensive revision (4 weeks):** Cheatsheet + Module 0, then two modules per week
  chosen by each student's weakest skills, daily practice from `question-bank.md`,
  mocks in the final week.
- **Top-up for strong students:** Modules 9 and 11 (the discriminator skills), then
  straight into mocks from the June 2025/2026 papers.

Teachers: see [teacher-guide.md](teacher-guide.md) for pacing, homework and assessment
suggestions, and notes on how the papers duplicate variants.

## Notes on the source material

- Question references use the form *June 2022 Paper 42, Q1(c) [6 marks]*; original PDFs
  are in `9626-topical-questions\9618 Past Papers\` (2026 papers in `9626-topical-questions\2026\`).
- Within each session, two of the three variants are usually clones (typically 41 = 43,
  with 42 distinct); `question-bank.md` records which.
- The 2026 papers in the collection are marked as live 2026 series material — check your
  centre's rules before using them for assessed mocks before the results window closes.
