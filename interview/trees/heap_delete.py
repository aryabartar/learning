def delete_max(array):
    deleted_element = array[0]
    array[0] = array[-1]
    array.pop(-1)

    max_heapify(array, 0)

    return deleted_element, array


def max_heapify(array, n):
    left = get_left(array, n)
    right = get_right(array, n)

    if left is None and right is None:
        return

    if right is None:
        if array[n] < array[left]:
            replace_position(array, n, left)
            max_heapify(array, left)
        else:
            return

    max_value = max(array[n], array[left], array[right])

    if array[left] == max_value:
        replace_position(array, n, left)
        max_heapify(array, left)

    if array[right] == max_value:
        replace_position(array, n, right)
        max_heapify(array, right)


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


print(delete_max([10, 5, 3, 2, 4]))
