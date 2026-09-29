"""
Module 8 worked example — Nov 2023 P42 Q1 (27 marks): two global stacks (100
letters each) with top pointers; PushData() routes vowels and consonants;
ReadData() reads 100 letters from StackData.txt with exception handling;
PopVowel()/PopConsonant() return "No data" when empty; main pops five letters
of the user's chosen kind and outputs them on one line.

Run with test input (choose vowel, then consonant, ...):
    printf "vowel\nconsonant\nconsonant\nvowel\nvowel\n" | python m08_two_stacks.py

Data file: ../data-files/N23-42/StackData.txt (recreated in the paper's format)
"""

StackVowel = [""] * 100          # 100 letters
StackConsonant = [""] * 100
VowelTop = 0                     # next free space in each stack
ConsonantTop = 0


def PushData(letter):
    global VowelTop, ConsonantTop
    if letter in "aeiou":
        if VowelTop == 100:
            print("Vowel stack is full")
        else:
            StackVowel[VowelTop] = letter
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print("Consonant stack is full")
        else:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop += 1


def ReadData():
    try:
        file = open("../data-files/N23-42/StackData.txt", "r")
        for _ in range(100):
            letter = file.readline().strip()
            PushData(letter)
        file.close()
    except Exception:
        print("File not found")


def PopVowel():
    global VowelTop
    if VowelTop == 0:
        return "No data"
    VowelTop -= 1
    return StackVowel[VowelTop]


def PopConsonant():
    global ConsonantTop
    if ConsonantTop == 0:
        return "No data"
    ConsonantTop -= 1
    return StackConsonant[ConsonantTop]


def main():
    ReadData()
    output = ""
    for _ in range(5):
        choice = input("Pop vowels or consonants? ").strip().lower()
        if choice == "vowel":
            output += PopVowel()
        else:
            output += PopConsonant()
    print(output)


main()
