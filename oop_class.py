class Oyuncu():
    gucu = None
    vurus_carpanimiz = None
    oyuncu_ismi = ""

    def __init__(self,gucu=10,vurus_carpanimiz=1.3,ismi="isimsiz"):
        self.oyuncu_ismi = ismi
        self.gucu = gucu
        self.vurus_carpanimiz = vurus_carpanimiz
        print("Ben çalıştım")


    def set_vurus_carpanı(self,carpan):
        self.vurus_carpanimiz = carpan

    def set_gucu(self,guc):
        self.guc = guc

    def get_vurus_gucu(self):
        return self.get_gucu() * self.vurus_carpanimiz

    def get_gucu(self):
        return self.gucu

    def __str__(self):
        return "Oyuncu {}".format(self.oyuncu_ismi)


class Mario(Oyuncu):
        def mario_musun(self):
            return True

class Luigi(Oyuncu):
        def mario_musun(self):
            return False

        def get_vurus_gucu(self):
            return self.gucu * 100

        @staticmethod
        def hiz_hesapla(ivme_katsayisi,max_hiz):
            print(ivme_katsayisi,max_hiz)

        def hiz(self):
            Luigi.hiz_hesapla(99,666)

class PlayerTwo(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)




class PlayerOne():
        def __init__(acdc = 1000):
            super()
            self.ac_dc = acdc

            print("Ben çalıştım")


        def hiz(self,a,b):
            Luigi.hiz_hesapla(a,b)


player_one = PlayerOne()

player_one.hiz(15,25)
