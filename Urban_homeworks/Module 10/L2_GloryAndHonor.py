"""
Задача "За честь и отвагу!":
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)
А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.
По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
осталось <кол-во воинов> воинов."
После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
"""


import time
from threading import Thread, Lock
from time import sleep


class Knight(Thread):
    __ENEMIES_COUNT = 100
    print_lock = Lock()

    def __init__(self, name, power, day_duration=1.0):
        if not isinstance(name, str) or not isinstance(power, int):
            raise TypeError('Wrong argument type!')
        else:
            if power <= 0:
                raise ValueError('Power is too low!')

        super().__init__()
        self.name = name
        self.power = power
        self.day_duration = day_duration

    def run(self):
        with Knight.print_lock:
            print(f'{self.name}, на нас напали!')
        remaining_enemies = self.__ENEMIES_COUNT
        current_day = 0
        while remaining_enemies > 0:
            current_day += 1
            sleep(self.day_duration)
            remaining_enemies -= self.power
            with Knight.print_lock:
                print(f'{self.name} сражается {current_day}-й день, '
                      f'осталось {0 if remaining_enemies < 0 else remaining_enemies} воинов')

        with Knight.print_lock:
            print(f'{self.name} одержал победу спустя вот столько дней: {current_day}')


day_duration = 0.2
knights = [
    Knight('Sir Lancelot', 13, day_duration),
    Knight('Sir Galahad', 20, day_duration)
]

for knight in knights:
    knight.start()

for knight in knights:
    knight.join()
print('Все битвы закончились!')
