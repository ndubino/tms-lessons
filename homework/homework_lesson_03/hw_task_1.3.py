x = float(input('Введите сумму вклада: '))
y = int(input('Введите количество лет: '))

balance = x * (1.10 ** y)

print('Сумма на счету через', y, 'лет:', balance)
