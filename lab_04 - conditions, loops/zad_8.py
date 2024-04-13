user_input = input('Wprowadź zdanie: ')

print(f'Posortowane długością (rosnąco) wyrazy w zdaniu: {sorted(user_input.split(), key=len)}')
