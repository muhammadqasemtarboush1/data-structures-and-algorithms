def array_insert_shift(arr, num):
    mid_len = int(len(arr)/2)
    if len(arr) % 2 != 0:
        arr.insert(mid_len+1, num)
    elif len(arr) % 2 == 0:
        arr.insert(mid_len, num)
    else:
        arr.append(num)
    return arr


print(array_insert_shift([2, 4, 6, -8], 5))
# print(array_insert_shift([42, 8, 15, 23, 42], 16))
