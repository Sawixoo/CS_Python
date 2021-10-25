import random


def black_jack():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
    random.shuffle(deck)

    print('Поиграем в Black Jack')
    counter = 0

    for i in range(2):
        current = deck.pop()
        print(f'Выдана карта с номиналом: {current}')
        counter += current

    while True:
        if counter < 21:
            search = input(f'У вас сейчас {counter} очков\nЖелаете взять карту?( Да | Нет )')
            search = search.lower()

            if search == 'да':
                current = deck.pop()
                print(f'Выдана карта с номиналом: {current}')
                counter += current
            elif search == 'нет':
                print(f'Ваши очки = {counter}. До 21 не хватило {21 - counter} очков')
                break
            else:
                print('[INFO] неизвестная команда')
        elif counter == 21:
            print('Поздравляю Вы победили!')
            break

        elif counter > 21:
            print(f'Вы проиграли!!!\nКоличество ваших очков = {counter}')
            break
    print('Игра завершена!!!')


