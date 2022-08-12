try:
    from hashtable.hashtable import *
except:
    from hashtable import *
from hashtable.repeated_word.text_ex import *


def repeated_word(text):
    text = text.lower().split(' ')
    hashmap = HashTable()
    for i in range(0, len(text)):
        if hashmap.contains(text[i].strip(',')):
            return text[i]
        else:
            hashmap.set(text[i].strip(','), i)
    return 'No duplicate founded'


if __name__ == "__main__":
    print(repeated_word(case_3))
