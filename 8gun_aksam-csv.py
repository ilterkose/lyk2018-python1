import csv

maxlar = []
sayilar =[]
with open("test.csv") as dosya:
    rows = csv.reader(dosya,delimiter=";",quotechar='"')
    for row in list(rows)[1:]:
        if row[3].isnumeric():
            sayi = int(row[3])
            sayilar.append(sayi)
            max_deger = sayilar.index(max(sayilar))
            min_deger = sayilar.index(min(sayilar))

    print("En küçük değeri içeren satır : {}".format(list(rows[max_deger + 1])))
    print("En küçük değeri içeren satır : {}".format(list(rows[max_deger + 1])))
