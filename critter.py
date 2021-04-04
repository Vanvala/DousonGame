# Моя зверюшка. Виртуальный питомец, о к-ром можно позаботиться

class Critter:

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += f'Имя {self.name}, уровень голода: {self.hunger}, уровень уныния: {self.boredom}'
        self.__pass_time()
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 < unhappiness <= 10:
            m = 'неплохо'
        elif 11 < unhappiness <= 15:
            m = 'не сказать, чтобы хорошо'
        else:
            m = 'ужасно'
        return m

    def talk(self):
        print(f'Привет, меня зовут {self.name}. Чувствую я себя {self.mood}')
        self.__pass_time()

    def eat(self):
        food = int(input('Введите количество еды от 1 до 5: '))
        while food not in range(1, 6):
            print('Введите количество еды от 1 до 5: ')
        print('Урр...Спасибо')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = int(input('Сколько времени вы хотите поиграть? от 1 до 5 ч: '))
        while fun not in range(1, 6):
            print('Сколько времени вы хотите поиграть? от 1 до 5 ч: ')
        print('Уиии')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input('Как вы назовёте зверушку: ')
    crit = Critter(crit_name)
    choice = None
    print(crit)
    while choice != '0':
        print(""" Моя зверушка
        0 - выйти
        1 - узнать о самочувствии зверушки
        2 - покормить зверушку
        3 - поиграть со зверушкой
        4 - секретный путкт
        """)
        choice = input('Ваш выбор: ')
        if choice == '0':
            print('До свидания.')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            food = int(input('Введите количество еды от 1 до 5: '))
            while food not in range(1, 6):
                print('Введите количество еды от 1 до 5: ')
            crit.eat()
        elif choice == '3':
            crit.play()
        elif choice == '4':
            print(crit)
        else:
            print('Извините, такого пунктна в меню нет', choice)


main()
input('Нажмите ввод, чтобы выйти')