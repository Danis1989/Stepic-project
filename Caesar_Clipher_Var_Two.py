rus_alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alf = 'abcdefghijklmnopqrstuvwxyz'
final_res= '' # Окончательный результат.

def not_in_alf(inc_val): # Функция для пропуска и неучастия в проверке или сдвиге всех небуквенных значений(символы и цифры)
    return inc_val.isalpha() != True

def right_step(inc_val): # Функция для проверки входящего параметра(шаг). Параметр должен быть числом, больше 0-ля.
    while True:
        return inc_val if inc_val.isdigit() and int(inc_val) > 0 else right_step(inc_val = input('Для ответа на вопрос введите число больше нуля ... ' ))

def one_or_two(inc_val): # Функция для проверки ответа пользователя. Ответ должен быть 1 или 2.
    while True:
        return inc_val if inc_val in '1' or inc_val in '2' else one_or_two(inc_val = input('Для ответа на вопрос введите 1 или 2 ...'))

def one_lang(inc_val): # Функция для проверки вводимого пользователем значения на однородность языка. Русский или английский.
    while True:
        flag_lang = 0
        for j in inc_val.lower():
            if not_in_alf(j):continue
            flag_lang += 1 if j not in user_choice_alf else 0
        if flag_lang == 0:
            return inc_val
        else:
            inc_val = input(f'Слово или предложение должно быть только на {lang_fl} языке ... ')

flag_user_res = one_or_two(input('Вы хотите зашифровать(1) или дешифровать(2)?. Для ответа введите соответствующую цифру 1 или 2 ... '))
sign = '+' if '1' in flag_user_res else '-'  # В зависимости от ответа будет применен + или - в формуле.

user_choice_enc = 'за' if '1' in flag_user_res else 'де'  # В зависимости от ответа пользователя будет сформирован смысл следующих вопросов для пользователя. Каких, отмечено *.
user_choice_alf = one_or_two(input(f'{user_choice_enc.title()}шифровать на русском(1), или на английском(2)?. Для ответа введите соответствующую цифру 1 или 2 ... '))  # *) .
lang_fl = 'русском' if '1' in user_choice_alf else 'английском'

user_choice_alf = rus_alf if '1' in user_choice_alf else eng_alf  # Выбор между русским и английским алфавитом.

shift_usr = one_lang(input(f'Для {user_choice_enc}шифровки введите вашу букву,слово или предложение на {lang_fl} языке ... ') )

shift_step = right_step(input('Введите шаг сдвига (цифра больше 0-ля) ... '))

for i in shift_usr:
    int_med_res = '' # Переменная для временного хранения проверяемых значений.
    flag_upper = False # Флаг для сигнала о том что проверяемое значение находится в верхнем регистре.

    if not_in_alf(i): # Если значение символ или цифра, то оно не участвует в проверках. В дальнейшем будет прибавлено к конечному результату.
        final_res+= i
        continue

    flag_upper = True if i.upper() == i else flag_upper # Если входящее значение имеет верхний регистр. flag_upper = True.

    int_med_res = user_choice_alf[eval(''.join(map(str, ('(', user_choice_alf.index(i.lower()), sign, shift_step, ')', '%', len(user_choice_alf)))))]

    # user_choice_alf: Получаем новый индекс в выбранном пользователем алфавите. Eval поможет сделать вычисление формулы записанной ввиде строки.
    # Соединяем(join) в строку(map) данные от пользователя(все данные переводим в тип str).
    # 1.user_choice_alf.index(shift_usr): Узнаем индекс буквы пользователя в алфавите который выбрал пользователь.
    # 2.sign: Знак + или - будет применен в формуле. В зависимости от шифровки или дешифровки.
    # 3.shift_step: Шаг, на который сдвинем вперед или назад букву, которую хотим (за)дешифровать.
    # 4.len(user_choice_alf): Длинна выбранного алфавита.

    final_res+= int_med_res.upper() if flag_upper== True else int_med_res # Если буква перед (де)шифровкой имела верхний регистр, то после шифровки новую букву возводим в верхний регистр.
#
print(final_res)


