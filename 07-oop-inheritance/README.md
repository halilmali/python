# Module 7 — OOP advanced: composition, inheritance, overriding

**Exam weight: 15–30 marks, roughly every other paper.** When Paper 4 says "inherits from",
"overrides", or shows a class containing an array of other objects, this module is the
difference between attempted and earned marks. The mark scheme for inheritance is
short and predictable — five or six specific points.

## 1. Inheritance — the exact mark points

From Nov 2023 P42 Q3(c) and J25/42 Q3 mark schemes, a subclass declaration earns:

1. **Class header inheriting from the parent** — `class MagicCharacter(Character):`
2. **Declaring the new attribute** (type comment in Python) — `# self.__Element : STRING`
3. **Constructor header with the extended parameter count** — `def __init__(self, name, dob, intelligence, speed, element):`
4. **Calling the parent constructor** — `super().__init__(name, dob, intelligence, speed)`
5. **Assigning the parameter to the new attribute** — `self.__Element = element`

```python
class Character:
    # self.__CharacterName : STRING
    # self.__DateOfBirth   : DATE
    # self.__Intelligence  : REAL
    # self.__Speed         : INTEGER
    def __init__(self, name, dob, intelligence, speed):
        self.__CharacterName = name
        self.__DateOfBirth = dob
        self.__Intelligence = intelligence
        self.__Speed = speed

class MagicCharacter(Character):
    # self.__Element : STRING
    def __init__(self, name, dob, intelligence, speed, element):
        super().__init__(name, dob, intelligence, speed)   # parent constructor first
        self.__Element = element
```

## 2. Overriding — redefine, no keyword needed

