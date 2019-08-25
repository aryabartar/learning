def find_unordered(elem, array):
    for i in array:
        if elem == i:
            return True

    return False


def find_ordered(elem, array):
    for i in array:
        if i < elem:
            break

        if elem == i:
            return True

    return False
