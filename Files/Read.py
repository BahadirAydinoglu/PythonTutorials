file = open("Dosya_1.txt","r", encoding="utf-8")

#***************for döngüsü ile
# for i in file:
#     print(i,end="")
# file.close()

#***************read ile
# content= file.read() #imleç sona kadar gider ve orada kalir
# print(content)

#***************readline ile. Satırlar arası boşluk ekleyerek satır satır yazar.
print(file.readline(),end="") # endli komutu satırlar arası boşluk eklemesin diye ekledik.
print(file.readline(),end="")
file.close()