# Module 1 — Pseudocode → Python foundations

**Exam weight: background marks in every paper.** Nearly every Paper 4 part is a
translation task: the paper gives pseudocode (sometimes complete, sometimes with blanks)
and you reproduce the logic in Python. This module makes the translation automatic.

## 1. The translation rules that matter

Everything is in `pseudocode-cheatsheet.md`; here are the five that decide marks:

1. **Assignment is `<-` in pseudocode, `=` in Python.** Comparisons that were `=` become
   `==`. Writing `if x = 5:` is a syntax error — under exam pressure this happens.
2. **`FOR i <- 0 TO 9` is inclusive both ends** → `range(0, 10)`. Translated bounds must
   match the printed pseudocode exactly, especially in sorts:
   `FOR Z <- 0 TO ArrayLength - Y - 2` → `range(0, ArrayLength - Y - 1)`.
3. **`DIV` is integer division** → `//` (or `int(a / b)`, the form the mark scheme's own
   models use). `MOD` → `%`.
4. **`OUTPUT "x = " & X`** → `print("x = " + str(X))` or `print(f"x = {X}")`. When
   concatenating with `+`, *every* piece must be a string.
5. **`INPUT` returns a string** → cast immediately: `int(input())`, `float(input())`.

## 2. Worked example — translate a complete recursive function (Nov 2021)

**Reference: November 2021 Paper 41 Q1(a)(b) [6 marks]** —
`9618 Past Papers\9618 Computer Science November 2021 Question paper 41.pdf`

The paper gives a function `Unknown(X, Y)` in pseudocode: if `X < Y` it outputs `X + Y`
and returns `Unknown(X + 1, Y) * 2`; if `X = Y` it returns 1; otherwise it outputs
`X + Y` and returns `Unknown(X - 1, Y) DIV 2`. Parts (a)–(b) ask you to write it as
program code and have the main program output the parameters and return value for three
calls (`Unknown(10, 15)`, `Unknown(10, 10)`, `Unknown(15, 10)`).

**Model solution** (`solutions/m01_unknown_function.py`):

```python
def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return int(Unknown(X - 1, Y) / 2)    # DIV

for (x, y) in [(10, 15), (10, 10), (15, 10)]:
    print("Parameters:", x, y)
    print("Return value:", Unknown(x, y))
```

Two translation details earn their keep here: the multiplication/division applies to the
**returned** value (it happens on the way back up), while the OUTPUT happens on the way
down; and `DIV` becomes `int(... / 2)` — the form the mark scheme's own models use.
Trace `Unknown(10, 15)` by hand first: it outputs 25, 26, 27, 28, 29 on the way down,
hits the base case at (15, 15), and the returns come back multiplied — 2⁵ = 32. Verify by
running; the exam gives you a computer precisely so that output-prediction parts can be
checked before you commit the screenshot.

**Mark scheme shape:** one mark for the correct structure/branching, one for both
recursive calls with the changed parameter, one for the outputs in the right places.

## 3. Worked example — I/O, casting and validation loop

**Reference: November 2022 Paper 41 Q1(c) [7 marks]** — reads a search value from the user,
validates it as a whole number in 0–100 inclusive, repeats until valid, then counts
occurrences in an array loaded from `IntegerData.txt`.

The validation loop is the transferable part — this exact shape appears in a dozen papers:

```python
def get_valid_value():
    valid = False
    while not valid:
        try:
            search_value = int(input("Enter a whole number between 0 and 100: "))
            if 0 <= search_value <= 100:
                valid = True
            else:
                print("Out of range")
        except Exception:
            print("Not a whole number")
    return search_value
```

**Mark scheme shape:** loop structure / input cast / range check with both ends / repeat
until valid / (here) using the value in the count. Learn the shape once, reuse everywhere
(J22/41 name-length + score validation, N25/42 direction/minutes validation,
N24/41 fence height/risk validation, J26/42 avatar criteria validation...).

## 4. Random numbers

Only occasional (J22/42, J25/41, N25/41, N25/42) but easy marks:

```python
import random
value = random.randint(1, 100)    # inclusive; MS allows inclusive or exclusive
```

J25/41 Q1(d) and N25/41 Q1(d) wrap random generation in an enqueue/push loop — combine with
Module 8.

## Practice set (open the PDFs, attempt before looking at anything)

| Reference | Task | Marks | Solution file |
|---|---|---|---|
| Nov 2021 P41 Q1 | Recursive trace + iterative rewrite (full question) | 17 | — (do the trace by hand) |
| Nov 2023 P42 Q2(a) | Translate an iterative divisor-sum function (MODULUS loop) | 5 | — |
| Nov 2023 P41 Q1(a) | Translate an iterative vowel-counting function (MID/LENGTH) | 5 | `solutions/m01_iterative_vowels.py` |
| Jun 2023 P41 Q1 | Read 25 ints from a file, validate input 0–100, linear search counting matches | 18 | `solutions/m01_data_linear_search.py` |

For the last one you need a `Data.txt` with 25 integers — `data-files/J23-41/Data.txt`.

## Common pitfalls (mark-losing habits)

- `=` inside `if` (should be `==`) — the single most common Paper 4 Python syntax error.
- Forgetting `int()` on `input()` then comparing with `>` or doing arithmetic — type error.
- `range(0, n)` where the pseudocode says `TO n` (off-by-one) — silently wrong, silently
  unmarked.
- Division producing floats where the paper wants integers (`10 / 3` → `3.3333` not `3`).
- Uppercase `TRUE`/`FALSE` in Python instead of `True`/`False`.

## Checkpoint

- [ ] I translate FOR loops with inclusive bounds without thinking.
- [ ] I know `DIV`→`//` and `MOD`→`%`, and I cast `input()` immediately.
- [ ] I can write the repeat-until-valid loop shape from memory.
- [ ] I traced a recursion on paper before running it.
