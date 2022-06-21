'''
C'deki header source dosyaları gibi
pypi.org sitesinde birçok hazır modüller bulunmakta.
>pip install package-name
 '''

#Yöntem 1
#import math
#import math as islem

#value = dir ()
#value = help(math)
#value = math.sqrt(3)

#value = islem.ceil(5.6)
#print(value)

#Yöntem 2 , her şeyi import ediyor ve direkt kullanabiliyoruz
from math import *

value = factorial(5)
print(value)