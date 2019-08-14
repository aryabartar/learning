import sys

a = [1]
print(sys.getsizeof(a))
a.extend([1,])
print(sys.getsizeof(a))
a.extend([1,])
print(sys.getsizeof(a))
a.extend([1, 2, 3, 4, 4, 5])
print(sys.getsizeof(a))
