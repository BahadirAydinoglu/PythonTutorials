# Name  = input("Kelime ?: ")
# Count = int(input("Kelime kaç kere tekrar edilsin ? : "))

# def PrintName(_count , _name):
#     i=0
#     for i in range(_count):
#         print(_name)

# PrintName(Count,Name)

#####################################################
# Liste=[]

# def AddNumber(number):
#     Liste.append(number)
#     print(Liste)

# while(True):
#     AddNumber(int(input("Sayiyi Giriniz: ")))

######################################################

AsalSayilar = []
def FindNumber(number):
    if (number%2!=0) and (number%3!=0) and (number%5!=0) and (number%7!=0):
        AsalSayilar.append(number)

IlkSayi = int(input("İlk Sayi : "))
SonSayi = int(input("Son Sayi : "))

for i in range(IlkSayi,SonSayi):
    FindNumber(i)

print(AsalSayilar)

