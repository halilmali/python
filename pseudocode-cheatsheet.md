# Cambridge Pseudocode → Python 3 Cheatsheet (Paper 4 edition)

Paper 4 questions are written in Cambridge pseudocode; you answer in Python (console mode).
Translating fluently — and knowing where the mark scheme expects Python conventions — is the
foundation of this whole course. Print this and keep it next to you.

Cover rules printed on every Paper 4 paper:

- Use **Python (console mode)** (or Java/VB console).
- A **class declaration can be used to declare a record**.
- If your language has no arrays, **a list can be used instead** (Python).
- Work not saved in the **evidence document** scores zero, even if correct.

## 1. Variables, declarations, type comments

Python declares nothing — the mark scheme's own models annotate types with comments, and
Paper 4 explicitly instructs: *"If you are writing in Python, include attribute declarations
using comments."*

```python
# pseudocode: DECLARE StackData : ARRAY[0:9] OF INTEGER
StackData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # array of 10 integers
StackPointer = 0                              # integer
```

| Pseudocode type | Python | Note |
|---|---|---|
| INTEGER | `int` | cast with `int()` |
| REAL | `float` | cast with `float()` |
| STRING / CHARACTER | `str` | cast with `str()` |
| BOOLEAN | `bool` | `True` / `False` (capitalised!) |
| DATE | `datetime.date` | `date(2019, 1, 1)`; `.year` gives the year |

## 2. Fixed-size structures

```python
# ARRAY[0:9] OF INTEGER            ->  10 elements
StackData = [0] * 10
# ARRAY[0:19, 0:2] OF INTEGER      ->  20 rows x 3 columns
ArrayNodes = [[-1, -1, -1] for _ in range(20)]   # separate row objects!
# initialise every element to -1:
ArrayNodes = [[-1 for _ in range(3)] for _ in range(20)]
```

**Trap:** `[[‑1]*3]*20` creates 20 references to the *same* row — changing one row changes
all of them. Always use a comprehension for 2D initialisation.

Python lists grow with `.append(x)` — accepted by the mark scheme, but when the question
says "declare an array of 30 elements", create the fixed-size list first (`[None]*30` or
`[0]*30`) so your indices and full-checks behave like the pseudocode.

## 3. Operators

| Pseudocode | Python | Note |
|---|---|---|
| `+  -  *` | `+  -  *` | |
| `/` (real division) | `/` | |
| `DIV` (integer division) | `//` or `int(a / b)` | mark scheme models use `int(...)`; `//` is cleaner and accepted |
| `MOD` | `%` | |
| `=` compare, `<-` assign | `==` compare, `=` assign | classic Paper 4 slip: `=` in an IF is a syntax error |
| `<>` | `!=` | |
| `AND  OR  NOT` | `and  or  not` | lowercase |
| `&` (string concat) | `+` (both sides must be `str`) | or f-strings: `f"x = {x}"` |

## 4. Console I/O

```python
# OUTPUT "Enter name"                              |  INPUT Name
name = input("Enter name: ")        # always a string!

# INPUT Num : INTEGER
num = int(input())                  # cast immediately
# INPUT Price : REAL
price = float(input())
```

- `input()` returns a string. If the question wants a number, cast at once — validation
  parts often award the cast as a mark point.
- `print()` adds a newline; `print(x, end=" ")` keeps one line; `print(a, b)` inserts a
  single space. Grid output (J22/42 Q2(b)(ii)) wants `end=" "` per row then a bare `print()`.

## 5. Selection

```python
# IF x > 10 THEN
#   OUTPUT "big"
# ELSE
#   OUTPUT "small"
# ENDIF
if x > 10:
    print("big")
else:
    print("small")
```

Multiple branches: pseudocode `CASE ... OF` → Python `elif` chain. There is no `switch`.

## 6. Loops

```python
# FOR X <- 0 TO 9 ... NEXT X                 (inclusive!)
for x in range(10):            # range(10) is 0..9 — inclusive upper bound - 1
    ...
# FOR X <- 0 TO 9 with step 2:
for x in range(0, 10, 2):      # pseudocode STEP 2
    ...
# REPEAT ... UNTIL valid
while True:
    value = int(input())
    if 1 <= value <= 100:
        break
# WHILE NOT EOF
while condition:
    ...
```

**The #1 loop bug:** pseudocode `FOR Y <- 0 TO ArrayLength - 2` means *inclusive* of
`ArrayLength - 2` → `range(0, ArrayLength - 1)`. When translating bubble sort from the
paper's pseudocode, keep each bound exactly as printed.

## 7. Modular programming

```python
# PROCEDURE OutputData(ArrayData : ARRAY OF INTEGER)
def output_data(array_data):
    ...

# FUNCTION Push(Value : INTEGER) RETURNS BOOLEAN
def push(value):
    ...
    return True

# BYREF: Python passes mutable objects (lists) by reference automatically.
# To let a function REBIND a global scalar, declare it:
def pop():
    global stack_pointer
    ...
```

- Mark schemes expect the `global` keyword inside functions that update module-level
  pointers/variables (their own Python models do exactly this, e.g. `global StackData`,
  `global QueueHead`).
- Pseudocode parameters `BYREF` (lists, arrays of objects) work naturally; `BYVAL` scalars
  are also fine because rebinding a parameter never affects the caller.
- Naming: identifiers from the paper (`StackData`, `Push`) are usually kept verbatim in the
  models. It is safe (and faster to mark) to mirror the paper's own names, even though
  camelCase is not PEP 8 style. This course uses the paper's names in solutions.

## 8. Strings

