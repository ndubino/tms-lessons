# Напишите функцию get_most_frequent_word, которая на вход принимает текст
# (только английские слова и пробелы), и возвращает самое часто встречающееся слово.
# Если таких слов несколько - верните любое.


def get_most_frequent_word(text):
    words = text.split()
    word_count = {}

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_frequent_word = max(word_count, key=word_count.get)

    return most_frequent_word


text = 'hello this is a string with words and spaces and big big woooooooooord and and and.'
result = get_most_frequent_word(text)
print('The most frequent word is:', result)