#Asilbek Asqarov
#Mohirdev python-darslari
#dars-21-01

#task1
def katta_harf(ismlar):
    for n in range(len(ismlar)):
        ismlar[n] = ismlar[n].title()
    return ismlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)