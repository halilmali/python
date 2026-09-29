# Module 8 — Stacks and queues (array-based ADTs)

**Exam weight: 20–29 marks whenever they appear — and some ADT question appears in
virtually every paper.** These are the highest-density marks in Paper 4: a fixed set of
operations (declare / push-enqueue / pop-dequeue / full-empty checks / pointer updates)
implemented over a global array, usually with part of the algorithm given as pseudocode.

## 1. The universal ADT skeleton

Every stack or queue question has the same five components. Learn them as a set:

1. **Declare** the array (fixed size, often initialised to −1 or 0 or empty string) and the
   pointer(s) as globals.
2. **Insert operation** (`Push`/`Enqueue`) — check full, store, update pointer, return
   TRUE/FALSE (or 1/−1).
3. **Remove operation** (`Pop`/`Dequeue`) — check empty, return the sentinel or the value,
   update pointer.
4. **Main program** that drives it — often with a deliberate overflow/underflow test.
5. **Screenshot evidence** with the paper's exact test data.

The sentinel values (−1, −999, `"Empty"`, `"FALSE"` string) are specified per paper — use
*exactly* what the paper says, because the main program's output message is marked against
it. Note N25/43's trap: `Dequeue()` returns the **string** `"False"`, not a Boolean.

## 2. Stack (LIFO) — the canonical implementation

June 2022 P42 gave us the master template (Module 2 worked it in full). Here is the
variant from **November 2025 Paper 41 Q1 [20 marks]**, where the pointer is the index of
the *last* element, initialised to −1, the stack holds 30 integers, and parts (d)–(e) add a
random-fill loop and a "pop everything, report min and max" function:

```python
Stack = [None for _ in range(30)]     # global; papers say "initialised to null"
TopOfStack = -1                        # global integer

def Push(NewValue):
    global TopOfStack
    if TopOfStack == 29:               # full
        return False
    TopOfStack += 1
    Stack[TopOfStack] = NewValue
    return True

def Pop():
    global TopOfStack
    if TopOfStack == -1:               # empty
        return -999                    # sentinel defined by the paper
    value = Stack[TopOfStack]
    TopOfStack -= 1
    return value

def FindValues():
    largest = -1
    smallest = 1001
    while TopOfStack != -1:
        value = Pop()
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    print("Largest:", largest)
    print("Smallest:", smallest)

# main: 40 random integers 0-1000 pushed until full ("Stack full")
import random
count = 0
while count < 40:
    if Push(random.randint(0, 1000)) is False:
        print("Stack full")
        break
    count += 1
FindValues()
```

Full runnable version: `solutions/m08_stack_n25.py`.

**Mark scheme shape for Push (4 marks):** full check returning FALSE / pointer increment /
store at the new top / return TRUE. For Pop: empty check with sentinel / read top /
pointer decrement / return. Note how J22/42's variant (pointer = next free space, initial 0)
flips the increments — *always re-derive from the paper's stated pointer semantics*.

## 3. Linear queue (FIFO)

Head/tail pointers. **June 2026 Paper 41 Q1 [26 marks]** is the clean specimen: 10-element
queue, pointers initialised to −1, `Enqueue()` (7 marks) with full check, `Dequeue()`
returning −1 when empty, then the main program attempts **11** inputs to force the overflow
message and dequeues four.

```python
Queue = [0] * 10
HeadPointer = -1
TailPointer = -1

def Enqueue(DataToInsert):
    global HeadPointer, TailPointer
    if TailPointer == 9:               # variant-dependent: some papers use a count
        return False
    if HeadPointer == -1:
        HeadPointer = 0
    TailPointer += 1
    Queue[TailPointer] = DataToInsert
    return True

def Dequeue():
    global HeadPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:
        return -1
    value = Queue[HeadPointer]
    HeadPointer += 1
    return value
```

Pointer conventions differ per paper (head at first item vs head before it; tail after last
vs at last) — the question *always* states them, and the mark scheme follows the statement.
Re-derive, don't recite. Full solution: `solutions/m08_queue_j26.py`.

Other linear-queue appearances: J24/41 Q3 (strings + check digit), J25/43 Q1 (fill from
file, dequeue-all with running total), N22/42 Q3 (enqueue 1–20 + recursive rewrite of
output), N25/43 Q2 (run-length compression — must consume via `Dequeue()`).

## 4. Circular queue (wrap-around)

**June 2025 Paper 41 Q1 [20 marks]**: 20-element queue of integers initialised to −1,
`HeadPointer`, `TailPointer`, `NumberItems`; the mark-earning twist is modular arithmetic:

