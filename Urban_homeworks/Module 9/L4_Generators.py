"""
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
"""


def all_variants(text):
    for sublen in range(1, len(text) + 1):
        for i in range(0, len(text) - sublen + 1):
            yield text[i:i + sublen]


a = all_variants("variants")
for i in a:
    print(i)