from typing import Union


def double_sorted(vals: list[Union[int, str]], reversed: bool = False) -> list[Union[int, str]]:
    return sorted(vals, key=lambda x: (isinstance(x, str), x), reverse=reversed)


print(double_sorted([5, 21.37, '6', 'test', 1, -1, '3.33', 'ala', 'ma', 'kota']))
print(double_sorted([5, 21.37, '6', 'test', 1, -1, '3.33', 'ala', 'ma', 'kota'], True))
