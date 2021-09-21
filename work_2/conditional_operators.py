
def task_if_1():
    user_data = int(input("Введите число: "))
    isHappy = True

    if isHappy or user_data == 6:
        print("User is happy")
    elif user_data == 5:
        print("Number is 5")
    elif user_data == 7:
        print("Number is 7")
    else:
        print("User is unhappy")

    if user_data != 5:
        print("Мы на месте")
        if user_data > 6:
            print("Number is bigger than 5")


def task_if_2():
    data = input()
    number = 5 if data == "Five" else 0
    print(number)


def task_if_3():
    a = int(input('Введите А: '))
    b = int(input('Введите В: '))

    if a % 2 == 0:
        print(f'Число {a} (A) является четным')
    elif b % 2 == 0:
        print(f'Число {b} (B) является четным')
    else:
        print('Оба числа не являются четными')


def task_if_4():
    a = int(input('введите число A:'))
    char = input('Введите знак операции:')
    b = int(input('введите число A:'))

    if char == '+':
        print(f'{a} + {b} = {a + b}')
    elif char == '-':
        print(f'{a} - {b} = {a - b}')
    elif char == '/':
        if b != 0: print(f'{a} / {b} = {a / b}')
    elif char == '*':
        print(f'{a} * {b} = {a * b}')
    else:
        print('Неизвестная операция.')


def task_if_5():
    var = 14

    if 10 < var <= 15 and var != 12 or var == 18:
        print(True)
    else:
        print(False)
