import string

def is_pangram(s):
    # trans_dict = {}
    # for simbol in ' 1234567890-_!?,.':
    #     trans_dict[simbol] = ''
    # trans_table = str.maketrans(trans_dict)
    # return len(set(s.translate(trans_table).lower())) == 26

    return set('qwertyuiopasdfghjklzxcvbnm').issubset(set(s.lower()))


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram('1bcdefghijklmnopqrstuvwxyz'))