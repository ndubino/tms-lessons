# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
#
def remove_vowels(input_str):
    def is_vowel(letter):
        return letter in ['a', 'e', 'i', 'o', 'u']

    result = list(filter(lambda letter: not is_vowel(letter), input_str.split()))

    return result

user_input = input("Enter an arbitrary number of small Latin letters separated by a space: ")
result = remove_vowels(user_input)
print(result)