#Asilbek Asqarov
#Mohirdev python-darslari
#dars-30

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Fan:
    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi
    def get_fan_name(self):
        return self.fan_nomi
        

class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    def fanga_yozil(self,fan_obyekti):
        self.fanlar.append(fan_obyekti)
    
    def remove_fan(self, fan_nomi):
        if fan_nomi in self.fanlar:
            self.fanlar.remove(fan_nomi)
        else:
            print("Siz bu fanga yozilmagansiz")
        
    def get_fanlar(self):
        return [fan.fan_nomi for fan in self.fanlar]

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
class Professsor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)
        self.fanlari = []
        self.guruhlari = 0
    def add_fanlari(self, fan_obyekti):
         self.fanlari.append(fan_obyekti)
         self.guruhlari += 1
    
    def get_fanlari(self):
        return [fan.fan_nomi for fan in self.fanlari]
    
    def get_guruhlari(self):
        return self.guruhlari
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_fanlari()}-fanlardan dars beradi. Guruhlari: {self.get_guruhlari()}"
        return info

class Foydalanuvchi(Shaxs):
    def __init__(self, ism , familiya, passport, tyil, username, email, password):
        super().__init__(ism, familiya, passport, tyil)
        self.username = username
        self.email = email
        self.password  = 12345
        self.is_logged_in =False
        self.login_fails = 0
    
    def login(self, username, password):
        if self.username == username and self.password ==password:
            self.is_logged_in = True
            return "Access Granted!"
        self.login_fails +=1
        return "Login yoki Password Xato!"
    
    def login_fails(self):
        return self.login_fails
    
    def update_email(self, new_email):
        self.email = new_email
        
    def get_info(self):
        """Profil haqida ma'lumot (Polimorfizm)"""
        info = f"Foydalanuvchi: {self.username}\n"
        info += f"To'liq ism: {self.ism} {self.familiya}\n"
        info += f"Email: {self.email}"
        return info
    
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, username, email,password, level):
        super().__init__(ism, familiya, passport, tyil, username, email, password)
        self.logs = []
        
    def ban_user(self, foydalanuvchi):
        logins = self.login_fails
        if logins <= 3:
            xabar  =f"{foydalanuvchi.username} bloklandi"
            self.logs.append("{self.foydalnuvchi}Banned")
            return xabar
    

matematika = Fan("Oliy Matematika")
dasturlash = Fan("Dasturlash")
fizika = Fan("Fizika")

talaba1 = Talaba("Alijon", "Valiyev", "AA1234567", 2005, "N100011")

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(dasturlash)


print(f"{talaba1.ism}, shu fanlarga yozilgan {talaba1.get_fanlar()}")

talaba1.remove_fan(matematika)
talaba1.remove_fan(fizika)

print(f"{talaba1.ism}, shu fanlarga yozilgan {talaba1.get_fanlar()}")

prof1 = Professsor("Hasan", "Husanov", "AH12345", 1964)

prof1.add_fanlari(matematika)
prof1.add_fanlari(fizika)

print(prof1.get_info())

user1 = Foydalanuvchi("Husan", "Hasanov", "AF12345", 2003, "husan2003", "husan@gmail.com",12345)
admin1 = Admin("Vali", "Aliyev", "AB98765", 1990, "admin01", "admin@site.uz", 777, "Super")

user1.login("husan2003", "xato_parol")
user1.login("husan2003", "xato_parol")
user1.login("husan2003", "xato_parol")

print(admin1.ban_user(user1))







        
        
        
    
    
    