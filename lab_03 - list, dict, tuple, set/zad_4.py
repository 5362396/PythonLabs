polish_months_names = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień',
                 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień',
                 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
polish_months = dict()

for i in range(12):
    polish_months[i+1] = polish_months_names[i]

if __name__ == '__main__':
    print(polish_months)
