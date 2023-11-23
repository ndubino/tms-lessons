# Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.

for number in range(101):
    print(number)
    user_input = input("Should we break? ")
    if user_input == "yes":
        break
