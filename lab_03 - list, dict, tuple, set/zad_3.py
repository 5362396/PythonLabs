user_input = input('Wpisz tekst, a wyświetlę z niego unikalne znaki: ')
unique = sorted(set(user_input.lower()))
print(unique)
