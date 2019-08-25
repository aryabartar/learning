def binary_search(element, array):
    def search(element, array, i, j):
        middle = int((i + j) / 2)

        if j < i:
            return False

        if i == j:
            if array[middle] == element:
                return True
            return False

        if element > array[middle]:
            return search(element, array, middle + 1, j)
        else:
            return search(element, array, i, middle - 1)

    return search(element, array, 0, len(array) - 1)


print(binary_search(4, [1, 2, 3, 5, 6, 7, 8, 9, 10]))
