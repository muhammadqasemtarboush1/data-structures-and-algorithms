def get_keys(arr, hash_1, hash_2):
    obj = {}
    for i in arr:
        if hash_2.contains(i):
            obj[i] = {i, hash_1.get(i), hash_2.get(i)}
        else:
            obj[i] = {i, hash_1.get(i), 'No_match'}
    return obj


def hash_left_join(hash_1, hash_2):
    arr = hash_1.key()
    return get_keys(arr, hash_1, hash_2)
