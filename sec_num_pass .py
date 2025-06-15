digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_."
chars = ''

def int_num(b): # Фун-я для перевода вх. параметра в int если параметр число.
    return int(b) if b.isdigit() else print("Введите цифру для ответа") # Вх. параметр число или нет.
    
def yes_no(c): # Фун-я для проверки ответа пользователя. Ввел пользователь да или нет
    return c if c == 'да' or c == 'нет' else print('Для точного ответа введите да или нет ')

def par_true(a):
    if a == 'да':
        a = 1
    return a

while True:
    pass_quan_usr = input("Введите кол-во паролей которое нужно сгенерировать ... ")
    if int_num(pass_quan_usr): # Если параметр число, переводим в int и выходим.
        break

while True:
    len_pass = input("Введите длину одного пароля ... ")
    if int_num(len_pass): # Если параметр число, переводим в int и выходим.
        break

while True:
    dig_yes_or_no = input("Включать ли цифры 0123456789. Введите да/нет ... ").lower()
    if yes_no(dig_yes_or_no):
        break


par_true(dig_yes_or_no)
#if dig_yes_or_no == 'да':
#    dig_yes_or_no = 1

print(dig_yes_or_no)
# while True:
#     dig_yes_or_no = input("Включать ли цифры 0123456789. Введите да/нет ... ").lower()
#     if yes_no(dig_yes_or_no):
#         par_true(dig_yes_or_no)
#
#     low_let_yes_or_no = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz. Введите да/нет ... ").lower()
#     if yes_no(low_let_yes_or_no):
#         par_true(low_let_yes_or_no)
#
#     upper_let_yes_or_no = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ. Введите да/нет ... ").lower()
#     if yes_no(upper_let_yes_or_no):
#         par_true(upper_let_yes_or_no)
#
#     pun_let_yes_or_no = input("Включать ли символы '!#$%&*+-=?@^_.. Введите да/нет ... ").lower()
#     if yes_no(pun_let_yes_or_no):
#         par_true(pun_let_yes_or_no)
#
#     amb_chr_yes_or_no = input("Исключать ли неоднозначные символы il1Lo0O. Введите да/нет ... ").lower()
#     if yes_no(amb_chr_yes_or_no):
#         par_true(amb_chr_yes_or_no)
#         break

#for i in range(pass_quan_usr):