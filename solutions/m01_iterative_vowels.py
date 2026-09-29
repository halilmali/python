"""
Module 1 practice — Nov 2023 P41 Q1(a): translate the paper's iterative
vowel-counting function (built on LENGTH and MID in the pseudocode) to Python,
then call it with the paper's test phrase.

Run:  python m01_iterative_vowels.py
"""

def IterativeVowels(Phrase):
    Total = 0
    for X in range(len(Phrase)):        # LENGTH(Phrase) -> len(Phrase)
        if Phrase[X] in "aeiou":        # MID(Phrase, X+1, 1) -> Phrase[X]
            Total += 1
    return Total


# main program — call with the paper's test word and output the result
print(IterativeVowels("house"))
