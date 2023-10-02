# Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список, состоящий из их квадратов.
# То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*args):
    return [x**2 for x in args]

result = generate_squares(1, 2, 3)
print(result)
