#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-15

#task1
lugat = {'boolean' : 'matiqiy qiymat',
         'float' : 'o\'nlik son',
         'for' : 'qayta bajarish',
         'if' : 'agar',
         'integer' : 'butun son',
         'else' : 'yoki',
         'string' : 'so\'z',
         'char' : 'harf',
         'tuple' : 'o\'zgarmas list',
         'keys' : 'kalitlar'
         }
for key, value in sorted(lugat.items()):
    print(f"{key.title()} - {value.capitalize()}")

#task2
print("Dunyo davlatlari: Davlatlarning poytaxti")
davlatlar = {
             'italiya' : 'rim',
             'malaziya' : 'kuala-lumpur',
             'qozog\'iston' : 'nursulton',
             'tojikiston' : 'dushanbe',
             'rossiya' : 'moskva',
             'aqsh' : 'washington d.c',
             'o\'bekiston' : 'toshkent',
             'qirg\'iziston' : 'bishkek',
             'singapur' : 'sungapur'
             }
for key, value in sorted(davlatlar.items()):
    print(f"{key.title()}\t {value.title()}")
    
#task3
user_search = input("Qaysi davlatning poytaxtini bilishni xoxlaysiz: ").lower()
capital = davlatlar.get(user_search)
if capital:
    print(f"{user_search.title()} ning poytaxti {capital.title()} shaxri")
else:
    print( "Bizda bunday ma'lumot yo'q" )
    
#task4
taomlar = {
    'osh': 35000,
    'shashlik': 15000,
    'manti': 6000,
    'somsa': 8000,
    'lagmon': 28000,
    'shurva': 25000,
    'norin': 40000,
    'qozon kabob': 45000,
    'mastava': 22000,
    'chuchvara': 24000
}
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma.title()} {taomlar[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma.title()} yo'q")







