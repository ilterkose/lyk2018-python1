# TEMEL DOSYA İŞEMLERİ
"""
dosya işelmlerinde belirli bir dosyanın işlenebilmesi içim
"""
"""
dosya = open("ilter.txt","w")
dosya.write("sa biz geldik!")

with open("köse.txt","w") as dosya2:
    dosya2.write("deneme2")
"""

# VİZE-FİNAL ÖRNEĞİ

# ogrenci_no = input("Ogrenci numarınızı giriniz.")
# vize1 = input("1. vize notunuzu giriniz:")
# vize2 = input("2. vize notunuzu giriniz:")
# final = input("final notunuzu giriniz:")
#
# with open("ogr_info.txt","w") as dosya:
#     dosya.write("{ogrencino} {vize1} {vize2} {final}\n".format(ogrencino=ogrenci_no,vize1=vize1,vize2=vize2,final=final))

# ogrenciler = {}
#
# with open ("ogr_info.txt", "r") as dosya2:
#         satirlarimiz = dosya2.read()
#         for ogrenci in satirlarimiz.split("\n"):
#             ogrenciler.update({
#
#             })
#
#
#

# HASTA BİLGİLERİ İLE İLGİLİ KENDİN YAZ!!!

def menu():
    print(""")
    Lütfen işleminizi seçiniz
    1-Öğrenci ekle
    2- Öğrenci Litele
    3- Öğrenci Ara
    4- Öğrenci Sil
    """)
    secim = input("İşlem :")
    if secim.isnumeric() and int(secim) < 5 and int(secim) > 0:
        return int(secim)
    else:
        print("Hatalı secim yaptınız")
        return menu()

def ogrencileri_ac(dosya):
    ogrenciler = {}
    with open(dosya,"r") as dosya2:
        satirlarimiz = dosya2.read().strip()
        for ogrenci in satirlarimiz.split("\n"):
            ogrencino,vize1,vize2,final = ogrenci.split(" ")
            ogrenciler.update ({ ogrencino:{
                    "vize1":vize1,
                    "vize2":vize2,
                    "final":final,
            }})
    return ogrenciler




while True:
    menu_no = menu()
    ogrencilistemiz = ogrencileri_ac("ogr_info.txt")
    if menu_no == 1:
        ogrenci_no = input("Ogrenci No:")
        vize1 = input('Vize 1:')
        vize2 = input('Vize 2:')
        final = input('Final :')
        if ogrencilistemiz.get(ogrenci_no,None) is not None:
            print("Gidiğiniz öğrenci bilgisi zaten sistemde var")
        else:
            if vize1.isnumeric() and vize2.isnumeric() and final.isnumeric():
                ""
            else:









# with open("ogr_info.txt","r") as dosya3:
#     dosya_verisi = dosya3.readlines()
#     print(dosya_verisi)


# with open("ilter.txt","r") as dosya:
#     dosya.seek(0)
#     print(dosya.read(10))
#
#     print(dosya.read(10))



