#Asilbek Asqarov
#Mohirdev python-darslari
#dars-35

import json

class Person:
    
    def __init__(self, name, lastname, age, address , phonenumber = None):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.address = address
        self.phonenumber = phonenumber
        
    def get_info(self):
        return f"{self.name} {self.lastname} {self.age} yoshda {self.address}da yashaydi!"
        
person1 = Person("Asilbek", "Asqarov", 19, 'Sebzor')
person3 = Person("Hasan", "Husanov", 20, "Sag'bon")
person4 = Person("Husan", "Husanov", 21, "Sag'bono")

people = [person1, person3, person4]

for person in people:
    print(person.get_info())
    
for person in people:
    filename = f"{person.name.lower()}.json"
    with open(filename, 'w') as file:
        json.dump(person.__dict__, file, indent=4)
    
files = ['asilbek.json', 'hasan.json', 'bilol.json', 'husan.json']
    
for f in files:
    try:
        with open(f) as file:
            shaxslar = json.load(file)
    except FileNotFoundError:
        print(f"{f} not found!")
    else:
        print(f"{shaxslar['name']} file found")
print("Profram finished!")
        


        
        

