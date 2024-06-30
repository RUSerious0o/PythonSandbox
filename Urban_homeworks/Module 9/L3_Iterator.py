"""
Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне. При создании и инициализации объекта этого класса создаются атрибуты:
start – начальное значение (если значение не передано, то 0)
end – конечное значение (если значение не передано, то 1)
"""

class EvenNumbers:
    def __init__(self, start=0, end=1):
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError('Int needed')

        if start > end:
            raise ValueError('End must be greater than Start')

        self.start, self.end, self.current = start, end, start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        result = self.current
        self.current += 2

        if result > self.end:
            raise StopIteration
        else:
            if result % 2 == 0:
                return result
            else:
                return result + 1


numbers = EvenNumbers(-4, 31)
for number in numbers:
    print(number, end=' ')
print()

numbers = EvenNumbers(-5, 20)
for number in numbers:
    print(number, end=' ')
print()

numbers = EvenNumbers()
for number in numbers:
    print(number, end=' ')
print()

numbers = EvenNumbers(1, 2)
for number in numbers:
    print(number, end=' ')
print()