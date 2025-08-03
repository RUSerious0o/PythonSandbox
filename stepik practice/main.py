import random


def is_yes_no_ugad(num):
    flag = False
    while flag == False:
        number_ugad = int(input())
        if number_ugad == num:
            print('Вы угадали, поздравляем!')
            flag = True
        elif number_ugad < num:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Слишком много, попробуйте еще раз')


flag = True


if __name__ == '__main__':
    while True:
        if flag == True:
            flag = False
        is_yes_no_ugad(random.randint(1, 100))
