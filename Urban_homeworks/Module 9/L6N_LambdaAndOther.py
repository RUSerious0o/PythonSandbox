from random import choice

# Задача "Функциональное разнообразие":
# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda left, right: left == right, first, second)))


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                print(data, file=file)

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.__words = words

    def __call__(self, *args, **kwargs):
        return choice(self.__words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
for _ in range(30):
    print(first_ball(), end=' ')
