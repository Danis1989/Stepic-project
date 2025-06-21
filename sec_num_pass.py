from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_."
chars = ''

def int_num(b): # Фун-я для перевода вх. параметра в int если параметр число.
    return int(b) if b.isdigit() else print("Введите цифру для ответа") # Вх. параметр число или нет.
    
def yes_no(c): # Фун-я для проверки ответа пользователя. Ввел пользователь да или нет
    c = c.lower()
    return c if c == 'да' or c == 'нет' else print('Для точного ответа введите да или нет ')

def par_true(a):
    if a == 'да':
        return a

while True:
    pass_quan_usr = input("Введите кол-во паролей которое нужно сгенерировать ... ")
    if int_num(pass_quan_usr): # Если параметр число, переводим в int и выходим.
        break

while True:
    len_pass = input("Введите длину одного пароля ... ")
    if int_num(len_pass): # Если параметр число, переводим в int и выходим.
        break

lst = []   

#while True:
for i in pass_quan_usr:
    for i in len_pass:
        dig_yes_or_no = input("Включать ли цифры 0123456789. Введите да/нет ... ")
        if yes_no(dig_yes_or_no):
            if par_true(dig_yes_or_no):
                dig_yes_or_no = randint(ord('1'), ord('9'))
                lst.append(chr(dig_yes_or_no))

        low_let_yes_or_no = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz. Введите да/нет ... ")
        if yes_no(low_let_yes_or_no):
            if par_true(low_let_yes_or_no):
                low_let_yes_or_no = randint(ord('a'), ord('z'))
                lst.append(chr(low_let_yes_or_no))

print(lst)
    # upper_let_yes_or_no = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ. Введите да/нет ... ")
    # if yes_no(upper_let_yes_or_no):
    #     if par_true(upper_let_yes_or_no):
    #         upper_let_yes_or_no = 1

    # pun_let_yes_or_no = input("Включать ли символы '!#$%&*+-=?@^_.. Введите да/нет ... ")
    # if yes_no(pun_let_yes_or_no):
    #     if par_true(pun_let_yes_or_no):
    #         pun_let_yes_or_no = 1

    # amb_chr_yes_or_no = input("Исключать ли неоднозначные символы il1Lo0O. Введите да/нет ... ")
    # if yes_no(amb_chr_yes_or_no):
    #     if par_true(amb_chr_yes_or_no):
    #         amb_chr_yes_or_no = 1

    # break

#for i i




