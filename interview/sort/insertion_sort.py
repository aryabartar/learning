def insertion_sort(array):
    for i in range(1, len(array)):

        biggest__index = 0

        for j in range(0, len(array) - i + 1):

            if array[j] > array[biggest__index]:
                biggest__index = j

        array[len(array) - i], array[biggest__index] = array[biggest__index], array[len(array) - i]

    return array


print(insertion_sort([2, 1, 3, -3, 22, 4, 2, 6]))
