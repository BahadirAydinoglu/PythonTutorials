from datetime import date, datetime
# from datetime import date
# from datetime import time
# import datetime

#result = dir(datetime)

#Tarih Saat Bilgisi
simdi   = datetime.now()
year    = simdi.year
month   = simdi.month
day     = simdi.day
hour    = simdi.hour

#Acıklayıcı Tarih/Saat Bilgisi
result = datetime.ctime(simdi)
print(result)

result = datetime.strftime(simdi,"%Y") # Sadece Yıl
result = datetime.strftime(simdi,"%X") # Sadece Saat
result = datetime.strftime(simdi,"%d") # Sadece Gün
result = datetime.strftime(simdi,"%A") # Sadece Haftanın Günü
result = datetime.strftime(simdi,"%B") # Sadece Ay

# t ="21 Nisan 2019"
# gun,ay,yil =t.split()
# print(F"Gün = {gun}")
# print(F"Ay = {ay}")
# print(F"Yil = {yil}")

#Bilgileri tek satırdan yükleyebiliriz
t= "1 July 2022 hour 09:05:00"
result = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")

BirthdayRuya = datetime(2022,2,25,10,49,00)
print(BirthdayRuya)

print(result)



