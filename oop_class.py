class Oyuncu():
    gucu = 10
    vurus_carpanimiz = 1.3

    def set_vurus_carpanı(self,carpan):
        self.vurus_carpanimiz = carpan

    def set_gucu(self,guc):
        self.guc = guc

    def get_vurus_gucu(self):
        return self.get_gucu() * self.vurus_carpanimiz

    def get_gucu(self):
        return self.gucu



oyuncu1 = Oyuncu()
print(oyuncu1.get_gucu())

oyuncu2 = Oyuncu()
oyuncu2.set_gucu(15)
oyuncu2.set_vurus_carpanı(2)

print("Oyuncu1 Gucu",oyuncu1.get_gucu())
print("Oyuncu2 Gucu",oyuncu2.get_gucu())
print("Oyuncu1 Vurus Gucu",oyuncu1.get_vurus_gucu())
print("Oyuncu2 Vurus Gucu",oyuncu2.get_vurus_gucu())