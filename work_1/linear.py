from math import sqrt


def first_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))

    c = a
    a = b
    b = c
    return f'A = {a} | B = {b}'


def second_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))

    y = sqrt(a**2 + b**2)
    p = y + a + b
    return f'P = {p}'


def third_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    c = float(input('Введите C: '))
    s = a + b
    s = s + c
    return f'S = {s}'


def fourth_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))

    g = sqrt(a * b)
    return f'G = {g}'
