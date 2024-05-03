def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3, 6)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, False, 'что-то']
values_dict = {'a': 4, 'b': 'еще строка', 'c': 8}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['pi', 3.14]
print_params(*values_list_2)            # c=True ==> OK
