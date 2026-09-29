"""
Module 1 worked example — Nov 2021 P41 Q1(a)(b): translate the paper's recursive
function Unknown(X, Y) to Python, then run all three calls from the paper,
outputting the parameters and each return value.

Structure of the original: if X < Y it outputs X + Y and returns
Unknown(X + 1, Y) * 2; if X = Y it returns 1; otherwise it outputs X + Y and
returns Unknown(X - 1, Y) DIV 2.  Note the multiplication/division applies to
the RETURNED value (on the way back up), while the OUTPUT happens on the way
down.

Run:  python m01_unknown_function.py
"""

def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return int(Unknown(X - 1, Y) / 2)    # DIV


def main():
    for (x, y) in [(10, 15), (10, 10), (15, 10)]:
        print("Parameters:", x, y)
        print("Return value:", Unknown(x, y))


main()
