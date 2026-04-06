#Asilbek Asqarov
#Mohirdev python-darslari
#dars-38

import datetime as dt
import re

#task 1
hozir = dt.datetime.now()
for n in range(10):
    next_date = hozir + dt.timedelta(days=n * 14)
    print(next_date.date())
    
#task 2
def kun_qoldi(nom, sana):
    ramazon = dt.date(2027, 2, 8)
    farq = ramazon - hozir.date()
    print(f"{nom}ga {farq.days} kun qoldi!")

kun_qoldi("Ramazon", dt.date(2026, 2, 18))
kun_qoldi("Qurbon hayiti", dt.date(2026, 5, 27))
#task 3
def until_birthday(sana):
    left = sana - hozir.date() 
    return left

sana = dt.date(2026, 10, 2)
print(until_birthday(sana))

#task4
andoza = r"^(\+998)?\s?(90|91|93|94|95|97|98|99|33|88|71)\s?\d{3}\s?\d{2}\s?\d{2}$"
phonenum = input("Enter your phone number:")
if re.match(andoza,phonenum):
    print("Raqam qabul qilindi!")
else:
    print("Xato raqam!")

#task 5
matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI" \
    "Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
andoza2 = "https?://[^\s]+"
website_adress = re.findall(andoza2, matn)
print(website_adress)