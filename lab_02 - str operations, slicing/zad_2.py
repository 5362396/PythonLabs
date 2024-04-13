user_input = input("Napisz łańcuch znaków z klawiatury: ")
input_lenght = len(user_input)

# Podział na połowy
index = len(user_input) // 2
first_half = user_input[:index]
second_half = user_input[index:]
print(f"Pierwsza połowa: {first_half}, druga połowa: {second_half}")

# Co drugi znak od końca
print(user_input[::-2])
