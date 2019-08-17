class Queue2Stack(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        s1 = self.s1
        s2 = self.s2

        while len(s1) != 0:
            s2.append(s1.pop())

        value = s2.pop()

        while len(s2) != 0:
            s1.append(s2.pop())

        return value


q = Queue2Stack()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())
