"""
Module 8 worked example — Nov 2024 P42 Q2 (29 marks): a queue encapsulated in a
record (array + head + tail pointers); Enqueue() completes the paper's
incomplete pseudocode (returns 1 or -1); Dequeue() is deliberately
NON-destructive (returns the value at HeadPointer without advancing it, -1 when
empty); ReturnAllData() concatenates queued values into one space-separated
string; main validates inputs >= 0.

Run with test inputs (10 valid integers; the -1 is rejected):
    printf "10\n9\n-1\n8\n7\n6\n5\n4\n3\n2\n1\n" | python m08_queue_record.py
"""

class TheQueue:
    # self.QueueArray  : ARRAY[0:99] OF INTEGER
    # self.HeadPointer : INTEGER
    # self.TailPointer : INTEGER
    def __init__(self):
        self.QueueArray = [-1] * 100
        self.HeadPointer = -1
        self.TailPointer = 0


# 2(c) complete the Enqueue pseudocode; the queue object passes BYREF in Python
def Enqueue(AQueue, TheData):
    if AQueue.TailPointer == 100:
        return -1
    if AQueue.HeadPointer == -1:        # queue currently empty
        AQueue.HeadPointer = 0
    AQueue.QueueArray[AQueue.TailPointer] = TheData
    AQueue.TailPointer += 1
    return 1


# 2(f) non-destructive read of the front value
def Dequeue(AQueue):
    if AQueue.HeadPointer == -1 or AQueue.HeadPointer >= AQueue.TailPointer:
        return -1
    return AQueue.QueueArray[AQueue.HeadPointer]


# 2(d) concatenate the queued values without consuming them
def ReturnAllData(AQueue):
    result = ""
    for index in range(AQueue.HeadPointer, AQueue.TailPointer):
        result += str(AQueue.QueueArray[index]) + " "
    return result


def main():
    game_queue = TheQueue()
    for _ in range(10):
        valid = False
        while not valid:
            value = int(input("Enter an integer (0 or more): "))
            if value >= 0:
                valid = True
            else:
                print("Value must be 0 or more")
        if Enqueue(game_queue, value) == 1:
            print("Stored")
        else:
            print("Queue full")
    print(ReturnAllData(game_queue))
    print("Front value:", Dequeue(game_queue))
    print("Front value:", Dequeue(game_queue))
    print(ReturnAllData(game_queue))       # unchanged — Dequeue is non-destructive


main()
