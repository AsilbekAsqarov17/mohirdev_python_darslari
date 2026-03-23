#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-17-01

#task1
savol = "Yaxshi ko'rgan kitobingizni  kiriting "
savol += "(dasturni to'xtatish uchun stop deb yozing): "
qiymat = ''
while True:
    qiymat = input(savol)
    if qiymat == 'stop':    
        break
print("Dastur tugadi")