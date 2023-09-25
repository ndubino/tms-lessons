my_list = [0, 5, 10, 146, -15, 24, 17, -150]
zero = False
for i in my_list:
    if i == 0:
        zero = True
        break
if zero:
    print('yes')
else:
    print('no')