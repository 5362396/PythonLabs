user_input = input('Wprowadź zdanie: ')

output = [(i, [ord(j) for j in i]) for i in user_input.split(' ')]
print(output)
