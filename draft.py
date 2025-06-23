def input_to_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Ошибка: введите число.")

pass_quan_usr = input_to_int("Введите кол-во паролей которое нужно сгенерировать ... ")
print(f"Вы ввели число: {pass_quan_usr} (тип: {type(pass_quan_usr)})")

