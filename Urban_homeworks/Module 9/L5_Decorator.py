"""
Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
"""

def is_prime(function):
    def wrapper(a, b, c):
        sum = function(a, b, c)
        if sum <= 2:
            raise ValueError('Работаем только с числами > 2')

        sum_is_prime = True
        for i in range(2, sum):
            if (sum % i) == 0:
                sum_is_prime = False
        print(f'the sum of {(a, b, c)} = {sum} is{" " if sum_is_prime else " not "}prime')
        return sum
    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


print(sum_three(3, 5, 7))
print(sum_three(3, 5, 9))
try:
    print(sum_three(0, 0, -2))
except Exception as e:
    print(e)
