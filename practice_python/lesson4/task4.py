import random

n = random.randint(1, 5)
while True:
    a = int(input('Guess: '))
    if a == n:
        print('Great!')
        break
    print('Try again')
