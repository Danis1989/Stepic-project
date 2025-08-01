from random import choice

answers = [
    'Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай',
    'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
    'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
    'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
    'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'
]

print('Привет, Мир! Я магический шар, и я знаю ответ на любой твой вопрос.\n')

user_name = input('Как тебя зовут? ... ')
print(f'Привет, {user_name}!\n')

def not_yes_no(arg):
    return arg.lower() not in ('да', 'нет')

while True:
    qwest2 = input(f'{user_name}, желаете ли вы задать вопрос? Да/Нет ... ').lower()
    while not_yes_no(qwest2):
        qwest2 = input(f'{user_name}, ответьте точнее, да или нет ... ').lower()
    if qwest2 == 'да':
        qwest1 = input('Введите ваш вопрос ... ')
        print(choice(answers))
    elif qwest2 == 'нет':
        print('Возвращайся, если возникнут вопросы!')
        break