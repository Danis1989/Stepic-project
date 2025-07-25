total_num = list(map(int,input('Введите общее кол-во деревьев ... ')[::-1]))
max_deg = max(total_num) + 1 # Для хранения степени числа
nums_user = list(map(str,input('Введите остальные числа через пробел ... ')[::-1].split()))
res_nums_user = 0 # Конечный результат
res_total_num = 0

for i in range(len(total_num)):
    res_total_num += total_num[i] * (pow(max_deg, i))

for j in nums_user:
    for i in range(len(j)):
        res_nums_user += int(j[i]) * (pow(max_deg, i)) # Переводим каждую цифру в степень.


if res_total_num == res_nums_user:
    print(f'{max_deg} проверка пройдена')
else:
    print('Проверка не пройдена')



