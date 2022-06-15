Cities= []
Sehirler=[]


def AddCity(City):
    Cities.append(City)

print(Cities)
AddCity("ANTALYA")    
print(Cities)
Sehirler= Cities[:]  #Cities listesini Sehirler listesine kopyaladık, [0:2] -> 0'dan başlaya 2.indexe kadar at demek
AddCity("ISTANBUL")

print(Cities)
print(Sehirler)
