#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-16-04

#task4
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

for davlat, info in davlatlar.items():
    print(f"{davlat.title()}ning poytaxti {info['poytaxt']} ")
    print(f"Hududi: {info['hudud']} kv.km")
    print(f"Aholisi {info['aholi']}")
    print(f"Pul birligi: {info['pul']}")
    print()