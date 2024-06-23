import datetime


class StringDataError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'У меня плохое настроение, строки не принимаю!'


class SubtractionError(Exception):
    def __get_weekday(self):
        weekday = datetime.date.today().weekday()
        if weekday == 0:
            return 'понедельник'
        if weekday == 1:
            return 'вторник'
        if weekday == 2:
            return 'среда'
        if weekday == 3:
            return 'четверг'
        if weekday == 4:
            return 'пятница'
        if weekday == 5:
            return 'суббота'
        if weekday == 6:
            return 'воскресенье'

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Отнять не получится, ведь сегодня {self.__get_weekday()}'


class NotImplementedYetError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Извините, функционал {self.data} пока не реализован'

def calc(*args, operation):
    if operation == '-':
        raise SubtractionError(operation)

    if not isinstance(operation, str):
        raise TypeError('Оператор нужен в виде строки')

    if operation == '+':
        try:
            return sum(args)
        except:
            result = ''
            for item in args:
                result += str(item)
            return result

    raise NotImplementedYetError(operation)


for operation in ('-', '+', '*', '/'):
    try:
        print(calc(2, 4, operation=operation))
    except Exception as e:
        print(e)

    try:
        print(calc(2, '4', operation=operation))
    except Exception as e:
        print(e)
    finally:
        print()

try:
    print(calc(2, 4, operation=4))
except Exception as e:
    print(e)
