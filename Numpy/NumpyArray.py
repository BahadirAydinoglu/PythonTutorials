import numpy as np

#result = np.array([1,3,5,7,9])
#result = np.arange(1,10) #1'den 9'a kadar kendisi doldurur
#result = np.arange(10,100,3)  #10'dan 100'e kadar 3'er arttırarak diziyi kendisi oluşturur.
#result = np.zeros(10) #10 tane sıfır
#result = np.ones(10) #10 tane 1 ve float tipinde
#result = np.linspace(0,100,5) # 0 ile 100 arasında 5 eşit parçaya bölerek diziyi oluşturur
#result = np.random.randint(0,10) #0 ile 9 arasında 1 sayı üretir, tek sayı yazarsak 0 'da belirtilen sayıya kadar random atar
#result = np.random.rand(5) #0 ile 1 arasında 5 tane sayı üretir,

# np_array =  np.arange(50)
# np_multi = np_array.reshape(5,10)
# print(np_multi.sum(axis=1)) #1.sütunları topladık

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.mean() #ortalama alır
result = rnd_numbers.argmax() # dizideki en büyük sayının indexini gösterir
print(result)