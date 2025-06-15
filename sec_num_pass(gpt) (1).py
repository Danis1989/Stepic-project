digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_."
chars = ''

def dig_num(a):
    return a.isdigit()

def abc(b):
    if dig_num(b):
        b = int(b)
        return b
    else:
        return print("Введите цифру для ответа")

# while True:
#     pass_quan_usr = input("Введите кол-во паролей которое нужно сгенерировать ... ")
#     if abc(pass_quan_usr):
#         break
#
# while True:
#     len_pass = input("Введите длину одного пароля ... ")
#     if abc(len_pass):
#         break

print(pass_quan_usr, len_pass)


