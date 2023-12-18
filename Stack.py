class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, data):
        self.data.append(data)
        return "Added: " + str(data)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            print("Stack is empty!")

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]

    def print(self):
        return self.data

stack = Stack()

print(stack.isEmpty())
print(stack.push(1))
print(stack.push([1, 2, "Hello"]))
print(stack.push("Random string"))
print(stack.print())
print(stack.pop())
print(stack.peek())
print(stack.print())