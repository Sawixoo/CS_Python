from math import sqrt


def twelfth_task(q):              # Цикл с постусловием
    s = 0
    i = 1

    while True:
        s = s + i
        i += 1

        if s > q:
            break
    return f'i - 2 = {i - 2}'


def thirteenth_task():
    n, i, s = 3, 1, 0

    while True:
        s = s + (3 * i + 2)
        i += 1

        if not i <= n:
            break
    return f'S = {s}'
