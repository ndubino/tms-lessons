def filter_negative_numbers(numbers):
    new_numbers = []
    for num in numbers:
        if num >= 0:
            new_numbers.append(num)
    return new_numbers


print(filter_negative_numbers([1, -2, 3, -4, 5]))  # [1, 3, 5]
print(filter_negative_numbers([1, 0, 100, -5, 4, -100]))  # [1, 0, 100, 4]