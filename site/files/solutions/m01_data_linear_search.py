"""
Module 1 practice — Jun 2023 P41 Q1 (18 marks): read 25 integers from Data.txt
into a local array; procedure PrintArray(); function LinearSearch() that counts
matches; main validates the user's search value (whole number 0-100) and outputs
"The number X is found N times."

Run with test input (e.g. searching for 7):
    echo 7 | python m01_data_linear_search.py

Data file: ../data-files/J23-41/Data.txt  (recreated in the paper's format)
"""

# 1(a) declare the array — the paper asks for it in the main program (local)
DataArray = [0] * 25


# 1(b) read the 25 integers from the file, with exception handling
def ReadFile():
    try:
        file = open("../data-files/J23-41/Data.txt", "r")
        for index in range(25):
            DataArray[index] = int(file.readline().strip())
        file.close()
    except Exception:
        print("File not found")


# 1(c)(ii) output the whole array on one line
def PrintArray(DataArray):
    for index in range(25):
        print(DataArray[index], end=" ")
    print()


# 1(c)(iii) linear search that COUNTS occurrences
def LinearSearch(DataArray, SearchValue):
    Count = 0
    for index in range(25):
        if DataArray[index] == SearchValue:
            Count += 1
    return Count


# 1(d) main program: validate input 0-100, search, report
def main():
    ReadFile()
    PrintArray(DataArray)
    Valid = False
    while not Valid:
        try:
            SearchValue = int(input("Enter a whole number between 0 and 100: "))
            if 0 <= SearchValue <= 100:
                Valid = True
            else:
                print("Out of range")
        except Exception:
            print("Not a whole number")
    Count = LinearSearch(DataArray, SearchValue)
    print(f"The number {SearchValue} is found {Count} times.")


main()
