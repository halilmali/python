# Module 2 — Procedures, functions, parameters and globals

**Exam weight: every paper, every question.** Paper 4 constantly asks for "a procedure to
output...", "a function that returns...", then "amend the main program to call it". You
must be fluent in the procedure/function split, parameter passing, and Python's `global`.

## 1. Procedures vs functions

- **Procedure** = does something (output, store, update). No return value.
  Pseudocode `PROCEDURE OutputHighScores()` → Python `def output_high_scores():`
- **Function** = computes and **returns**. Pseudocode `FUNCTION ... RETURNS BOOLEAN` →
  `def ...(): ... return True`.

Mark scheme language to internalise: *"returns a value in all instances"*. Every branch of
your function must `return`. A full check that returns `False` in one branch and nothing in
the other loses the mark even if the logic is right.

## 2. Parameters

```python
# pseudocode: PROCEDURE PrintArray(DataArray : ARRAY OF INTEGER)
def print_array(data_array):        # arrays/lists pass by reference — mutations stick
    for value in data_array:
        print(value, end=" ")
    print()
```

- Python passes **lists/objects by reference**: the callee can modify the caller's array.
  This matches pseudocode `BYREF` and is exactly what ADT implementations rely on.
- Scalars (`int`, `float`, `str`, `bool`) behave like `BYVAL`: rebinding the parameter
  inside the function does not affect the caller. That is fine — mark schemes know it.
- Where a paper explicitly says a parameter is `BYREF` for a *scalar* (rare, e.g. pointer
  updates), return the new value instead, or use `global`. The mark scheme accepts the
  return-based approach.

## 3. Globals — the `global` keyword

Paper 4 loves **global data structures**: the paper says "the array is used globally" and
then asks for procedures that mutate it. In Python, *reading* a global needs nothing, but
*rebinding* (assigning) a global scalar inside a function needs the `global` declaration:

```python
StackData = [0] * 10        # global array
StackPointer = 0            # global integer

def push(value):
    global StackPointer     # required: we assign to it below
    if StackPointer == 10:
        return False
    StackData[StackPointer] = value   # mutating the list needs no declaration
    StackPointer += 1
    return True
```

The mark schemes' own Python models do exactly this (`global StackData`,
`global QueueHead`, `global NumberItems`). Forgetting `global` gives
`UnboundLocalError` at runtime — a bug that costs you your screenshot mark if untested.

**Decision rule:** if the function assigns (`=`) to a module-level *name*, declare it
`global` at the top of the function. Mutating a list in place (`lst[i] = ...`,
`lst.append(...)`) needs no declaration.

## 4. Worked example — stack with global structures (June 2022)

**Reference: June 2022 Paper 42 Q1 [25 marks]** —
`9618 Past Papers\9618 Computer Science June 2022 Question paper 42.pdf`

Task in brief: a stack of up to 10 integers stored in a **global** 1D array with a global
pointer initialised to 0; declare the structures; output the stack and pointer; write
`Push()` (returns FALSE when full, else stores, updates pointer, returns TRUE); test by
attempting 11 user-entered numbers (deliberate overflow); write `Pop()` (returns −1 when
empty, else returns top and updates pointer); pop two and re-output.

Full model solution: `solutions/m02_stack_j22.py`. The part worth studying here is the
*modular skeleton* — how the question's parts become procedures and how the main program
strings them together:

```python
StackData = [0] * 10        # global array of integers
StackPointer = 0            # global integer, next free space

def output_stack():
    print("Stack contents:")
    for i in range(9, -1, -1):
        print(StackData[i])
    print("StackPointer =", StackPointer)

def push(value):
    global StackPointer
    if StackPointer == 10:
        return False
    StackData[StackPointer] = value
    StackPointer += 1
    return True

def pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    StackPointer -= 1
    return StackData[StackPointer]

# main program
for _ in range(11):                      # 11 pushes into 10 slots = overflow test
    number = int(input("Enter a number: "))
    if push(number):
        print("Added to stack")
    else:
        print("Stack is full")
output_stack()
```

**Mark scheme shape (1(c), 6 marks):** header returning BOOLEAN / full check returns FALSE /
store value / increment pointer / return TRUE. Note each of those is a mark — and note the
11th input must produce the "full" message in your screenshot, because that *is* the test.

## 5. Worked example — functions returning objects (June 2022)

**Reference: June 2022 Paper 41 Q2(f) [8 marks]** — a `Defend()` function that takes a
`Balloon` object as a parameter, reads an opposing strength, calls `ChangeHealth()` with
the negative of the strength, outputs messages, and **returns the amended object**.

Objects pass by reference, and returning them is natural in Python:

```python
def defend(balloon):
    strength = int(input("Enter opponent strength: "))
    balloon.change_health(-strength)
    print("Defence successful" if balloon.get_health() > 0 else "Balloon destroyed")
    return balloon
```

This "object in, mutate, object out" pattern recurs (J26/41 `AddTrain()`, N25/41
`InsertData()` taking a Record object). Module 6 builds the class side.

## Practice set

| Reference | Task | Marks | Skills |
|---|---|---|---|
| Jun 2022 P42 Q1 | Full stack question (declare/output/Push/test/Pop) | 25 | globals, modular, ADT |
| Nov 2022 P41 Q1 | File read + linear search + bubble sort, all as subprograms | 23 | modular skeleton |
| Jun 2024 P41 Q1 | Initialise/BinarySearch/sort as functions with array parameters | 27 | parameter passing |
| Nov 2024 P42 Q2 | Queue encapsulated in a record; explicit BYREF/BYVAL in Enqueue blanks | 29 | record + parameters |
| Jun 2025 P42 Q1 | Stack calculator: Push/Pop/Calculate as functions over a global stack | 27 | globals, modular |

## Common pitfalls

- Missing `global` on a rebound scalar → `UnboundLocalError` mid-exam.
- A function with a branch that doesn't return → "returns in all instances" mark lost.
- Doing the OUTPUT inside a *function* that the paper says RETURNS (or vice versa) — read
  whether the part says procedure or function; the header mark follows the paper's wording.
- Mutating a caller's list and *also* forgetting the paper asked you to return it.

## Checkpoint

- [ ] I can write a function that returns a value on every branch.
- [ ] I know when `global` is needed and when it isn't.
- [ ] I can explain why lists pass by reference and ints don't.
- [ ] I built the June 2022 stack and tested it with the printed 11-input overflow data.
