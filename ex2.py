left, right = 1, 100

while left <= right:
    middle = (left + right) // 2
    user_num = int(input("Введите число ... "))

    if middle == user_num:
        print('Вы угадали )')
        break
    elif middle < user_num:
        left = middle + 1
        continue
    else:
        right = middle - 1
        continue
