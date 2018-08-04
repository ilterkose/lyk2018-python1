import os

satir = os.path.abspath("../denememememem")
print(satir)


satir2 = os.path.abspath("./ilter")
dosya = os.path.join(satir2,"köse")


print(satir2)

if os.path.exists(dosya):
    print(os.remove(dosya))


"""
for i in os.listdir(satir):
    yeni_path = os.path.join(satir,i)
    print(os.path.isdir(yeni_path))
    print(os.path.isfile(yeni_path))
    print(i)
"""