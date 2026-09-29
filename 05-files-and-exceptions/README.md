# Module 5 — File handling and exception handling

**Exam weight: 5–8 marks per appearance, most papers; up to 25 when it's the whole
question.** The single most reliable mark cluster in Paper 4: *open with try/except, read
in the stated order, close in a suitable place* — the mark scheme gives a dedicated mark to
the exception handling and another to the close.

## 1. The three patterns

**A. Fixed count of lines** (e.g. "30 cards, number then colour" — J22/42 Q3(c); "5
questions, 3 lines each" — J21/41 Q3):

```python
try:
    file = open("CardValues.txt", "r")
    for _ in range(30):
        number = int(file.readline().strip())
        colour = file.readline().strip()
        Cards[index] = Card(number, colour)   # or .append
        index += 1
    file.close()
except Exception:
    print("File not found")
```

**B. Unknown length, loop until EOF** (J25/41 Q2, N25/41 Q3(e), J26/42 Q2(b)):

```python
try:
    file = open("TheData.txt", "r")
    line = file.readline().strip()
    while line != "":
        parts = line.split(",")
        value = int(parts[0])
        colour = parts[1].strip()
        ...                       # process
        line = file.readline().strip()
    file.close()
except Exception:
    print("File could not be opened")
```

**C. Write a new file** (J22/41 Q1(f), J26/41 Q2(c), N25/42 Q3(d) — note N25/42 explicitly
demands exception handling on the *write*):

```python
try:
    file = open("SelectedToys.txt", "w")
    for toy in selected:
        file.write(toy.ToyName + "," + str(toy.NumberBricks) + ","
                   + toy.Difficulty + "," + toy.Category + "\n")
    file.close()
except Exception:
    print("File could not be written")
```

Mode `"a"` appends (J25/41 Q2 writes six colour files by appending one item per line).

## 2. Non-negotiable details

- **`strip()` every line** — the trailing `"\n"` breaks `int()` and any `==` comparison.
- **Read order = the order the paper states.** "in the order: number, colour" is literal;
  the mark scheme awards the reads separately.
- **Cast numeric fields** (`int()`, `float()`) — usually its own mark point.
- **Close "in a suitable place"** — after the loop, inside the `try` (so it still runs on
  the success path). The mark scheme checks placement.
- **The except branch should output something** — "with catch and output" is the wording.
- **Data files may not exist in your practice folder** — create them (the course ships
  recreations in `data-files/`). In the real exam the file *is* provided; the except branch
  still earns its mark if the file opens.

## 3. Worked example — read a file into an array of objects (June 2023 P42 Q3(c))

**Reference: June 2023 Paper 42 Q3 [33 marks]** — the big one: `Employees.txt` stores, per
employee, hourly pay, employee number, job title — plus a bonus value line *only for
managers*. Your main program must instantiate `Employee` or `Manager` accordingly, then
`HoursWeek1.txt` (employee number + hours) drives `SetPay()`, then output everyone's total
pay.

The variable-length record is the teaching point: read the three fixed fields, then **peek**
at the next line and decide from its *type* — a bonus value parses as a number, a job title
does not:

```python
try:
    file = open("Employees.txt", "r")
    for i in range(8):
        hourly_pay = float(file.readline().strip())
        employee_number = int(file.readline().strip())
        next_line = file.readline().strip()
        try:
            bonus = float(next_line)        # parses -> manager's bonus
            job_title = file.readline().strip()
            employees[i] = Manager(hourly_pay, employee_number, bonus, job_title)
        except ValueError:
            employees[i] = Employee(hourly_pay, employee_number, next_line)
    file.close()
except Exception:
    print("File not found")
```

Note the *narrow* inner `except ValueError` — catching only what the peek can throw,
instead of a bare except that would also swallow real file errors.

Full runnable solution with both classes and the hours file:
`solutions/m07_employees.py`. This question combines Modules 5, 6 and 7 — attempt it after
those modules as a consolidation task.

## 4. Worked example — unknown length + split + six output files (June 2025 P41 Q2)

**Reference: June 2025 Paper 41 Q2 [25 marks]** — read `TheData.txt` (72 lines like
`10,red`, filename entered by the user), split each line into a number and a colour, store
into six per-colour arrays, then append each item to its colour's file (`Red.txt`,
`Blue.txt`, ...), with exception handling on both reading and writing.

