from math import sqrt


def ninth_tack():                # Цикл с предусловием
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        return f'A = {a}'


def tenth_tack():
    n = float(input('Введите N: '))

    s = 0
    i = 1
    while i <= n:
        s = s + i
        i = i + 2
    else:
        return f'S = {s}'


def eleventh_task():
    i = 0
    i += 1
    p = 1
    while p <= 30:
        p = p * i
        i += 1
    else:
        return f'i = {i}'
