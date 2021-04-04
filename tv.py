# Программа-эмулятор пульта управления тв

class Tv:
    def __init__(self, name, channel=0, volume=0):
        self.name = name
        self.channel = channel
        self.volume = volume
        print(f'Телевизор марки {self.name} включён на канале {self.channel}. Громкость {self.volume}')

    def __str__(self):
       return f'Сейчас мы на {self.channel} канале, громкость {self.volume}'

    def change_channel(self):
        change = None
        while change not in range(1, 101):
            change = int(input('Нажмите на канал от 1 до 100: '))
        self.channel = change
        print(f'Вы находитесь на {self.channel} канале')

    def change_volume(self):
        choice = None
        while choice not in range(1,3):
            choice = int(input(f'Нажмите 1, чтобы увеличить громкость, 2 - чтобы уменьшить, сейчас громкость {self.volume}: '))

        if choice == 1:
            change = int(input('На сколько увеличить? '))
            self.volume += change
            if self.volume > 100:
                self.volume = 100
                print('Мы на максимуме')
        elif choice == 2:
            change = int(input('На сколько уменьшать? '))
            self.volume -= change
            if self.volume < 0:
                self.volume = 0
                print('Мы на минимуме')
        else:
            print('Что-то не так(')


def main():
    tv_name = input('Введите марку телевизора:')
    tv = Tv(tv_name)
    choice = None
    print(tv)
    while choice != '0':
        print(""" Телевизор включён
            0 - выйти
            1 - узнать о состоянии телевизора
            2 - переключить канал
            3 - изменить громкость
           
            """)
        choice = input('Ваш выбор: ')
        if choice == '0':
            print('До свидания.')
        elif choice == '1':
            print(tv)
        elif choice == '2':
            tv.change_channel()
        elif choice == '3':
            tv.change_volume()
        else:
            print('Извините, такого пунктна в меню нет', choice)


main()
input('Нажмите ввод, чтобы выйти')

