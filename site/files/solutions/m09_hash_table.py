"""
Module 9 worked example — Nov 2025 P41 Q3 (25 marks): a hash table as a 100x10
2D array; Hash(Key) = Key MOD 100; collisions live in the next free slot of the
same row; Record class with PUBLIC Key/Data attributes (per the paper);
InitialiseHashTable(); ReadData() reads "key,string" lines from
HashTableData.txt, splits and inserts; GetRecord() hashes and searches the row,
returning the data or "Not found".

Run with test input (five keys incl. collisions):
    printf "528\n1128\n1828\n1062\n39\n" | python m09_hash_table.py

Data file: ../data-files/N25-41/HashTableData.txt (recreated in the paper's format)
"""

class Record:
    # self.Key  : INTEGER   (public, per the paper)
    # self.Data : STRING
    def __init__(self, key, data):
        self.Key = key
        self.Data = data


HashTable = [[None for _ in range(10)] for _ in range(100)]


def Hash(Key):
    return Key % 100


def InitialiseHashTable():
    global HashTable
    HashTable = [[None for _ in range(10)] for _ in range(100)]


def InsertData(RecordToInsert):
    address = Hash(RecordToInsert.Key)
    slot = 0
    while slot < 10 and HashTable[address][slot] is not None:
        slot += 1
    if slot < 10:
        HashTable[address][slot] = RecordToInsert


def ReadData():
    try:
        file = open("../data-files/N25-41/HashTableData.txt", "r")
        line = file.readline().strip()
        while line != "":
            parts = line.split(",")
            InsertData(Record(int(parts[0]), parts[1].strip()))
            line = file.readline().strip()
        file.close()
    except Exception:
        print("File could not be opened")


def GetRecord(Key):
    address = Hash(Key)
    for slot in range(10):
        entry = HashTable[address][slot]
        if entry is not None and entry.Key == Key:
            return entry.Data
    return "Not found"


def main():
    InitialiseHashTable()
    ReadData()
    for _ in range(5):
        key = int(input("Enter a key: "))
        print(GetRecord(key))


main()
