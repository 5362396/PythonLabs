def split_surnames(surnames: list) -> None:
    a_m = []
    n_z = []
    for surname in surnames:
        if surname[0].upper() <= 'M':
            a_m.append(surname)
        else:
            n_z.append(surname)

    with open('A-M_nazwiska.txt', 'w', encoding='utf-8') as file:
        for i in a_m:
            file.write(i + '\n')
    with open('N-Z_nazwiska.txt', 'w', encoding='utf-8') as file:
        for i in n_z:
            file.write(i + '\n')


split_surnames(['Nowak', 'Kowalski', 'Wiśniewski', 'Kamiński', 'Lewandowski', 'Zieliński'])
