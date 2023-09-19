month = int(input("Введите номер месяца (от 1 до 12): "))
day = int(input("Введите число (от 1 до 31): "))

valid_date = (month in range(1, 13)) and (day in range(1, 32))

print(valid_date)
