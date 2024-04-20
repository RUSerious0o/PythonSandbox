immutable_var = 'some', 'list', 'of', 'constant', 'expressions', 1, 3
print(immutable_var)
# immutable_var[2] = 'new string'   # ошибка: нельзя менять элементы кортежа, если за ними нет изменяемого объекта
mutable_list = 'This list can not be changed'.split(' ')
word = 'not'
if word in mutable_list:
    mutable_list.remove(word)
print(mutable_list)
