# Анаграммы
#
# Комп выбирает какое-либо слово и хоатически переставляет буквы
# задача игрока одгадать слово
import random
# Создаем последовательность слов
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
# Случайным образом переставляем слова
word = random.choice(WORDS)
# создадим переменную, с которой будем затем сопостовлена версия игрока
correct = word
# создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ""
if word == "питон":
    help_word = 'python'
elif word == "анаграмма":
    help_word = 'jumble'
elif word == "простая":
    help_word = 'simple'
elif word == "сложная":
    help_word = 'complex'
elif word == "ответ":
    help_word = 'answer'
else:
    help_word = 'cup holder'

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
    """
    Добро пожаловать в игру 'Анаграммы' !
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Ввод, не вводя своей версии.)
    Напишите ? для подсказки
    """
)
score = False
print('Вот анаграмма:', jumble)
guess = input('\nПопробуйте отгадать исходное слово: ')
while guess != correct and guess != "":
    if guess == '?':
        print(f' Подсказка: слово на английском {help_word}')
        score = True
    print('К сожалению вы не правы')
    guess = input('\nПопробуйте отгадать исходное слово: ')

if guess == correct:
    if score == True:
        print('Да, именно так! Вы отгадали с подсказкой\n')
    else:
        print('Да, именно так! Вы отгадали без подсказки\n')

print('Спасибо за игру!')
input('\n\nНажмите Ввод, чтобы выйти.')