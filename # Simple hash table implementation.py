def search(key):
         index = hash_function(key)
    if hash_table[index] is not None:
        for k, v in hash_table[index]:
            if k == key:
                return v
    return None




