user_input = input('Wprowadź dowolną wartość: ')

try:
    int(user_input)
    print('Podana wartość jest rzutowalna na typ int')
except ValueError:
    print('Podana wartość nie jest rzutowalna na typ int')

try:
    float(user_input)
    print('Podana wartość jest rzutowalna na typ float')
except ValueError:
    print('Podana wartość nie jest rzutowalna na typ float')
