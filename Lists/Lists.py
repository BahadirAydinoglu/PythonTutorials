numbers = [1,10,5,16,4,9,10]
letters = ['a','x','y','z']

# Maksimum ve Minimum değer yazdırma
MinVal = min(numbers)
MaxVal = max(numbers)
print(f"Minimum Deger : {MinVal} \nMaksimum Deger : {MaxVal}")

#Dizinin sonuna değer eklemek
numbers.append(32)
print(numbers)

#Dizinin istenilen indexine değer eklemek
numbers.insert(3,78)
print(numbers)

#Dizinden eleman silme , içine index girilebilir
numbers.pop()
print(numbers)

#Dizinden değere göre silme işlemi
numbers.remove(5)
print(numbers)

#Dizini sayısal büyüklüğe göre sıralama , string degerleri alfabetik sıralama. reverse tam tersi
numbers.sort()
letters.sort()
print(numbers)

#Dizindeki elemanın sayısını sayma
print(numbers.count(10))  # 10 kaç tane var

#Dizini silme clear()
#numbers.clear()
#print(numbers)

#Dizinde arama , 16 değeri numbers dizininde var mı
result = 16 in numbers
print(result)