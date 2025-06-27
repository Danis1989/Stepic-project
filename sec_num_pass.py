from random import *
from random import shuffle

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_."
chars = ''



def int_num(b): # Фун-я для перевода вх. параметра в int если параметр число.
    usr = input(b)
    return int(usr) if usr.isdigit() else print("Введите цифру для ответа") # Вх. параметр число или нет.

def yes_no(c): # Фун-я для проверки ответа пользователя. Ввел пользователь да или нет
    while True:
        usr = input(c).lower()

        if usr == 'да' or usr == 'нет':
            return usr
        else:
            print('Для точного ответа введите да или нет ')

def par_true(a):
    usr = a
    return usr if usr == 'да' else None

while True:
    pass_quan_usr = int_num("Введите кол-во паролей которое нужно сгенерировать ... ")
    if pass_quan_usr:
        break

while True:
    len_pass = int_num("Введите длину одного пароля ... ")
    if len_pass:
        break

dig_yes_or_no = yes_no("Включать ли цифры 0123456789. Введите да/нет ... ")
low_let_yes_or_no = yes_no("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz. Введите да/нет ... ")
upper_let_yes_or_no = yes_no("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ. Введите да/нет ... ")
pun_let_yes_or_no = yes_no("Включать ли символы '!#$%&*+-=?@^_.. Введите да/нет ... ")
#amb_chr_yes_or_no = input("Исключать ли неоднозначные символы il1Lo0O. Введите да/нет ... ")

lst = [dig_yes_or_no, low_let_yes_or_no, upper_let_yes_or_no, pun_let_yes_or_no]


for i in range(pass_quan_usr):
    cnt = len_pass
    chars = ''

    while cnt >= 0:

        if par_true(lst[0]) and cnt > 0:
            chars = choice(digits) + chars
            #chars.append(choice(digits))
            cnt-=1
        if par_true(lst[1]) and cnt > 0:
            chars = choice(lowercase_letters) + chars
            #chars.append(choice(lowercase_letters))
            cnt-=1
        if par_true(lst[2]) and cnt > 0:
            chars = choice(uppercase_letters) + chars
            #chars.append(choice(uppercase_letters))
            cnt-=1
        if par_true(lst[3]) and cnt > 0:
            chars = choice(punctuation) + chars
            #chars.append(choice(punctuation))
            cnt-=1
        else:
            break

    #print(shuffle(chars))
    chars = shuffle(list(chars))
    print(chars)
    print(type(chars))




