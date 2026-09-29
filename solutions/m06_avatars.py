"""
Module 6 worked example — Jun 2026 P42 Q2 (30 marks): class Avatar (TheName,
Glasses boolean, Hair, Age; constructor; getters; MeetCriteria() matching two
attribute values); read 30 SPACE-separated records from AvatarFile.txt with
exception handling; validate the user's criteria (glasses yes/no; hair from a
list); output matching avatars.

Run with test input (glasses, hair, e.g. "yes\nblonde\n"):
    printf "yes\nblonde\n" | python m06_avatars.py

Data file: ../data-files/J26-42/AvatarFile.txt (recreated in the paper's format)
"""

class Avatar:
    # self.__TheName  : STRING
    # self.__Glasses  : BOOLEAN
    # self.__Hair     : STRING
    # self.__Age      : INTEGER
    def __init__(self, the_name, glasses, hair, age):
        self.__TheName = the_name
        self.__Glasses = glasses
        self.__Hair = hair
        self.__Age = age

    def GetTheName(self):
        return self.__TheName

    def GetGlasses(self):
        return self.__Glasses

    def GetHair(self):
        return self.__Hair

    def GetAge(self):
        return self.__Age

    def MeetCriteria(self, glasses, hair):
        # matches when both attributes equal the criteria
        return self.__Glasses == glasses and self.__Hair.lower() == hair


AvailableAvatars = [None] * 30     # global array of Avatar objects


def ReadData():
    # 2(b) read 30 space-separated records, exception handling
    try:
        file = open("../data-files/J26-42/AvatarFile.txt", "r")
        for i in range(30):
            parts = file.readline().split()
            AvailableAvatars[i] = Avatar(parts[0], parts[1] == "True",
                                         parts[2], int(parts[3]))
        file.close()
    except Exception:
        print("File could not be opened")


def get_criteria():
    # 2(c) validated inputs — glasses yes/no, hair from the allowed list
    answer = ""
    while answer != "yes" and answer != "no":
        answer = input("Does the avatar wear glasses? (yes/no): ").strip().lower()
    glasses = answer == "yes"

    hair = ""
    while hair not in ("black", "brown", "blonde", "red"):
        hair = input("Hair colour (black/brown/blonde/red): ").strip().lower()
    return glasses, hair


def main():
    ReadData()
    glasses, hair = get_criteria()
    for i in range(30):
        if AvailableAvatars[i] is not None and AvailableAvatars[i].MeetCriteria(glasses, hair):
            print(AvailableAvatars[i].GetTheName(),
                  AvailableAvatars[i].GetAge(),
                  AvailableAvatars[i].GetHair(),
                  "glasses" if AvailableAvatars[i].GetGlasses() else "no glasses")


main()
