# def array_insert_shift(arr, num):
#     mid_len = int(len(arr)/2)
#     if len(arr) % 2 != 0:
#         arr.insert(mid_len+1, num)
#     elif len(arr) % 2 == 0:
#         arr.insert(mid_len, num)
#     else:
#         arr.append(num)
#     return arr

# New function without build in len, insert ,append
def array_insert_shift(arr, n):
    arr_len = 0
    for i in arr:
        arr_len += 1
    if(arr_len % 2 != 0):
        arr_len = arr_len//2 + 1
    else:
        arr_len = arr_len//2
    shifted_Array = arr[0:arr_len] + [n] + arr[arr_len:]
    return shifted_Array


print(array_insert_shift([2, 4, 9, 6, -8], 5))


""" 
Pseudo Code

defined array-insert-shift(array,number) :
    declare new variable arrLen = 0 
    for i in array 
        increment the arrLen to count the length on the array
    if the arrLen of array %2 != 0 "odd" 
        divide it by 2 then + 1
    else arrLen is even 
        divide it by 2
    declare new array = arr[start to:arrLen] concat with +[number]+ concat with the rest of the array arr[arrLen:]
    retun the new array 
    
"""
