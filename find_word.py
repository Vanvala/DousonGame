import random
# Игра в которой компьютер выбирает слово, а игрок должен его отгадать
WORDS = ('роскомнадзор', 'заблокировать', 'Телеграмботы', 'ведомство', 'создатели', 'правоохранители',
         'администрация', 'запрос', 'деятельность', 'данные', 'слабовик', 'судья')
# Сообщаем сколько букв в слове и даём пять попыток угадать букву в слове
word = random.choice(WORDS)
print(f'Привет, угадай слово из тенденций 2021 года {WORDS}. Даётся 5 попыток узнать букву в слове')
for i in range(5):
    tries = input('\n Пробуйте буквы: ')
    if tries in word:
        print('Да')
    else:
        print("Нет")

guess = input('\nСлово?: ')
correct = word

while guess != correct and guess != '':

