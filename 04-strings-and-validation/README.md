# Module 4 — String processing and input validation

**Exam weight: 10–20 marks most papers.** Two recurring families: (a) string algorithms
where builtins are banned or limited, (b) validation loops that repeat until input is
acceptable. Both are mark-scheme-formulaic once you've seen them.

## 1. The string toolkit vs the bans

| Task | Allowed default | When banned |
|---|---|---|
| Length | `len(s)` | count with a loop |
| Slice / MID | `s[start-1:start-1+n]` | index char by char |
| Compare | `<`, `>`, `==` | compare `ord()` char by char |
| Case | `s.lower()`, `s.upper()` | `ord()` ± 32 arithmetic |
| Split | `s.split(",")` | scan for the separator |

**Read the ban carefully.** J26/42 Q1(b) says find the longest/shortest string "without
using inbuilt functions", but *permits* `LENGTH` — so `len()` is fine and manual char loops
are pointless there. N24/41 Q1(c) bans builtin comparison outright — that's when you write:

```python
# return 1 if a sorts before b, else 2 — char-by-char, no builtin comparison
def compare_strings(a, b):
    shortest = len(a) if len(a) < len(b) else len(b)
    for i in range(shortest):
        if ord(a[i]) < ord(b[i]):
            return 1
        if ord(a[i]) > ord(b[i]):
            return 2
    if len(a) <= len(b):
        return 1
    return 2
```

**Mark scheme shape (4 marks here):** loop over shared positions / both `<` and `>` returns
/ tie-break on length / correct return convention. Every branch returns — always.

## 2. Worked example — MID-based sort key (June 2023 P42 Q1)

**Reference: June 2023 Paper 42 Q1 [14 marks]** — global array of ten animal names; the
paper's `SortDescending()` pseudocode compares only the **first character**
(`MID(name, 1, 1)` in their convention) in a bubble sort, with four blanks to complete;
output one name per line.

The transferable idea: *the sort key can be any expression* — first character, length,
lowercase form. Python translation of the key comparison:

```python
Animals = ["ant", "walrus", "cat", "ibex", "dog", "yak", "eel", "goat", "fox", "bat"]

def sort_descending():
    array_length = len(Animals)
    for x in range(array_length - 1):
        for y in range(array_length - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:     # first char only
                Animals[y], Animals[y + 1] = Animals[y + 1], Animals[y]
```

Watch the direction: "descending" flips the comparison. Half the marks in sort questions
are the direction and the bounds.

## 3. Worked example — longest/shortest without builtins (June 2026 P42 Q1)

**Reference: June 2026 Paper 42 Q1 [18 marks]** — nine given strings; find the longest and
shortest without inbuilt functions (length allowed); then an insertion sort into
alphabetical order that "must work for any length" without inbuilt sorting.

```python
Strings = ["avatar", "orc", "goblin", "elf", "troll", "wraith", "gnome", "hud", "sprite"]

longest = Strings[0]
shortest = Strings[0]
for s in Strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s
print("Longest:", longest)
print("Shortest:", shortest)

def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

Full runnable version with the paper's flow: `solutions/m04_strings_j26.py`.

## 4. Worked example — check digit (June 2024 P41 Q3(d))

**Reference: June 2024 Paper 41 Q3(d)(i) [6 marks]** — validate an 8-character string of
digits with a check digit: alternate positions weighted ×1 and ×3 (starting weight 1 at the
first character), sum the products, take `total DIV 10`, then `total MOD 10`; if the check
value is 10 the check digit is `'X'`.

Weighted-sum algorithms are pure DIV/MOD loops — slow down and implement exactly:

```python
def validate_check_digit(code):
    total = 0
    weight = 1
    for i in range(7):                 # first 7 characters, weight alternates 1,3,1,3...
        total += int(code[i]) * weight
        weight = 3 if weight == 1 else 1
    check = (total // 10) % 10         # then DIV 10, then MOD 10 — per the spec
    if check == 10:
        check = 0                      # or 'X' — follow the printed rule exactly
    return check == int(code[7])
```

(Recreate the precise weighting from the paper when you attempt it — the pattern above is
the *shape*. The mark scheme awards: correct loop, both weights, the DIV/MOD chain, the
special case, the comparison.)

## 5. Validation loops — the reusable shapes

**Range validation (most common):**

```python
valid = False
while not valid:
    value = int(input("Enter difficulty (1-5): "))
    if 1 <= value <= 5:
        valid = True
    else:
        print("Invalid difficulty")
```

**Choice from a list** (J26/42 avatar hair colour; N22/42 move letter):

```python
hair = ""
while hair not in ["black", "brown", "blonde", "red"]:
    hair = input("Hair colour (black/brown/blonde/red): ").lower()
```

**Search-until-found** (N22/42 Q2(e) — name must exist in the loaded array):

```python
found = False
while not found:
    name = input("Character name: ")
    for i in range(len(characters)):
        if characters[i].get_name() == name:
            found = True
            index = i
    if not found:
        print("Unknown character")
```

**Case-insensitive match** (N21/41 Q2(e): "Silver" must match "silver"/"SILVER") — compare
`.lower()` on both sides. The mark scheme awards the case-folding explicitly.

## 6. Worked example — run-length compression (Nov 2025 P43 Q2(e))

**Reference: November 2025 Paper 43 Q2(e) [6 marks]** — a queue holds the characters of a
binary string read from a file; repeatedly `Dequeue()` and produce a run-length string, e.g.
`1100011` → each run described by count then digit (`2`×1, `3`×0, `2`×1 → `2132` in the
paper's count-then-value order — check the paper's own example). No run longer than 9.

The skill: consume a stream via the ADT (you *must* use `Dequeue()` — that's a mark), track
the current run, and build the output string with concatenation:

```python
def compress():
    global NewString
    NewString = ""
    current = dequeue()
    count = 1
    while current is not None:
        nxt = dequeue()
        if nxt == current and count < 9:
            count += 1
        else:
            NewString += str(count) + current
            current = nxt
            count = 1
```

Full version with the queue: `solutions/m08_run_length_queue.py` (Module 8).

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Nov 2023 P41 Q1 | Translate vowel counter (MID/LENGTH), then rewrite recursively | 16 |
| Jun 2023 P42 Q1 | Sort ten strings by first character, 4 blanks | 14 |
| Nov 2024 P41 Q1 | Read 45 strings; char-by-char compare; bubble sort | 22 |
| Jun 2026 P42 Q1 | Longest/shortest + insertion sort, no builtins | 18 |
| Jun 2026 P43 Q1 | Lowercase count without builtin count; bubble sort by length with early exit | 18 |
| Jun 2024 P41 Q3 | Linear queue + check-digit validation | 17 |
| Nov 2025 P43 Q2 | Queue + run-length compression from file | 24 |

## Common pitfalls

- Using a banned builtin — zero for those mark points, however elegant.
- Off-by-one on `MID`: pseudocode positions are 1-based, Python 0-based; state your
  assumption in a comment.
- Validation loop that accepts the bad value because the `valid = True` line is outside the
  `if` — test with the paper's invalid input before screenshotting.
- Case-sensitive comparison where the paper demands case-insensitive (it always names the
  requirement explicitly — circle it).

## Checkpoint

- [ ] I can implement compare-by-`ord()` and length-by-loop when builtins are banned.
- [ ] I know a sort key can be `s[0]`, `len(s)`, `s.lower()` — whatever the paper says.
- [ ] I can write range/list/search validation loops from memory.
- [ ] I implement weighted check-digit sums mechanically, following the spec line by line.
