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
        self.length += 1

        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode[1] > self.headNode[1]:
            self.__appendToHead(newNode)
            return

        # Check it is going to be inserted
        # between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode

        while rightNode != None:
            if newNode[1] > rightNode[1]:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # Once we reach here it must be added at the tail
        leftNode.nextNode = newNode

