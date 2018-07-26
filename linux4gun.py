def hesap_makinesi():
    while True:
        secim = input("Hesap makinesine hoş geldiniz. İşlemler için belirtilen tuşlara basınız. \n 1-Toplama \n 2-Çıkarma \n 3-Bölme \n 4-Çarpma")
        if (secim == "1"):
                birinci_sayi = int(input("birinci sayiyi giriniz"))
                ikinci_sayi = int(input("İkinci sayi  giriniz"))
                def toplama(birinci_sayi, ikinci_sayi):
                    return birinci_sayi + ikinci_sayi

                print("Sonucunuz:", toplama(birinci_sayi, ikinci_sayi))

        elif (secim == "2"):
                birinci_sayi = int(input("birinci sayiyi giriniz"))
                ikinci_sayi = int(input("İkinci sayi  giriniz"))

                def cikarma(birinci_sayi, ikinci_sayi):
                    return birinci_sayi - ikinci_sayi

                print("Sonucunuz:", cikarma(birinci_sayi, ikinci_sayi))

        elif (secim == "3"):
            birinci_sayi = int(input("birinci sayiyi giriniz"))
            ikinci_sayi = int(input("İkinci sayi  giriniz"))

            def bolme(birinci_sayi, ikinci_sayi):
                return birinci_sayi / ikinci_sayi

            print("Sonucunuz:",bolme(birinci_sayi, ikinci_sayi))

        elif (secim == "4"):
            birinci_sayi = int(input("birinci sayiyi giriniz"))
            ikinci_sayi = int(input("İkinci sayi  giriniz"))

            def carpma(birinci_sayi, ikinci_sayi):
                return birinci_sayi * ikinci_sayi

            print("Sonucunuz:",carpma(birinci_sayi, ikinci_sayi))


hesap_makinesi()


