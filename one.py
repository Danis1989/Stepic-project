from random import *

begin, end = 1, 5

res_rand = randint(begin, end)

while end != 0:

    user_num = int(input('Введите число ... '))

    if res_rand == user_num:
        print('Вы угадали, поздравляем!')
        break
    elif res_rand < user_num:
        print('Слишком много, попробуйте еще раз')
        continue
    else:
        print('Слишком мало, попробуйте еще раз')
        continue