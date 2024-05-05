def get_password(num):
    result = ''
    for first_num in range(1, num // 2 + 1):
        for second_num in range(2, num + 1):
            if first_num == second_num:
                continue

            if num % (first_num + second_num) == 0:
                result += str(first_num) + str(second_num)

    return result


for num in range(3, 21):
    print(num, get_password(num))