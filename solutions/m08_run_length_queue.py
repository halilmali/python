"""
Module 4/8 worked example — Nov 2025 P43 Q2 (24 marks): a global linear queue
of strings (max 100) with QueueHead, QueueTail and NumberItems; Enqueue()/
Dequeue() per the paper's conventions (Dequeue returns the STRING "False" when
empty — a deliberate trap); ReadData() loads '1'/'0' lines from BinaryData.txt;
Compress() repeatedly dequeues to build a run-length string (count then digit,
runs capped at 9).

Run:  python m08_run_length_queue.py

Data file: ../data-files/N25-43/BinaryData.txt (recreated in the paper's format)
"""

Queue = [""] * 100
QueueHead = -1
QueueTail = -1
NumberItems = 0
NewString = ""                   # global output string, per the paper


def Enqueue(DataToInsert):
    global QueueTail, NumberItems
    if NumberItems == 100:
        return False
    QueueTail += 1
    Queue[QueueTail] = DataToInsert
    NumberItems += 1
    if QueueHead == -1:
        QueueHead = 0
    return True


def Dequeue():
    global QueueHead, NumberItems
    if NumberItems == 0:
        return "False"           # string, not a Boolean — the paper's trap
    value = Queue[QueueHead]
    QueueHead += 1
    NumberItems -= 1
    return value


def ReadData():
    # read one '1' or '0' per line, for any number of lines up to 100
    try:
        file = open("../data-files/N25-43/BinaryData.txt", "r")
        line = file.readline().strip()
        while line != "":
            Enqueue(line)
            line = file.readline().strip()
        file.close()
    except Exception:
        print("File could not be opened")


def Compress():
    global NewString
    NewString = ""
    current = Dequeue()
    while current != "False":
        count = 1
        nxt = Dequeue()
        while nxt == current and count < 9:
            count += 1
            nxt = Dequeue()
        NewString += str(count) + current     # count then digit
        current = nxt


def main():
    ReadData()
    Compress()
    print(NewString)


main()
