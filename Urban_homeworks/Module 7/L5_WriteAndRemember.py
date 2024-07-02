"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением -
записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
"""


def custom_write(file_name, strings):
    if not isinstance(strings, list):
        raise TypeError('Хочу список строк!')

    strings_positions = {}
    string_number = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            current_pos = file.tell()
            strings_positions[(string_number, current_pos)] = string
            file.write(string + '\n')
            string_number += 1

    return strings_positions


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)