| Pseudocode | Python | Note |
|---|---|---|
| `LENGTH(S)` | `len(s)` | often the ONLY builtin allowed |
| `MID(S, start, n)` | `s[start-1 : start-1+n]` | pseudocode positions are usually 1-based! |
| `LEFT(S, n)` | `s[:n]` | |
| `RIGHT(S, n)` | `s[-n:]` | |
| `UCASE(S)` | `s.upper()` | |
| `LCASE(S)` | `s.lower()` | |
| `TOUPPER(ch)` / `TOLOWER(ch)` | `ch.upper()` / `ch.lower()` | |
| `ASC(ch)` | `ord(ch)` | |
| `CHR(n)` | `chr(n)` | |
| `SPLIT`-like tasks | `s.split(',')` | banned where the paper says "no inbuilt split" — write a loop |

Where the paper bans builtins (e.g. "find the longest string without inbuilt functions",
"inbuilt length allowed"), the ban applies to that feature only — the ban's scope is always
stated in the question. Compare char-by-char with `ord()` or `<`/`>` when comparison
builtins are forbidden.

## 9. File handling (text)

Paper 4 wants **exception handling** on file operations — it usually carries a dedicated
mark ("appropriate use of exception handling, with catch and output") and a separate mark
for closing the file in a suitable place.

```python
# reading a fixed number of lines
try:
    file = open("CardValues.txt", "r")
    for _ in range(30):
        number = int(file.readline().strip())
        colour = file.readline().strip()
        cards.append(Card(number, colour))
    file.close()
except Exception:
    print("File not found")

# reading to end of file, unknown length
try:
    file = open("TheData.txt", "r")
    line = file.readline().strip()
    while line != "":
        value, colour = line.split(",")
        ...
        line = file.readline().strip()
    file.close()
except Exception:
    print("File could not be opened")

# writing a new file
try:
    file = open("NewHighScore.txt", "w")
    for i in range(10):
        file.write(names[i] + " " + str(scores[i]) + "\n")
    file.close()
except Exception:
    print("File could not be written")

# appending (one item per line)
file = open("Red.txt", "a")
file.write(item + "\n")
file.close()
```

- `strip()` every line — trailing `"\n"` breaks `int()` and equality checks.
- Read order = the order stated in the question (number then colour, name then x then y...).
- Variable-length records (J23/42 `Employees.txt`: bonus line only for managers) need a
  "peek": read the next line, decide from its content.
- `open(...)` mode `"r"` read, `"w"` write (overwrites), `"a"` append.

## 10. OOP

```python
class Card:
    # self.__Number : INTEGER
    # self.__Colour : STRING
    def __init__(self, number, colour):
        self.__Number = number
        self.__Colour = colour

    def get_number(self):
        return self.__Number
```

- **Private** = double underscore prefix: `self.__Number`. The privacy mark is awarded on
  the double underscore.
- **Attribute declarations as comments** directly above `__init__` — the question asks for
  them explicitly, and they earn the "declared with correct data types" mark.
- Constructor header marks accept the Python parameter count (`self` counts as one extra:
  a 4-parameter constructor is `def __init__(self, a, b, c, d)` — "Python 5").
- Inheritance: `class Manager(Employee):` then `super().__init__(...)` to call the parent
  constructor. Overriding needs no keyword — just redefine the method with the same name.
- `__str__` is *not* asked for; produce whatever string the question's OUTPUT format shows.

## 11. Records

The rubric lets a class serve as a record, but when the paper says `TYPE RecordData` and
Python has no records, use a class with plain (public) attributes:

```python
# TYPE RecordData
#   ID     : STRING
#   Total  : INTEGER
class RecordData:
    def __init__(self, record_id):
        self.ID = record_id   # string
        self.Total = 0        # integer
```

Some papers explicitly demand **public** attributes (N25/41 Q3(a)) — then plain
`self.Key = ...` without underscores is the mark-earning form.

## 12. Random numbers

```python
import random
number = random.randint(1, 100)   # inclusive both ends; MS: "allow inclusive or exclusive"
```

## 13. DIV/MOD arithmetic in context

Check-digit and hashing questions are DIV/MOD machines:

```python
mid = (lower + upper) // 2          # binary search
bucket = key % 100                  # hash: key MOD 100
check = (total // 10) % 10          # weighted check digit
```

## 14. Functions must return in ALL branches

Mark points literally say "returns a value in all instances / in all possible situations".
A function that falls through a branch without returning loses the mark:

```python
def push(value):                 # every path returns
    global stack_pointer
    if stack_pointer == 10:
        return False
    StackData[stack_pointer] = value
    stack_pointer += 1
    return True
```

## 15. Where Python is actually *easier* (use it)

- Tuple swap in sorts: `ArrayData[x][z], ArrayData[x][z+1] = ArrayData[x][z+1], ArrayData[x][z]`
  — explicitly accepted by the mark scheme.
- Slicing for string algorithms (unless banned).
- `del lst[-1]` for pop-from-list models (seen in the mark scheme's own answers).
- f-strings for the exact output formats the paper demands.

## 16. Evidence discipline (worth marks every paper)

1. Save each program with the exact name given (`Question1_J22` → `Question1_J22.py` is fine).
2. After each part: save, run, **screenshot the console output**, paste code *and* screenshot
   into the evidence document at the right part.
3. Use the **exact test data** printed in the paper — screenshots are marked against it
   (including deliberate overflow/invalid-input tests, e.g. 11 pushes into a 10-slot stack).
4. Screenshot content is specified: e.g. N25/42 Q3(e)(ii) requires the new file's contents
   *and its filename* visible in one screenshot.
