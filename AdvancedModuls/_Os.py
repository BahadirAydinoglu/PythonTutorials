import os

result = dir(os)
result = os.name # İsletim sisteminin adini verir
result = os.getcwd() #Dosyanin bulunduğu konum
#os.mkdir("YeniKlasor") # Bulunulan klasöre yeni klasör ekler

result = os.listdir #Bulunulan klasördeki dosyaları listeler
print(result)