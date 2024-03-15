import sys

print('Wprowadź liczbę całkowitą:')
user_input = int(sys.stdin.readline())
products = list()
multiplier = 1

while user_input > 0:
    digit = user_input % 10
    products.append(str(multiplier) + ' * ' + str(digit))
    multiplier *= 10
    user_input //= 10

sys.stdout.write('Podaną liczbę można zapisać jako: ' + ' + '.join(reversed(products)))
