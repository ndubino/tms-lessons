# Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
#

def remove_vowels(input_str):
    def is_vowel(letter):
        return letter.lower() in ['a', 'e', 'i', 'o', 'u']

    result = list(filter(lambda letter: not is_vowel(letter), input_str))

    return result

user_input = input("Enter an arbitrary number of small Latin letters separated by a space: ")
result = remove_vowels(user_input)
print(result)