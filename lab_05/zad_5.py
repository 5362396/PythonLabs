import random


def roll_the_dice() -> list[tuple[str, str]]:
    n: int = int(input("Wprowadź liczbę rzutów kostką: "))
    output: dict = dict()

    for i in range(n):
        spots: int = random.randint(1, 6)
        try:
            output[spots] += 1
        except KeyError:
            output[spots] = 1

    return [(f"oczka: {i}", f"rzutów: {output[i]}") for i in output.keys()]


print(sorted(roll_the_dice()))
