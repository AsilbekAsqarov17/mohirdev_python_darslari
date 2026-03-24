#Asilbek Asqarov
#Mohirdev python-darslari
#dars-21-03

#task3
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism} ning bahosi: ")
        baholar[ism] = baho
    return baholar

ismlar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(ismlar[:])
print(ismlar)
print(baholar)