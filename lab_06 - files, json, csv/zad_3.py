def n_extreme_values(input_list: list[int | float], n: int, maximum: bool = True) -> list:
    if not all([(isinstance(i, (int, float))) for i in input_list]):
        return ['This list does not contain only numbers!']
    else:
        numbers_sorted = input_list.copy()
        numbers_sorted.sort(reverse=maximum)
        return numbers_sorted[:n]


example_list = [64, 12.3, 11, -321, -10, 5.5]
example_list_wrong = [64, 12.3, 11, -321, -10, 'boom', 5.5]
print(n_extreme_values(example_list, 3))
print(n_extreme_values(example_list, 5, False))
print(n_extreme_values(example_list_wrong, 3))
