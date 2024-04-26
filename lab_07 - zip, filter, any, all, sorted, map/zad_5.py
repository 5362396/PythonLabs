from typing import Callable


def sort_dict(vals: dict[str, list[int]], function: Callable) -> dict[str, list[int]]:
    is_reversed = True
    if function == min:
        is_reversed = False
    return dict(sorted(vals.items(), key=lambda x: function(x[1]), reverse=is_reversed))


ex = {'Jan': [2, 4, 8, 16, 32, 64], 'Paweł': [1, 2, 3, 4, 5], 'Karol': [99]}

print(sort_dict(ex, max))
print(sort_dict(ex, min))
print(sort_dict(ex, sum))
# print(sort_dict(ex, abs))  # nie działa
