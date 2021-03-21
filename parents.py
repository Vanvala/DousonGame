# Программа "Кто твой папа?". Пользователь вводит имя, а прога выдаёт его отца

parent_1 = {'А́йзек Ази́мов': 'Юда Аронович Азимов', 'Жюль Габрие́ль Верн': 'Пьер Верн', 'Рэй Ду́глас Брэ́дбери': 'Леонард Сполдинг Брэдбери',
           'Ро́джер Джо́зеф Желя́зны': 'Юзеф Желязны'}
parents = {'Айзек Айзимов': 'Юда Аронович Азимов', 'Жюль Верн': 'Пьер Верн', 'Рэй Брэдбери': 'Леонард Сполдинг Брэдбери',
           'Роджер Желязны': 'Юзеф Желязны'}

print('Программа "Кто твой папа?", отцы писателей-фантастов')

choice = None
while choice != 0:

    print("""
    0 - Выйти
    1 - Найти имя отца фантаста
    2 - Добавить пару сын - отец
    3 - Изменить имя отца
    4 - Удалить пару 
    """)
    print("\nВот наши фантасты: ")
    for parent in parents.keys():
        print(parent)

    choice = int(input('\nВаш выбор:'))
    if choice == 0:
        print('До свидания:')

    elif choice == 1:

        son = input('\nВведите имя писателя: ')
        if son in parents:
            father = parents.get(son)
            print(f'Отец {son} {parents.get(son)}')
        else:
            print('Увы нет такого писателя в списке')

    elif choice == 2:
        son = input('\nКакого автора вы хотите добавить? ')
        if son not in parents:
            father = input('\nВведите имя отца: ')
            parents[son] = father
            print(f'\nПара {son} - {father} добавлена в список')
        else:
            print('\nТакое имя уже существует.')

    elif choice == 3:
        son = input('\nКакого отца писателя вы хотите исправить?')
        if son in parents:
            father = input('\nВведите имя отца: ')
            parents[son] = father
            print(f'\nИмя отца {son} исправлена')

    elif choice == 3:
        son = input('\nКакого писателя вы хотите удалить? ')
        if son in parents:
            del parents[son]
            print(f'\nПара {son}-{parents.get(son)} удалена')
        else:
            print('Ничем помоч не могу такого автора нет')

    else:
        print('Извините в меню нет такого пункта', choice)

input('\n\nНажмите Ввод, чтобы выйти')
