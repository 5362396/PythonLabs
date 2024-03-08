name = 'Marianna'
unique_letters = dict.fromkeys(name, 1)
print(unique_letters)

# Czy można w funkcji fromkeys() użyć dynamicznie podawanej wartości dla każdego klucza słownika?
# Samą funkcją nie można, ale robiąc update dicta co wywołanie funkcji można.
unique_letterz = dict()
for index, letter in enumerate(name):
    unique_letterz.update(dict.fromkeys(letter, index))

print(unique_letterz)
