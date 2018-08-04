"""
try:
    with open("deneme.xtxr") as file:
        data = file.read()
except FileNotFoundError:
    with open('deneme.xtxr',"w") as file:
        print("Dosya oluşturuldu.")
        file.write("x")
except ZeroDivisionError

deneme = "ismail"
if deneme != "mustafa":
    raise Exception("dememe mustafa olmalı")
"""

class BenimExce(Exception):
    pass

deneme = "ismail"

if deneme != "mustafa":
    raise BenimExce("deneme ilter olmalı")
