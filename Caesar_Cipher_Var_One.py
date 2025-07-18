rus_alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alf = 'abcdefghijklmnopqrstuvwxyz'

final_res = '' # Окончательный результат.
int_med_res = '' # Промежуточный результат.

def not_in_alf(inc_val): # Функция для пропуска и неучастия в проверке или сдвиге всех небуквенных значений(символы и цифры)
    return inc_val.isalpha() != True

def num(inc_val): # Функция для проверки входящего значения(должно быть цифрой больше нуля)
    while True:
        return inc_val if inc_val.isdigit() and int(inc_val) > 0 else num(input('Для ответа на вопрос введите число больше нуля ... ' ))

def one_or_two(inc_val): # Функция для проверки ответа пользователя. Ответ должен быть 1 или 2.
    while True:
        return inc_val if inc_val in '1' or inc_val in '2' else one_or_two(inc_val = input('Для ответа на вопрос введите 1 или 2 ...'))

flag_user_res = one_or_two(input('Вы хотите зашифровать(1) или дешифровать(2)?. Для ответа введите соответствующую цифру 1 или 2 ... '))

user_choice_enc = 'за' if '1' in flag_user_res else 'де'  # В зависимости от ответа пользователя будет сформирован смысл следующего вопроса(*) для него.
sign = '+' if '1' in flag_user_res else '-'  # В зависимости от ответа будет применен + или - в дальнейшем.

shift_usr = input(f'Для {user_choice_enc}шифровки введите вашу букву,слово или предложение на русском или английском языке ... ')  # (*)

shift_step = num(input('Введите шаг сдвига (цифра) больше 0 - ля ... '))


for j in shift_usr:
    flag_upper = False # Флаг для сигнала о том что проверяемое значение находится в верхнем регистре.

    if j == j.upper(): # Если буква равна своему аналогу в верхнем регистре.
        flag_upper, j = True, j.lower() # Получаем сигнал об этом, переводим временно букву в нижний регистр.

    user_choice_alf = rus_alf if j in rus_alf else eng_alf # В зависимости от того буква русская или английская, переменная примет тот или иной алфавит.

    if not_in_alf(j):  # Если значение символ или цифра, то оно не участвует в проверках. В итоге будет прибавлено к конечному результату сразу.
        final_res += j
        continue

    int_med_res = user_choice_alf[eval(''.join(map(str, ('(', user_choice_alf.index(j), sign, shift_step, ')', '%', len(user_choice_alf)))))]

    final_res += int_med_res.upper() if flag_upper == True else int_med_res # Если буква перед (де)шифровкой имела верхний регистр - то после шифровки новую букву возводим в верхний регистр.

print(final_res)



