# Пользователь вводит произвольное количество слов через пробел. Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
# в которой все слова из списка соединены через символ разделитель.
#

from functools import reduce


def my_join(words, separator):
    result = reduce(lambda x, y: x + separator + y, words)
    return result


user_input = input("Введите произвольное количество слов через пробел: ")
words = user_input.split()

separator = input("Введите символ-разделитель: ")

result = my_join(words, separator)
print(result)
