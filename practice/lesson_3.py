seconds_total = int(input('Кол-во секунд: '))
seconds = seconds_total % 60
minutes = seconds_total // 60 % 60
hours = seconds_total // (60 * 60) % 24
days =  seconds_total // (24 * 60 * 60)
print(str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))
