class DQ:
    def __init__(self):
        self.data = []

    def addFront(self, data):
        self.data.insert(0, data)
        return f"Value {data} was added!"

    def addRear(self, data):
        self.data.append(data)
        return f"Value {data} was added!"

    def isEmpty(self):
        return not self.data

    def removeFront(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            return "Stack is empty!"
    
    def removeRear(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            return "Stack is empty!"

    def __str__(self):
        return str(self.data)

    def contains(self, data):
        if not self.isEmpty():
            for item in self.data:
                if item == data:
                    return True
            return False
        else:
            return "Stack is empty!"

dq = DQ()
print(dq.isEmpty())
print(dq.addRear(100))
print(dq)
print(dq.addRear(200))
print(dq.addRear(300))
print(dq.addRear(400))
print(dq)
print(dq.addFront("A"))
print(dq.addFront("B"))
print(dq.addFront("C"))
print(dq)
print(dq.contains(300))
print(dq.removeRear())
print(dq)
print(dq.removeFront())
print(dq)
print(dq.contains("C"))
