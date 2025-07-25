num_user = list(input('Введите ваше число ... '))[::-1]
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_list = list()  # Для хранения нового набора чисел. Если из входящего потока идут буквы в верхнем регистре.
res = 0 # Конечный результат
max_deg = 0 # Для хранения степени каждого числа

for i in num_user:

    if i in uppercase_letters: # Если есть буква
        new_list += [uppercase_letters.index(i) + 10] # Переводим букву в число. Добавляем в список.
    else:
        new_list += [int(i)] # Если цифра. Добавляем в список без дополнительных манипуляций.
    max_deg = max(new_list) # Находим максимальную цифру для степени.

for j in range(len(new_list)):
    res += new_list[j] * (pow(max_deg, j)) + 1 # Переводим каждую цифру в степень.
print(res)
