class Stack(object):
    def __init__(self):
        self.array = []
        self.end = 0

    def __len__(self):
        return str(self.end)

    def push(self, item):
        self.array.append(item)
        self.end += 1

    def pop(self):
        if self.end == 0:
            return Exception("Stack is empty!")

        self.end -= 1
        return self.array.pop(self.end)


s = Stack()
s.push(1)
s.push(2)
print(s.pop())
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

