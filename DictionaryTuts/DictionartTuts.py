
Ogrenciler = {}

Number  = input("Öğrenci No: ")
Name    = input("Öğrenci Adı: ")
SurName = input("Öğrenci Soyadı: ")
Phone   = input("Öğrenci Tel: ")



Ogrenciler.update({
    Number : {
        "Ad"    : Name,
        "Soyad" : SurName,
        "Tel"   : Phone
    }
})
print(Ogrenciler)

Number  = input("Öğrenci No: ")
Name    = input("Öğrenci Adı: ")
SurName = input("Öğrenci Soyadı: ")
Phone   = input("Öğrenci Tel: ")


Ogrenciler.update({
    Number : {
        "Ad"    : Name,
        "Soyad" : SurName,
        "Tel"   : Phone
    }
})
print(Ogrenciler)

OgrenciBul = input("Öğrenci Numarasını Gir: ")
Ogrenci = Ogrenciler[OgrenciBul]
print(Ogrenci)
