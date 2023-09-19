from typing import Tuple, Any

l = int(input("Длинна стороны квадрата: "))
p = l * 4
a = l ** 2
d = l ** 0.5
result: tuple[int, int | Any, Any] = (p, a, d)
print("Периметр, площадь, диагональ квадрата.", result)

