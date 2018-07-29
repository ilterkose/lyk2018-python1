
"""
def dovizkuru(dolar):
     return dolar * 4.83

dolarlarim = [54,67.12]

print(list(map(dovizkuru,dolarlarim)))
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
