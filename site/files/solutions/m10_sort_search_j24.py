"""
Module 10 worked example — Jun 2024 P41 Q1 (27 marks): read a validated count
(1-20), fill a global array, Initialise() procedure, bubble sort, iterative
BinarySearch(), then the main program outputs the array before and after
sorting and searches for a user value.

Run with test input (count, values, search value), e.g.:
    printf "10\n23\n17\n5\n90\n12\n44\n1\n8\n63\n29\n44\n" | python m10_sort_search_j24.py
"""

NumberArray = [0] * 20          # global array
NumberCount = 0


# 1(b) read the count and the values
def Initialise():
    global NumberCount
    valid = False
    while not valid:
        NumberCount = int(input("How many numbers (1-20)? "))
        if 1 <= NumberCount <= 20:
            valid = True
        else:
            print("Count must be between 1 and 20")
    for index in range(NumberCount):
        NumberArray[index] = int(input("Enter a number: "))


# 1(d) bubble sort ascending — no inbuilt sorting
def BubbleSort():
    for x in range(NumberCount - 1):
        for y in range(NumberCount - x - 1):
            if NumberArray[y] > NumberArray[y + 1]:
                NumberArray[y], NumberArray[y + 1] = NumberArray[y + 1], NumberArray[y]


# 1(e) iterative binary search; returns the index or -1
def BinarySearch(SearchValue):
    first = 0
    last = NumberCount - 1
    while first <= last:
        middle = (first + last) // 2
        if NumberArray[middle] == SearchValue:
            return middle
        elif NumberArray[middle] > SearchValue:
            last = middle - 1
        else:
            first = middle + 1
    return -1


def OutputArray():
    for index in range(NumberCount):
        print(NumberArray[index], end=" ")
    print()


def main():
    Initialise()
    print("Before sorting:")
    OutputArray()
    BubbleSort()
    print("After sorting:")
    OutputArray()
    search_value = int(input("Enter a value to search for: "))
    result = BinarySearch(search_value)
    if result == -1:
        print("Not found")
    else:
        print(f"Found at position {result}")


main()
