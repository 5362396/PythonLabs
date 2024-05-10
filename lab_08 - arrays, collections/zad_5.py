from array import array
import random


def ten_percent(vals: array) -> list[int | float]:
    vals = sorted(vals)
    return vals[len(vals):len(vals)-int(len(vals)/10)-1:-1]


print(ten_percent(array('i', [random.randint(0, 100) for x in range(100)])))
print(ten_percent(array('f', [1.23, 3.45, 7.89, 5.42, 8.62, 2.54, 3.51, 3.31, 6.22, 5.23,
                              5.24, 4.23, 5.32, 8.78, 9.63, 7.44, 4.74, 7.3, 1.23, 7.42])))
