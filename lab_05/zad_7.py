def sum_of_points(**punctations: int) -> int:
    return sum(punctations.values())


print(sum_of_points(manchester=94, barca=92, bayern=91, liverpool=88, real=87))
