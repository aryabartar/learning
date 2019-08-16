class Deque(object):
    def __init__(self):
        self.array = []

    def add_front(self, item):
        self.array = [item] + self.array

    def add_rear(self, item):
        self.array.append(item)

    def remove_front(self, item):
        return self.array.pop(0)

    def remove_rear(self, item):
        return self.array.pop(len(self.array))
