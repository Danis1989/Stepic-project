from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_."
num_pass = 0  # Подсчет кол-ва паролей для форматир. вывода.

def int_num(b):  # Фун-я для перевода вх.параметра в int если параметр число, число должно быть больше 0.
    usr = input(b)
    return int(usr) if usr.isdigit() and int(usr) > 0 else print("Введите цифру для ответа, больше 0")  # Вх. параметр число или нет.

def yes_no(c):  # Фун-я для проверки ответа пользователя. Ввел пользователь да или нет
    while True:
        usr = input(c).lower()
        if usr == 'да' or usr == 'нет':
            return usr
        else:
            print('Для точного ответа введите да или нет ')

def par_true(usr): # Фун-я для проверки положительного ответа пользователя
    return usr if usr != 'нет' else None

while True:
    pass_quan_usr = int_num("Введите кол-во паролей которое нужно сгенерировать ... ")
    if pass_quan_usr:
        break

while True:
    len_pass = int_num("Введите длину одного пароля ... ")
    if len_pass:
        break

def sry(j):
    flag = 
    for i in j:
        if i != 'да':
            print('Один из ответов должен быть положительным')

while True:

    dig_yes_or_no = yes_no("Включать ли цифры 0123456789. Введите да/нет ... ")
    low_let_yes_or_no = yes_no("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz. Введите да/нет ... ")
    upper_let_yes_or_no = yes_no("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ. Введите да/нет ... ")
    pun_let_yes_or_no = yes_no("Включать ли символы '!#$%&*+-=?@^_.. Введите да/нет ... ")
    amb_chr_yes_or_no = yes_no("Исключать ли неоднозначные символы il1Lo0O. Введите да/нет ... ")

    lst = [dig_yes_or_no, low_let_yes_or_no, upper_let_yes_or_no, pun_let_yes_or_no]


# else:
#     break


# if par_true(amb_chr_yes_or_no):
#     digits = digits[2:-1]
#     lowercase_letters = lowercase_letters.translate(str.maketrans('', '', 'ijo'))
#     uppercase_letters = uppercase_letters.translate(str.maketrans('', '', 'LO'))
#     punctuation = punctuation[:14]
#
# for i in range(pass_quan_usr):
#     cnt_len_pass = len_pass
#     chars = []
#
#     while True:
#
#         if par_true(lst[0]) and cnt_len_pass > 0:
#             chars.append(choice(digits))
#             cnt_len_pass -= 1
#         if par_true(lst[1]) and cnt_len_pass > 0:
#             chars.append(choice(lowercase_letters))
#             cnt_len_pass -= 1
#         if par_true(lst[2]) and cnt_len_pass > 0:
#             chars.append(choice(uppercase_letters))
#             cnt_len_pass -= 1
#         if par_true(lst[3]) and cnt_len_pass > 0:
#             chars.append(choice(punctuation))
#             cnt_len_pass -= 1
#         elif cnt_len_pass == 0:
#             break
#     num_pass += 1
#
#     shuffle(chars)
#     print(f'Пароль №{num_pass}: ', *chars, sep='')
