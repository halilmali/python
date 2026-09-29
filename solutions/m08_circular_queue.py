"""
Module 8 worked example — Jun 2025 P41 Q1 (20 marks): circular queue of 20
integers initialised to -1, with HeadPointer, TailPointer and NumberItems
globals; wrap-around via MOD; Enqueue() returns FALSE when full; Dequeue()
returns -1 when empty; self-test stores 25 attempted values (overflow) then
dequeues 5.

Run:  python m08_circular_queue.py
"""

Queue = [-1] * 20
HeadPointer = 0
TailPointer = -1
NumberItems = 0


def Enqueue(NewItem):
    global TailPointer, NumberItems
    if NumberItems == 20:           # full
        return False
    TailPointer = (TailPointer + 1) % 20      # wrap-around
    Queue[TailPointer] = NewItem
    NumberItems += 1
    return True


def Dequeue():
    global HeadPointer, NumberItems
    if NumberItems == 0:            # empty
        return -1
    value = Queue[HeadPointer]
    HeadPointer = (HeadPointer + 1) % 20      # wrap-around
    NumberItems -= 1
    return value


def main():
    # attempt to store 25 values (values 1..25) — 20 succeed, 5 report failure
    for value in range(1, 26):
        if Enqueue(value):
            print(value, "-> Successful")
        else:
            print(value, "-> Unsuccessful")
    for _ in range(5):
        print("Dequeued:", Dequeue())


main()
