"""
Module 8 worked example — Jun 2025 P42 Q1 (27 marks): a stack of up to 20
strings with TopOfStack; Push() returns 1 or -1; Pop() returns "-1" as a STRING
when empty; ReadData() takes a filename parameter, reads an unknown number of
lines with exception handling and pushes each line; Calculate() initialises the
total from the first value popped (always a number), then repeatedly pops an
operator and the number to apply, until the stack is empty ("^" = power).

Run with the paper's test filename:
    echo StackData.txt | python m08_stack_calculator.py

Data file: ../data-files/J25-42/StackData.txt (recreated in the paper's format)
"""

StackData = [""] * 20            # global array of 20 strings
TopOfStack = 0                   # next free space


def Push(DataToPush):
    global TopOfStack
    if TopOfStack == 20:
        return -1
    StackData[TopOfStack] = DataToPush
    TopOfStack += 1
    return 1


def Pop():
    global TopOfStack
    if TopOfStack == 0:
        return "-1"              # STRING sentinel, per the paper
    TopOfStack -= 1
    return StackData[TopOfStack]


def ReadData(filename):
    # unknown number of lines; exception handling; "Stack full" if Push fails
    try:
        file = open("../data-files/J25-42/" + filename, "r")
        line = file.readline().strip()
        while line != "":
            if Push(line) == -1:
                print("Stack full")
            line = file.readline().strip()
        file.close()
    except Exception:
        print("File could not be opened")


def apply_operator(operator, total, number):
    if operator == "+":
        return total + number
    if operator == "-":
        return total - number
    if operator == "*":
        return total * number
    if operator == "/":
        return total / number
    if operator == "^":
        return total ** number
    return total


def Calculate():
    # total initialised to the first value in the stack (always a number)
    total = int(Pop())
    while TopOfStack > 0:
        operator = Pop()          # next value: a mathematical operator
        number = int(Pop())       # then the number to apply
        total = apply_operator(operator, total, number)
    return total


def main():
    filename = input("Enter the data filename: ")
    ReadData(filename)
    print("Final total:", Calculate())


main()
