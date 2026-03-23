#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-17-02

#task2
savol = "Yoshingizni kiriting "
savol += "(dasturni to'xtatish uchun exit yoki quit deb yozing): "
qiymat = ''
while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    elif int(qiymat) <=7:
        print("Narh: 2000")
    elif int(qiymat) >7 and int(qiymat)<=18:
        print("Narh: 3000")
    elif int(qiymat) >18 and int(qiymat) <=65:
        print("Narh: 10000")
    else:
        print("Narh: bepul")
        
print("Dastur tugadi")
#second type input
while qiymat != 'exit' and qiymat != 'quit':
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        print("Exiting")
    elif int(qiymat) <=7:
        print("Narh: 2000")
    elif int(qiymat) >7 and int(qiymat)<=18:
        print("Narh: 3000")
    elif int(qiymat) >18 and int(qiymat) <=65:
        print("Narh: 10000")
    else:
        print("Narh: bepul")
print("Dastur tugadi")

#third type with qiymat==false
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        ishora =False
    elif int(qiymat) <=7:
        print("Narh: 2000")
    elif int(qiymat) >7 and int(qiymat)<=18:
        print("Narh: 3000")
    elif int(qiymat) >18 and int(qiymat) <=65:
        print("Narh: 10000")
    else:
        print("Narh: bepul")
        
print("Dastur tugadi")



