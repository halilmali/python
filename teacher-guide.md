# Teacher Guide — Running the 9618 Paper 4 Python Course

## What this course is

A 13-module skills course (Modules 0–12) mapping every recurring Paper 4 skill family to
real past-paper questions. It was built by cataloguing all 32 Paper 4 papers in the
collection (June & November 2021–2026, all variants) question by question — the catalogue
is [question-bank.md](question-bank.md), and it drives every practice set.

## Key structural facts (use these when planning)

- **Fixed format:** 75 marks, 2h30, three self-contained programs, evidence document +
  screenshots throughout. Language choice is Java/VB/Python console — this course trains
  Python.
- **Variant cloning:** within each session two variants are usually identical (typically
  41 = 43, with 42 distinct; see question-bank.md for the per-session pattern). Students
  do NOT need to attempt all three variants — one of 41/43 plus 42 per session is full
  coverage. Roughly 23 unique papers exist in the collection.
- **Mark-scheme behaviour toward Python** (verified across the 2022–2026 schemes):
  - `global` keyword expected where functions rebind module-level pointers.
  - Privacy mark = the double underscore (`self.__X`); attribute *declarations* are
    supplied as `#` type comments (papers instruct this explicitly).
  - Constructor header marks count `self` ("taking 4 parameters (Python 5)").
  - A dedicated mark for exception handling with catch *and output*, another for closing
    the file in a suitable place.
  - Functions must "return a value in all instances".
  - Where builtins are banned, the mark points describe the manual algorithm — a builtin
    call earns nothing.
  - No negative marking: never leave a part blank.
- **Data files** (e.g. `CardValues.txt`) are described by format in the papers but the
  files themselves are not published. The course ships format-accurate recreations with
  synthetic content in `data-files/` — have students build their own as an exercise too;
  it forces them to read the paper's field-order statements carefully.

## Suggested pacing

### Standard course — 13 weeks (one lesson + one homework per module)

| Week | Module | Homework (from the module's practice set) |
|---|---|---|
| 1 | 0 + 1 | Nov 2021 P41 Q1 (trace + run); Jun 2023 P41 Q1 |
| 2 | 2 | Jun 2022 P42 Q1 (full stack) |
| 3 | 3 | Nov 2022 P42 Q1 (2D jobs); Jun 2022 P41 Q1 (high scores) |
| 4 | 4 | Nov 2024 P41 Q1; Jun 2026 P43 Q1 |
| 5 | 5 | Jun 2025 P41 Q2; Jun 2026 P41 Q2 |
| 6 | 6 | Jun 2022 P42 Q3; Nov 2022 P42 Q2 |
| 7 | 7 | Jun 2023 P41 Q2; Jun 2025 P42 Q3 |
| 8 | 8 | Jun 2026 P41 Q1; Jun 2025 P41 Q1 |
| 9 | 9 | Jun 2026 P43 Q3; Jun 2025 P43 Q3 |
| 10 | 10 | Jun 2024 P41 Q1; Nov 2024 P41 Q1 |
| 11 | 11 | Nov 2023 P41 Q1; Nov 2022 P41 Q3 |
| 12 | 12 | Mock 1 (Jun 2023 P42) + self-mark |
| 13 | 12 | Mock 2 (Jun 2024 P42) + self-mark; remaining mocks as revision homework |

### Intensive revision — 4 weeks

Week 1: Modules 0–3 · Week 2: Modules 4–7 · Week 3: Modules 8–11 · Week 4: three mocks
with self-marking between them. Use the worked examples as lesson demonstrations and set
the practice sets as timed homework (marks ÷ 2 = minutes).

## Assessment and self-marking

- Publish the mark scheme alongside each paper (same folder in the collection). Train
  students to mark their own code against mark *points*, not impressions — this is itself
  exam training, since the paper's mark points are visible in the MS as one-per-line
  criteria.
- Have students log every lost mark in three buckets: **syntax slip / misread question /
  didn't know** (Module 12 §6). The distribution tells you what to re-teach; in our
  experience the middle bucket dominates until evidence discipline is habitual.
- Grade boundaries for Paper 4 typically land around 55–65/75 for A*; treat 60 as the
  mock target and 45 as the "passing the skills" floor.

## Classroom management notes

- **Screenshots discipline:** set homework as "code + screenshot + evidence doc" from week
  1, exactly as the exam demands. Marking a screenshot alongside the code is what makes
  the habit stick.
- **No-internet rule:** train with documentation closed. The papers' pseudocode and the
  cheatsheet are the only references in the exam.
- **Timing:** from Module 2 onward, put minutes on the board (marks × 2). Module 12's
  protocol assumes this has been rehearsed.
- **Pair-debugging:** the ADT modules (8–9) benefit from 10-minute pair sessions on paper
  before coding — tracing one insert/remove by hand is the reliable unblocker.
- The `solutions/` folder is for *after* attempts, or for live demos. Consider withholding
  it (or shipping `.pyc`-only) if you use the worked examples as assessed tasks.

## Mapping to the syllabus (2024–2027, Paper 4 section)

| Course module | Syllabus content (Paper 4 emphasis) |
|---|---|
| 1–2 | 19.1 programming techniques: data types, subroutines, structured programming |
| 3–4 | 19.2/19.3: arrays, files, string handling, validation |
| 5 | 19.3 file organisation and access; exception handling |
| 6–7 | 20.10 OOP: object classes, constructors, inheritance, polymorphism, containment |
| 8–9 | 19.4/20.10: abstract data types (stack, queue, linked list, binary tree), hash tables |
| 10–11 | 20.11/19.2: algorithm design — sorting, searching, recursion |
| 0, 12 | Practical exam skills: testing, evidence, program writing under time pressure |

(Section numbers follow the 2024–2027 syllabus wording; adjust if you teach an earlier
syllabus — the skill mapping is unchanged.)

## Caveats

- The 2026 series papers are recent live material — check your centre's policy before
  using them for assessed mocks before results are released.
- Mark scheme summaries in this course paraphrase Cambridge's published schemes for
  teaching purposes; always mark against the full original scheme.
- The sample data files are recreations, not the originals; the course states this in
  each file that uses one.
