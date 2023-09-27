# Программа загадывает случайное число от 0 до 100. Пользователь пытается угадать, вводя числа. Если пользователь
# угадал - выведите поздравление и завершите программу. Если пользователь не угадал, подскажите ему в в какую сторону
# идти. То есть, если число пользователя слишком большое - выведите “не угадал, число больше загаданного”. Если
# меньше - выведите “не угадал, число меньше загаданного”.

import random

number = random.randint(0, 100)

while True:
    user_guess = int(input("Угадайте число от 0 до 100: "))

    if user_guess == number:
        print("Поздравляем! Вы угадали число:", number)
        break
    elif user_guess < number:
        print("Не угадали, число больше загаданного.")
    else:
        print("Не угадали, число меньше загаданного.")