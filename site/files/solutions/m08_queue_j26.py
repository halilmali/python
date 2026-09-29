"""
Module 8 worked example — Jun 2026 P41 Q1 (26 marks): linear queue of 10
integers, head and tail pointers initialised to -1; Enqueue() (full check,
FALSE when full); Dequeue() returns -1 when empty; main attempts 11 inputs to
force the overflow message, then dequeues four values and outputs them.

Run with any 11 integers, e.g.:
    seq 1 11 | python m08_queue_j26.py
"""

Queue = [0] * 10
HeadPointer = -1
TailPointer = -1


def Enqueue(DataToInsert):
    global HeadPointer, TailPointer
    if TailPointer == 9:            # no free space at the tail
        return False
    if HeadPointer == -1:           # first element starts the queue
        HeadPointer = 0
    TailPointer += 1
    Queue[TailPointer] = DataToInsert
    return True


def Dequeue():
    global HeadPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:
        return -1                   # empty queue sentinel
    value = Queue[HeadPointer]
    HeadPointer += 1
    return value


def main():
    # 11 attempted inserts — the 11th must report unsuccessful
    for _ in range(11):
        number = int(input("Enter an integer: "))
        if Enqueue(number):
            print("Successful")
        else:
            print("Unsuccessful — queue is full")
    # dequeue four values
    for _ in range(4):
        value = Dequeue()
        if value == -1:
            print("Queue empty")
        else:
            print("Dequeued:", value)


main()
