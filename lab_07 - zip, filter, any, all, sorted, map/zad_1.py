from typing import Any


def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), vals))


print(extract_numbers([5, 21.37, '6', 'test', True, False, 1, -1, '3.33']))
