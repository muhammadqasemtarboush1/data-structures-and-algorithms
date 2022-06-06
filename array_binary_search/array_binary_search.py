# Insertion sort	Ω(n)	θ(n^2)	O(n^2)
def insertion_sort(array):
    for element in range(1, len(array)):
        index = element - 1
        next_e = array[element]
        while (array[index] > next_e) and (index >= 0):
            array[index + 1] = array[index]
            index = index - 1
            array[index + 1] = next_e
    return array


def binary_search(arr, val):
    if len(arr) == 0:
        return "error: invalid input you can not add empty array"
    first = 0
    mid = 0
    last = len(arr) - 1
    while first <= last:
        mid = (last + first) // 2
        if arr[mid] < val:
            first = mid + 1
        elif arr[mid] > val:
            last = mid - 1
        else:
            return mid
    return -1

# array = [20, 40, 2, 4, 6, 860, 80]
# x = 20
# result = binary_search(insertion_sort(array), x)
# print(result)