Model excerpt (`solutions/m05_split_colours.py`):

```python
colour_files = {"red": "Red.txt", "green": "Green.txt", "orange": "Orange.txt",
                "pink": "Pink.txt", "blue": "Blue.txt", "yellow": "Yellow.txt"}

def read_data(filename):
    red, green, orange, pink, blue, yellow = [], [], [], [], [], []
    try:
        file = open(filename, "r")
        line = file.readline().strip()
        while line != "":
            value, colour = line.split(",")
            value = int(value)
            if colour == "red":
                red.append(value)
            elif colour == "green":
                green.append(value)
            # ... remaining colours
            line = file.readline().strip()
        file.close()
    except Exception:
        print("File could not be opened")
    return red, green, orange, pink, blue, yellow

def write_files(arrays):
    for colour, values in arrays.items():
        try:
            file = open(colour_files[colour], "a")
            for value in values:
                file.write(str(value) + "\n")
            file.close()
        except Exception:
            print("Could not write " + colour_files[colour])
```

**Mark scheme shape:** try/except with output (dedicated mark) / open with user filename /
EOF loop / split on comma / cast / store to the right array / open-append per file / write
one per line / close.

## 5. Worked example — write with exception handling (Nov 2025 P42 Q3(d))

**Reference: November 2025 Paper 42 Q3(d) [5 marks]** — after building a binary tree in a
2D array from `TreeData.txt`, write the whole tree array to a **new** file `Tree.txt`, one
node per line, comma-separated, "include exception handling when writing to the file".

```python
def write_all_to_file():
    try:
        file = open("Tree.txt", "w")
        for node in range(50):
            file.write(str(TreeArray[node][0]) + "," + str(TreeArray[node][1]) + ","
                       + str(TreeArray[node][2]) + "\n")
        file.close()
    except Exception:
        print("Could not write Tree.txt")
```

The screenshot for part (e)(ii) must show **the contents of `Tree.txt` and its filename**
in one image — open the file in a text editor beside the console before screenshotting.

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2021 P41 Q3(c) | Read 15 lines (3 per question) into objects, exception handling | part of 31 |
| Jun 2022 P41 Q1 | Read high scores + write top ten to a new file | 29 |
| Jun 2022 P42 Q3(c) | Read 30 cards (number, colour) into an array of objects | part of 27 |
| Nov 2021 P41 Q2(e) | Read `Pictures.txt` into 100 objects, count, exception handling | 8 |
| Nov 2022 P42 Q2(d) | Read 10 characters (name, x, y) into objects | 7 |
| Jun 2024 P41 Q2(b) | Read 9 CSV trees into objects, raise if file missing | 7 |
| Jun 2025 P41 Q2 | Unknown length, split, six colour files | 25 |
| Jun 2026 P41 Q2(b) | Read 16 CSV toy records, exception handling | 8 |
| Nov 2025 P42 Q3(c)(d) | Read 50 ints into tree; write tree to new file | 4 + 5 |
| Jun 2026 P42 Q2(b) | Read 30 space-separated avatars (string, bool, string, int) | 7 |

Sample data files for several of these are in `data-files/` (recreated formats).

## Common pitfalls

- No `try/except` → lose the dedicated exception-handling mark (it's free if you just
  always write it).
- Forgetting `file.close()` → lose the placement mark.
- `int(line)` without `strip()` → `ValueError` on the hidden `"\n"`.
- Reading fields in the wrong order after assuming the format — the order is always
  spelled out; underline it.
- Writing with `"w"` when the paper says append (`"a"`), or forgetting `"\n"` between
  written records.

## Checkpoint

- [ ] I can write patterns A, B and C from memory, including close and except-with-output.
- [ ] I always `strip()` before casting.
- [ ] I can peek ahead for variable-length records.
- [ ] I know when the paper demands exception handling on a *write*, not just a read.
