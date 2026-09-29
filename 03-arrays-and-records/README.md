# Module 3 — 1D arrays, 2D arrays, parallel arrays and records

**Exam weight: ~20–30 marks in every paper.** Arrays are the substrate of Paper 4 — every
ADT in this syllabus is an array wearing a costume. This module covers declaration,
initialisation, traversal, formatted output, parallel arrays, and records.

## 1. 1D arrays — declare, initialise, traverse

```python
# DECLARE ArrayData : ARRAY[0:9] OF INTEGER
ArrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]    # J21-style given values
# or fixed-size empty structure to fill later:
DataArray = [0] * 100                               # "declare a 1D array of 100 integers"
```

Output formats the papers ask for — practise each:

```python
# one per line
for value in DataArray:
    print(value)
# all on one line, space-separated (J23/41 Q1(b), N25/42 Q2(b), J25/43 Q2(d))
for value in DataArray:
    print(value, end=" ")
print()
# "The number 7 is found 2 times."  (J23/41 Q1(d))
print(f"The number {search} is found {count} times.")
```

## 2. 2D arrays — the initialisation trap

```python
# ARRAY[0:9, 0:9] OF INTEGER   (10 x 10, J22/42 Q2)
ArrayData = [[0 for _ in range(10)] for _ in range(10)]

# ALWAYS this pattern. NEVER:
#   ArrayData = [[0] * 10] * 10      <- 10 references to the SAME row
```

Why: with `[[0]*10]*10`, `ArrayData[0][3] = 5` changes the shared row, so row 7 "also"
changes. This bug is invisible until you test with output — and the row you're testing with
is usually the one that gets corrupted.

Row-major traversal with a grid print (J22/42 Q2(b)(ii) — output as a 2D grid):

```python
for x in range(10):
    for z in range(10):
        print(ArrayData[x][z], end=" ")
    print()
```

2D arrays in the exam are usually **structured records in rows**: a binary tree as
`ArrayNodes[20][3]` (left pointer, data, right pointer — N21/N22/J26/N25), a linked list as
index/data/pointer columns (N24/41, J26/42), or jobs `[100][2]` (N22/42). Reading the
*column meanings* off the question table is the skill; the loops are easy.

## 3. Parallel arrays (June 2022 P41)

**Reference: June 2022 Paper 41 Q1 [29 marks]** — a top-ten table: global arrays of 11
player names (3 characters) and 11 scores, a `ReadHighScores()` that loads them from
`HighScore.txt`, an `OutputHighScores()` printing `Name Score`, a procedure that inserts a
new score in descending position, and `WriteTopTen()` saving to `NewHighScore.txt`.

Parallel arrays are just two 1D arrays sharing an index. Model excerpt
(`solutions/m03_high_scores.py`):

```python
PlayerNames = [""] * 11    # 3-character strings
PlayerScores = [0] * 11    # integers
```

The insert procedure is the classic "sorted insert" — shift from the end until the slot is
found. Practise it here, then it transfers to the linked-list and queue questions.

## 4. Records — the class-as-record pattern

Papers declare `TYPE RecordData ... ENDTYPE`. The cover rule allows a class declaration as
a record, and Python has no record type, so use a small class. When the paper says
attributes are public (N25/41 Q3(a) explicitly does), use plain names:

```python
# TYPE ToyRecord
#   ToyName       : STRING
#   NumberBricks  : INTEGER
#   Difficulty    : STRING
#   Category      : STRING
class ToyRecord:
    def __init__(self, toy_name, number_bricks, difficulty, category):
        self.ToyName = toy_name            # string
        self.NumberBricks = number_bricks  # integer
        self.Difficulty = difficulty       # string
        self.Category = category           # string
```

An **array of records** is then just a list of these objects. J26/41 Q2 is the full journey:
read 16 comma-separated toys, filter by difficulty (validated), write matches to
`SelectedToys.txt` in comma-separated form (`solutions/m05_toys_filter.py` — Module 5).

A record can also **contain an array**: J23/42's `Employee` has `PayYear2022[0:51]`
(52 weekly pays, all initialised to 0.0):

```python
class Employee:
    def __init__(self, hourly_pay, employee_number, job_title):
        self.HourlyPay = hourly_pay
        self.EmployeeNumber = employee_number
        self.JobTitle = job_title
        self.PayYear2022 = [0.0 for _ in range(52)]
```

## 5. Worked example — 2D array + random fill (June 2022 P42 Q2)

**Reference: June 2022 Paper 42 Q2(a) [4 marks]** — declare a 10×10 integer 2D array and
initialise every element with a random number between 1 and 100.

```python
import random

ArrayData = [[0 for _ in range(10)] for _ in range(10)]
for x in range(10):
    for z in range(10):
        ArrayData[x][z] = random.randint(1, 100)
```

**Mark scheme shape:** correct 2D declaration / nested loops / random in range (mark scheme
allows inclusive or exclusive interpretation) / assignment into the right indices.
Part (b)(ii) then wants the grid output shown in §2 above — three marks for
row loop, column loop with spacing, newline per row.

## 6. Worked example — 2D array with column meanings (Nov 2022 P42 Q1)

**Reference: November 2022 Paper 42 Q1 [23 marks]** — `Jobs[0:99, 0:1]` holding job numbers
and priorities; initialise to −1; `AddJob()` stores a pair or reports full; `InsertionSort()`
orders by priority keeping pairs together; `PrintArray()` formats output.

Sorting a 2D array "by column 1 while dragging column 0 along" is a recurring twist. Model
excerpt (`solutions/m03_jobs_insertion_sort.py`):

```python
def insertion_sort():
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        key_job = Jobs[i][0]
        key_priority = Jobs[i][1]
        j = i - 1
        while j >= 0 and Jobs[j][1] > key_priority:
            Jobs[j + 1][0] = Jobs[j][0]
            Jobs[j + 1][1] = Jobs[j][1]
            j -= 1
        Jobs[j + 1][0] = key_job
        Jobs[j + 1][1] = key_priority
```

The whole row moves as a unit — that is the mark point examiners look for.

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2021 P41 Q1 | Linked list as array of records (declare + traverse + add) — pairs with Module 9 | 24 |
| Jun 2022 P41 Q1 | Parallel-array high-score table, read/write files | 29 |
| Jun 2022 P42 Q2 | 2D random array, grid output, sort, recursive search | 23 |
| Nov 2022 P42 Q1 | 2D job array + insertion sort by priority | 23 |
| Nov 2024 P42 Q3 | 2D string array from file, two-key bubble sort, formatted output | 17 |
| Jun 2026 P41 Q2 | Records: read 16 toys, filter, write matches | 28 |
| Nov 2025 P41 Q3 | Hash table as 100×10 2D array of Record objects | 25 |

## Common pitfalls

- The shared-row 2D initialisation bug.
- Hardcoding lengths (`for i in range(10)`) where the paper says the structure must work
  "for any length" — use `len(array)`.
- Mixing up row/column order after re-reading the question's table — annotate the columns
  (`# col 0 = left pointer, col 1 = data, col 2 = right pointer`) before writing code.
- Forgetting that a "record" question wants the class *declared and used*, not a
  parallel-array shortcut (the declaration marks live in the class).

## Checkpoint

- [ ] I initialise 2D arrays with a comprehension, never `[[x]*n]*m`.
- [ ] I can print an array as a grid and as one space-separated line.
- [ ] I can declare a record-as-class with type comments and build an array of them.
- [ ] I can insertion-sort a 2D array by one column, moving whole rows.
