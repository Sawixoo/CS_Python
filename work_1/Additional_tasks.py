

def fourteenth_task():        # Дополнительные задачи
    x = float(input('Введите X: '))
    if not x < 0:
        if x >= 1:
            y = 4 * x - 1
        else:
            y = 2 * x + 1
    else:
        y = x**2 + 1
    return f'Y = {y}'


def fifteenth_task():
    a = float(input('Введите А: '))

    if not a == 0:
        c = 3 / a
        if a > 0:
            return 'X < c'
        else:
            return 'X > c'
    else:
        return 'X - Любое'


def sixteenth_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    if a != 0:
        return f'Уравнение имеет один корень b / a = { b / a}'
    else:
        if b != 0:
            return 'Любое число корень уравнения'
        else:
            return 'Уравнение не имеет корней'


def seventeenth_task(a, b):
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))

    if a == 0:
        if b == 0:
            return 'x - любое'
        else:
            return 'Решений нет'
    else:
        c = b / a
        if a > 0:
            return 'X > c'
        else:
            return 'X < c'


def eighteenth_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    c = float(input('Введите C: '))
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    return f'min = {min}'


def nineteenth_task():
    st = float(input('Введите st: '))

    if st < 5:
        zp = 130
    else:
        if st <= 15:
            zp = 180
        else:
            zp = 180 + (st - 15) * 10
    return f'ZP = {zp}'


def twentieth_task():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    x = float(input('Введите X: '))
    if x < 10:
        y = x + a
    else:
        if x <= 23:
            y = x + b
        else:
            y = x + a**2
    return f'Y = {y}'


def twenty_first_task(a, b, c):
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    c = float(input('Введите C: '))
    if a > c:
        return 'Кошка не подходит'
    else:
        if c <= b:
            return 'Кошка подходит'
        else:
            return 'Кошка не подходит'


def twenty_second_task(a, b, c, x, y):
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    c = float(input('Введите C: '))
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))
    if a > b:
        r = a
        a = b
        b = r
    if b > c:
        r = b
        b = c
        c = r
    if a > b:
        r = a
        a = b
        b = r
    if x > y:
        r = x
        x = y
        y = r
    if a < x and b < y:
        return 'Пройдет'
    else:
        return 'Не пройдет'
