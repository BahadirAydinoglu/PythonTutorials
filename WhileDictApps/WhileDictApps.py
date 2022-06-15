Count = int(input("Kaç Ürün Eklemek İstiyorsunuz ? : "))
i=0

Urunler = []

while i<Count:
    i+=1
    name = input("Ürünün Adı : ")
    price= int(input("Ürünün Fiyatı: "))
    stock= int(input("Ürünün Adeti: "))
    Urunler.append({
        "name": name,
        "stock": stock,
        "price" : price
    })

print(Urunler)