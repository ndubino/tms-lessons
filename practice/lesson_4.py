# task 1
i = sum(range(101))

print("1: {}".format(i))

# task 2
i = sum(range(100, 1001))

print("2: {}".format(i))

# task 3
m = 0
for i in range(100, 1001, 2):
    m += i
print(f'3: {m}')

# task 4
m = 1
for i in range(1, 11):
    m *= i
print(f'4: {m}')