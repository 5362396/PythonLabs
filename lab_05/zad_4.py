import math
from typing import Union

Num = Union[int, float]


def row_kwadratowe(a: Num, b: Num, c: Num) -> Num | tuple[Num, Num]:
    delta: Num = b**2 - 4 * a * c
    if delta < 0:
        # brak pierwiastków
        return -1
    elif delta == 0:
        # jeden pierwiastek
        x: Num = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1: Num = (-b - math.sqrt(delta)) / (2 * a)
        x2: Num = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))
