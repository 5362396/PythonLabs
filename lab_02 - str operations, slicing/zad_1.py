user_input = input("Napisz kilka słów przedzielonych wybranym przez siebie separatorem: ")
source_separator = input("Napisz jakiego separatora użyłeś/aś: ")
target_separator = input("Napisz na jaki separator chcesz go zmienić: ")

user_input.strip()
source_separator.strip()
target_separator.strip()

# pierwsza metoda
input_split = user_input.split(source_separator)
print(target_separator.join(input_split))

# druga metoda
print(user_input.replace(source_separator, target_separator))
