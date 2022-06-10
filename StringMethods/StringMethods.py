message = "I am an engineer"
"""
message = message.upper()  # message içeriğini büyük harfe çevirir
message = message.lower()  #  küçük harfe çevirir
message = message.title()  # ilk harfleri büyük harf yapar
message = message.capitalize() # Sadece ilk harfi büyük yapar
message = message.strip()  # message içeriğinin başi ve sonundaki boşluklari siler
message = message.split() # message içeriğini boşluklara bakarak dizi haline getirir message.split("*") bu da yildiza göre ayirir.
message = ' '.join(message) # message dizinindeki elemanları birleştirecek ve araya boşluk ekleyecek
index = message.find("engineer") # engineer kelimesini message değişkeninde arar ve bulduğunda ilk indexini geri döndürür
isFound = message.startswith("e") # e işe başlayan kelime var mi, varsa true döndürür
message = message.replace("an","ben") # message değişkeninde an kelimesini arar ve onu ben kelimesini çevirir

result = message.isalpha() # message içeriği alfabetik mi
result = message.isdigit() # message içeriği digit mi 
"""



print(message)