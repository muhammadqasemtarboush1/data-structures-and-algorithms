'''
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
'''


def swap(arr, i, low):
    if i != low:
        temp = arr[i]
        arr[i] = arr[low]
        arr[low] = temp


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    # i = left
    # while left < right:
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)
    swap(arr, right, low + 1)

    return low + 1


def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)
        return arr
    elif len(arr) <= 1:
        return arr


if __name__ == "__main__":
    pass
    # array = [8, 4, 23, 42, 16, 15]
    # print(quick_sort(array, 0, len(array) - 1))
