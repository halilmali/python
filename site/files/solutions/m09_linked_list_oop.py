"""
Module 9 worked example — Jun 2025 P43 Q3 (29 marks): a linked list built from
object references — class Node (TheData, NextNode) and class LinkedList
(HeadNode); InsertNode() at the head; RemoveNode() searches and unlinks
(returning TRUE/FALSE); Traverse() concatenates the data into a string.
Self-test inserts several values, removes one present and one absent, and
traverses.

Run:  python m09_linked_list_oop.py
"""

class Node:
    # self.__TheData  : INTEGER
    # self.__NextNode : Node
    def __init__(self, data):
        self.__TheData = data
        self.__NextNode = None

    def GetData(self):
        return self.__TheData

    def GetNext(self):
        return self.__NextNode

    def SetNext(self, node):
        self.__NextNode = node


class LinkedList:
    # self.__HeadNode : Node
    def __init__(self):
        self.__HeadNode = None

    def InsertNode(self, NewNode):
        NewNode.SetNext(self.__HeadNode)     # insert at head
        self.__HeadNode = NewNode

    def RemoveNode(self, TheData):
        current = self.__HeadNode
        previous = None
        while current is not None and current.GetData() != TheData:
            previous = current
            current = current.GetNext()
        if current is None:
            return False                     # not found
        if previous is None:                 # removing the head node
            self.__HeadNode = current.GetNext()
        else:                                # splice out
            previous.SetNext(current.GetNext())
        return True

    def Traverse(self):
        result = ""
        current = self.__HeadNode
        while current is not None:
            result += str(current.GetData()) + " "
            current = current.GetNext()
        return result


def main():
    my_list = LinkedList()
    for value in [8, 3, 5, 1, 9]:            # inserted head-first
        my_list.InsertNode(Node(value))
    print("List:", my_list.Traverse())
    print("Remove 5:", my_list.RemoveNode(5))
    print("Remove 7:", my_list.RemoveNode(7))
    print("List:", my_list.Traverse())


main()
