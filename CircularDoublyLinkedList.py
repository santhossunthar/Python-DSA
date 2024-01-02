class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
        else:
            currentNode = self.head
            lastNode = currentNode.prev
            lastNode.next = newNode
            newNode.next = currentNode
            newNode.prev = lastNode
            currentNode.prev = newNode
        return True

    def prepend(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
        else:
            currentNode = self.head
            lastNode = currentNode.prev
            newNode.next = currentNode
            newNode.prev = lastNode
            lastNode.next = newNode
            self.head = newNode
        return True

    def insert(self, index, data):
        if self.head is None:
            return False
        else:
            currentNode = self.head

            for _ in range(index - 1):
                currentNode = currentNode.next

            newNode = Node(data)
            prevNode = currentNode.prev
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = currentNode
            currentNode.prev = newNode
            return True

    def remove(self, data):
        if self.head is None:
            return False
        else:
            currentNode = self.head

            while currentNode.data != data and currentNode.next != self.head:
                currentNode = currentNode.next

            prevNode = currentNode.prev
            nextNode = currentNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            return True

    def print(self):
        currentNode = self.head

        while currentNode.next != self.head:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print(currentNode.data, end=" -> ")
        print("None")

cdll = CDLL()
cdll.append(100)
cdll.append(200)
cdll.append(300)
cdll.print()
cdll.remove(100)
cdll.print()