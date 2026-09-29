# Module 9 — Linked lists, binary trees, hash tables

**Exam weight: 20–30 marks whenever they appear.** These are the "hard half" of Paper 4's
ADT questions — pointer manipulation over arrays or objects. Every variant has been asked
between 2021 and 2026; the mark schemes break each one into small, learnable steps.

## 1. Linked list in a 1D/2D array (with pointers)

Two array layouts appear:

- **2D array with an empty-list chain** (N24/41 Q3, J26/42 Q3): columns
  `data | next-pointer`, plus `FirstNode` (start of the real list) and `FirstEmpty` (start
  of the free list). Empty nodes hold −1.
- **Array of records** (J21/41 Q1): `NodeData`, `NextNode` fields, `StartPointer`,
  `EmptyList` pointers.

The canonical insertion at the **front** (N24/41 Q3(b), 6 marks):

```python
def InsertData():
    global FirstNode, FirstEmpty
    for _ in range(5):
        value = int(input("Enter a positive integer: "))
        if FirstEmpty == -1:
            print("List is full")
        else:
            this_node = FirstEmpty                    # take node from the free list
            FirstEmpty = LinkedList[this_node][1]
            LinkedList[this_node][0] = value          # store data
            LinkedList[this_node][1] = FirstNode      # point at old first node
            FirstNode = this_node                     # new head
```

**Removal** (N24/41 Q3(d), 5 marks) needs a *previous* pointer trail:

```python
def RemoveData(ValueToRemove):
    global FirstNode, FirstEmpty
    current = FirstNode
    previous = -1
    while current != -1 and LinkedList[current][0] != ValueToRemove:
        previous = current
        current = LinkedList[current][1]
    if current == -1:
        print("Value not found")
    else:
        if previous == -1:                        # removing the head
            FirstNode = LinkedList[current][1]
        else:
            LinkedList[previous][1] = LinkedList[current][1]   # splice out
        LinkedList[current][0] = -1               # return node to the free list
        LinkedList[current][1] = FirstEmpty
        FirstEmpty = current
```

**Mark scheme shape (insert-at-front):** input/loop / full check / take node from empty
list / advance `FirstEmpty` / store value / link to previous head / update `FirstNode`.
**J26/42 Q3(c)** raises the difficulty: insert at the **end** of the data list while
maintaining the separate empty-list chain (8 marks) — the same two chains, plus a traversal
to the last node first.

## 2. Linked list with object references (June 2025 P43 Q3)

**Reference: June 2025 Paper 43 Q3 [29 marks]** — class `Node` (TheData, NextNode), class
`LinkedList` (HeadNode); `InsertNode()` inserts at the head; `RemoveNode()` searches for a
value and unlinks it (6 marks, returns TRUE/FALSE); `Traverse()` builds a string.

Object references replace array indices; `None` replaces −1:

```python
class Node:
    # self.__TheData  : INTEGER
    # self.__NextNode : Node
    def __init__(self, data):
        self.__TheData = data
        self.__NextNode = None
    def GetNext(self):
        return self.__NextNode
    def SetNext(self, node):
        self.__NextNode = node
    def GetData(self):
        return self.__TheData

class LinkedList:
    # self.__HeadNode : Node
    def __init__(self):
        self.__HeadNode = None

    def InsertNode(self, new_node):
        new_node.SetNext(self.__HeadNode)
        self.__HeadNode = new_node

    def RemoveNode(self, data):
        current = self.__HeadNode
        previous = None
        while current is not None and current.GetData() != data:
            previous = current
            current = current.GetNext()
        if current is None:
            return False
        if previous is None:
            self.__HeadNode = current.GetNext()
        else:
            previous.SetNext(current.GetNext())
        return True
```

Full solution with traversal and tests: `solutions/m09_linked_list_oop.py`.

## 3. Binary tree in a 2D array (the classic)

Layout (identical in N21/41, N22/41, J26/43, N25/42):
`ArrayNodes[node][0] = left pointer, [1] = data, [2] = right pointer`; `RootPointer = −1`,
`FreeNode = 0`; −1 = null.

**Insert (N25/42 Q3(b), 7 marks / J26/43 Q3(b), 7 marks):**

```python
def AddNode(NewValue):
    global RootPointer, FreeNode
    if FreeNode > 49:                        # tree capacity 50
        print("The tree is full")
        return
    ArrayNodes[FreeNode][0] = -1             # new node: no children yet
    ArrayNodes[FreeNode][1] = NewValue
    ArrayNodes[FreeNode][2] = -1
    if RootPointer == -1:
        RootPointer = FreeNode               # first node becomes the root
    else:
        current = RootPointer
        placed = False
        while not placed:
            if NewValue < ArrayNodes[current][1]:
                if ArrayNodes[current][0] == -1:
                    ArrayNodes[current][0] = FreeNode
                    placed = True
                else:
                    current = ArrayNodes[current][0]
            else:
                if ArrayNodes[current][2] == -1:
                    ArrayNodes[current][2] = FreeNode
                    placed = True
                else:
                    current = ArrayNodes[current][2]
    FreeNode += 1
```

**Recursive in-order traversal (J26/43 Q3(e), 7 marks; N21/41 Q3(e), 7 marks):**

```python
def InOrder(index):
    if ArrayNodes[index][0] != -1:
        InOrder(ArrayNodes[index][0])
    print(ArrayNodes[index][1])
    if ArrayNodes[index][2] != -1:
        InOrder(ArrayNodes[index][2])
# call: InOrder(RootPointer)
```

