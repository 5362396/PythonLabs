import zad_4

english_months_names = ['January', 'February', 'March', 'April',
                        'May', 'June', 'July', 'August',
                        'September', 'October', 'November', 'December']
english_months = dict()

for i in range(12):
    english_months[i+1] = english_months_names[i]

print(english_months)

months = {
    'pl': zad_4.polish_months,
    'en': english_months,
}

print(months['pl'][4], months['en'][4])
