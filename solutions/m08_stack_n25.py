"""
Module 8 worked example — Nov 2025 P41 Q1 (20 marks): stack of 30 integers in a
global array (elements "null"), TopOfStack is the index of the LAST element,
initialised to -1; Push() returns FALSE when full; Pop() returns -999 when
empty; main generates 40 random integers 0-1000 and pushes until full;
FindValues() pops everything and reports the largest and smallest.

Run:  python m08_stack_n25.py
"""

import random

Stack = [None for _ in range(30)]   # global array of 30 integers
TopOfStack = -1                     # index of last element


def Push(NewValue):
    global TopOfStack
    if TopOfStack == 29:            # stack full
        return False
    TopOfStack += 1
    Stack[TopOfStack] = NewValue
    return True


def Pop():
    global TopOfStack
    if TopOfStack == -1:            # stack empty
        return -999                 # sentinel defined by the paper
    value = Stack[TopOfStack]
    TopOfStack -= 1
    return value


def FindValues():
    largest = -1                    # values are 0-1000, so these are safe starts
    smallest = 1001
    while TopOfStack != -1:
        value = Pop()
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    print("The largest value was", largest)
    print("The smallest value was", smallest)


def main():
    # (d) 40 random integers, push until full, then stop with "Stack full"
    for _ in range(40):
        if not Push(random.randint(0, 1000)):
            print("Stack full")
            break
    # (e)(f) pop everything, report largest and smallest
    FindValues()


main()
