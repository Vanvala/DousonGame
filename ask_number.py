# Создаём функцию, к-рая просит внести число из диапозона и кратность

def ask_number(question, low, high):
    """Просит ввести число из диапозона и кратность"""
    response = None
    while response not in range(low, high):
        response = int(input(question))

    return response


# q = ask_number('введите число из диапозона 1 -100:', 1, 101)
# print(q)
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    i = text.find(' ')

    return i


index = first_word("Hiy ")

print(index)

