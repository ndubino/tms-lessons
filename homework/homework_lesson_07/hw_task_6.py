# Решите прошлую задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров.
# А также чтобы работало с именованными параметрами.
#
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Входные параметры args: {args}")
        print(f"Входные параметры kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d

y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')
