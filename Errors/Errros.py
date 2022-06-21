
#print(a)           -> NameError
#int("1a2")         -> ValueError
#print(10/0)        -> ZeroDivisonError
#print("denem"e)    -> SyntaxError

#docs.python.org 'da geri kalan build hatalarını bulabiliriz.


#Error Handling

try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except ZeroDivisionError as e:
    print("Hatali Input")
    print(e)
except  ValueError as e:  # Yukarıya yanyana da yazılabilir. Parantez içine almalısın
    print("Deger Girmelisiniz")
    print(e)
else:
    print("Girilen Değerler Doğru")


#Ya da 
try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except Exception as e:  #Exception sınıfı ile genel ifade
    print("Hatali Input")
    print(e)
else:
    print("Girilen Değerler Doğru")    
finally: #Her zaman çalışır
    print("Try/Except Sonlandırıldı")
