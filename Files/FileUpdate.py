# with open("Dosya_1.txt","r+",encoding="UTF-8")as file: #r+ hem açma hem okuma hem de yazma modlarını açmak demek
#     print(file.read())
#     file.write("\nAtakan Aydinoglu")
#     file.seek(0)
#     print(file.read())

with open("Dosya_1.txt","a",encoding="UTF-8") as file: # a ile ekleme yapacağımızı belirtiyoruz, o yüzden cursor en sona gidiyor.
    file.write("\nBatuhan Karacakaya")    

with open ("Dosya_1.txt","+r",encoding="UTF-8")as file:
    print(file.read())