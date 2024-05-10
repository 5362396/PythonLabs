import csv
from collections import namedtuple

with open('zamowienia.csv', newline='', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
    Order = namedtuple('Zamowienie', [x.replace(" ", "_") for x in next(reader, None)])
    lines = []
    for i in range(10):
        lines.append(Order._make(next(reader, None)))
    for j in lines:
        print(j)
