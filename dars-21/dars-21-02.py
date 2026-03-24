#Asilbek Asqarov
#Mohirdev python-darslari
#dars-21-02

#task2
def katta_harf(ismlar):
    yangi_ismlar = []
    for ism in ismlar:
        yangi_ismlar.append(ism.title())
    return yangi_ismlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar[:])
print(ismlar)
print(yangi_ismlar)