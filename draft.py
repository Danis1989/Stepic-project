from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_."
chars = ''

#lsti = randint(int(digits[0]),int(digits[5]))
lsti = []
lsti.append(choice(lowercase_letters))
lsti.append(choice(uppercase_letters))
print(lsti)
#print(digits[-1])

# def yes_no(c): # Фун-я для проверки ответа пользователя. Ввел пользователь да или нет
#     while True:
#         usr = input(c.lower())
#         if usr == 'да' or usr == 'нет':
#             return usr
#         else:
#             print('Для точного ответа введите да или нет ')
#
#
# dig_yes_or_no = yes_no("Включать ли цифры 0123456789. Введите да/нет ... ")
# low_let_yes_or_no = yes_no("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz. Введите да/нет ... ")
# upper_let_yes_or_no = yes_no("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ. Введите да/нет ... ")
# pun_let_yes_or_no = yes_no("Включать ли символы '!#$%&*+-=?@^_.. Введите да/нет ... ")
# amb_chr_yes_or_no = input("Исключать ли неоднозначные символы il1Lo0O. Введите да/нет ... ")
#
# lst = dig_yes_or_no, low_let_yes_or_no, upper_let_yes_or_no, pun_let_yes_or_no
#
# for i in range(len(lst)):
#     print(lst)



