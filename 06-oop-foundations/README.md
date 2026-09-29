# Module 6 — OOP foundations: classes, constructors, getters, setters

**Exam weight: ~20–30 marks in every paper.** Every Paper 4 has an OOP question. The core
subset — declare a class with private attributes, write the constructor, write getters,
instantiate from file data — appears in *every* session and is highly formulaic.

## 1. The canonical class skeleton

Every OOP question starts the same way. Learn this template until writing it takes 60
seconds:

```python
class Card:
    # self.__Number : INTEGER     <- attribute declarations as comments:
    # self.__Colour : STRING      <- the paper asks for these explicitly in Python
    def __init__(self, number, colour):
        self.__Number = number        # private: double underscore
        self.__Colour = colour

    def get_number(self):
        return self.__Number

    def get_colour(self):
        return self.__Colour
```

Why each line earns marks (from the mark schemes):

- **Class declaration** — "Class Card declaration (and end where appropriate)".
- **Attributes private with correct identifiers and data types** — the double underscore is
  the privacy mark; the *comments* supply the data types (Python has no declarations).
- **Constructor header** — "taking N parameters (Python N+1)": `self` counts as one.
- **Constructor assigns parameters to attributes.**
- **Get methods**: header with no parameter, returning the attribute; the second and
  further getters are usually bundled into one mark.

## 2. What the class diagram tells you

Paper 4 presents the class as a table: attributes on the left, methods on the right, with
one-line descriptions. Read it mechanically:

- `Number : INTEGER` → attribute with type (→ your `#` comment).
- `Constructor()` with "Takes two values as parameters and sets them" → `__init__(self, a, b)`.
- `GetNumber()` "Returns the number of the card" → trivial getter.
- Anything with `Set...` or "changes" → setter (may clamp/validate — see below).
- Inheritance questions add "inherits from X" text — Module 7.

## 3. Worked example — Card class (June 2022 P42 Q3)

**Reference: June 2022 Paper 42 Q3(a)(b) [8 marks]** —
`9618 Past Papers\9618 Computer Science June 2022 Question paper 42.pdf`

In brief: class `Card` with private attributes Number (integer) and Colour (string);
constructor taking both; get methods returning each. Then (part c, 7 marks) read 30 cards
from `CardValues.txt` into an array of Card objects — covered in Module 5.

```python
class Card:
    # self.__Number : INTEGER
    # self.__Colour : STRING
    def __init__(self, number, colour):
        self.__Number = number
        self.__Colour = colour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour
```

That is 8 marks for roughly 12 lines. This is why OOP is the best return-on-time in the
paper. Full solution including the file reading and the selection game:
`solutions/m06_card_game.py`.

## 4. Worked example — setters with clamping (Nov 2023 P41 Q3(a)(iii))

**Reference: November 2023 Paper 41 Q3(a)(iii) [4 marks]** — `SetXPosition()` and
`SetYPosition()` must only accept values in 0–10000; out-of-range values are clamped to the
nearest bound. Part (iv) then writes `Move(direction)` updating position by 10 using the
set methods.

```python
def SetXPosition(self, new_x):
    if new_x > 10000:
        self.__XPosition = 10000
    elif new_x < 0:
        self.__XPosition = 0
    else:
        self.__XPosition = new_x
```

The mark scheme awards the range check, both clamps, and the assignment. Then `Move()`
*must* go through the setters ("using the set methods" is stated — and marked): direct
attribute assignment would lose the point.

## 5. Instantiating and arrays of objects

```python
Player1 = Card(5, "red")                       # direct instantiation
AvailableAvatars = [None] * 30                 # declare the array, fill from file
AvailableAvatars[i] = Avatar(name, glasses, hair, age)
```

Read-from-file-into-objects is Module 5's pattern A/B combined with this. When the paper
says "declare an array of 100 Picture objects" — `[None] * 100` then fill by index; the
declaration mark is for the structure, not the contents.

## 6. Objects as parameters and return values

Recurring shape (J22/41 Q2(f), J26/41 Q3, N25/41 Q3(d)): a function takes an object,
mutates it via its methods, sometimes returns it:

```python
def AddTrain(self, new_train):
    if self.__NumberTrains == self.__NumberPlatforms:
        return False
    self.__Trains[self.__NumberTrains] = new_train
    self.__NumberTrains += 1
    return True
```

Note the private attribute access *inside* the class is fine; outside the class you must go
through getters — Python won't stop you from touching `obj.__X` from outside, but the
mark scheme does.

## 7. Worked example — full OOP + file + validation flow (June 2026 P42 Q2)

**Reference: June 2026 Paper 42 Q2 [30 marks]** — class `Avatar` (TheName, Glasses boolean,
Hair, Age), constructor, getters, `MeetCriteria()` matching two attribute values; read 30
**space-separated** records from `AvatarFile.txt` (e.g. name / glasses / hair / age) with
exception handling; validate user criteria (glasses yes/no; hair from a list); output
matching avatars.

This paper is the whole Module 6 in one question. Attempt it after Modules 5+6; the full
model is `solutions/m06_avatars.py`. Note the boolean field: `"True"` in the file must be
converted to Python `True` (`parts[1] == "True"`).

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2021 P41 Q3 | TreasureChest: class + file + quiz loop | 31 |
| Jun 2022 P41 Q2 | Balloon: object as parameter/return | 25 |
| Jun 2022 P42 Q3 | Card + file + selection game | 27 |
| Nov 2021 P41 Q2 | Picture + file search, case-insensitive | 30 |
| Nov 2022 P41 Q2 | Card + Hand (composition) | 31 |
| Nov 2022 P42 Q2 | Character + file + movement validation | 31 |
| Jun 2024 P41 Q2 | Tree + CSV file + filter criteria | 31 |
| Nov 2024 P41 Q2 | Horse + Fence, validated course input | 34 |
| Jun 2026 P42 Q2 | Avatar + space-separated file + matching | 30 |
| Nov 2025 P41 Q2 | Train/Station composition | 25 |

## Common pitfalls

- Forgetting the `# type` comments — the paper explicitly instructs them for Python and the
  "correct data types" mark lives there.
- Public attributes where private is demanded (or vice versa: N25/41 Q3(a) Record class
  explicitly wants public).
- Getters that print instead of return ("Returns the number..." — RETURN).
- Instantiating with the wrong argument order — match the constructor's parameter order to
  the file's field order.
- Accessing `self.__X` from *outside* the class instead of using a getter.

## Checkpoint

- [ ] I can write the canonical class skeleton (comments + `__init__` + getters) from memory.
- [ ] I know the mark points a bare class declaration is worth.
- [ ] I can build and fill an array of objects.
- [ ] I can write a clamping setter and a mutator that routes through setters.
