# Комп выбирает число в диапозоне, а игрок пробует отгадать
import random


def instruction():
    print('\tДобро пожаловать в игрк "Отгадай число"')
    print('\nЯзагадал число от 1 до 100')
    print('Отгадай число за минимальное число попыток')


def ask_number(question, low, high):
    """Просит ввести число из диапозона и кратность"""
    response = None
    while response not in range(low, high):
        response = int(input(question))

    return response


def main():
    instruction()
    the_number = random.randint(1, 101)
    quess = ask_number('Введите число: ', 1, 101)
    tries = 1

    while quess != the_number:
        if quess > the_number:
            print('Меньше!')
        else:
            print("Больше!")
        tries += 1
        quess = ask_number('Введите число: ', 1, 101)
    print(f'вам удалось разгадать число {the_number} за {tries} попыток')
main()
input('\n\nНажмите ввод, чтобы выйти.')


