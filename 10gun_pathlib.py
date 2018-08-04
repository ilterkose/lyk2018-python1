import os
from pathlib import Path

dosya = Path(".")
sedanin_klasoru = dosya / "seda"
sedanin_klasoru_2 = dosya / "seda" / "eda"
edanin_dosyasi = dosya / "seda" / "eda" / "deneme.txt"

if sedanin_klasoru_2.exists() is False:
        sedanin_klasoru_2.mkdir()

if edanin_dosyasi.exists() is False:
    with edanin_dosyasi.open("w") as file:
        file.write("Merhaba Dümya")

for i in sedanin_klasoru.glob("*.py"):
    with i.open() as file:
        print(file.read())


for i in sedanin_klasoru.glob("*.py"):
    with i.open() as file:
        print(file.read())

for i in sedanin_klasoru.glob("*.py"):
    i.replace(sedanin_klasoru / "deneme2.py")
    if i.is_file():
        print("Bu bir dosyadir")
