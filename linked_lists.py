from node import Node


class LinkedList:
    def __init__(self):
        self.headNode = None

    def append(self, value):
        newNode = Node(value)
        if not self.headNode:
            self.headNode = newNode
            return
        currentNode = self.headNode
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def prepend(self, value):
        newNode = Node(value, self.headNode)
        self.headNode = newNode

    def size(self):
        count = 0
        currentNode = self.headNode
        while currentNode:
            count += 1
            currentNode = currentNode.nextNode
        return count

    def head(self):
        return self.headNode

    def tail(self):
        currentNode = self.headNode
        if not currentNode:
            return None
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        return currentNode

    def at(self, index):
        currentNode = self.headNode
        for i in range(index):
            if not currentNode:
                return None
            currentNode = currentNode.nextNode
        return currentNode

    def pop(self):
        if not self.headNode:
            return None
        if not self.headNode.nextNode:
            value = self.headNode.value
            self.headNode = None
            return value
        currentNode = self.headNode
        while currentNode.nextNode.nextNode:
            currentNode = currentNode.nextNode
        value = currentNode.nextNode.value
        currentNode.nextNode = None
        return value

    def contains(self, value):
        currentNode = self.headNode
        while currentNode:
            if currentNode.value == value:
                return True
            currentNode = currentNode.nextNode
        return False

    def find(self, value):
        currentNode = self.headNode
        index = 0
        while currentNode:
            if currentNode.value == value:
                return index
            currentNode = currentNode.nextNode
            index += 1
        return None

    def toString(self):
        currentNode = self.headNode
        nodes = []
        while currentNode:
            nodes.append(f"({currentNode.value})")
            currentNode = currentNode.nextNode
        nodes.append("null")
        return " -> ".join(nodes)

    def insertAt(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        newNode = Node(value)
        currentNode = self.headNode
        for i in range(index - 1):
            if not currentNode:
                return
            currentNode = currentNode.nextNode
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def removeAt(self, index):
        if index == 0 and self.headNode:
            self.headNode = self.headNode.nextNode
            return
        currentNode = self.headNode
        for i in range(index - 1):
            if not currentNode:
                return
            currentNode = currentNode.nextNode
        if not currentNode or not currentNode.nextNode:
            return
        currentNode.nextNode = currentNode.nextNode.nextNode


if __name__ == "__main__":
    list = LinkedList()

    list.append("dog")
    list.append("cat")
    list.append("parrot")
    list.append("hamster")
    list.append("snake")
    list.append("turtle")

    print(list.toString())
