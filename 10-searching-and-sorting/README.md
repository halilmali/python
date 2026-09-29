# Module 10 — Searching and sorting (no builtins allowed)

**Exam weight: 10–20 marks in most papers.** When Paper 4 asks for a sort or search it
nearly always says "you must not use any built-in sorting functions" — the mark scheme
describes the manual algorithm, so `list.sort()` earns zero. Learn these four algorithms as
*translations of the syllabus pseudocode*, not as generic code.

## 1. Linear search — two return conventions

The syllabus uses both; the paper states which it wants:

**Found / not found (Boolean)** — J21/41 Q2(b), N21/41 Q2(e):

```python
def LinearSearch(DataArray, SearchValue):
    for index in range(len(DataArray)):
        if DataArray[index] == SearchValue:
            return True
    return False
```

**Count of matches** — J23/41 Q1(c) ("The number 7 is found 2 times."), N22/41 Q1(c):

```python
def LinearSearch(DataArray, SearchValue):
    count = 0
    for index in range(len(DataArray)):
        if DataArray[index] == SearchValue:
            count += 1
    return count
```

Return-in-all-branches matters here: the `return True` inside the loop plus the final
`return False` is the pattern the mark scheme calls "returns in all instances".

## 2. Binary search — iterative and recursive

Binary search requires **sorted data** (papers make you sort first — that's the point).

**Iterative** (June 2024 P41 Q1(e), 6 marks):

```python
def BinarySearch(DataArray, SearchValue):
    first = 0
    last = len(DataArray) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if DataArray[middle] == SearchValue:
            found = True
        elif DataArray[middle] > SearchValue:
            last = middle - 1
        else:
            first = middle + 1
    if found:
        return middle
    return -1
```

**Recursive** (N25/42 Q2(e) — the paper fixes the four-parameter signature; J24/42 Q3(d)
same):

```python
def RecursiveBinarySearch(DataArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper) // 2
        if DataArray[Mid] == SearchValue:
            return Mid
        elif DataArray[Mid] > SearchValue:
            return RecursiveBinarySearch(DataArray, Lower, Mid - 1, SearchValue)
        else:
            return RecursiveBinarySearch(DataArray, Mid + 1, Upper, SearchValue)
    return -1
```

Compare with J22/42 Q2(c): the paper gave this exact function as incomplete pseudocode with
six blanks (note that variant computes `Mid` as `(Lower + (Upper − 1)) DIV 2` — when the
paper provides pseudocode, translate *it*, don't substitute your own version). The mark
scheme awards: mid calculation / found return / both branch recursions / not-found return
/ correct bounds.

## 3. Bubble sort — from the syllabus pseudocode

Paper 4 prints bubble sort pseudocode and asks for a translation (J22/42 Q2(b)(i)) or a
completion of it (J21/41 Q2(e), four/five blanks). The syllabus shape, translated:

```python
def BubbleSort():
    for x in range(len(ArrayData)):
        for y in range(len(ArrayData) - 1):
            for z in range(len(ArrayData) - y - 1):
                if ArrayData[x][z] > ArrayData[x][z + 1]:
                    ArrayData[x][z], ArrayData[x][z + 1] = ArrayData[x][z + 1], ArrayData[x][z]
```

That is J22/42's three-loop row-sorting variant. The tuple swap on the last line is
**explicitly accepted** by the mark scheme ("Accept for MP5: ...").

**Early-exit efficiency variant** (J26/43 Q1(f), 5 marks — "stop as soon as the array is in
order"):

```python
def BubbleSortByLength():
    in_order = False
    while not in_order:
        in_order = True
        for i in range(len(DataArray) - 1):
            if len(DataArray[i]) > len(DataArray[i + 1]):
                DataArray[i], DataArray[i + 1] = DataArray[i + 1], DataArray[i]
                in_order = False
```

The `swapped`/`in_order` flag *is* the mark point. Other bubble variants:
N24/42 Q3(d) — two keys (level descending, then score descending, over parallel columns of
a 2D string array); N24/41 Q1(d) — sorting strings with the char-by-char compare from
Module 4; J23/42 Q1 — first-character key, descending.

## 4. Insertion sort — iterative and recursive

**Iterative** (N22/42 Q1(e) on a 2D array; J25/43 Q2(e); J26/42 Q1(c) on strings):

```python
def InsertionSort():
    for i in range(1, len(Numbers)):
        key = Numbers[i]
        j = i - 1
        while j >= 0 and Numbers[j] > key:
            Numbers[j + 1] = Numbers[j]
            j -= 1
        Numbers[j + 1] = key
```

**Recursive** (June 2024 P42 Q3(b)(i), 4 marks — the paper *provides* the recursive
pseudocode `RecursiveInsertion` to translate, then (c) asks for the same algorithm
iteratively, 4 marks):

```python
def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    RecursiveInsertion(IntegerArray, NumberElements - 1)
    last = IntegerArray[NumberElements - 1]
    pointer = NumberElements - 2
    while pointer >= 0 and IntegerArray[pointer] > last:
        IntegerArray[pointer + 1] = IntegerArray[pointer]
        pointer -= 1
    IntegerArray[pointer + 1] = last
    return IntegerArray
# call: RecursiveInsertion(Numbers, len(Numbers))
```

Translate the printed pseudocode line by line — the parameter names and the recursion
position are mark points.

## 5. Worked example — full sort+search pipeline (June 2024 P41 Q1)

**Reference: June 2024 Paper 41 Q1 [27 marks]** —
`9618 Past Papers\9618 Computer Science June 2024 Question paper 41.pdf`

In brief: read a count (validated 1–20), fill a global array of integers, `Initialise()`
procedure, bubble sort, then an iterative `BinarySearch()`; main program prints the array,
sorts, searches for a user value and outputs found/not-found with screenshots at each
stage.

This is the module's whole pipeline in one question. Full model:
`solutions/m10_sort_search_j24.py`. Mark scheme shape: validation loop / array fill /
bubble translate / binary search (header, mid, three branches, loop condition) /
main-program calls + messages.

## 6. Choosing the algorithm the paper wants

- Paper prints pseudocode → translate it exactly (names, bounds, direction).
- Paper says "efficient"/"stop when in order" → flagged bubble.
- Paper says nothing and offers a choice → bubble (safest, matches syllabus pseudocode).
- Paper sorts 2D/parallel data → move whole rows together (Module 3).
- Paper bans comparisons/length builtins → Module 4's char-by-char tools.

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2024 P41 Q1 | Count, fill, bubble, iterative binary search | 27 |
| Jun 2024 P42 Q3 | Recursive insertion translate → iterative; recursive binary search | 23 |
| Jun 2024 P42 Q3(d) | Recursive binary search from spec | 6 |
| Jun 2025 P43 Q2 | Insertion sort + binary search, no builtins | 20 |
| Jun 2026 P43 Q1 | Count + bubble by length with early exit | 18 |
| Nov 2024 P41 Q1 | Char-by-char compare + bubble sort of strings | 22 |
| Nov 2024 P42 Q3 | Two-key bubble sort on a 2D string array | 17 |
| Jun 2023 P42 Q1 | First-character descending bubble, 4 blanks | 14 |
| Nov 2022 P41 Q1 | File + linear search count + bubble | 23 |

## Common pitfalls

- `list.sort()`, `sorted()`, `max()`, `min()`, `in` where the paper bans builtins — zero
  for those mark points.
- Translation drift: changing the paper's loop bounds or comparison direction "to make it
  work" — mark it against their pseudocode, not against correctness vibes.
- Forgetting the not-found return (−1 / FALSE) — "returns in all instances".
- Binary search on unsorted data — sort first; papers always sequence it.
- Off-by-one at the edges (`last = len(...) - 1`, `first <= last`).

## Checkpoint

- [ ] I can write linear search in both return conventions.
- [ ] I can write iterative and recursive binary search from memory.
- [ ] I can translate bubble sort from printed pseudocode, including blanks and early exit.
- [ ] I can write insertion sort iteratively and translate the recursive variant.
