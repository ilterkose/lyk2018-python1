"""
class DataModel():
    veriler = {}
    def veriyi_modla(self,veri):
        if type(veri) == str:
            return veri.upper()

        else:
            return veri


    def __setattr__(self, key, value):

        yeni_value = self.veriyi_modla(value)

        #print(key,value)
        #if key == "mustafa":
            #value = "verimiz : {veri}".format(veri=value)

        return object.__setattr__(self,key,yeni_value)

    def __getattribute__(self,item):
        return object.__getattribute__(self,item)


class DataTable(DataModel):
    pass


data = DataTable()
data.mustafa = "deneme"
data.deneme = "kose"
print(data.deneme)
"""
"""
class Insan():
    ozellikler = {"gozu": "Gri"}

    def __setattr__(self, key, value):
        self.ozellikler.update({key: value})

    def __getattr__(self, item):
        if item != "ozellikler":
            if item.endswith("_feet"):
                return self.ozellikler.get(item[:-5]) / 0.3048
            else:
                return self.ozellikler.get(item)

    def save(self):
        print(self.ozellikler)


ihsan = Insan()
ihsan.gozu = "Yeşil"
ihsan.boyu = 1.85
print(ihsan.boyu_feet)
feet = ihsan.boyu_feet
print(feet)
print(ihsan.boyu)
ihsan.ogrenci = True
ihsan.save()

"""

class BenimSinifim(object):
    pass

sinifim = BenimSinifim()
sinifim.masasayisi = 15
sinifim.ogrencisayisi = 30
sinifim.kalemsayisi = 90
deneme = sinifim.__dict__
deneme.update({"ogrencisayisi":99})
print(sinifim.ogrencisayisi)
print(sinifim.__dict__)
