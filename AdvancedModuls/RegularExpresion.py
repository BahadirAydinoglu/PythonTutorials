import re

result = dir(re)

#re module

str = "Python Kursu : Python Programlama Rehber | 40 saat"
result = re.findall("Python",str) # Python ifadesini strde bulur ve liste şekline çevirir
result = len(result) # Kaç adet var onu bulur

#result = re.split(" ",str)      # Boşluk ifadesine göre stryi bölüp liste haline getirir. Boşlukları yok sayar
#result = re.sub(" ","-",str)    # Boşluk ifadelerini - ile değiştirir
#result = re.search("Python",str) # Python ifadesini arar match döndürür, ilk bulduğunu döndürür
#result = result.span() # resultta dönen değerin span değerini döndürür , start baş end bitişi gösterir


result = re.findall("[sat]",str) # str'de s,a,t harflerini arar ve liste şekline çevirir
result = re.findall("[a-e]",str) # str'de a'dan e'ye kadar harfleri arar, [1-9] yazarsak bu 2 rakam arasını arar
                                 
                                 # [0-39] 'de 0'dan 3'e kadar arar buna ek olarak 9'u da arar
                                 # ^ yazarsak içeridekinin dışındakileri arar                                 
result = re.findall("...",str)   # .. 2 basamaklı her şeyi arar

result = re.findall("^P",str)  # P ile başlayan ifade var mı ?
result = re.findall(" $",str)  # n ile biten ifade var mı ?                

#docs.python.org sitesinden geri kalanı var
print(result)