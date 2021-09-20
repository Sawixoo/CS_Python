from math import sqrt


def first_task(a, b):
    c = a
    a = b
    b = c
    return f'A = {a} | B = {b}'


def second_task(a, b):
    y = sqrt(a**2 + b**2)
    p = y + a + b
    return f'P = {p}'


def third_task(a, b, c):
    s = a + b
    s = s + c
    return f'S = {s}'


def fourth_task(a, b):
    g = sqrt(a * b)
    return f'G = {g}'
