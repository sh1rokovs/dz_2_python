def div(*args):
    # arg1 = int(input('Добавить Делимое '))
    # arg2 = int(input('Добавить делитель '))
    arg1 = 3
    arg2 = 4
    if arg2 != 0:
        return arg1 / arg2
    else:
        print('Неправильные числа')


print(f'Результат {div()}')
