def encrypt(phrase: str, key: int, lang: str = 'ru', shift: str = 'right') -> str:
    dictionary = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    dictionary_eng = 'abcdefghijklmnopqrstuvwxyz'

    result = ''
    for letter in phrase:
        dict_ = dictionary if lang == 'ru' else dictionary_eng
        if letter.isupper():
            dict_ = dict_.upper()

        if letter not in dict_:
            result += letter
            continue

        # print(dict_.find(letter))
        index = (dict_.find(letter) + key) % len(dict_) if shift == 'right' else \
            dict_.find(letter) - key
        result += dict_[index]

    return result


def calculate_word_len(word: str) -> int:

    return 0


if __name__ == '__main__':
    # print(encrypt('To be, or not to be, that is the question!', 17, 'en'))
    # print(encrypt('Блажен, кто верует, тепло ему на свете!', 10))
    # print(encrypt('Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.', 7, shift='left'))
    # print(encrypt('Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.', 25, lang='en', shift='left'))
    # for i in range(1, 26):
    #     print(i, encrypt('Hawnj pk swhg xabkna ukq nqj.', i, lang='en', shift='left'))

    # for i in range(1, 26):
    #     print(encrypt('Year', i, lang='en'), end=' ')

    phrase = 'Day, mice. "Year" is a mistake!'
    print(encrypt('Day', 3, lang='en'))
