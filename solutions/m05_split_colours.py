"""
Module 5 worked example — Jun 2025 P41 Q2 (25 marks): ask for a filename, read
lines like "10,red" of unknown length, split into value and colour, store into
six per-colour arrays, then append each value to its colour's file, with
exception handling on both reading and writing.

Run with test input (the filename):
    echo TheData.txt | python m05_split_colours.py

Data file: ../data-files/J25-41/TheData.txt (recreated in the paper's format)
"""

ColourFiles = {"red": "Red.txt", "green": "Green.txt", "orange": "Orange.txt",
               "pink": "Pink.txt", "blue": "Blue.txt", "yellow": "Yellow.txt"}


def ReadData(filename):
    Red = []
    Green = []
    Orange = []
    Pink = []
    Blue = []
    Yellow = []
    try:
        file = open("../data-files/J25-41/" + filename, "r")
        line = file.readline().strip()
        while line != "":                      # unknown number of lines
            parts = line.split(",")            # "10,red" -> ["10", "red"]
            value = int(parts[0])
            colour = parts[1].strip()
            if colour == "red":
                Red.append(value)
            elif colour == "green":
                Green.append(value)
            elif colour == "orange":
                Orange.append(value)
            elif colour == "pink":
                Pink.append(value)
            elif colour == "blue":
                Blue.append(value)
            elif colour == "yellow":
                Yellow.append(value)
            line = file.readline().strip()
        file.close()
    except Exception:
        print("File could not be opened")
    return Red, Green, Orange, Pink, Blue, Yellow


def WriteFile(Values, Colour):
    # append each value on its own line, with exception handling
    try:
        file = open("../data-files/J25-41/" + ColourFiles[Colour], "a")
        for value in Values:
            file.write(str(value) + "\n")
        file.close()
    except Exception:
        print("Could not write " + ColourFiles[Colour])


def main():
    filename = input("Enter the data filename: ")
    Red, Green, Orange, Pink, Blue, Yellow = ReadData(filename)
    WriteFile(Red, "red")
    WriteFile(Green, "green")
    WriteFile(Orange, "orange")
    WriteFile(Pink, "pink")
    WriteFile(Blue, "blue")
    WriteFile(Yellow, "yellow")
    print("Red:", Red)
    print("Blue:", Blue)


main()
