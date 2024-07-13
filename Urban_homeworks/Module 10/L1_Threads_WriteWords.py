"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов, file_name -
название файла, куда будут записываться слова. Функция должна вести запись слов "Какое-то слово № <номер слова по
порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
"""

from time import sleep
from _datetime import datetime
from threading import Thread


def time_estimate(func):
    def wrapper(*args):
        start = datetime.now()
        func(*args)
        print(f'Estimated time: {datetime.now() - start}')
    return wrapper


def write_words(word_count, file_name, delay=0.1):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(delay)
    print(f'Завершилась запись в файл {file_name}')


def async_write_words(tasks):
    threads = []
    for task in tasks:
        thread = Thread(target=write_words, args=(task[0], task[1], 0.01))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


tasks = [
    (10, 'example_1.txt'),
    (30, 'example_2.txt'),
    (200, 'example_3.txt'),
    (100, 'example_4.txt')
]

time_estimate(lambda: [write_words(words_count, file_name, 0.01) for words_count, file_name in tasks])()
time_estimate(async_write_words)(tasks)
