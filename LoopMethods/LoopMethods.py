import enum


for item in range (10): # 0'dan 9'a kadar.
    print(item)


for item in range(50,100,10):  #50'den 90'e kadar 10'ar 10'ar.
    print(item)

greeting = "Hello"

for item in enumerate(greeting): #index numarasıyla yazar
    print(item)

#zip
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip (list1,list2)))
