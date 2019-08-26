def partition(arr, i, j):
    min = i
    max = j

    pivot = i
    i = i + 1

    while i < j:

        while i < max and arr[i] < arr[pivot]:
            i += 1
        while min < j and arr[j] > arr[pivot]:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]

    return j


def quick_sort(arr, i, j):
    if j - i < 1:
        return

    middle = partition(arr, i, j)
    print(arr[i:j + 1])

    quick_sort(arr, i, middle - 1)
    quick_sort(arr, middle + 1, j)


a = [5, 2, 4, 55, 6, 66, -55, -1]
quick_sort(a, 0, len(a) - 1)
print(a)
