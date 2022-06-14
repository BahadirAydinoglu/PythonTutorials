import random

sayi = random.randint(0,100)
print("RASTGELE SAYI ÜRETİLDİ\n")
tahmin =0
Puan = 100
while not tahmin==sayi:
    Puan -=5
    tahmin=int(input("Tahmin : "))
    if tahmin>sayi:
        print("Kücük Sayi Giriniz: ")
    else:
        print("Büyük Sayı Giriniz")    

print(F"Tahmin Doğru, Sayı = {sayi} Puan= {Puan}")