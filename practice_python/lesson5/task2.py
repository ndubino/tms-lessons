# 5
# Напишите функцию is_palindrome, которая принимает на вход строку
# и возвращает True если это палиндром, иначе False

def is_palindrome():
    s = input()
    return s == s[::-1]

print(is_palindrome())

# 6
# Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка.

def list_sum(lst):
    total_sum = 0
    for i in lst:
        total_sum += i
    return total_sum

print(list_sum([1,2,3,4,5]))

# 7
# Создать функцию sum_and_max, которая принимает на вход неопределенное количество аргументов и возвращает
# их сумму и максимальное из них. Использовать встроенные sum и max разрешено.

# def sum_and_max():
