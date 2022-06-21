from math import radians


""" 
Dosya açmak ve oluşturmak için open() fonksiyonu kullanilir.

open(dosya_adi,dosya_erisme_modu)  => Dosya erişme modu, dosyayi hangi amaçla açtiğimizi belirtir.

"w" : (Write) yazma modu Dosyayi konumda oluşturur. Ya da dosya içeriğini siler yeniden baştan yazar
"a" : (Append) ekleme. Dosya konumda yoksa oluşturur.
"x" : (Create) oluşturma. Dosya halihazirda varsa hata verir.
"r" : (Read) okuma. Varsayilan. Dosya konumda yoksa hata verir.

"""

#"w" : (Write) yazma modu Dosyayi konumda oluşturur.

#file = open("newfile.txt","w")
#file = open("/home/bahadira/Desktop/dosya.txt","w")
#file.close()
#print(file)

file = open ("Dosya_1.txt","w")
file.write("Bahadir Aydinoğlu")
file.close()
file= open("Dosya_1.txt","a")
file.write("\nİrem Aydinoğlu")
file.close()

