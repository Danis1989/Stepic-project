rus_alf = 'абвгдеежзийклмнопрстуфхцчшщъыьэюя'
eng_alf = 'abcdefghijklmnopqrstuvwxyz'
user_choice_alf = None
usr = 'Привеgg'

for i in range(len(usr)):


    if usr[i] in rus_alf:
        user_choice_alf = rus_alf
    elif usr[i] in eng_alf:
        user_choice_alf = eng_alf

    print(user_choice_alf)
