liste = ["1","2","5a","10b","abc","10","50"]

#1 Liste Elemanları İçindeki Sayısal Değerleri Bulunuz.
""" NumericValues =[]

def CheckNumbers(elements):
    import re
    if not (re.search("[a-z]",elements) or re.search("[A-Z]",elements)):
        NumericValues.append(elements)

for i in range(len(liste)):
    CheckNumbers(liste[i])

print(NumericValues)
 """

#Girilen Parola İçin Türkçe karakter hatası verdir

Parola = input("Parola Giriniz:")

def CheckChar(Parola):
    import re
    if (re.search("[ç,ş,i,ö,ğ,ü]",Parola)):
        raise Exception("Parolada Türkçe Karakter Var")
    else:
        print("Parola Doğru")

CheckChar(Parola)

