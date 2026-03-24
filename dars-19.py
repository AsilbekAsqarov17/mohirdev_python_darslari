#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-19

#task1
def yosh_hisobla(ism, tugilgan_yil, joriy_yil= 2026):
    print(f"{ism.title()} {joriy_yil-tugilgan_yil} yoshda")
    
yosh_hisobla("Asilbek", 2006)

#task2
def sq_and_cube(number):
    print(f"{number} ning kvadrati:{number**2}  kubi:{number**3}")

sq_and_cube(2)    

#task3
def odd_or_even(number):
    if(number%2==0):
        print(f"{number} is Even!")
    else:
        print(f"{number} is Odd!")

odd_or_even(13)

#task4
def bigger_or_equal(num1, num2):
    if num1==num2:
        print("Numbers equal!")
    elif num1>num2:
        print(f"{num1} is bigger than {num2}!")
    else:
        print(f"{num2} is bigger than {num1}!")

bigger_or_equal(12, 7)

#task5 & 6
def darajaga_kotarish(son, daraja =2):
    print(f"{son}ning {daraja}-darjasi {son**daraja} teng!")

darajaga_kotarish(3, 4)
darajaga_kotarish(3)
#task7
def qoldiqsiz_bolinish(number):
    for n in range(2, 11):
        if number%n==0:
            print(f"{number} {n}ga qoldiqsiz bo'linadi!")

qoldiqsiz_bolinish(70)
    








    
    
    