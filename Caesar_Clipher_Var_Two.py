rus_alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alf = 'abcdefghijklmnopqrstuvwxyz'
res = '' # Окончательный результат.


def right_step(inc_val):
    while True:
        return inc_val if inc_val.isdigit() and int(inc_val) > 0 else right_step(inc_val = input('Для ответа на вопрос введите число больше нуля ... ' ))

def one_or_two(inc_val):
    while True:
        return inc_val if inc_val in '1' or inc_val in '2' else one_or_two(inc_val = input('Для ответа на вопрос введите 1 или 2 ...'))

def one_lang(inc_val):
    while True:
        return inc_val if inc_val[i in rus_alf for i in inc_val] == 1 else one_or_two(inc_val = input('Слово или предложение должно быть на одном языке ...')) #or inc_val[i in eng_alf for i in inc_val] == True else

flag_user_res = input('Вы хотите зашифровать(1) или дешифровать(2)?. Для ответа введите соответствующую цифру 1 или 2 ... ')
one_or_two(flag_user_res)

user_choice_enc = 'за' if '1' in flag_user_res else 'де'  # В зависимости от ответа пользователя будет сформирован смысл следующего вопроса(*) для него.
sign = '+' if '1' in flag_user_res else '-'  # В зависимости от ответа будет применен + или - в дальнейшем.

user_choice_alf = input(f'{user_choice_enc.title()}шифровать на русском(1), или на английском(2)?. Для ответа введите соответствующую цифру 1 или 2 ... ')  # (*).
one_or_two(user_choice_alf)
language = 'русском' if '1' in user_choice_alf else 'английском'

user_choice_alf = rus_alf if '1' in user_choice_alf else eng_alf  # Выбор между русским и английским алфавитом.

shift_usr = input(f'Для {user_choice_enc}шифровки введите вашу букву,слово или предложение на {language} языке ... ')  # (*)

#user_choice_alf = rus_alf if [i in rus_alf for i in shift_usr] == True else eng_alf

shift_step = input('Введите шаг сдвига (цифра) ... ')
right_step(shift_step)

for i in range(len(shift_usr)):
    int_med_res = ''
    flag = False

    if shift_usr[i].isalpha() != 1:
        res += shift_usr[i]
        continue

    flag = True if shift_usr[i].upper() == shift_usr[i] else flag # Если входящий символ имеет верхний регистр. Flag = True.

    int_med_res = user_choice_alf[eval(''.join(map(str, ('(', user_choice_alf.index(shift_usr[i].lower()), sign, shift_step, ')', '%', len(user_choice_alf)))))]

    # user_choice_alf: Получаем новый индекс в выбранном пользователем алфавите. Eval поможет сделать вычисление формулы записанной ввиде строки.
    # Соединяем(join) в строку(map) данные от пользователя(все данные переводим в тип str).
    # 1.user_choice_alf.index(shift_usr): Узнаем индекс буквы пользователя в алфавите который выбрал пользователь.
    # 2.sign: Знак + или - будет применен в формуле. В зависимости от шифровки или дешифровки.
    # 3.shift_step: Шаг, на который сдвинем вперед или назад букву, которую хотим (за)дешифровать.
    # 4.len(user_choice_alf): Длинна выбранного алфавита.

    res += int_med_res.upper() if flag == True else int_med_res # Если буква перед (де)шифровкой имела верхний регистр то после шифровки новую букву возводим в верхний регистр.

print(res)


