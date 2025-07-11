from random import *

n = int(input())

left = 1
count = 0

user_num = randint(left, n)

while left <= n:
    middle = (left + n) // 2

    if user_num == middle:
        count += 1
        break

    elif middle < user_num:
        left = middle + 1
        count += 1
    else:
        n = middle - 1
        count += 1

print(count)
