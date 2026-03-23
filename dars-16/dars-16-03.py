#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-16-03

#task3
kinolar = {
    'ali' : ['teminator', 'rambo', 'titanic'],
    'vali' : ['tenet', 'inception', 'intersteller'],
    'hasan' : ['abdullajon', 'bomba', 'shaytanat'],
    'husan' : ['mahallda dub-dub gap', 'john wick']
    }
for azolar in kinolar.keys():
    print(f"{azolar.title()} sevimli kinolari: ")
    for kino in kinolar[azolar]:
        print(kino.title())
    print()