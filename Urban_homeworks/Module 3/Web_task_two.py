def caesar_crypt(str_):
    def encrypt_word(from_, to_):
        nonlocal const_upper
        nonlocal const_lower
        nonlocal str_
        nonlocal encrypted_str

        for i in range(from_, to_):
            if str_[i] in const_upper:
                encrypted_str += const_upper[(const_upper.find(str_[i]) + word_len) % len(const_upper)]
            else:
                encrypted_str += const_lower[(const_lower.find(str_[i]) + word_len) % len(const_lower)]

    const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const_lower = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_str = ''

    word_len = 0
    word_to_process = False
    for i in range(len(str_)):
        if str_[i].isalpha():
            word_len += 1
            if i == len(str_) - 1:
                encrypt_word(i - word_len, i)
        else:
            encrypt_word(i - word_len, i)
            encrypted_str += str_[i]
            word_len = 0

    return encrypted_str


print(caesar_crypt('Day, mice. "Year" is a mistake! z'))
