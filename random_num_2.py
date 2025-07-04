from random import *

print('Добро пожаловать в числовую угадайку')  # Приветстсвие игрока.


def boun_n(arg):  # Фун-я boun_n. Является ли число цифрой, а не
    return arg.isdigit() and int(arg) > 1  # буквой или символом, больше 1.


def is_valid(arg):
    return arg.isdigit() and 1 <= int(arg) <= boun_num  # Фун-я is_valid. Является ли число цифрой, а не
    # буквой или символом, в диапазоне от 1 до 100.


cnt = 0  # Подсчет попыток игрока.

while True:  # Бесконечный цикл.
    boun_num = input('Введите число, большее единицы для обозначения границы выбора случайного числа ... ')

    if boun_n(boun_num):  # Если фун-я boun_n Истина, то число для обозначения границы выбора
        boun_num = int(boun_num)  # из str переводим в int.
        break                     # Выходим из цикла.
    else:
        print('Введенное вами значение должно быть целым числом не меньше 2-х')

musterys_num = randint(1, boun_num)  # Загадываестя рандомное, неизвестное число
# которое игрок должен угадать.

while True:

    user_num = input('Введите число которое вы загадали ... ')  # Число вводимое пользователем.

    if is_valid(user_num):  # Если фун-я is_valid Истина, число пользователя
        user_num = int(user_num)  # из str преоб. в int.

        if user_num == musterys_num:  # Если число пользователя и рандомное число совпадают.
            cnt += 1
            print(f'Вы угадали, поздравляем! Количество затраченных попыток = {cnt}')  # Вывод результатов игры.
            ansver = input('Желаете начать новую игру?. Для продолжения игры введите "Да" или любой другой ответ для выхода: ... ').lower().strip()
            # Ввод ответа на предложение.
            if ansver != 'да':  # Ответ отрицательный, выходим из программы.
                break
            else:  # Ответ положительный, вновь запр-ся у пользователя граница поиска, загадыватся рандомное число.
                while True:  # Бесконечный цикл.
                    boun_num = input(
                        'Введите число, большее единицы для обозначения границы выбора случайного числа ... ')

                    if boun_n(boun_num): # Если фун-я boun_n Истина, то число для обозначения границы выбора
                        boun_num = int(boun_num) # из str переводим в int.
                        cnt = 0                  # Счетчик сбрасываем.
                        break                    # Выходим из цикла.
                    else:
                        print('Введенное вами значение должно быть целым числом не меньше 2-х')

        elif user_num < musterys_num:  # Если число пользователя меньше рандомного число.
            cnt += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_num > musterys_num:  # Если число пользователя больше рандомного число.
            cnt += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
    else:  # Если число пользователя вне диапазона при проверке фун-ей is_valid.
        cnt += 1
        print(f'А может быть все-таки введем целое число от 1 до {boun_num} включительно?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')  # Прощаемся с игроком.