**Recursive search** (N22/41 Q3(c), given as incomplete pseudocode with four blanks —
translate to Python: base case index −1 → FALSE; compare data; recurse left or right).

Variants on this layout: N21/41 Q3 (AddNode pseudocode with 6 blanks, then in-order),
N25/42 Q3(c)(d) (fill the tree from a 50-line file, then write the array to `Tree.txt`).

## 4. Binary tree with object references (J24/42 Q2, J25/41 Q3)

**Reference: June 2025 Paper 41 Q3 [30 marks]** — `Node` holds `LeftNode`/`RightNode` of
type Node; a `Tree` class holds `FirstNode`; `Insert()` walks references; then a
**recursive in-order** `OutputInOrder()` (5 marks).

```python
class Node:
    # self.__LeftNode  : Node
    # self.__Data      : INTEGER
    # self.__RightNode : Node
    def __init__(self, data):
        self.__LeftNode = None
        self.__Data = data
        self.__RightNode = None

class Tree:
    # self.__FirstNode : Node
    def __init__(self):
        self.__FirstNode = None

    def Insert(self, new_node):
        if self.__FirstNode is None:
            self.__FirstNode = new_node
            return
        current = self.__FirstNode
        placed = False
        while not placed:
            if new_node.GetData() < current.GetData():
                if current.GetLeft() is None:
                    current.SetLeft(new_node)
                    placed = True
                else:
                    current = current.GetLeft()
            else:
                if current.GetRight() is None:
                    current.SetRight(new_node)
                    placed = True
                else:
                    current = current.GetRight()

    def OutputInOrder(self, node):
        if node is None:
            return
        self.OutputInOrder(node.GetLeft())
        print(node.GetData())
        self.OutputInOrder(node.GetRight())
```

Full solution: `solutions/m09_binary_tree_oop.py`. J24/42 Q2 is the same idea with
`Node` objects stored *inside an array* within a `TreeClass` (pointer = index) — read its
table carefully.

## 5. Hash table (J25/42 Q2, N25/41 Q3)

**Reference: November 2025 Paper 41 Q3 [25 marks]** — 100×10 2D array; `Hash(Key)` returns
`Key MOD 100`; collisions live in the *next free slot of the same row*; `Record` class with
**public** Key/Data attributes; `ReadData()` reads `HashTableData.txt` (`key,string`),
splits, and inserts; `GetRecord()` hashes and searches the row, returning the data or
`"Not found"`.

```python
class Record:
    # self.Key  : INTEGER   (public, per the paper)
    # self.Data : STRING
    def __init__(self, key, data):
        self.Key = key
        self.Data = data

def Hash(key):
    return key % 100

def InsertData(record):
    address = Hash(record.Key)
    slot = 0
    while slot < 10 and HashTable[address][slot] is not None:
        slot += 1
    if slot < 10:
        HashTable[address][slot] = record

def GetRecord(key):
    address = Hash(key)
    for slot in range(10):
        entry = HashTable[address][slot]
        if entry is not None and entry.Key == key:
            return entry.Data
    return "Not found"
```

J25/42 Q2's variant: 200-slot 1D table + a separate 100-slot `Spare` array for overflow,
with a record type `(Key, Item1, Item2)` and initialisation to −1 fields. Model:
`solutions/m09_hash_table.py`. The test data (N25: keys 528, 1128, 1828, 1062, 39) is
chosen to force collisions — your screenshot must show the collided keys landing in the
same row.

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2021 P41 Q1 | Linked list as array of records, add + traverse | 24 |
| Nov 2021 P41 Q3 | 2D-array tree: AddNode blanks + recursive in-order | 28 |
| Nov 2022 P41 Q3 | 2D-array tree: hard-coded data, recursive search + post-order | 21 |
| Nov 2024 P41 Q3 | 2D-array linked list: insert front, remove | 19 |
| Jun 2026 P42 Q3 | 2D-array linked list with empty-list chain, add at end | 27 |
| Jun 2026 P43 Q3 | 2D-array tree: AddNode + recursive in-order | 25 |
| Jun 2025 P43 Q3 | Object-reference linked list, remove is hard | 29 |
| Jun 2025 P41 Q3 | Object-reference tree + recursive in-order | 30 |
| Jun 2024 P42 Q2 | Tree as array of Node objects, two classes | 30 |
| Jun 2025 P42 Q2 | Hash table + Spare overflow array | 22 |
| Nov 2025 P41 Q3 | Hash table 100×10 + Record class + file | 25 |

## Common pitfalls

- Drawing the array on paper first is not optional — pointer bugs are 10× harder to find in
  your head. Trace one insert by hand, then code it.
- Forgetting to update `FreeNode` (or the free-list head) after taking/returning a node.
- In removal: not handling the head-of-list special case.
- Off-by-one on capacity checks (`> 49` vs `> 50` for a 50-node tree).
- In hash tables: searching the whole table instead of just the hashed row/bucket.

## Checkpoint

- [ ] I can implement array-based list/tree insert with both chains updated correctly.
- [ ] I can write removal with the previous-pointer trail, including head special case.
- [ ] I can write recursive in-order traversal in both array-index and object-reference forms.
- [ ] I can implement MOD hashing with per-row collision storage.
