# прога выводит список слов в случайном порядке

from random import choice

lst = ['роскомнадзор', 'заблокировать', 'Телеграмботы', 'ведомство', 'создатели', 'правоохранители',
         'администрация', 'запрос', 'деятельность', 'данные', 'слабовик', 'судья']

while lst:
    word = choice(lst)
    print(word)
    lst.remove(word)
