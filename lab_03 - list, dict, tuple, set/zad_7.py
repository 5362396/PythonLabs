from string import ascii_lowercase, digits

user_input = input('Napisz łańcuch znaków do analizy: ')

input_lowercased = user_input.lower()

letters = len([i for i in input_lowercased if i in ascii_lowercase])
digits = len([i for i in input_lowercased if i in digits])

print(f'W łańcuchu znaków jest {letters} liter ({letters/len(input_lowercased)*100:.2f}%)'
      f' i {digits} cyfr ({digits/len(input_lowercased)*100:.2f}%)')
