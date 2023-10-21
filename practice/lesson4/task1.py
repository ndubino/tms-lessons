total_sum = 0
for i in range(101):
    total_sum += i
print(total_sum)

total_sum = 0
for i in range(100, 1001):
    total_sum += i
print(total_sum)

total_sum = 0
for i in range(100, 1001):
    if i % 2 == 0:
        total_sum += i
print(total_sum)

total_sum = 1
for i in range(1, 11):
    total_sum *= i
print(total_sum)

total_sum = 1
for i in range(10):
    total_sum *= 2
print(total_sum)


total_sum = 0
last_number = 0

while total_sum <= 1000:
    last_number += 1
    total_sum += last_number

print(total_sum, last_number)
