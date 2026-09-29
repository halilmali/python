# Module 11 — Recursion: trace, translate, convert

**Exam weight: 6–17 marks in roughly two-thirds of papers.** Paper 4 tests recursion in
three ways: *trace it* (predict output), *translate it* (recursive pseudocode → Python, or
fill blanks), and *convert it* (iterative ↔ recursive). The mark scheme splits each into
mechanical points: base case / comparison / recursive call with changed parameter /
aggregation / no superfluous code.

## 1. Reading a recursive function

Every exam recursion has the same anatomy:

```python
def recursive_value(number, to_find):
    if number == to_find:               # base case 1
        return number
    if number % to_find == 0:           # condition
        return number + recursive_value(number - 1, to_find)   # change + aggregate
    return recursive_value(number - 1, to_find)                # change, no aggregate
```

The four questions to ask of any recursion:
1. What stops it (base case)?
2. What changes in each call (the "progress" — must move toward the base case)?
3. What do the returned values do on the way back (aggregation, or just propagation)?
4. What side effects (OUTPUT/print) happen on the way **down** vs on the way **up**?

## 2. Tracing — the discipline

N21/41 Q1(b) has the main program call the given recursive function `Unknown(X, Y)` three
times and output each return value; the marks are for correct outputs. Trace in a table —
one row per call, columns for parameters, branch taken, print, return:

```
Call           Branch        Prints      Returns
Unknown(10,15) x < y         25          Unknown(11,15) * 2
Unknown(11,15) x < y         26          Unknown(12,15) * 2
...            ...           ...         ...
Unknown(15,15) x = y         —           1
```

Then unwind: the returns multiply on the way back up, so `Unknown(10, 15)` = 2⁵ = 32.
Always trace mechanically; "it looks like it doubles" is how marks die. Then **verify by
running** — the exam gives you a computer; output-prediction parts can be checked before
you commit the screenshot.

## 3. Worked example — iterative → recursive (Nov 2023 P41 Q1)

**Reference: November 2023 Paper 41 Q1 [16 marks]** — the paper supplies an iterative
pseudocode function counting vowels in a string (using MID and LENGTH); part (a) asks you
to translate it to Python (5 marks); part (b) asks you to **rewrite it recursively**
(6 marks).

Iterative translation:

```python
def IterativeVowels(Phrase):
    total = 0
    for x in range(len(Phrase)):
        if Phrase[x] in "aeiou":       # or explicit comparisons per the printed code
            total += 1
    return total
```

Recursive rewrite — the standard "index parameter" pattern:

```python
def RecursiveVowels(Phrase, x):
    if x == len(Phrase):               # base case: past the end
        return 0
    if Phrase[x] in "aeiou":
        return 1 + RecursiveVowels(Phrase, x + 1)
    return RecursiveVowels(Phrase, x + 1)
# call: RecursiveVowels("imagine", 0)
```

**Mark scheme shape (recursive version):** base case / comparison per character /
recursive call with progress (+1 or shorter string) / aggregation of 1 / remainder correct
with *nothing superfluous* (that literal point exists in the mark scheme — leave out
debug prints).

## 4. Worked example — recursive → iterative (Nov 2021 P41 Q1(c))

**Reference: November 2021 Paper 41 Q1(c) [7 marks]** — after running the given recursive
`Unknown(X, Y)` (Module 1's example), rewrite it as an **iterative** `IterativeUnknown()`
and call it with the same three parameter pairs.

Conversion recipe: replace recursion with a loop whose condition mirrors the base case,
and turn "recursive call" into "update the variables". The only subtlety here is that the
`* 2` and `DIV 2` apply to the *returned* value on the way back up — so accumulate them
into a running result, once per step:

```python
def IterativeUnknown(X, Y):
    result = 1
    while X != Y:
        print(X + Y)               # each level printed X + Y on the way down
        if X < Y:
            X += 1
            result = result * 2    # applied to the return value at each level
        else:
            X -= 1
            result = int(result / 2)
    return result
```

Same prints, same return values — that's the 7 marks. (Check `Unknown(15, 10)` by hand:
five halvings starting from 1 collapse to 0 — integer division. Candidates who used real
division get 0.03125 and lose the mark.)

## 5. Worked example — fill-in-the-blanks recursion (Nov 2023 P42 Q2(b))

**Reference: November 2023 Paper 42 Q2(b)(i) [7 marks]** — a divisor-sum function given as
incomplete recursive pseudocode: five gaps covering the base case (`Number = 0` → return
0... per the printed structure), the match condition, the two recursive calls with changed
parameters, and the aggregation.

Method: fill the gaps **on the paper first** (they are 5 of the 7 marks), then translate
the completed function to Python. The mark scheme awards one mark per gap, plus one for
both recursive calls being accurate *and* correctly placed, plus one for the remainder with
nothing superfluous. The same fill-blanks pattern appears in N22/41 Q3(c) (tree search),
N21/41 Q3(b) (tree AddNode), J22/42 Q2(c) (binary search), J22/41 Q3(c) (queue Enqueue).

## 6. Recursion over structures

- **Recursive traversal** — array-based tree (J26/43 Q3(e), N21/41 Q3(e), 7 marks each) and
  object-based tree (J25/41 Q3(c), 5 marks): in-order = left / print / right, with the −1
  or `None` base case. Written out in Module 9.
- **Recursive counting over an array** (N25/43 Q3(a), 9 marks): the paper requires passing
  "the array without the first element" — Python slicing makes this natural:

```python
def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:                      # base case: empty array
        return 0
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    return RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
```

  Keep the parameter names and structure the paper specifies even where a Pythonic loop
  would be shorter — the recursion *is* the requirement.

## 7. Practice set

| Reference | Task | Marks |
|---|---|---|
| Nov 2021 P41 Q1 | Trace + iterative rewrite of a recursive function | 17 |
| Nov 2023 P41 Q1 | Translate iterative vowels; rewrite recursively | 16 |
| Nov 2023 P42 Q2 | Translate iterative divisor-sum; complete recursive version | 17 |
| Nov 2022 P42 Q3(d) | Convert a given iterative output function to recursion | 6 |
| Nov 2022 P41 Q3(c)(d) | Recursive tree search (blanks) + recursive post-order | 12 |
| Jun 2024 P42 Q3 | Recursive insertion sort translate + iterative; recursive binary search | 23 |
| Nov 2025 P43 Q3(a) | RecursiveCount with array-minus-first-element | 9 |
| Jun 2026 P43 Q3(e) | Recursive in-order traversal on 2D-array tree | 7 |

## Common pitfalls

- Missing or unreachable base case → `RecursionError` at runtime (maximum depth exceeded).
- Recursive call that doesn't progress toward the base case (forgetting `x + 1` or
  `NumberElements - 1`).
- Aggregating on the wrong side (adding before the call when the aggregation is meant to
  happen on the way back — trace to check which the pseudocode intends).
- Extra prints in a fill-blanks answer — the "nothing superfluous" point is real.
- Deep recursion on large arrays: fine at exam scale (20–100 elements), but know that
  Python's default recursion limit (~1000) exists.

## Checkpoint

- [ ] I can trace a recursion in a table, down and up, without guessing.
- [ ] I can rewrite a simple recursion as a loop and a loop as a recursion.
- [ ] I can fill recursive pseudocode gaps: base case, progress, aggregation.
- [ ] I can write recursive tree traversals in both array and object forms.
