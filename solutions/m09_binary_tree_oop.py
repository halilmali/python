"""
Module 9 worked example — Jun 2025 P41 Q3 (30 marks): a binary search tree built
from object references — class Node (LeftNode, Data, RightNode) and class Tree
(FirstNode); Insert() walks references to the leaf position; OutputInOrder() is
a recursive traversal. Self-test inserts the paper's sequence and prints the
in-order output (ascending).

Run:  python m09_binary_tree_oop.py
"""

class Node:
    # self.__LeftNode  : Node
    # self.__Data      : INTEGER
    # self.__RightNode : Node
    def __init__(self, data):
        self.__LeftNode = None
        self.__Data = data
        self.__RightNode = None

    def GetData(self):
        return self.__Data

    def GetLeft(self):
        return self.__LeftNode

    def GetRight(self):
        return self.__RightNode

    def SetLeft(self, node):
        self.__LeftNode = node

    def SetRight(self, node):
        self.__RightNode = node


class Tree:
    # self.__FirstNode : Node
    def __init__(self):
        self.__FirstNode = None

    def Insert(self, NewNode):
        if self.__FirstNode is None:
            self.__FirstNode = NewNode
            return
        current = self.__FirstNode
        placed = False
        while not placed:
            if NewNode.GetData() < current.GetData():
                if current.GetLeft() is None:
                    current.SetLeft(NewNode)
                    placed = True
                else:
                    current = current.GetLeft()
            else:
                if current.GetRight() is None:
                    current.SetRight(NewNode)
                    placed = True
                else:
                    current = current.GetRight()

    def OutputInOrder(self, node):
        # recursive in-order traversal: left, data, right
        if node is None:
            return
        self.OutputInOrder(node.GetLeft())
        print(node.GetData())
        self.OutputInOrder(node.GetRight())

    def traverse(self):
        self.OutputInOrder(self.__FirstNode)


def main():
    my_tree = Tree()
    for value in [10, 5, 15, 8, 12, 6, 20, 11, 9, 4]:
        my_tree.Insert(Node(value))
    my_tree.traverse()


main()
