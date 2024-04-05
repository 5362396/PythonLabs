from random import choice


def wheel_of_fortune():
    passwords = []
    with open('filmy.txt', 'r', encoding='utf-8', newline='') as file:
        for line in file:
            passwords.append(line.replace('\r', '').replace('\n', ''))
    password = choice(passwords)
    correct_letters = []

    while True:
        print(correct_letters)
        display = ''
        for letter in password:
            if letter in correct_letters or letter.lower() in correct_letters or letter == ' ':
                display += letter
            else:
                display += '_'
        print(f'{display}\nWprowadź literę lub hasło')
        user_input = input()
        if len(user_input) > 1:
            if user_input.lower() == password.lower():
                print(f'Wygrałeś, hasło to: {password}')
                break
            else:
                print('Hasło jest nie poprawne')
        else:
            if user_input.lower() in password.lower():
                correct_letters.append(user_input.lower())
            elif user_input in password:
                correct_letters.append(user_input)
            else:
                print('Hasło nie zawiera tej litery.')

            if len(correct_letters) == len(password.strip(' ')):
                print('Brawo, zgadłeś hasło po literkach.')
                break


wheel_of_fortune()
