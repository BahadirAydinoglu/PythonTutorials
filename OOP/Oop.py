#class


class Person:
    pass
    #class attributes
    address ="Bilgi Yok"
    #constructor (yapıcı metod)
    def __init__(this, name, year):
        #object attributes // Sınıfın alacağı değişken değerleri
        this.name = name
        this.year = year
        #init kısmı, sınıfın çağrıldığı her seferde çalışır
    #instance methods
    def intro(this):
        print(F"Benim Adım {this.name}")
    def calculateage(this):
        return 2022-this.year      

#instance (object)
p1 = Person("Ali",1990)
p2 = Person("Rüya",2022)

p1.address = "İzmir"
p2.address = "Antalya"

print(F"İsim: {p1.name}, Yıl: {p1.year}, Adres: {p1.address}")
p1.year = 1995
print(F"İsim: {p1.name}, Yıl: {p1.year}, Adres: {p1.address}")
print(F"İsim: {p2.name}, Yıl: {p2.year}, Adres: {p2.address}")

p1.intro()
p2.intro()
print(F"Yaşım {p1.calculateage()} ")
print(F"Yaşım {p1.calculateage()} ")