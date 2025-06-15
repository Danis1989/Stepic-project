from random import *

left, right = 1, 100

comp_num = randint(left, right)

while left <= right:

    middle = (left + right) // 2

    print(f'middle = {middle} comp_num = {comp_num}')

    if comp_num == middle:
        print('Число угадано )')
        break
    elif middle < comp_num:
        left = middle + 1
    else:
        right = middle - 1



