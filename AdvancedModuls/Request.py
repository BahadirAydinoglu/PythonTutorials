#Herhangi bir internet sitesine bağlanıp kaynak kodları görebiliyoruz.
#Jsonplaceholder todosta örnek bir json veri tipi var. Bu veriyi çekip kullanabiliyoruz.
import requests
import json
result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
#print(result[0]["title"])
for i in result:
    #print(i)
    print(i["title"])
    print(i["userId"])


