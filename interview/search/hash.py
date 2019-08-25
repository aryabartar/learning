# HashTable() Create a new, empty map. It returns an empty map collection.
# put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
# get(key) Given a key, return the value stored in the map or None otherwise.
# del Delete the key-value pair from the map using a statement of the form del map[key].
# len() Return the number of key-value pairs stored
# in the map in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def _hash_function(self, value):
        return value % self.size

    def _rehash(self, position, rehashed_number):
        return position + rehashed_number + 1

    def put(self, key, val):
        rehashed_number = 0
        position = self._hash_function(key)

        while self.array[position] is not None:
            if rehashed_number == self.size:
                raise IndexError("no")
            rehashed_number += 1
            position = self._rehash(position, rehashed_number)

        self.array[position] = (key, val)
