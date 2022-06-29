import json


person_string = '{"name":"Bahadir","languages":["python","C#"]}'

#JSON string to Dict
#result = json.loads(person_string)
#print (result)
with open("AdvancedModuls/person.json") as f:
    data = json.load(f)
    print(data)
    print(data["name"])


person_dict = {
    "name" : "Ali",
    "languages" : ["Python","C#"]
}

result = json.dumps(person_dict)  # person_dict dictonarysini jsona çevirdi

#with open("person.json","w") as f:
    #json.dump(person_dict,f)

