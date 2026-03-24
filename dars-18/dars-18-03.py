#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-18-03

#task3
mahsulotlar = {
    'osh': 35000,
    'shashlik': 15000,
    'manti': 6000,
    'somsa': 8000,N
    'lagmon': 28000,
    'shurva': 25000,
    'norin': 40000,
    'qozon kabob': 45000,
    'mastava': 22000,
    'chuchvara': 24000
}

buyurtma = []
n=1
while True:
    buyurtma.append(input(f"{n} mahsulot nomini kriting: "))
    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q): ")
    if javob =='ha':
        n+=1
        continue
    else:
        break

while buyurtma:
    mahsulot = buyurtma.pop()
    if mahsulot.lower() in  mahsulotlar:
        print(f"{mahsulot.title()} narhi {mahsulotlar[mahsulot]} so'm")
    else:
        print("Bizda bu mahsulot yo'q")
