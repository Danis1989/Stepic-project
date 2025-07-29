num = int(input('Введите число которое нужно перевести в новое основание ... '))  # Число которое нужно изменить.
new_found = int(input('Введите новое основание ... '))  # Новое основание.
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inter_res = 0  # Промежуточный результат.
final_res = ''  # Финальный результат.


def con_letter(a):  # Функция для перевода числа больше 9- ти в букву.
    return uppercase_letters[a % 10]


while num > 0:

    inter_res = num % new_found

    if inter_res > 9:
        inter_res = con_letter(inter_res)

    num = int(num / new_found)

    final_res += str(inter_res)

print(final_res[::-1])
