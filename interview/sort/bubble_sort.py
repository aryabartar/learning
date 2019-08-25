def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubble_sort([2, 1, 3, -3, 22, 4, 2, 6]))
