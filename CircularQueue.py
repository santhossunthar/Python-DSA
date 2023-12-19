class CQ:
    def __init__(self, k):
        self.head = self.tail = self.size = 0
        self.k = k
        self.data = [None]*k

    def isFull(self):
        return self.size == self.k

    def enqueue(self, data):
        if not self.isFull():
            self.data[self.tail] = data
            self.size += 1
            self.tail = (self.tail + 1) % self.k
            return True
        else:
            return "Queue is full!"

    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
        if not self.isEmpty():
            self.head = (self.head + 1) % self.k
            self.size -= 1
            return True
        else:
            return "Queue is empty!"

    def __str__(self):
        return str(self.data)




cq = CQ(5)
print(cq.isEmpty())
print(cq.enqueue(1))
print(cq.enqueue(2))
print(cq.enqueue(3))
print(cq.enqueue(4))
print(cq.enqueue(5))
print(cq.enqueue(6))
print(cq.isFull())
print(cq.dequeue())
print(cq.enqueue(100))
print(cq)
print(cq.enqueue(200))
print(cq)
print(cq.dequeue())
print(cq.enqueue(200))
print(cq)
print(cq.dequeue())
print(cq)
print(cq.enqueue(300))
print(cq)

print(cq.dequeue())
print(cq)
print(cq.enqueue(400))
print(cq)

print(cq.dequeue())
print(cq)
print(cq.enqueue(500))
print(cq)

print(cq.dequeue())
print(cq)
print(cq.enqueue(1))
print(cq)

print(cq.dequeue())
print(cq)
print(cq.enqueue(2))
print(cq)