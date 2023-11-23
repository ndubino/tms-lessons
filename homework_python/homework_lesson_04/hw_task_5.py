# Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //

number = int(input("Введите произвольное число: "))

sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

print("Сумма цифр числа:", sum_of_digits)
