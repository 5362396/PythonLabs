import this

user_input = input('Wprowadź zdanie: ')
encoded_text = ''

for char in user_input:
    try:
        encoded_text += this.d[char]
    except KeyError:
        encoded_text += char

print(f'Zakodowane zdanie: {encoded_text}')