Python overrides by simply redefining the method in the subclass (no `Overrides` keyword —
that's VB/Java syntax). The mark scheme's point is "method header overriding parent method":

```python
class Character:
    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1     # +10%

class MagicCharacter(Character):
    def Learn(self):                                        # overrides Learn()
        if self.__Element == "fire" or self.__Element == "water":
            self.__Intelligence = self.__Intelligence * 1.2
        elif self.__Element == "earth":
            self.__Intelligence = self.__Intelligence * 1.3
        else:
            self.__Intelligence = self.__Intelligence * 1.1
```

Polymorphism then works automatically: a variable holding either class calls whichever
`Learn()` it has. Questions that output "type-dependent" values (J23/41: print vertical
position *if the object is a helicopter*) are solved with a class check:

```python
if isinstance(vehicle, Helicopter):
    print(vehicle.GetVerticalPosition())
```

## 3. Worked example — Vehicle / Helicopter (June 2023 P41 Q2)

**Reference: June 2023 Paper 41 Q2 [32 marks]** —
`9618 Past Papers\9618 Computer Science June 2023 Question paper 41.pdf`

In brief: parent class `Vehicle` (ID, max speed, current speed, increase amount, horizontal
position) with constructor, getters, setters, and `IncreaseSpeed()` that limits to max
speed; child class `Helicopter` adds vertical position/vertical change/max height and
**overrides** `IncreaseSpeed()` to also apply the vertical limit; an output procedure prints
position and speed for any vehicle, plus vertical data if it is a helicopter; main
instantiates a car and a helicopter and increases each one's speed twice.

The full model is `solutions/m07_vehicle_helicopter.py`. The part to study is the override:

```python
class Helicopter(Vehicle):
    # self.__VerticalPosition : INTEGER
    # self.__VerticalChange   : INTEGER
    # self.__MaxHeight        : INTEGER
    def __init__(self, vehicle_id, max_speed, increase_amount, vertical_position,
                 vertical_change, max_height):
        super().__init__(vehicle_id, max_speed, increase_amount)
        self.__VerticalPosition = vertical_position
        self.__VerticalChange = vertical_change
        self.__MaxHeight = max_height

    def IncreaseSpeed(self):                     # overrides Vehicle.IncreaseSpeed
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        Vehicle.IncreaseSpeed(self)              # or re-implement the horizontal logic
```

**Mark scheme shape:** inherits header / new attributes with types / constructor calls
parent / override redefines the limit logic / isinstance-based output.

## 4. Worked example — Employee/Manager with overriding + super (June 2023 P42 Q3(b))

**Reference: June 2023 Paper 42 Q3(b) [7 marks]** — `Manager` inherits `Employee`, adds a
bonus *percentage*; its `SetPay()` **overrides** the parent: the hours are increased by the
bonus percentage *before* delegating to the parent's `SetPay()`.

```python
class Manager(Employee):
    # self.__BonusValue : REAL
    def __init__(self, hourly_pay, employee_number, bonus_value, job_title):
        super().__init__(hourly_pay, employee_number, job_title)
        self.__BonusValue = bonus_value

    def SetPay(self, week_number, hours_worked):       # override
        hours_worked = hours_worked * (1 + self.__BonusValue / 100)
        Employee.SetPay(self, week_number, hours_worked)   # delegate to parent
```

The "increase then call parent" pattern (bonus, then store) is the exam's favourite
override shape. The surrounding file-driven instantiation is Module 5's worked example.

## 5. Composition — objects owning objects

Equally frequent, and easier: a class whose attributes include other objects or arrays of
them.

- **N22/41 Q2(b)**: `Hand` holds an array of 5 `Card` objects + `FirstCard` + count.
- **J26/41 Q3**: `Path` holds `BoardArray[0:99]` of `TheObject` (100 objects, initialised
  empty) and `NumberSpaces`.
- **N25/41 Q2**: `Station` holds `Trains[0:9]` of `Train` + platform count.
- **N25/43 Q1(b)**: `Board` holds a **2D** 10×10 grid of `BoardObject`, each initialised
  empty (code `"-"`, value 0).

```python
class Station:
    # self.__StationID     : STRING
    # self.__NumberPlatforms : INTEGER
    # self.__NumberTrains  : INTEGER
    # self.__Trains        : ARRAY[0:9] OF Train
    def __init__(self, station_id, number_platforms):
        self.__StationID = station_id
        self.__NumberPlatforms = number_platforms
        self.__NumberTrains = 0
        self.__Trains = [None for _ in range(10)]

    def AddTrain(self, new_train):
        if self.__NumberTrains == self.__NumberPlatforms:
            return False
        self.__Trains[self.__NumberTrains] = new_train
        self.__NumberTrains += 1
        return True

    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains"
        result = f"The trains at station {self.__StationID} are: "
        for i in range(self.__NumberTrains):
            result += f"{self.__Trains[i].GetTrainIDNumber()} on route number {self.__Trains[i].GetRoute()}; "
        return result
```

Note the empty-object initialisation (N25/43 wants each grid cell to *be* a BoardObject
with code `"-"`): build it in a loop, not with `[None]*n` when the paper demands real empty
objects.

**Mark scheme shape:** class declaration / array attribute declared with type / constructor
initialises every element (or to the specified empty object) / methods use the contained
objects through their getters.

## 6. Choosing: inheritance or composition?

Read the question text. "X **inherits from** Y" / "X **is a** Y" → inheritance.
"X **contains/has** Y" / class diagram shows Y as an attribute type → composition. Papers
never leave it ambiguous; both earn a fixed, short mark list, so treat either as free marks
once fluent.

## Practice set

| Reference | Task | Marks |
|---|---|---|
| Jun 2023 P41 Q2 | Vehicle/Helicopter full inheritance question | 32 |
| Jun 2023 P42 Q3 | Employee/Manager + variable-length file | 33 |
| Nov 2023 P41 Q3 | Character/BikeCharacter, clamped setters, validated input | 30 |
| Nov 2023 P42 Q3 | Character + DATE + MagicCharacter override | 31 |
| Jun 2025 P42 Q3 | Animal/Parrot/Wolf — two subclasses overriding one method | 26 |
| Nov 2022 P41 Q2 | Card + Hand composition + scoring | 31 |
| Jun 2026 P41 Q3 | Path owning 100 objects + string building | 21 |
| Nov 2025 P41 Q2 | Train/Station composition | 25 |
| Nov 2025 P43 Q1 | Board with 10×10 grid of BoardObjects | 31 |

## Common pitfalls

- Forgetting `super().__init__(...)` — a dedicated mark point in every inheritance question.
- Re-declaring inherited attributes in the subclass (never needed; just call super).
- Override that doesn't handle the "else" case the paper specifies (the +10% fallback).
- Composition constructor that leaves the object array as `None` when the paper demands
  initialised empty objects.
- Using the subclass's new private attribute *before* assigning it in `__init__`.

## Checkpoint

- [ ] I can write the 5-point subclass skeleton from memory, including super().
- [ ] I can override a method and delegate to the parent where the paper requires it.
- [ ] I can build a class that owns an array of other objects, initialised per spec.
- [ ] I know when to use isinstance() for type-dependent output.
