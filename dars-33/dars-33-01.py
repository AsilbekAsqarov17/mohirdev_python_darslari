#Asilbek Asqarov
#Mohirdev python-darslari
#dars-33-01

#first way
file = open('C:/Users/Oliya/Desktop/mohirdev_python_darslar/dars-33/Bugun.txt')
bugun = file.read()
print(bugun)
file.close()



#second way
with open("C:/Users/Oliya/Desktop/mohirdev_python_darslar/dars-33/Bugun.txt") as file:
    bugun = file.read()
    
print(bugun)