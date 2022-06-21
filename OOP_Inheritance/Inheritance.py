
#Inheritance (Kalıtım): Miras Alma

#Person -> name,surname,age, eat(),run(), drink() attribute ve metodlarına sahip
#Student(Person) ve Teacher(Person) ile bu özellikleri bu yeni tanımlanan sınıflara taşıyabiliriz.

class Person():
    def __init__(this,fname,fsurname):
        this.name = fname
        this.surname = fsurname        
    
    def eat(this):
        pass
    def run(this):
        pass
    def drink(this):
        pass
    def me(this):
        print(F"My name is {this.name} {this.surname}")       

class Student(Person):
    def __init__(this,fname,fsurname,number):
        Person.__init__(this,fname,fsurname)
        this.studentnumber = number # Bu attribute Personda yok ama Studentta var
        print("Student Created")

    # Student.me Person.me methodunu ezdi. Buna <<override>> deniyor
    def me(this):
        print(F"Benim Adım {this.name} Soyadım {this.surname}")    


class Teacher(Person):
    def __init(this,fname,fsurname,fbranch):
        super().__init__(fname,fsurname)
        this.branch = fbranch

p1 = Person("Bahadir","Aydinoglu")
s1 = Student("Ruya","Aydinoglu",1226)

t1 = Teacher("Irem","Gozukan")

p1.me()
s1.me()

print(s1.studentnumber)
t1.branch = "TURKCE"
print(t1.branch,t1.name,t1.surname)