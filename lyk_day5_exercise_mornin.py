"""
1- Gelirlerini gir
2- Giderlerini gir
3- Kalan paranı gör

"""

def menu():
    print("""
    Gelir Gider Hesaplayıcısına hoş geldinizz.
    1- Bu ayki gelirlerinizi giriniz.
    2-Aylık giderlerinizi giriniz.
    3-Kalan paranızı görmek için seçiniz
    
    """)

    secim = input("Seçiminizi giriniz:")

    if secim.isnumeric() and int(secim) <= 3 and int(secim) > 0:
        return int(secim)
    else:
        print("Hatalı Secim yaptınız.")
        return menu()




def gelir_ekle(ggtablo,dosya_ismi):
    gelirler = {}
    gelir_ad = input("Gelirinizin adı:(kira-maaş-vb)")
    gelir_miktar = input("Gelir miktarınızı giriniz:")
    gelir_tarih = input("Gelirinizin tarihini giriniz:")

    with open(dosya_ismi, "a") as dosya2:
        for gelir in gelirler.items():
            gelirler.update({gelir_ad: {"Miktar": gelir_miktar, "Tarih": gelir_tarih}})
            gelir_bilgiler = gelir[1]
            gelir_ad = gelir[0]
            gelir_miktar = gelir_bilgiler.get("gelirad")
            gelir_tarih = gelir_bilgiler.get("gelirtarih")


        dosya2.write("Geliriniz Adı: {gelirad} Miktar: {gelirmiktar} Tarih : {gelirtarih} \n".format(gelirad =gelir_ad,
                                                                        gelirmiktar=gelir_miktar,
                                                                        gelirtarih=gelir_tarih))

def gider_ekle(ggtablo,dosya_ismi):

    gider_ad = input("Giderizin adı:(kira-maaş-vb)")
    gider_miktar = input("Giderinizin miktarı:")
    gider_tarih = input("Giderinizin tarihi")


    with open(dosya_ismi, "a") as dosya3:
        for gider in giderler.items():
            gider_bilgiler = gider[1]
            gider_ad = gider[0]
            gider_miktar = gider_bilgiler.get("gelirad")
            gider_tarih = gider_bilgiler.get("gelirtarih")

        dosya3.write("Gideriniz Adı: {giderad} Miktar:{gidermiktar} Tarih: {gidertarih} \n".format(giderad =gider_ad,
                                                                        gidermiktar=gider_miktar,
                                                                        gidertarih=gider_tarih))
def ggtablo_ac(dosya):
    with open(dosya,"r") as dosya:
        tablomuz = dosya.read.strip()
        for paralar in tablomuz.split("\n"):
            gelir_ad,gelir_miktar,gelir_tarih = paralar.split(" ")
            ggtablo.update ({gelir_ad: { "Miktar":gelir_miktar , "Tarih":gelir_tarih}})
    return paralar




while True:
    menu_no = menu()
    ggtablo = {}
    giderler = {}
    gelirler = {}

    if menu_no == 1:
        yenigelir = gelir_ekle(ggtablo,"gg_ozet.txt")
        print(yenigelir)
        ggtablo.update(yenigelir)
    if menu_no == 2:
        yenigider = gider_ekle(ggtablo,"gg_ozet.txt")
        ggtablo.update(yenigider)