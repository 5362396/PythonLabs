from timeit import timeit

setup = """
from array import array
import random
"""

stmt1 = """
tab_of_chars = array('u', ['a' for _ in range(1_000_000)])
"""

stmt2 = """
list_of_chars = ['a' for _ in range(1_000_000)]
"""

stmt3 = """
tab_of_ints = array('i', [random.randint(1, 100) for _ in range(1_000_000)])
"""

stmt4 = """
list_of_ints = [random.randint(1, 100) for _ in range(1_000_000)]
"""

stmt5 = """
tab_of_longs = array('l', [random.randint(1, 100) for _ in range(1_000_000)])
"""

stmt6 = """
list_of_longs = [random.randint(1, 100) for _ in range(1_000_000)]
"""


print('Tablica znaków: ', timeit(stmt1, setup, number=100))
print('Lista znaków: ', timeit(stmt2, setup, number=100))
print('Tablica typu int: ', timeit(stmt3, setup, number=100))
print('Lista typu int: ', timeit(stmt4, setup, number=100))
print('Tablica typu long: ', timeit(stmt5, setup, number=100))
print('Lista typu long: ', timeit(stmt6, setup, number=100))
