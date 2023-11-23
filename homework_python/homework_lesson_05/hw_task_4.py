# Напишите функцию get_longest_word, которая на вход принимает текст
# (только английские слова и пробелы), и возвращает самое длинное слово из этого текста.
# Для разбиения строки на слова используйте функцию split.

def get_longest_word(text):
    words = text.split()
    if not words:
        return None
    longest_word = max(words, key=len)
    return longest_word


text = 'hello this is a string with words and spaces and big big woooooooooord'
result = get_longest_word(text)
print('The longest word is:', result)
