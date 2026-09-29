# Module 0 — How Paper 4 works (and how to set up like a candidate)

**Time: 1 lesson.** Before any Python, understand the game you are playing. Paper 4 is as
much an *evidence management* exam as a programming exam.

## The exam in numbers

| Fact | Detail |
|---|---|
| Duration | 2 hours 30 minutes |
| Total marks | 75, in 3 big questions |
| Language | Python 3 (console mode) — your choice from Java/VB/Python |
| Format | On-computer. You write, run, screenshot, and paste code + screenshots into `evidence.doc`/`evidence.docx` |
| Structure | Q1 ≈ 17–29 marks, Q2 ≈ 22–34, Q3 ≈ 17–33 — question types rotate (see `question-bank.md`) |

## The three-question pattern (2021–2026)

Almost every paper is three self-contained programs:

1. **One "algorithm/ADT" question** — a stack, queue, linked list, binary tree or hash
   table built on a global array, often with part of the algorithm given as pseudocode
   (to translate or complete).
2. **One "data" question** — read a text file into an array/records/objects, process,
   sometimes write results to a file. Heavy on exception handling.
3. **One "OOP" question** — declare classes with private attributes and a constructor,
   sometimes inherit/override, sometimes compose objects inside objects.

The rotation is not strict (some papers are ADT + OOP + algorithms), so the course trains
the underlying *skills*, then assembles them into full-paper runs in Module 12.

## The rules that cost real marks

Read the front cover of any past paper and internalise these:

1. **"If work is not saved in the evidence document, you will not receive marks for that
   task."** Correct code left in the IDE scores zero. After *every* part: save program →
   run → screenshot output → paste code and screenshot into the evidence document.
2. **Exact save names.** `Save your program as Question1_J22` — markers see these names.
3. **Exact test data.** Where the paper prints test inputs (often including an overflow or
   invalid case), your screenshot must show those exact inputs. The screenshot marks are
   awarded against the printed data, not "any run".
4. **Screenshot contents are specified.** Example: November 2025 Paper 42 Q3(e)(ii) requires
   the new file's contents *and the filename* visible in one screenshot.
5. **No internet, no email.** You may not look anything up. Train without a browser.

## What the mark scheme actually rewards (Python-specific)

Drawn from the 2022–2026 mark schemes (see `question-bank.md` for the full analysis):

- **`global` keyword**: when a procedure/function updates a module-level pointer or array,
  the model answers declare it (`global StackData`, `global QueueHead`). Do the same.
- **`self.__Attribute`** for private — the double underscore *is* the privacy mark.
- **Attribute declarations as comments** above the constructor: the papers explicitly
  instruct this for Python, and the comments earn the "declared with correct data types"
  mark.
- **`try/except` on file operations** usually carries its own dedicated mark, plus one for
  closing the file in a suitable place.
- **Functions must return in all branches** — mark points say "in all instances".
- **Banned builtins score zero for their mark points**: if the paper says "no inbuilt
  sorting function", the mark scheme describes the manual algorithm, so `list.sort()`
  earns nothing.
- **Marks are never deducted** (Cambridge Marking Principle): wrong extra code just earns
  nothing — so always *attempt* every part.

## Setting up your training environment

1. Install Python 3.11+ (or use whatever your school provides) and an editor — IDLE, VS Code
   or Thonny are all fine. Train in the same environment you'll use in the exam.
2. Create a course working folder. Every worked example and practice solution in this course
   lives in `solutions/`.
3. Sample data files matching the formats the papers describe are in `data-files/` — the
   original exam data files are not published, so these are recreations with the same
   structure; make your own too.
4. Time yourself from Module 1 onwards using the marks as minutes (75 marks / 150 minutes
   ≈ 2 minutes per mark).

## How to use this course

- Modules 1–11 teach one skill family each: read the notes, study the worked example
  (a real past-paper question, cited), then do the practice set against the original PDFs.
- `pseudocode-cheatsheet.md` is your constant companion — print it.
- `question-bank.md` indexes every paper question by skill.
- Module 12 is exam technique: a timed full-paper protocol and a mock schedule.

## Checkpoint

- [ ] I can name the three question families and roughly what each is worth.
- [ ] I know the evidence-document workflow (save → run → screenshot → paste) and why a
      correct unsaved answer is worth zero.
- [ ] My Python environment runs; I can create and run `hello.py`.
- [ ] I have the pseudocode cheatsheet printed or pinned.
