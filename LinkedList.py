class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def print(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next

        print("Null")

ll = LinkedList()

ll.add(1)
ll.add("Hello")
ll.add([1, 2, 3])
ll.add(("Hello", [1, 2], 100))
ll.add({1, 2, 3})
ll.add({"name": "007"})

ll.print()