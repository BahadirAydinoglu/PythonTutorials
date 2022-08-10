import numpy as np
numbers = np.array([0,5,10,15,20,25,50,75])
#result = numbers[5]
#print(result)

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
#result = numbers[0]
result = numbers2[0,2] #0.satır 2.index
result = numbers2[:,2] #tüm satırların 2.indeksleri
print(result)
