from timeit import timeit

setup = """
from collections import deque
kolejka = deque('Ala ma kota'.split())
"""

stmt1 = """
for x in range(30_000):
    kolejka.append('?')
"""

stmt2 = """
for x in range(30_000):
    kolejka.appendleft('Czy')
"""

print('Deque - Append: ', timeit(stmt1, setup, number=10))
print('Deque - AppendLeft: ', timeit(stmt2, setup, number=10))

setup = """
lista = 'Ala ma kota'.split()
"""

stmt1 = """
for x in range(30_000):
    lista.append('?')
"""

stmt2 = """
for x in range(30_000):
    lista.insert(0, 'Czy')
"""
print('List - Append: ', timeit(stmt1, setup, number=10))
print('List - Insert: ', timeit(stmt2, setup, number=10))
