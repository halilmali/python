# 9618 Paper 4 — Master Question Bank (2021–2026)

Every Paper 4 question paper in the collection `C:\Users\mali\Desktop\cs\9626-topical-questions\`,
catalogued question by question. Question papers whose content is identical share one row
(the row names the variants). Use this bank to find practice questions for each skill.

**How to read a reference.** `J22/42 Q1(c)` means June 2022, Paper 42, Question 1 part (c).
The original PDFs are in `9626-topical-questions\9618 Past Papers\` (and `\2026\`).
Marks are shown in brackets. "→ M8" points to the course module that teaches the skill.

> Within every session, two of the three variants are usually clones. As of 2024 the
> pattern is stable: **41 = 43**, and **42 is the distinct paper**. Practising one of
> 41/43 plus 42 per session covers everything.

## Unique papers at a glance

| Paper | Q1 (topic, marks) | Q2 | Q3 | Distinct skills / data files |
|---|---|---|---|---|
| J21/41·42·43 | Unordered linked list in array of records (24) | Bubble sort from pseudocode with 5 blanks (20) | TreasureChest quiz OOP + file read (31) | records; fill-blanks; exception handling → M3 M6 M9; `TreasureChestData.txt` |
| J22/41·43 | High-score table, file read/write, sorted insert (29) | Balloon OOP, object as parameter/return (25) | Circular queue, Enqueue pseudocode with 5 blanks (21) | validation; file write → M4 M5 M6 M8; `HighScore.txt` → `NewHighScore.txt` |
| J22/42 | Stack of 10 ints, Push/Pop (25) | 2D array random fill, bubble sort, recursive binary search with 6 blanks (23) | Card game OOP + file read (27) | random; 2D output grid; recursion → M3 M8 M10 M11; `CardValues.txt` |
| J23/41·43 | Read 25 ints, linear search counts matches (18) | Vehicle/Helicopter inheritance + overriding (32) | Two parallel stacks from files (25) | local array; polymorphism; exception handling → M5 M6 M7 M8 M10; `Data.txt`, `AnimalData.txt`, `ColourData.txt` |
| J23/42 | Sort 10 strings by first char, 4 blanks (14) | Circular queue of records (28) | Employee/Manager inheritance + two files (33) | records; array attribute in class; parent call in override → M3 M6 M7 M8; `Employees.txt`, `HoursWeek1.txt` |
| N21/41·42 | Recursive trace + rewrite iteratively (17) | Picture OOP + file search, case-insensitive (30) | Binary tree in 2D array, AddNode blanks + recursive in-order (28) | recursion→iteration; case-insensitive match → M4 M9 M11; `Pictures.txt` |
| N22/41·43 | Read 100 ints, linear search count, bubble sort (23) | Card + Hand OOP composition (31) | Binary tree 2D array: recursive search blanks + post-order (21) | composition; two recursions → M3 M6 M7 M9 M11; `IntegerData.txt` |
| N22/42 | 2D job array, insertion sort (23) | Character OOP, file of 10 objects, movement (31) | Linear queue + iterative→recursive conversion (21) | insertion sort on 2D; WASD validation → M3 M4 M6 M8 M11; `Characters.txt` |
| N23/41·43 | Vowel counter: translate, then rewrite recursively (16) | Queue of string IDs + record frequency counts (29) | Character/BikeCharacter inheritance, clamped setters (30) | iterative→recursive; queue+records → M4 M8 M9 M11 |
| N23/42 | Two stacks (vowels/consonants) from file (27) | Divisor sum: translate iterative, complete recursive (17) | Character + DATE attribute, MagicCharacter override (31) | two stacks; date arithmetic; fill-blanks → M1 M5 M7 M8; `StackData.txt` |
| N24/41·43 | Read 45 strings, char-by-char compare, bubble sort (22) | Horse/Fence OOP, validated input, success % (34) | Linked list in 2D array: insert front, remove (19) | no builtin compare; dual free-list pointers → M3 M4 M6 M9; `Data.txt` |
| N24/42 | EventItem/Character scoring game (29) | Queue as record structure, Enqueue blanks, BYREF/BYVAL (29) | High-score 2D array, two-key bubble sort (17) | record containing array; two-key sort → M3 M6 M8; `HighScoreTable.txt` |
| J24/41·43 | 1–20 ints, bubble sort, iterative binary search (27) | Tree OOP + CSV file filter + exception handling (31) | Linear queue of strings + check-digit algorithm (17) | check digit (weighted sum, DIV) → M4 M5 M6 M8 M10; `Trees.txt` |
| J24/42 | Word game, three difficulty files (22) | Binary tree as array of Node objects, two classes (30) | Recursive insertion sort translate→iterative; recursive binary search (23) | OOP tree; recursion everywhere → M6 M9 M10 M11; `Easy.txt`, `Medium.txt`, `Hard.txt` |
| J25/41 | Circular queue of ints, random fill (20) | Read `TheData.txt`, split by colour, write six files (25) | Binary tree with object-reference nodes + recursive in-order (30) | file write×6; reference-based tree → M5 M6 M9 M11; `TheData.txt` → 6 outputs |
| J25/42 | Stack calculator from file (27) | Hash table + overflow (Spare) array (22) | Animal/Parrot/Wolf inheritance, overriding (26) | stack evaluation; hash table; super().__init__ → M5 M7 M8 M9; `StackData.txt`, `SecondStack.txt`, `HashData.txt` |
| J25/43 | Queue from file, dequeue-all total (26) | Insertion sort + binary search, no builtins (20) | Linked list OOP: insert, remove (hard), traverse (29) | object-reference list → M5 M8 M9 M10; `QueueData.txt` |
| J26/41 | Linear queue, overflow test (26) | Toy records: filter by difficulty, write matches (28) | Path class owning 100-object array (21) | record type; composition; file write → M3 M5 M6 M7 M8; `Toys.txt` → `SelectedToys.txt` |
| J26/42 | Longest/shortest string, insertion sort (18) | Avatar OOP + space-separated file + validated matching (30) | Linked list 2D array with separate empty-list chain (27) | no-builtin limits; free-list maintenance → M4 M6 M9; `AvatarFile.txt` |
| J26/43 | Count occurrences, bubble sort by length, early exit (18) | Character OOP + CSV file, two-criteria filter (29) | Binary tree 2D array, AddNode + recursive in-order (25) | efficient bubble; generic criteria matching → M4 M6 M9 M10; `Characters.txt` |
| N25/41 | Stack of 30, random fill, pop min/max (20) | Train/Station composition OOP (25) | Hash table 100×10 2D array + Record class (25) | public attributes; hash collisions in-row → M3 M6 M7 M9; `HashTableData.txt` |
| N25/42 | Bird OOP movement with validated inputs (28) | 20 unique random ints, bubble sort, recursive binary search (26) | Binary tree 2D array + write tree to new file (21) | unique randoms; file WRITE exception handling → M4 M5 M9 M10 M11; `TreeData.txt` → `Tree.txt` |
| N25/43 | Board/BoardObject 10×10 2D grid OOP (31) | Queue from file + run-length compression (24) | RecursiveCount (pass array-minus-first) + manual split, no builtins (20) | deepest composition; manual split → M4 M6 M7 M8 M11; `BinaryData.txt` |

## Skill → question index

Find practice questions for one skill fast. Marks in brackets.

### Arrays & records (M3)
- 1D array basics: J23/41 Q1 [18]; N22/41 Q1 [23]; J25/43 Q2 [20]
- 2D arrays: J22/42 Q2 [23]; N22/42 Q1 [23]; N24/42 Q3 [17]; N25/41 Q3 [25]; N25/43 Q1 [31]
- Parallel arrays: J22/41 Q1 [29]
- Records: J23/42 Q2 [28]; J26/41 Q2 [28]; N23/41 Q2 [29]; N24/42 Q2 [29]
- Array of objects: J22/42 Q3 [27]; N22/42 Q2 [31]; N25/41 Q2 [25]

### Strings & validation (M4)
- String algorithms without builtins: N24/41 Q1(c) [4]; J26/42 Q1 [18]; J26/43 Q1 [18]; N25/43 Q3(b) [10]
- Case-insensitive matching: N21/41 Q2(e) [7]
- Validation loops: J22/41 Q1 [29]; N22/42 Q2(e)(f) [12]; N25/42 Q1(c) [8]
- Check-digit algorithm: J24/41 Q3(d) [6]
- Run-length encoding: N25/43 Q2(e) [6]

### Files & exception handling (M5)
- Read into array: J23/41 Q1 [18]; N22/41 Q1 [23]; N24/41 Q1(a) [6]
- Read into objects: J21/41 Q3(c) [8→31]; N22/42 Q2(d) [7]; J24/41 Q2(b) [7]
- Unknown length + split + cast: J25/41 Q2 [25]; N25/41 Q3(e) [5]; J26/42 Q2(b) [7]
- Write a file: J22/41 Q1(f) [4]; J26/41 Q2(c) [8]; N25/42 Q3(d) [5]
- Write multiple files: J25/41 Q2 [25]

### OOP (M6, M7)
- Class + constructor + getters: J22/42 Q3(a)(b) [8]; J24/41 Q2(a) [7]; N25/42 Q1(a) [9]
- Objects as parameters/returns: J22/41 Q2(f) [8]; J26/41 Q3 [21]
- Composition (object owns objects): N22/41 Q2(b) [10]; J26/41 Q3 [21]; N25/41 Q2 [25]; N25/43 Q1 [31]
- Inheritance + overriding + super: J23/41 Q2 [32]; J23/42 Q3 [33]; N23/41 Q3 [30]; N23/42 Q3 [31]; J25/42 Q3 [26]
- Date attribute: N23/42 Q3(a)(v) [2]

### Stacks & queues (M8)
- Stack global array: J22/42 Q1 [25]; N23/42 Q1 [27]; N25/41 Q1 [20]; J25/42 Q1 [27]
- Two stacks: J23/41 Q3 [25]
- Linear queue: N22/42 Q3 [21]; J24/41 Q3 [17]; J26/41 Q1 [26]; J25/43 Q1 [26]; N25/43 Q2 [24]
- Circular queue: J22/41 Q3 [21]; J23/42 Q2 [28]; J25/41 Q1 [20]
- Queue as record: N24/42 Q2 [29]

### Linked lists, trees, hash tables (M9)
- Array-based linked list: J21/41 Q1 [24]; N24/41 Q3 [19]; J26/42 Q3 [27]
- Object-based linked list: J25/43 Q3 [29]
- 2D-array binary tree: N21/41 Q3 [28]; N22/41 Q3 [21]; J26/43 Q3 [25]; N25/42 Q3 [21]
- Object-based binary tree: J24/42 Q2 [30]; J25/41 Q3 [30]
- Hash table: J25/42 Q2 [22]; N25/41 Q3 [25]

### Searching & sorting (M10)
- Linear search: J21/41 Q2(b) [6]; J23/41 Q1(c) [7]; N22/41 Q1(c) [7]
- Binary search (iterative): J24/41 Q1(e) [6]
- Binary search (recursive): J22/42 Q2(c) [8]; J24/42 Q3(d) [6]; N25/42 Q2(e) [6]
- Bubble sort: J21/41 Q2(e) [4]; J22/42 Q2(b) [5]; N22/41 Q1(e) [4]; J26/43 Q1(f) [5]
- Insertion sort: N22/42 Q1(e) [5]; J25/43 Q2(e) [6]; J26/42 Q1(c) [5]
- Recursive insertion sort: J24/42 Q3(b)(c) [10]
- Custom keys / two-key sort: J23/42 Q1 [14] (first char); J26/43 Q1 [18] (length, early exit); N24/42 Q3(d) [4] (two keys); N24/41 Q1(c)(d) [7] (char-by-char)

### Recursion (M11)
- Trace + convert to iteration: N21/41 Q1 [17]
- Convert iteration → recursion: N22/42 Q3(d) [6]; N23/41 Q1(b) [6]
- Recursive search on tree: N22/41 Q3(c)(d) [12]
- Recursive traversal: J25/41 Q3(c) [6]; J26/43 Q3(e) [7]
- Recursive counting: N25/43 Q3(a) [9]

### Pseudocode translation & fill-in-the-blanks (M1, M11)
- Full translation: N23/41 Q1(a) [5]; N23/42 Q2(a) [5]; J24/42 Q3(b) [4]; J23/41 Q3(b) [8]
- Fill blanks: J21/41 Q2(e) [4]; J22/41 Q3(c) [6]; J22/42 Q2(c) [8]; N21/41 Q3(b) [8]; N22/41 Q3(c) [5]; N23/42 Q2(b) [7]; N24/42 Q2(c) [5]

## Frequency notes (what the exam rewards most)

Across 2021–2026 (counting unique papers, n≈23):

1. **ADT implementation from a spec** — appears in effectively every paper (~25–30 marks): stack, queue (linear/circular), linked list, binary tree, hash table.
2. **OOP with private attributes + constructor + getters** — every paper (~20–30 marks); inheritance appears roughly every other session.
3. **File read with exception handling** — most sessions (5–8 marks per appearance); file write appears periodically (J22/41, J25/41, J26/41, N25/42).
4. **Sorting + searching without builtins** — most sessions.
5. **Recursion** — in some form in roughly two-thirds of sessions (binary search, traversals, iterative↔recursive conversions).
6. **Pseudocode→code translation or fill-in-the-blanks** — nearly every paper.
7. Validation loops, formatted output, and screenshot evidence — constant background marks.
