"""
Module 4 worked example — Jun 2026 P42 Q1 (18 marks): nine given strings; find
the longest and shortest WITHOUT inbuilt functions (length permitted); then
insertion sort the array into alphabetical order (no inbuilt sort), working for
any length; output the sorted list.

Run:  python m04_strings_j26.py
"""

Strings = ["avatar", "orc", "goblin", "elf", "troll",
           "wraith", "gnome", "hud", "sprite"]


# 1(b) longest and shortest — len() allowed, comparison builtins not needed here
def find_longest_shortest(strings):
    longest = strings[0]
    shortest = strings[0]
    for s in strings:
        if len(s) > len(longest):
            longest = s
        if len(s) < len(shortest):
            shortest = s
    return longest, shortest


# 1(c) insertion sort, alphabetical, must work for any length
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    longest, shortest = find_longest_shortest(Strings)
    print("Longest:", longest)
    print("Shortest:", shortest)
    sorted_strings = insertion_sort(Strings)
    for s in sorted_strings:
        print(s)


main()
