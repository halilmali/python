"""
Module 6 worked example — Jun 2022 P42 Q3 (27 marks): class Card (private
Number, Colour; constructor; getters); read 30 cards from CardValues.txt into
an array of objects; ChooseCard() validates an index 1-30, rejects already
selected cards and loops until an available one is chosen; player 1 picks 4
cards and they are output.

Run with the paper's test data (Test 1: 1 5 9 10):
    printf "1\n5\n9\n10\n" | python m06_card_game.py

Data file: ../data-files/J22-42/CardValues.txt (recreated in the paper's format)
"""

class Card:
    # self.__Number : INTEGER
    # self.__Colour : STRING
    def __init__(self, number, colour):
        self.__Number = number
        self.__Colour = colour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


Cards = [None] * 30          # array of Card objects
CardSelected = [False] * 30  # 3(d): which cards are taken


def ReadCards():
    # 3(c) read number then colour for each of the 30 cards
    try:
        file = open("../data-files/J22-42/CardValues.txt", "r")
        for i in range(30):
            number = int(file.readline().strip())
            colour = file.readline().strip()
            Cards[i] = Card(number, colour)
        file.close()
    except Exception:
        print("File not found")


# 3(d) validated, availability-checked selection loop
def ChooseCard():
    valid = False
    while not valid:
        index = int(input("Enter a card index (1-30): "))
        if 1 <= index <= 30:
            if not CardSelected[index - 1]:
                valid = True
                CardSelected[index - 1] = True
            else:
                print("That card is already selected")
        else:
            print("Index must be between 1 and 30")
    return index


def main():
    ReadCards()
    # 3(e)(i) player 1 selects 4 cards
    Player1 = [None] * 4
    for i in range(4):
        Player1[i] = Cards[ChooseCard() - 1]
    for i in range(4):
        print("Card", i + 1, "- number:", Player1[i].GetNumber(),
              "colour:", Player1[i].GetColour())


main()
