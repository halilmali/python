"""
Module 5 worked example — Jun 2026 P41 Q2 (28 marks): read 16 comma-separated
toy records from Toys.txt into an array of record objects (exception handling);
validate the user's difficulty choice; filter by difficulty; write matching
records to SelectedToys.txt in comma-separated form.

Run with test input (e.g. difficulty "Expert"):
    echo Expert | python m05_toys_filter.py

Data file: ../data-files/J26-41/Toys.txt (recreated in the paper's format)
"""

# 2(a) record type declared as a class (per the cover rule)
class ToyRecord:
    # self.ToyName      : STRING
    # self.NumberBricks : INTEGER
    # self.Difficulty   : STRING
    # self.Category     : STRING
    def __init__(self, toy_name, number_bricks, difficulty, category):
        self.ToyName = toy_name
        self.NumberBricks = number_bricks
        self.Difficulty = difficulty
        self.Category = category


def ReadData():
    # 2(b) read 16 records with exception handling
    toys = [None] * 16
    try:
        file = open("../data-files/J26-41/Toys.txt", "r")
        for i in range(16):
            line = file.readline().strip()
            parts = line.split(",")
            toys[i] = ToyRecord(parts[0], int(parts[1]), parts[2], parts[3])
        file.close()
    except Exception:
        print("File could not be opened")
    return toys


def get_difficulty():
    # 2(c) loop until a valid difficulty is entered
    valid = False
    while not valid:
        difficulty = input("Enter difficulty (Easy/Intermediate/Expert): ").strip().lower()
        if difficulty in ("easy", "intermediate", "expert"):
            valid = True
        else:
            print("Invalid difficulty")
    return difficulty


def SelectToys(toys, difficulty):
    # 2(d) filter — linear search by attribute
    selected = []
    for toy in toys:
        if toy is not None and toy.Difficulty.lower() == difficulty:
            selected.append(toy)
    return selected


def WriteFile(selected):
    # 2(e) write matches to a new file, comma-separated
    try:
        file = open("../data-files/J26-41/SelectedToys.txt", "w")
        for toy in selected:
            file.write(toy.ToyName + "," + str(toy.NumberBricks) + ","
                       + toy.Difficulty + "," + toy.Category + "\n")
        file.close()
        print(len(selected), "toys written to SelectedToys.txt")
    except Exception:
        print("File could not be written")


def main():
    toys = ReadData()
    difficulty = get_difficulty()
    selected = SelectToys(toys, difficulty)
    for toy in selected:
        print(toy.ToyName, toy.NumberBricks, toy.Difficulty, toy.Category)
    WriteFile(selected)


main()
