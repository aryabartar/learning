def insert(array, n):
    array.append(n)

    max_heapify(array, len(array) - 1)

    return array


def max_heapify(array, n):
    parent = get_parent(n)

    if parent is None:
        return

    if array[parent] < array[n]:
        replace_position(array, parent, n)
        max_heapify(array, parent)

    else:
        return


def replace_position(array, i, j):
    array[i], array[j] = array[j], array[i]


def get_left(array, n):
    left_position = 2 * n + 1
    if len(array) <= left_position:
        return None
    return left_position


def get_right(array, n):
    right_position = 2 * n + 2
    if len(array) <= right_position:
        return None
    return right_position


def get_parent(n):
    if n == 0:
        return None

    return int((n - 1) / 2)


print(insert([10, 5, 3, 2, 4], 15))
