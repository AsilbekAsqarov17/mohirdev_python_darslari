#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-16-02

#task2
shaxs_0 = {
    'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
    'tyil': 810,
    'manzil': 'Buxoro',
    'umr': 60,
    'asarlari' : ['Al-jome\' as-sahih', 'Al-adab al-mufrad','At-tarix al-kabir', 'At-tarix as-sag\'ir']
}

shaxs_1 = {
    'ism': 'Abdulla Qodiriy',
    'tyil': 1894,
    'manzil': 'Toshkent',
    'umr': 44,
    'asarlari' : ['O\'tkan kunlar', 'Mehrobdan chayon', 'Obid ketmon' ]
}

shaxs_2 = {
    'ism': 'Erkin Vohidov',
    'tyil': 1936,
    'manzil': "Farg'ona",
    'umr': 80,
    'asarlari' : ['Tong nafasi', 'Qo\'shiqlarim sizga', 'O\'zbegim', 'Qiziquvchan Matmusa']
}

shaxs_3 = {
    'ism': 'Alisher Navoiy',
    'tyil': 1441,
    'manzil': 'Xirot',
    'umr': 60,
    'asarlari' : ['Xamsa', 'Lison ut-Tayr', 'Mahbub Al-Qulub', 'Munojat']
}

shaxslar = [shaxs_0, shaxs_1, shaxs_2, shaxs_3]

for shaxs in shaxslar:
    print(f"\n{shaxs['ism']} ning mashxur asarlari:")
    for asar in shaxs['asarlari']:
        print(asar)

    