```python
def Enqueue(NewItem):
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 20:
        return False
    TailPointer = (TailPointer + 1) % 20      # wrap-around
    Queue[TailPointer] = NewItem
    NumberItems += 1
    return True

def Dequeue():
    global HeadPointer, NumberItems
    if NumberItems == 0:
        return -1
    value = Queue[HeadPointer]
    HeadPointer = (HeadPointer + 1) % 20
    NumberItems -= 1
    return value
```

Full solution: `solutions/m08_circular_queue.py`. Earlier circular-queue questions:
J22/41 Q3 (Enqueue pseudocode with 5 blanks to complete, BYREF parameters) and J23/42 Q2
(circular queue of **records** with empty-record initialisation: `ID = ""`, quantity −1).

## 5. Two stacks, side by side (June 2023 P41 Q3 / Nov 2023 P42 Q1)

Same skeleton twice, with a routing condition. N23/42: read 100 letters from
`StackData.txt`; vowels push to `StackVowel`, consonants to `StackConsonant`; pop functions
return `"No data"` when empty; main pops five letters of the user's chosen kind and outputs
them on one line. J23/41 pushes animal names and colours to two stacks, then pops one of
each per output ("black horse"), with push-back rules when one stack empties.

```python
def PushData(letter):
    global VowelTop, ConsonantTop
    if letter in "aeiou":
        if VowelTop == 99:
            print("Vowel stack full")
        else:
            VowelTop += 1
            StackVowel[VowelTop] = letter
    else:
        if ConsonantTop == 99:
            print("Consonant stack full")
        else:
            ConsonantTop += 1
            StackConsonant[ConsonantTop] = letter
```

Full solution: `solutions/m08_two_stacks.py`.

## 6. Stack that evaluates (June 2025 P42 Q1(e))

**Reference: June 2025 Paper 42 Q1(e) [7 marks]** — `StackData.txt` holds an alternating
pattern of numbers and operators (`+ - * / ^`); `Calculate()` pops the first value to
**initialise the total** (the paper guarantees it is a number), then repeatedly pops an
operator followed by the number to apply, until the stack is empty. `^` is Python's `**`.
The paper works a full example in its text — follow it, and note that the pop order is
number → (operator, number) pairs. This is the ADT question at its most algorithmic — do it
after Modules 1 and 8; model: `solutions/m08_stack_calculator.py`.

## 7. Queue as a record (Nov 2024 P42 Q2)

**Reference: November 2024 Paper 42 Q2 [29 marks]** — the queue lives *inside* a record
(array + head + tail together), `Enqueue()` is given as incomplete pseudocode with three
blanks and explicit BYREF/BYVAL, and `Dequeue()` is deliberately **non-destructive** (reads
the value without advancing the head). In Python, wrap the three fields in a class:

```python
class TheQueue:
    def __init__(self):
        self.QueueArray = [-1] * 100     # integer
        self.HeadPointer = -1            # integer
        self.TailPointer = 0             # integer
```

and pass the queue object into the functions (Python objects are BYREF — the pseudocode's
`BYREF AQueue` maps to ordinary parameter passing). Model:
`solutions/m08_queue_record.py`.

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2022 P42 Q1 | Stack, pointer = next free space, 11-push overflow test | 25 |
| Jun 2023 P41 Q3 | Two stacks from files + push-back output rules | 25 |
| Nov 2023 P42 Q1 | Two stacks (vowels/consonants) from file | 27 |
| Jun 2025 P41 Q1 | Circular queue, random fill, success/unsuccessful loop | 20 |
| Jun 2025 P42 Q1 | Stack calculator from file | 27 |
| Jun 2026 P41 Q1 | Linear queue, 11-input overflow, dequeue four | 26 |
| Nov 2025 P41 Q1 | Stack (top = last index), random fill, min/max | 20 |
| Nov 2024 P42 Q2 | Queue in a record, blanks, non-destructive Dequeue | 29 |
| Jun 2023 P42 Q2 | Circular queue of records | 28 |

## Common pitfalls

- Using a memorised pointer convention when the paper states a different one (this is the
  #1 cause of lost ADT marks).
- Sentinel mismatch: returning `False` where the paper says `−1`, or the string `"Empty"`
  where the main program prints a message built from the return value.
- Forgetting `global` on the pointers (Module 2) — the store works, the pointer doesn't.
- Not running the deliberate overflow/underflow test the paper prints, so the screenshot
  can't earn its mark.

## Checkpoint

- [ ] I derive Push/Pop/Enqueue/Dequeue from the paper's stated pointer semantics, not memory.
- [ ] I use the paper's exact sentinel values and messages.
- [ ] I can implement wrap-around with `%`.
- [ ] I always run the printed overflow/invalid test and screenshot it.
