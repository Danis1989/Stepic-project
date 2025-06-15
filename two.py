from random import *

left, right = 1, 100

while left != 0:
    middle = (left + right) // 2
    #user_num = int(input("Введите число ... "))
    user_num = randint(left,right)
    print(user_num)

    if middle == user_num:
        print('Вы угадали )')
        break
    elif middle < user_num:
        left = middle + 1
        continue
    else :
        right = middle - 1
        continue