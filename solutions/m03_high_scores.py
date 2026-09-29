"""
Module 3 worked example — Jun 2022 P41 Q1 (29 marks): top-ten high score table
held in global parallel arrays (11 names of 3 characters, 11 scores); read from
HighScore.txt; output; insert a new score in descending order; write the result
to NewHighScore.txt.

Run with the paper's test flow (name then score, 5 players, then the new entry):
    printf "ACE\n95\nBOB\n80\nCID\n70\nDEL\n60\nEVE\n50\nAAA\n999\n" | python m03_high_scores.py

Data file: ../data-files/J22-41/HighScore.txt (recreated in the paper's format)
"""

# global parallel arrays — 11 entries so a new entry can be appended before sorting
PlayerNames = [""] * 11        # 3-character strings
PlayerScores = [0] * 11        # integers


# 1(b) read names and scores from the file
def ReadHighScores():
    try:
        file = open("../data-files/J22-41/HighScore.txt", "r")
        for index in range(11):
            PlayerNames[index] = file.readline().strip()
            PlayerScores[index] = int(file.readline().strip())
        file.close()
    except Exception:
        print("File not found")


# 1(c) output each name and score on one line
def OutputHighScores():
    for index in range(11):
        print(PlayerNames[index], PlayerScores[index])


# 1(e) input and validate a player name (3 characters) and score (1-100000)
def GetPlayerDetails():
    valid = False
    while not valid:
        name = input("Enter a 3-character player name: ")
        if len(name) == 3:
            valid = True
        else:
            print("Name must be exactly 3 characters")
    valid = False
    while not valid:
        score = int(input("Enter a score between 1 and 100000: "))
        if 1 <= score <= 100000:
            valid = True
        else:
            print("Score out of range")
    return name, score


# 1(e)(ii) insert the new entry, keeping descending order; drop the 11th
def InsertScore(name, score):
    PlayerNames[10] = name
    PlayerScores[10] = score
    for i in range(10, 0, -1):
        if PlayerScores[i] > PlayerScores[i - 1]:
            PlayerNames[i], PlayerNames[i - 1] = PlayerNames[i - 1], PlayerNames[i]
            PlayerScores[i], PlayerScores[i - 1] = PlayerScores[i - 1], PlayerScores[i]
        else:
            break


# 1(f) write the top ten to a new file
def WriteTopTen():
    try:
        file = open("../data-files/J22-41/NewHighScore.txt", "w")
        for index in range(10):
            file.write(PlayerNames[index] + " " + str(PlayerScores[index]) + "\n")
        file.close()
        print("New high score table written")
    except Exception:
        print("File could not be written")


def main():
    ReadHighScores()
    OutputHighScores()
    name, score = GetPlayerDetails()
    InsertScore(name, score)
    OutputHighScores()
    WriteTopTen()


main()
