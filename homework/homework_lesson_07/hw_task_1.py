# Пользователь вводит произвольное количество латинских букв через пробел. Буквы могут быть как в верхнем, так и в
# нижнем регистре (на результат работы это влиять не должно).
# Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей.
# В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
# Выведите результат работы функции на экран.
#

def map_to_tuples(input_str):
    letters = input_str.split()
    result = [(letter.upper(), letter.lower()) for letter in letters]
    return result


user_input = input("Enter an arbitrary number of Latin letters separated by a space.: ")
result = map_to_tuples(user_input)
print(result)
