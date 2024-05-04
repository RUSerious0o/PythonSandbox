def test(*args, num=10, **kwargs):
    if len(args) > 0:
        print(*args, end=' ')
    print(num, end=' ')
    if len(kwargs) > 0:
        print(*kwargs.items(), end=' ')
    print()


def factor_n(num):
    if not isinstance(num, int) or num < 1:
        print('Ошибка ввода')
        return 0

    return factor_n(num - 1) * num if num > 1 else num


test(1, True, 'Правда', 3.14)
test()
test(100, **{'1': 'one', '2': 'two'})
print()

print(factor_n(3))
print(factor_n(5))
print(factor_n(10))
print(factor_n(1))
print(factor_n(-1))
print(factor_n('число'))