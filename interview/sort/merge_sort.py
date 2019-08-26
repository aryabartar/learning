def merge(array1, array2):
    new_array = []
    i = 0
    j = 0
    while i < len(array1) or j < len(array2):
        if i == len(array1):
            new_array.append(array2[j])
            j += 1
            continue

        if j == len(array2):
            new_array.append(array1[i])
            i += 1
            continue

        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1

    return new_array


def merge_sort(array):
    if len(array) == 1:
        return array

    middle = int(len(array) / 2)
    first_array = merge_sort(array[0:middle])
    last_array = merge_sort(array[middle:])

    return merge(first_array, last_array)


print(merge_sort([10, 2, 55, 100, -100, -1, 3, 6]))
