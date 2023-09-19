month_days = dict(january=31, february=28, march=31, april=30, may=31, june=30, july=31, august=31, september=30,
                  october=31, november=30, december=31)

month_name = input('Введите название месяца на английском: ')

if month_name not in month_days:
    print('Неверное название месяца.')
else:
    days = month_days[month_name]
    print(f'В месяце {month_name.capitalize()} {days} дней.')
