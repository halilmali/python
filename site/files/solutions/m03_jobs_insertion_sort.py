"""
Module 3 worked example — Nov 2022 P42 Q1 (23 marks): 2D array Jobs[0:99, 0:1]
of job numbers and priorities; Initialise() fills with -1; AddJob() stores a
pair or reports full; InsertionSort() orders by priority keeping pairs together;
PrintArray() formatted output.

Run:  python m03_jobs_insertion_sort.py
(The five jobs from the paper are added from a fixed list; no input needed.)
"""

Jobs = [[0, 0] for _ in range(100)]     # [job number, priority]
NumberOfJobs = 0


def Initialise():
    global NumberOfJobs
    for x in range(100):
        Jobs[x][0] = -1
        Jobs[x][1] = -1
    NumberOfJobs = 0


def AddJob(JobNumber, Priority):
    global NumberOfJobs
    if NumberOfJobs >= 100:
        print("Not added")
        return
    Jobs[NumberOfJobs][0] = JobNumber
    Jobs[NumberOfJobs][1] = Priority
    NumberOfJobs += 1


def InsertionSort():
    global Jobs
    for i in range(1, NumberOfJobs):
        key_job = Jobs[i][0]
        key_priority = Jobs[i][1]
        j = i - 1
        while j >= 0 and Jobs[j][1] > key_priority:
            Jobs[j + 1][0] = Jobs[j][0]      # move the WHOLE row
            Jobs[j + 1][1] = Jobs[j][1]
            j -= 1
        Jobs[j + 1][0] = key_job
        Jobs[j + 1][1] = key_priority


def PrintArray():
    for x in range(NumberOfJobs):
        print(Jobs[x][0], "priority", Jobs[x][1])


def main():
    Initialise()
    # the five jobs from the paper's part (d)
    AddJob(349, 5)
    AddJob(212, 8)
    AddJob(776, 1)
    AddJob(905, 3)
    AddJob(411, 9)
    print("Before sorting:")
    PrintArray()
    InsertionSort()
    print("After sorting:")
    PrintArray()


main()
