"""
filter kullanarak veri okuyarak ### olanları çekicez
"""
"""
with open("bio_odev.fastq","r") as dosya:
    veriler =[]
    satirlarimiz = dosya.read()
    for i in satirlarimiz.split("+\n"):
        veriler.append(i)

print(veriler[:10])
"""

# ODEV

class ayirara():

    def filtrele(self,dosya):
        if dosya.find("#") > -1:
            return True
        return False

    def arayici(self,dosya):
        with open("bio_odev.fastq") as file:
            data = file.read().split("+\n")
            hepsi = list(filtrele(data))
            okunanlar = []
            for i in hepsi:
                    okunanlar.append(i)

    def okunansatirlar(self):
        print("Okunan satırlar: {}".format(len(okunanlar))

ayirara.arayici("bio_odev.fastq")


# HOCANIN YAZDIĞI KOD

class ParseFASTQ():
    file_date = []
    filtered_data = []
    filter_keyword = None

    def __init__(self, file_name):

        with open(file_name) as file_data:
            self.file_data = file_data.read().split("+\n")

    def filter(self,data):
        if data.find(self.filter_keyword) > -1:
            return True
        else:
            return False


    def find(self, keyword):
        self.filter_keyword = keyword
        self.filtered_data = list(filter(self.filter))
