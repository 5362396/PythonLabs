wysokosc = int(input('Wprowadź wysokość diamentu - liczbę nieparzystą między 3 a 9 włącznie: '))

if 3 <= wysokosc <= 9 and wysokosc % 2 == 1:
    n = 1
    while n < wysokosc:
        text = 'o' * n
        print(text.center(wysokosc))
        n += 2
    while n >= 0:
        text = 'o' * n
        print(text.center(wysokosc))
        n -= 2
else:
    print('Wprowadzono niedopuszczalną wysokość')
