import string as sg
import random
import json

class Keepasx():

    file_name = "parola"
    chest = {}

    def __init__(self,file_name):
        self.file_name = "parola"
        while True:
            menu = input("""
            Lütfen işlem seçiniz:
            1- Yeni parola oluştur
            2- Parolaları listele
            3- Parola ara
            ÇIKMAK İÇİN Q'YA BASIN
            """)

            if menu == "1":
                self.register_new_pass()
            elif menu == "2":
                self.list("parola")
            elif menu == "q" or "Q":
                break

    def register_new_pass(self):

        self.username = input("Kullanıcı adınızı giriniz:")
        self.password = input("Parolanızı giriniz:")
        self.description = input("Neyinizin parolası not düşünüz:")


        self.chest.update({ "Kullanici adiniz:" : self.username,
                            "Parolaniz": self.password,
                            "Aciklama": self.description})
        print(self.chest)
        with open(self.file_name,"a") as file:
            json.dump(self.chest,file)


    def load(self):
        """
        with open(self.file_name) as file:
            file_data = file.read.split("\n")
            for veriler in file_data:
                veri_yigini = veriler.split("@ayrac@")
                self.chest.append({
                "username": veri_yigini[0],
                "password": veri_yigini[1],
                "description": veri_yigini[2]})
                """
        pass

    def list(self,file_name):

        with open(self.file_name) as file:
            data = json.load(dict(file))
            print(data)

    def generate_pass(self,length):
        string_data =sg.printable
        return ''.join([string_data[random.randint(0,len(string_data)-1)] for i in range(0,length)])

keep = Keepasx("parola")
keep()
