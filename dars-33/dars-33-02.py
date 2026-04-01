#Asilbek Asqarov
#Mohirdev python-darslari
#dars-33-02

import pickle

with open("D:\pi_million_digits.txt") as file:
    pi = file.read()
    
pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')

bdate = "02102006"

print(bdate in pi)

pi = float(pi)
filename = "C:/Users/Oliya/Desktop/mohirdev_python_darslar/dars-33/dars-33pifloat.pkl "
with open(filename, 'wb') as file:
    pickle.dump(pi, file)
    
print("Data saved!")
    
