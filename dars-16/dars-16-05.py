#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-16-05

#task5
davlatlar = {
    "o'zbekiston": {
        'poytaxt': 'toshkent',
        'hudud': 448978,
        'aholi': 33000000,
        'pul': "so'm"
    },
    "rossiya": {
        'poytaxt': 'moskva',
        'hudud': 17098246,
        'aholi': 144000000,
        'pul': 'rubl'
    },
    "aqsh": {
        'poytaxt': 'vashington',
        'hudud': 9631418,
        'aholi': 327000000,
        'pul': 'dollar'
    },
    "malayziya": {
        'poytaxt': 'kuala-lumpur',
        'hudud': 329750,
        'aholi': 25000000,
        'pul': 'rinngit'
    }
}

search_davlat = input("Davlat nomini kiriting: ")
if search_davlat in davlatlar:
    print(f"{search_davlat.title()}ning poytaxti {davlatlar[search_davlat]['poytaxt']}")
    print(f"Hududi: {davlatlar[search_davlat]['hudud']}")
    print(f"Aholisi: {davlatlar[search_davlat]['aholi']}")
    print(f"Pul birligi: {davlatlar[search_davlat]['pul']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")


