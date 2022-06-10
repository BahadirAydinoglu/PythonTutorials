plakalar = {"Kocaeli" : 41, "Istanbul" : 34 , "Antalya" : 7}
print(plakalar["Kocaeli"])

plakalar["Izmir"] = 35

print(plakalar)

users = {
    "Bahadir" : {
        "age" : 31,
        "mail" : "bahadirayd@gmail.com",
        "phone": 5553456789
    },
    "Irem"    : {
        "age" : 32,
        "mail": "iremayd52@gmail.com",
        "phone": 6989962
    }
}

print(users["Bahadir"])
print(users["Irem"]["mail"])