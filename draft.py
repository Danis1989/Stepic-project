
# from random import *
# dig_yes_or_no = randint(ord('a'), ord('m'))
# print(chr(dig_yes_or_no))

def int_num(b): # Фун-я для перевода вх. параметра в int если параметр число.
    return int(b) if b.isdigit() else print("Введите цифру для ответа") # Вх. параметр число или нет.

lst = []

for i in 4:
    lst.append(i)

print(lst)
