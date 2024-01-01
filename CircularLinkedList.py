class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            currentNode = self.head
            newNode.next = currentNode

            while currentNode.next != self.head:
                currentNode = currentNode.next

            currentNode.next = newNode          
        return True

    def prepend(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            currentNode = self.head
            newNode.next = currentNode

            while currentNode.next != self.head:
                currentNode = currentNode.next
            
            currentNode.next = newNode
            self.head = newNode
        return True

    def insert(self, index, data):
        if self.head is None:
            return False
        else:
            currentNode = self.head

            for _ in range(index - 2):
                currentNode = currentNode.next
            
            newNode = Node(data)
            nextNode = currentNode.next
            currentNode.next = newNode
            newNode.next = nextNode
            return True

    def remove(self, data):
        if self.head is None:
            return False
        else:
            currentNode = self.head
            prevNode = None

            while currentNode.data != data:
                prevNode = currentNode
                currentNode = currentNode.next

            if prevNode is not None:
                prevNode.next = currentNode.next
                return True
            else:
                return False
    
    def print(self):
        currentNode = self.head

        while currentNode.next != self.head:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print(currentNode.data, end=" -> ")
        print("None")

cll = CLL()
cll.append(100)
cll.append(200)
cll.append(300)
cll.append(400)
cll.print()
cll.prepend("hello")
cll.print()
cll.insert(3, "world")
cll.print()
cll.remove(100)
cll.print()