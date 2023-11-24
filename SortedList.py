# Name: Hazem Bin Ryaz Patel
# Admission Number: 2200550
# Class: DAAA/FT/2B/07

from node import Node
class SortedList:
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        # Set the incoming tuple as a new node
        newNode = Node(newNode)
        self.length += 1
        if self.headNode == None:
            self.headNode = newNode
            return
        
        # Check if it is going to be new head
        if newNode.data[1] > self.headNode.data[1]:
            self.__appendToHead(newNode)
            return

        leftNode = self.headNode
        rightNode = self.headNode.nextNode

        while rightNode != None:
            if newNode.data[1] > rightNode.data[1]:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        leftNode.nextNode = newNode

    # Sorted list isn't subscriptable, so we need to convert it to a list
    # So that it can work with option 3 
    def to_list(self):
        list_version = []
        current_node = self.headNode
        while current_node is not None:
            list_version.append(current_node.data)
            current_node = current_node.nextNode
        return list_version
