import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError("K is out of bound")
        return self.A[k]

    def _resize(self, capacity):
        B = self.make_array(capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = capacity

    def append(self, item):
        if self.capacity <= self.n:
            self._resize(self.capacity * 2)

        self.A[self.n] = item
        self.n += 1

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()


d = DynamicArray()
d.append(1)
print(len(d))
d.append(2)
print(len(d))
d.append(10)
print(len(d))
d.append(1)
print(len(d))

print(d[3])
