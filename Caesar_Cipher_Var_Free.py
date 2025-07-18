shift_usr = input().split()
user_choice_alf = 'abcdefghijklmnopqrstuvwxyz'
final_res= '' # Окончательный результат.

def not_in_alf(inc_val): # Функция для пропуска и неучастия в проверке или сдвиге всех небуквенных значений(символы и цифры)
    return inc_val.isalpha() != True

for i in shift_usr:
    step_len = 0 # Для формирования шага, для каждого слова отдельно.
    for k in i:
        if not_in_alf(k) == 0:# Подсчет кол-ва букв(исключая символы) в каждом отдельном слове.
            step_len += 1
    for j in i:
        int_med_res = '' # Переменная для временного хранения проверяемых значений.
        flag_upper = False # Флаг для сигнала о том что проверяемое значение находится в верхнем регистре.


        if not_in_alf(j): # Если значение символ или цифра, то оно не участвует в проверках. В дальнейшем будет прибавлено к конечному результату.
            final_res += j
            continue

        flag_upper = True if j.upper() == j else flag_upper # Если входящее значение имеет верхний регистр. flag_upper = True.

        int_med_res = user_choice_alf[eval(''.join(map(str, ('(', user_choice_alf.index(j.lower()), '+', step_len, ')', '%', len(user_choice_alf)))))]

        final_res += int_med_res.upper() if flag_upper == True else int_med_res # Если буква перед (де)шифровкой имела верхний регистр, то после шифровки новую букву возводим в верхний регистр.
    final_res +=' '

print(final_res)
