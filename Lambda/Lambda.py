from tabnanny import check


def square(num) : return num**2
numbers = [1,3,5,9 , 10,12,4]
# map komutu bir listenin elemanlarının herbirinin fonksiyona sokulmasını sağlar
# geri dönüşü adres şeklinde olduğu için başına list de ekliyoruz ki liste şeklinde dönsün diye.
result = list(map(square,numbers))

# bu şekilde de olur
#for item in map(square,numbers):
    #print(item)
#print(result)


#Yukarıdaki işlemi lambda ile de yapabiliriz. ilk argüman giriş değeri, 2.si çıkış, 3.sü de koşulacak elemanların bulunduğu liste
# Bu şekilde de yazılabilir -> square = lambda num: num**2 . square yazarak aynı işlemi yaptırtabiliriz.
LambdaResult = list(map(lambda num: num**2,numbers))
print(LambdaResult)

def check_even(num): return num%2==0

EvenResult = list(filter(check_even, numbers))
print(EvenResult)

EvenResult_A = list(filter(lambda numb: numb%2==0,numbers ))
print(EvenResult_A) 