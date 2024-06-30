"""
Задача 1: Фабрика Функций
Написать функцию, которая возвращает различные математические функции (например, деление, умножение) в зависимости от переданных аргументов.
"""

def get_operation(operator):
    if operator == '+':
        def operation(x, y):
            return x + y
        return operation

    if operator == '-':
        def operation(x, y):
            return x - y
        return operation

    if operator == '*':
        def operation(x, y):
            return x * y
        return operation

    if operator == '/':
        def operation(x, y):
            return x / y
        return operation

    raise NotImplementedError('Операция неизвестна')


print('Задача 1: Фабрика функций')
for operator in ('+', '-', '*', '//', '/'):
    try:
        print(get_operation(operator)(3, 5), end='\t\t')
    except Exception as e:
        print(e, end='\t\t')


"""
Задача 2: Лямбда-Функции
Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def. Например, возведение числа в квадрат
"""


def square(x):
    return x ** 2


data = [3, 7, 4, 11]
print('\n\nЗадача 2 лямбда\n', [square(x) for x in data])
square_lambda = lambda x: x ** 2
print([square_lambda(num) for num in data])

"""
Задача 3: Вызываемые Объекты
Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь прямоугольника, то есть a*b.
"""

class Rect:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, *args, **kwargs):
        return self.a * self.b

    def __str__(self):
        return f'Стороны прямоугольника: {self.a}, {self.b}'


rect = Rect(4, 5)
print(f'\nЗадача 3: Вызываемые объекты\n{rect} \nПлощадь : {rect()}')