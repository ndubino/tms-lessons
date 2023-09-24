# Task 2.2
# Пользователь вводит название месяца на английском. Выведите количество дней в этом месяце (не учитывая
# високосный год).
#
month_days = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

month_name = input("Input name of month: ").lower()

if month_name in month_days:
    days = month_days[month_name]
    print(f"In {month_name.capitalize()} {days} days.")
else:
    print("Incorrect.")