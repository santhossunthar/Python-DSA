class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head

            while currentNode.next:
                currentNode = currentNode.next
            
            currentNode.next = newNode
            newNode.prev = currentNode
        return True

    def prepend(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            currentNode.prev = newNode
            newNode.next = currentNode
            self.head = newNode
        return True

    def insert(self, index, data):
        if self.head is None:
            return False
        else:
            currentNode = self.head

            for _ in range(index - 1):
                currentNode = currentNode.next

            if currentNode is None:
                return False

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

        currentNode = self.head

        while currentNode.data != data:
            currentNode = currentNode.next

        prevNode = currentNode.prev
        nextNode = currentNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return True

    def print(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

dll = DLL()
dll.append(100)
dll.append(200)
dll.append(300)
dll.print()
dll.prepend("hello")
dll.print()
dll.insert(3, "some")
dll.print()
dll.remove(100)
dll.print()


            


