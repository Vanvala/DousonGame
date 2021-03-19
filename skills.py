# Прога "Генератор персонажа". Создаём персонажа, распределяем умения

skills = [[0,'Сила'], [0,'Здоровье'], [0,'Мудрость'], [0,'Ловкость']]
SCORE = 30

print('Ваш персонаж обладает силой, здороьем, мудростью, ловкостью. Вам надо распределить 30 баллов между этими качествами\n')
print('Нажмите 0, чтобы выйти\n')
print('Нажмите 1, для создания персонажа\n')
print('Нажмите 2, для редактирования\n')

choice = None

while choice != 0:
    choice = int(input('\nВаш выбор: '))

    if choice == 0:
        print('До свидания:')

    if choice == 1:
        print('Создаём персанажа')

        skill_1 = int(input('Сила: '))
        if skill_1 > SCORE:
            print('Больше 30')
            skill_1 = int(input('Сила: '))
            skills[0][0] = skill_1
            print('\nОсталось: ', SCORE - skill_1)
        else:
            skills[0][0] = skill_1
            print('\nОсталось: ', SCORE - skill_1)

        skill_2 = int(input('Здоровье: '))
        if skill_2 + skill_1 > SCORE:
            print('Больше', SCORE - skill_1)
            skill_2 = int(input('Здоровье: '))
            skills[1][0] = skill_2
            print('\nОсталось: ', SCORE - skill_1 - skill_2)
        else:
            skills[1][0] = skill_2
            print('\nОсталось: ', SCORE - skill_1 - skill_2)

        skill_3 = int(input('Мудрость: '))
        if skill_3 + skill_2 + skill_1 > SCORE:
            print('Больше', SCORE - skill_1 - skill_2)
            skill_3 = int(input('Мудрость: '))
            skills[2][0] = skill_3
            print('\nОсталось: ', SCORE - skill_1 - skill_2 - skill_3)

        else:
            skills[2][0] = skill_3
            print('\nОсталось: ', SCORE - skill_1 - skill_2 - skill_3)

        skill_4 = int(input('Ловкость: '))
        if skill_4 + skill_3 + skill_2 + skill_1 > SCORE:
            print('Больше', SCORE - skill_1 - skill_2 - skill_3)
            skill_1 = int(input('Ловкость: '))
            skills[3][0] = skill_1
            print('\nОсталось: ', SCORE - skill_1 - skill_2 - skill_3 - skill_4)

        else:
            skills[3][0] = skill_4
        print('Ваш герой: ', skills)

    if choice == 2:
        print('Редактируем персанажа')

        skill_1 = int(input('Сила: '))
        if skill_1 > SCORE:
            print('Больше 30')
            skill_1 = int(input('Сила: '))
            skills[0][0] = skill_1
            print('\nОсталось: ', SCORE - skill_1)
        else:
            skills[0][0] = skill_1
            print('\nОсталось: ', SCORE - skill_1)

        skill_2 = int(input('Здоровье: '))
        if skill_2 + skill_1 > SCORE:
            print('Больше', SCORE - skill_1)
            skill_2 = int(input('Здоровье: '))
            skills[1][0] = skill_2
            print('\nОсталось: ', SCORE - skill_1 - skill_2)
        else:
            skills[1][0] = skill_2
            print('\nОсталось: ', SCORE - skill_1 - skill_2)

        skill_3 = int(input('Мудрость: '))
        if skill_3 + skill_2 + skill_1 > SCORE:
            print('Больше', SCORE - skill_1 - skill_2)
            skill_3 = int(input('Мудрость: '))
            skills[2][0] = skill_3
            print('\nОсталось: ', SCORE - skill_1 - skill_2 - skill_3)

        else:
            skills[2][0] = skill_3
            print('\nОсталось: ', SCORE - skill_1 - skill_2 - skill_3)

        skill_4 = int(input('Ловкость: '))
        if skill_4 + skill_3 + skill_2 + skill_1 > SCORE:
            print('Больше', SCORE - skill_1 - skill_2 - skill_3)
            skill_1 = int(input('Ловкость: '))
            skills[3][0] = skill_1
            print('\nОсталось: ', SCORE - skill_1 - skill_2 - skill_3 - skill_4)

        else:
            skills[3][0] = skill_4
        print('Ваш герой: ', skills)

input('\n\nНажмите Ввод, чтобы выйти')


