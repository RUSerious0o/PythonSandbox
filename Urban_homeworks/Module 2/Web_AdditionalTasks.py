import enum


# For # 1
def print_star_triangle(verts):
    rng = range(1, verts + 1)
    for line in rng:
        for j in range(0, line):
            print('*', end='')
        print()


# For # 2
def print_mult_table(from_row, to_row, from_col, to_col):
    def print_table_row(from_col, to_col, mult=1, is_header=False):
        if is_header:
            print('', end='\t')
        else:
            print(mult, end='\t')

        for num in range(from_col, to_col + 1):
            print(num * mult, end='\t')
        print()

    print_table_row(from_col, to_col, is_header=True)
    for mult in range(from_row, to_row + 1):
        print_table_row(from_col, to_col, mult=mult)


# For # 3
def print_nums_triangle(verts):
    current_number = 1
    for i in range(0, verts):
        for j in range(0, i):
            print(current_number, end='\t')
            current_number += 1
        print()


# If # 1
def identify_triangle(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return 'Равносторонний'

    if side_a == side_b or side_b == side_c or side_c == side_a:
        return 'Равнобедренный'

    return 'РаЗносторонний'


# If # 2
def find_mid_value(num_one, num_two, num_three):
    if num_one < num_two < num_three:
        return num_two

    if num_two < num_three < num_one:
        return num_three

    if num_two == num_three:
        return num_two

    return num_one


# If # 3
def mix_colors(color_one, color_two):
    if color_one == color_two:
        if color_one == 1:
            return 'красный'
        if color_one == 2:
            return 'синий'
        if color_one == 0:
            return 'желтый'

    if color_one + color_two == 3:
        return 'фиолетовый'
    if color_one + color_two == 1:
        return 'оранжевый'
    if color_one + color_two == 2:
        return 'зеленый'

    return 'непонятный'

# test cases
print_star_triangle(3)
print()

print_mult_table(7, 12, 3, 6)
print()

print_nums_triangle(6)
print()

print(identify_triangle(4, 4, 4))
print(identify_triangle(1, 4, 4))
print(identify_triangle(6, 4, 17))
print()

print(find_mid_value(67, 100, 54))
print(find_mid_value(67, 32, 54))
print(find_mid_value(67, 67, 54))
print(find_mid_value(32, 67, 67))
print(find_mid_value(67, 32, 67))
print()

print('Введите два номера смешиваемых цветов:',
      '1 - Красный',
      '2 - Синий',
      '3 - Желтый',
      sep='\n')

input_is_valid = False
num_one, num_two = 1, 3
wrong_input_msg = 'необходимо ввести два числа (диапазон: 1 -> 3)'

while (not input_is_valid):
    args = input().split()

    if len(args) != 2:
        print(wrong_input_msg)
        continue

    input_is_valid = True
    for arg in args:
        if not arg.isnumeric():
            input_is_valid = False
            print(wrong_input_msg)
            break

    if input_is_valid:
        num_one = int(args[0]) % 3
        num_two = int(args[1]) % 3

print(f'Смешали, получился: {mix_colors(num_one, num_two)}')
