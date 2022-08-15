def get_keys(arr, hash_1, hash_2):
    obj = {}
    for i in arr:
        if hash_2.contains(i):
            obj[i] = {i, hash_1.get(i), hash_2.get(i)}
        else:
            obj[i] = {i, hash_1.get(i), 'No_match'}
    return obj



def hash_left_join(hash_1, hash_2):
    # if len(hash_1.key()) > len(hash_2.key()):
    #     arr = hash_1.key()
    # else:
    #     arr = hash_2.key()
    arr = hash_1.key()
    return get_keys(arr, hash_1, hash_2)
