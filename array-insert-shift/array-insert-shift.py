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
def innset_shift_Array(arr, n):
    arr_lan = 0
    for i in arr:
        arr_lan += 1
    if(arr_lan % 2 != 0):
        arr_lan = arr_lan//2 + 1
    else:
        arr_lan = arr_lan//2
    shifted_Array = arr[0:arr_lan] + [n] + arr[arr_lan:]
    return shifted_Array


print(innset_shift_Array([2, 4, 9, 6, -8], 5))


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
