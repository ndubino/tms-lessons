# Напишите функцию-декоратор my_decorator, в которую можно обернуть функцию, которая принимает один входной параметр.
# Ваш декоратор должен будет выводить в консоль входной параметр оборачиваемой функции, запускать функцию,
# а затем выводить результат этой функции.
#
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Входной параметр: {args}')
        result = func(*args, **kwargs)
        print(f'Результат: {result}')
        return result
    return wrapper

@my_decorator
def my_func(x):
    return x ** 2

y = my_func(4)
print(f'y = {y}')
