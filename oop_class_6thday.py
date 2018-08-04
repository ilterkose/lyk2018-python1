import oop_class
from helpers.matematik import carp,topla
from helpers import carp,topla
from helpers import *


class Canli():
    dogumu = " "
    kilosu = 0
    aclik = 0
    susuzluk = 0
    enerji = 100

    def __init__(self,dogumu, kilosu, aclik, susuzluk):
        self.dogumu = dogumu
        self.kilosu = kilosu
        self.aclik = aclik
        self.susuzluk = susuzluk

    def enerji_hesapla(self):
        kalan_aclik = 100 - self.aclik
        enerji_carpanı = kalan_aclik * 0.1
        return enerji_carpanı

    def hareket(self,mesafe):
        self.enerji -= mesafe * self.enerji_hesapla()
            if (self.enerji <= 0):
                self.kilosu -= 1
                if self.kilosu <= 0:
                    self.yasiyormu = False
    def beslenir(self,nekadar):



class Kedigiller(Canli):
    def __init__(self,dogumu):
        Canli.__init__(self,10,0,0)

    def miyaw(self):
    print("Miyawww Miyak")

class Kediler(Kedigiller):
    cinsi = "Tekir"
    rengi = " "
    def __str__(self):
        return "Miyaaawwww"

# class Cezve(Kediler):
    

if __name__ == "__main__":
    luigi = oop_class.Luigi()


