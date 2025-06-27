while cnt >= 0:

    if par_true(lst[0]) and cnt > 0:
        chars += choice(digits)
        cnt -= 1
    if par_true(lst[1]) and cnt > 0:
        chars += choice(lowercase_letters)
        cnt -= 1
    if par_true(lst[2]) and cnt > 0:
        chars += choice(uppercase_letters)
        cnt -= 1
    if par_true(lst[3]) and cnt > 0:
        chars += choice(punctuation)
        cnt -= 1
    else:
        break

print(*((sample(chars, len_pass))), sep='')

numbers = ['1', '2', '3']
print(type(numbers))
numbers = '.'.join(numbers)
print(numbers)  # Вывод: 1, 2, 3



