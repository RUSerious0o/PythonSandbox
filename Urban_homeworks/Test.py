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

def func_(list_, num_, str_):
    list_[0] = 10
    num_ = 50
    str_ = 'str'
    new_list = []
    # for item in list_:
    #     new_list.append(item)

    new_list.extend(list_)
    new_list[0] = 20

    print(list_, num_, str_, new_list)


def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def unique_numbers(input_times):
    list_ = []
    for i in range(input_times):
        list_.extend(input().split(' '))

    for item in list_:
        if not item.isnumeric():
            list_.remove(item)

    print(sorted(set(map(int, list_))))


lst_ = [1, 2, 3]
n = 25
s_ = 'string'
func_(lst_, n, s_)
print(lst_, n, s_)
print_params(a=1, b=2)

# help(sorted)
unique_numbers(3)
