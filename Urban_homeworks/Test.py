# Мысли вслух по поводу вэбинара о первом модуле

# arr_ = [12, 'string', 32]
# # map(str, arr_)
# arr_.extend(set('some symbols  '))
# arr_[5] = 15
# print(arr_)
#
# num_ = 27
# print(type(num_), id(num_))
# num2 = 27
# print(type(num2), id(num2))

# dict_ = {'name': 'yura'}
# dict_.setdefault('name', 'typo')
# print('yura' in dict_, dict_)
#
# set_ = set([1, 2, 3, 4, 5])
# print(set_)
# set_2 = set([2, 3, 4, 6, 7])
# print(set_ & set_2)

# list_ = range(0, 15)
# print(*list_)

# Таблица умножения, второй вэбинар
# def print_mult_table(from_num, to_num):
#     def print_table_string(*args, mult=1):
#         for num in args:
#             print(num * mult, end='\t')
#         print()
#
#     rng = range(from_num, to_num)
#     for i in rng:
#         print_table_string(*rng, mult=i)
#
#
# print_mult_table(1, 17)
