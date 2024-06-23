def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)
    except Exception as e:
        print(f'А у нас тут что-то внезапное: {e}')
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
