# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя. Если он ответил “yes” - завершите
# программу. Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you"
# и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

for number in range(101):
    print(number)
    while True:
        user_input = input("Should we break? ")
        if user_input == "yes":
            exit()
        elif user_input == "no":
            break
        else:
            print("Don't understand you.")