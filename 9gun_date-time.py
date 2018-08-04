import datetime
import locale


locale.set
date = datetime.datetime
print(date.today().day)
print(date.today().month)
print(date.today().year)
print(date.today().hour)
print(date.today().minute)
print(date.today().microsecond)
print(date.utcnow())

yenitarih = date.today() + datetime.timedelta(days=7,minutes=30)
print(yenitarih.minute)

print(date.now() - yenitarih)
