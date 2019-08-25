def binary_search(element, array):
    def search(element, array, i, j):
        if i == j:
            if array[i] == element:
                return True
            return False

        middle = int((i + j) / 2)

        return (
                search(element, array, i, middle) or
                search(element, array, middle + 1, j)
        )

    return search(element, array, 0, len(array) - 1)


print(binary_search(4, [1, 2, 3, 10, 22, 3, 44, 5, 32, 3]))
