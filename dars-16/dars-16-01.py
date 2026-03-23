#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-16-01

#task1
shaxs_0 = {
    'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
    'tyil': 810,
    'manzil': 'Buxoro',
    'umr': 60
}

shaxs_1 = {
    'ism': 'Abdulla Qodiriy',
    'tyil': 1894,
    'manzil': 'Toshkent',
    'umr': 44
}

shaxs_2 = {
    'ism': 'Erkin Vohidov',
    'tyil': 1936,
    'manzil': "Farg'ona",
    'umr': 80
}

shaxs_3 = {
    'ism': 'Alisher Navoiy',
    'tyil': 1441,
    'manzil': 'Xirot',
    'umr': 60
}

shaxslar = [shaxs_0, shaxs_1, shaxs_2, shaxs_3]

for shaxs in shaxslar:
    print(f"{shaxs['ism']} {shaxs['tyil']}-yilda {shaxs['manzil']}da tavallud topgan. "
          f"{shaxs['umr']} yil umr ko'rgan.")

    