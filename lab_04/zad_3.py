for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j:>4}', end='')
        if j == 1:
            print('|', end='')
    if i == 1:
        print(f'\n{"":=^42}', end='')
    print('')
