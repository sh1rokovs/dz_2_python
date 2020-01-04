# name = input('Введите имя')
# surname = input('Введите Фамилию')
# year = int(input('Введите год рождения'))
# city = input('Введите город рождения')
# email = input('Введите email')
# telephone = input('Введите телефон')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Ivanov',
              name='Ivan',
              year='1990',
              city='Syzran',
              email='error@mail.ru',
              telephone='8-903-333-22-87'))
