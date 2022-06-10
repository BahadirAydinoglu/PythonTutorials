name = 'Bahadir'
surname = 'Aydinoglu'
age = 36
Sentence = 'My name is '+ name +' '+ surname +' and I am ' +str(age) + ' years old'
print(Sentence)
print(len(Sentence))  # Cümlenin uzunluğunu bulma methodu
print(Sentence[2:5])  # 2.karakterden başla 5'e kadar yaz , 5 yazmazsak sona kadar gider.

#String Formatlama
print('Benim adım {} {}'.format(name,surname))
print('Benim adım {1} {0}'.format(name,surname))  #index numaralarıyla str değişkenleri yazabiliriz.
print('Benim adım {n} {s}'.format(n=name,s=surname))  #index numaralarına değişken atayarak da yazdırabiliriz.
print('Ben {} {} ve {} yasindayim'.format(name,surname,age))


#Formatlanmış Float Veri Gösterme
result = 200 / 700
print('Result is: {r:1.3}'.format(r=result))  # float degeri 1 tam 3 ondalık şeklinde gösterebiliyoruz, 1 alan büyüklüğü

#fstring
print(f"My name is {name} {surname} and I'm {age} years old" )

