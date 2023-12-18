class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)
        return "Added: " + str(data)

    def isEmpty(self):
        return len(self.data) == 0

    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            return "Queue is empty!"

    def peek(self):
        return self.data[0]

    def print(self):
        return self.data

queue = Queue()
print(queue.print())
queue.enqueue(1)
queue.enqueue("Hello")
queue.enqueue([1, "Hello", {1, 2, 3}])
print(queue.print())
print(queue.dequeue())
print(queue.print())
print(queue.peek())