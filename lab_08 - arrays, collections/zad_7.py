import numpy as np
import random
import time
from collections import Counter, deque


def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())


def spinit(wheel_of_fortune: deque, winning_value: int | str, ticks: int):
    if winning_value not in wheel_of_fortune:
        print('Wygrana wartość nie znajduje się w kole fortuny, podaj istniejącą.')
    else:
        waits = np.logspace(0.0, 1.0, num=ticks) / ticks

        for tick in range(ticks):
            wheel_of_fortune.rotate(random.randint(0, len(wheel_of_fortune)))
            print(f'{wheel_of_fortune}', end='')
            time.sleep(waits[tick])
            print('\r', end='')

        if wheel_of_fortune[0] != winning_value:
            print('\nPrzegrana, kręcimy dalej...')
            time.sleep(3)
            spinit(wheel_of_fortune, winning_value, 100)
        else:
            print('\nWygrana!')


kolo = create_kolo_fortuny(100, 200, 'bankrut', 500, 1000, 'winner')
print(spinit(kolo, 'winner', 100))
