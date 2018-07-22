"""
kisiler = { 'ilter' : {'okul':  'ozu'  , 'yas': 20, 'boy':170  }, 'yaren' : { 'okul' : 'ozu', 'yas': 20, 'boy': 150 }}
liste = kisiler.values()
liste = list(liste)
print(liste)

Logical Expressions (mantıksal ifadeler)

and or 

> <  >= <= 

==

!=




if 5 > 4 and 3 > 1:
    print("Buyuk")



x = 5
y = 6

if x > y:
    print("x y'den büyüktür")
else:
    print("değil")


l = [1, 2, 3, 4, 5]

if 2 in l:
    print("Listede 2 var")

if 6 not in l:
    print("6 yok")



dictionary = { "x" : "y" }
print(dictionary.get("z",":)"))


if dictionary.get("z") is None:
    print("z var")
else:
    print("z yok")
    print(dictionary.get("z"))




 # DÖNGÜLER (FOR - WHILE)

#for dongu_degiskeni in veri_seti:
 #  dongu fonksiyonu

isimler = ["burak", "elif", "betül", "Mr.Robot"]

for isim in isimler:
    if isim == "Mr.Robot" :
        print("Git kali kullan")
    else:
        print("Merhaba {}".format(isim))


for i in range(5,24):
    print(i)

for i in range(0, 24, 3):
    print(i)


#WHILE
isimler = ["burak", "elif", "betül", "Mr.Robot"]

sayac = 0

while sayac < len(isimler):
    isim = isimler[sayac]
    if isim != "Mr.Robot":
        print("Merhaba {}".format(isim))
    else:
        soru = input("Kimsin sen? :")
        print("Sana da merhaba {}".format(soru))
    sayac += 1

"""


karakter = "9. Mustafa Akgül Özgür Yazılım Yaz Kampı"
print("Bu cümle {} karakterden oluşmuştur.".format(len(karakter)))

print(karakter.split(" "))

print(karakter.replace("Yaz", "Kış",1 ))


list = ["ilter","ahmet","hatice", "güzel yaren"]
print("|".join(list)