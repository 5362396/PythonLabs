import csv
import datetime


def format_row(row):
    row[4] = row[4][:-2].replace(",", ".").replace(" ", "")
    date = row[2].split(".")
    row[2] = datetime.datetime(int(date[2]), int(date[1]), int(date[0])).strftime("%Y-%m-%d")

    return row


poland = []
germany = []

with open('zamowienia.csv', newline='', encoding='utf-8', errors='ignore') as file:
    reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
    columns = next(reader, None)
    reader = list(map(format_row, reader))
    for row in reader:
        if row[0] == 'Polska':
            poland.append(row)
        else:
            germany.append(row)

with open('zamowienia_polska.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(columns)
    for wiersz in poland:
        writer.writerow(wiersz)

with open('zamowienia_niemcy.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(columns)
    for wiersz in germany:
        writer.writerow(wiersz)
