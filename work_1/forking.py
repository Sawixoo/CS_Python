from math import sqrt


def fifth_task():                  # Разветвляющийся алгоритм

    x = float(input('Введите X: '))

    if x >= 0:
        y = sqrt(x)
    else:
        y = x**2
    return f'X = {x} | Y = {y}'


def sixth_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    c = float(input('Введите C: '))
    d = b**2 - 4 * a * c
    if d >= 0:
        x1 = ((-b - sqrt(d)) / (2 * a))
        x2 = ((-b + sqrt(d)) / (2 * a))
        return f'X1 = {x1} | X2 = {x2}'
    else:
        return 'Нет решения'


def seventh_task():
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))

    if x == 0:
        return '[Error] division by zero'
    else:
        z = y / x
        return f'X = {x} | Y = {y} | Z = {z}'


def eight_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))

    s = a * b
    if s > 500:
        s = s * 0.9
        return f'S = {s}'
    else:
        return f'S = {s}'

