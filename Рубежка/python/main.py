import random as r
from modul import var1, var2, function3


# Задание 1
def ygadai():
    a = r.randint(0, 21)
    print(a)
    while True:
        ch = int(input("Введите число:"))
        if a == ch:
            print(f'Поздравляю вы угадали!')
            break
        else:
            print(f'Поздравляю вы не угадали!')


# Задание 2
def work_user():
    name = input('Введите имя: ')
    age = int(input("Введите возраст: "))

    if age >= 18:
        print(f'{name}, вам уже больше 18 лет!')
    else:
        print(f'{name}, вам еще меньше 18 лет!')


# задание 3
class Home:
    def __init__(self, n_floors, name, date):
        self.n_floors = n_floors
        self.name = name
        self.date = date

    def __str__(self):
        return f'Количество этажей: {self.n_floors}\nНазвание дома: {self.name}\nГод построения: {self.date}'

# задание 4


def arr_nol():
    arr = [10, 0, 2, 15, 21]

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 'Ноль'

    print(arr)


def main():
    print('Задание 1:')
    ygadai()

    print('Задание 2:')
    work_user()

    print('Задание 3:')
    home = Home('13', 'home 1', '2021')
    print(home)

    print('Задание 4:')
    arr_nol()

    print('Задание 4')
    print(f'{var1}, {var2}, {function3(2, 2, 2)}')


if __name__ == '__main__':
    main()
