from functools import reduce
"""
def dovizkuru(dolar):
     return dolar * 4.83

dolarlarim = [54,67.12]

print(list(map(dovizkuru,dolarlarim)))
"""
"""
def hepsinikucult(kelime):
    return kelime.lower()

kelimeler = ["Ahmet","dErYaK","tOLGa"]

kucukkelimeler = list(map(hepsinikucult,kelimeler))
print(kucukkelimeler)


def dovizkuru(para,hangisi):
    if hangisi == 1:
        return para * 4.85
    else:
        return para * 5.65

paralarim = [54,67,12]
hangisi_euro = [1,0,1]

print(list(map(dovizkuru,paralarim,hangisi_euro)))
"""

eski_map = map
eski_filter = filter

def filter(func,liste):
    sonuc = []
    for i in liste:
        if func(i):
            sonuc.append(i)
    return sonuc



def map(func,liste):
    sonuc = []
    for i in liste:
        sonuc.append(func(i))
    return sonuc

kisiler = ["Ahmet","İhsan","Mustafa","Deryak","Tolga"]
sayilar = ["1","2","3","4"]
print(list(map(int,sayilar)))


def abidikgubidikfonksiyon(gubidik):
    return gubidik * 1200

def hello(name):
    return "Hello {}".format(name)

def twist(dansci):
    if dansci == "Deryak":
        return True
    else:
        return False

print(list(filter(twist,kisiler)))

def birlestir(birinci,ikinci):
    print(birinci)
    print(ikinci)
    return birinci + " " + ikinci

saysay = 1
def ucuc(rakam1,rakam2):
    global saysay
    saysay +=1
    print("{asama}. Aşama 1. Parametre: {bir},2. Parametre: {iki} Sonuç:{sonuc}".format(sonuc= rakam1 * rakam2,asama=saysay,bir=rakam1,iki=rakam2))
    return rakam1 * rakam2

rakamlar = [1,2,3,4,5,6,7,8,9]

print(reduce(ucuc,rakamlar))


print(list(reduce(birlestir,kisiler)))