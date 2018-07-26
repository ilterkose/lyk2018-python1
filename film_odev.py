"""
İzlediğim filmlerin ve dizilerin listesini tutan tüm program
1-İzlediğim filmin ismini,yılını,izlediğim tarihi,oyuncuların kaydınız tutan bir yazılım
"""


while True:
    print(("*" * 55))
    print("Hoş geldiniz. AkgülFlix ")
    secim = input("Film Eklemek için 1'e basınız. ||| İzlediğiniz Filmleri Görmek için 2'ye basınız. ||| Çıkmak için 3'e basınız. \n" + "*" * 56 )
    filmler = []

    if (secim == "3"):
        print("Çıkış yapıyorsunuz")
        break
    elif (secim == "1"):
        film_name = str(input("Film adını giriniz:"))
        film_cikis= str(input("Filmin Vizyona Giriş Yılını giriniz:"))
        if (type(film_cikis) != type(str)) :
            print("buraya sadece rakam girebilirsiniz")
            break
        film_izlenme_tarih = str(input("İzlediğiniz tarihi giriniz:"))
        if film_izlenme_tarih is not "numeric":
            print("buraya sadece rakam girebilirsiniz")
            break
        oyuncular = []
        oyuncu_sayisi = int(input("Kaç tane oyuncu girmek istiyorsunuz:"))

        for i in range(oyuncu_sayisi):
            oyuncular.append(input("Oyuncu isimlerini giriniz:"))

        filmler.append({"Film adı": film_name, "Film Çıkış Tarihi": film_cikis,"Film İzlenme Tarihi": film_izlenme_tarih,"Oyuncular": oyuncular}) #BUNU UNUTMA

        print("İzlediğiniz film eklendi \n",filmler)

    elif (secim == "2"):
        print(filmler)
    else:
        print("Yanlış bir tuşa bastınız.")