"""
Module 2 worked example — Jun 2022 P42 Q1 (25 marks): a stack of up to 10
integers in a global array; pointer = next free space, initialised to 0;
Push()/Pop() with the paper's sentinel conventions; main program tests the
deliberate overflow with 11 inputs, then pops two elements.

Run with the paper's test data:
    echo "11 12 13 14 15 16 17 18 19 20 21" | tr ' ' '\n' | python m02_stack_j22.py
"""

# 1(a) global data structures
StackData = [0] * 10        # array of 10 integers
StackPointer = 0            # integer, points to next available space


# 1(b) output all 10 elements and the pointer
def OutputStack():
    for index in range(10):
        print(StackData[index])
    print("StackPointer =", StackPointer)


# 1(c) Push: FALSE if full, else store, update pointer, TRUE
def Push(Value):
    global StackPointer
    if StackPointer == 10:
        return False
    StackData[StackPointer] = Value
    StackPointer += 1
    return True


# 1(e)(i) Pop: -1 if empty, else return top and update pointer
def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    StackPointer -= 1
    return StackData[StackPointer]


# main program
def main():
    # 1(d)(i) attempt 11 pushes — the 11th must report "not added"
    for _ in range(11):
        Number = int(input("Enter a number: "))
        if Push(Number):
            print("Number added to stack")
        else:
            print("Stack is full — number not added")
    OutputStack()

    # 1(e)(ii) remove two elements, output updated contents
    Pop()
    Pop()
    print("After removing two elements:")
    OutputStack()


main()
