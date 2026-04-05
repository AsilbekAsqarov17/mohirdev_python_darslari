#Asilbek Asqarov
#Mohirdev python-darslari
#dars-37


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, phonenumber, tyil, passport = None):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.phonenumber = phonenumber
        self.tyil = tyil
        self.passport = passport

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"Phone Number:{self.phonenumber}, {self.tyil}-yilda tug'ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    
    
class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, phonenumber, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, phonenumber, tyil)
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

    
