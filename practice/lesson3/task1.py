total_second = int(input('Кол-во секунд? '))
seconds = total_second % 60
minutes = total_second // 60 % 60
hours = total_second // 360 % 24
days = total_second // 360 * 24
print(str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))