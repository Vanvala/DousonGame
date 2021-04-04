# Игра викторина, надо ответить на вопросы из текстового файла
import sys, shelve

def open_file(file_name, mode):
    """открывает файл"""
    try:
        the_file = open(file_name, mode,  encoding='utf-8')
    except IOError as e:
        print(f'Невозможно открыть файл {file_name}. Работа будет завершена', e)
        input('Нажмите Ввод, чтобы выйти')
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Возвращает отформатированную очередную строку"""
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line

def next_block(the_file):
    """Возвращает отформатированную очередную блок данных"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    score = next_line(the_file)

    return category, question, answers, correct, explanation, score

def welcome(title):
    """Приветствует и сообщает тему"""
    print('\t\tДобро пожаловать в игру викторина')
    print("\t\t", title, "\n")


def save_score(name,  scores):
    s = shelve.open('score')
    s[name] = scores
    s.close()


def save_score_txt(name, scores):
    with open('score.txt', 'a') as file:
        file.write(f'\n{name} - {scores}')

def main():
    trivia_file = open_file('trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    scores = 0
    name = input('Введите Ваше имя: ')
    # Извлечение первого блока
    category, question, answers, correct, explanation, score = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category, '\n', question)
        for i in range(4):
            print(f'\t\t{i+1} - {answers[i]}')
        print(f'Этот вопрос стоит {score}')
        # получение ответа
        answer = input('Ваш ответ: ')
        if answer == correct:
            print('Da!', end='')
            scores += int(score)
        else:
            print('Нет!', end='')
        print(explanation)
        print(f'Вы набрали {scores} очков')
        category, question, answers, correct, explanation, score = next_block(trivia_file)

    trivia_file.close()
    print(f'Это был последний вопрос. Вы набрали {scores} баллов')
    save_score_txt(name, scores)

main()
input('Нажмите Ввод, чтобы выйти')






