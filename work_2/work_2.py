
def task_1():
    number = 5
    digit = 4.54356876
    word = 'Result'
    boolean = True

    str_num = '5'
    print(word + ': ' + str(number + int(str_num)))
    del number
    number = 7
    print(f'{word}:', number)


def task_2():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num1 *= 5

    print("Result(+):", num1 + num2)
    print("Result(-):", num1 - num2)
    print("Result(/):", num1 / num2)
    print("Result(*):", num1 * num2)
    print("Result(**):", num1 ** num2)
    print("Result(//):", num1 // num2)
    print("Result(%):", num1 % num2)

    word = "Hi"
    print(word * 2)
    word = True


def task_3():
    name = input('Введите фамилию:')
    print(name*3)


def task_4():
    a = float(input('Введите А: '))
    b = float(input('Введите В: '))
    c = float(input('Введите C: '))

    print(f'Сумма: {a+b+c} \nВычитание: {a - b -c} \nДеление: {a / b / c} \n'
          f'Умножение: { a * b *c } \nОстаток при делении: {a % b % c}')


def task_5():
    integer = 5
    digit = 5.12
    str_num = '10'

    print(f'Result: {int(integer) * int(digit) * int(str_num)}')