string = "GNU/Linux 2018"

for derya in string:
    print(derya)

matris = [
    [1,2],
    [4,5]
]

print(matris)

for row in matris:
    for column in row:
        print(column)

for i in range(len(matris)):
    row = matris[i]
    for j in range(len(row)):
        print(row[j])


string = "9. Mustafa Akgül Özgür Yazılım Yaz Kampı!"
string2 = "klsajfhlaskşfjasşlkfjalk"
print(string,string2)
print(string + string2)

deneme = "ilter köse"
print(" | ".join(deneme))

sozluk = {'anahtar': 'veri',
          'anahtar1': 'icveri1',
          'anahtar2': {'icanahtar', 'icveri'}}
for eleman in sozluk.items():
    print(eleman[0],eleman[1])

for anahtar in sozluk.keys():
    print(anahtar)


for veri in sozluk.values():
    print(veri)
    if type(veri) == dict:
        for icveri in veri.values():
            print(" {} bu ic veri".format(icveri))
    elif type(veri) == list:
        for iclist in veri:
            print("{} bu da içteki list".format(iclist))



sozluk_updates = {'adilcan': 1}
sozluk.update(sozluk_updates)
print(sozluk)
sozluk_updates = {'adilcan': 32}
sozluk.update(sozluk_updates)
print(sozluk)
print(sozluk.get("adilcan","yok"))
print(sozluk.get("orcun","yok"))
print(sozluk.get("orcun"))

keyne = None
verine = 32

for i in sozluk.items():
    if i[1] == verine:
        keyne = i[0]
print(keyne)

print(sozluk.pop("adilcan"))
print(sozluk)
print(sozluk.popitem())
print(sozluk)
print(sozluk.clear())
print(sozluk)