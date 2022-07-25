'''

  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
'''


def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1

        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = value

    return arr


if __name__ == '__main__':
    array = [8, 4, 23, 42, 16, 15]
    print(insertion_sort(array))
    #   [4, 8, 15, 16, 23, 42]
    array = [5, 12, 7, 5, 5, 7]
    print(insertion_sort(array))
    # [5, 5, 5, 7, 7, 12]
    array = [2, 3, 5, 7, 13, 11]
    print(insertion_sort(array))
    # [2, 3, 5, 7, 11, 13]
