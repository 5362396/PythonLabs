from random import choice

col_1 = [
    'Koleżanki i koledzy',
    'Z drugiej strony',
    'Podobnie',
    'Nie zapominajmy jednak, że',
    'W ten oto sposób',
    'Praktyka dnia codziennego dowodzi, że',
    'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
    'Różnorakie i bogate doświadczenia',
    'Troska organizacji, a szczególnie',
    'Wyższe założenia ideowe, a także',
]

col_2 = [
    'realizacja nakreślonych zadań programowych',
    'zakres i miejsce szkolenia kadr',
    'stały wzrost ilości i zakres naszej aktywności',
    'aktualna struktura organizacji',
    'nowy model działalności organizacyjnej',
    'stałe zabezpieczenie informacyjno programowe naszej działalności',
    'wzmacnianie i rozwijanie struktur',
    'konsultacja z szerokim aktywem',
    'rozpoczęcie powszechnej akcji kształtowania postaw',
]

col_3 = [
    'zmusza nas do przeanalizowania',
    'spełnia istotną rolę w kształtowaniu',
    'wymaga sprecyzowania i określenia',
    'pomaga w przygotowaniu i realizacji',
    'zabezpiecza udział szerokiej grupie w kształtowaniu',
    'spełnia ważne zadania w wypracowaniu',
    'umożliwia w większym stopniu tworzenie',
    'powoduje docenianie wagi',
    'przedstawia intersującą próbę sprawdzenia',
    'pociąga za sobą proces wdrażania i unowocześniania',
]

col_4 = [
    'istniejących warunków administracyjno-finansowych.',
    'dalszych kierunków rozwoju.',
    'systemu powszechnego uczestnictwa.',
    'postaw uczestników wobec zadań stawianych przez organizację.',
    'nowych propozycji.',
    'kierunków postępowego wychowania.',
    'systemu szkolenia kadry odpowiadającego potrzebom.',
    'odpowiednich waruknków aktywizacji.',
    'modelu rozwoju.',
    'form oddziaływania.',
]

user_input = int(input("Ile zdań mam wygenerować? Wprowadź liczbę: "))

for n in range(user_input):
    print(f'{choice(col_1)} {choice(col_2)} {choice(col_3)} {choice(col_4)}')
