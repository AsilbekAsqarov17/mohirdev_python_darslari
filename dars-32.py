#Asilbek Asqarov
#Mohirdev python-darslari
#dars-32

class Shaxs:
    __odamlar_soni = 0
    
    def __init__(self, ism , familiya, tyil, passport):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__passport = passport
        Shaxs.__odamlar_soni += 1
        
    def get_password(self):
        return self.__passport
    
    def set_password(self, password):
        self.__passport == password
    
    @classmethod
    def get_num_people(cls):
        return cls.__odamlar_soni
    
    def get_yosh(self, yil):
        yosh = yil - self.tyil
        return yosh
    
    def get_info(self):
        info = f"{self.ism} {self.familiya} "
        info += f"Tu'gilgan yili:{self.tyil} "
        return info
     
    def __repr__(self):
        return f"Shaxs Ismi: {self.ism}, Familiyasi: {self.familiya}, Tyil:{self.tyil}"
    
        
class Talaba(Shaxs):
    __talabalar_soni = 0
    
    def __init__(self,ism, familiya, tyil, passport , talaba_id):
        super().__init__(ism, familiya, tyil, passport)
        self.__talaba_id = talaba_id
        Talaba.__talabalar_soni += 1
        
    def get_id(self):
        return self.__talaba_id
    
    def set_id(self, new_id):
        self.__talaba_id = new_id
    
    @classmethod
    def get_num_students(cls):
        return cls.__talabalar_soni
    
    def get_yosh(self, yil):
        yosh = yil - self.tyil
        return yosh
    
    def __repr__(self):
        return f"Talaba Ismi: {self.ism}, Familiyasi: {self.familiya}, Tyil:{self.tyil}, {self.get_yosh(2026)} yoshda"
    
    def __eq__(self, boshqa_talaba):
        return self.get_yosh(2026) == boshqa_talaba.get_yosh(2026)
    
    
class University:
    
    def __init__(self, uni_name):
        self.uni_name = uni_name
        self.uni_students = []
        
    def __repr__(self):
        return f"University Name: {self.uni_name}"
    
    def add_students(self, *students):
        for student in students:
            if isinstance(student, Talaba):
                self.uni_students.append(student)
            else:
                print("Talaba obyektni kiriting!")
    
    def __len__(self):
        return len(self.uni_students)
    
    def __getitem__(self, index):
        return self.uni_students[index]
    
    def __setitem__(self, index, student):
        if isinstance(student, Talaba):
            self.uni_students[index] = student
    
    def __add__(self, value):
        if isinstance(value, University):
            new_uni = University(f"{self.uni_name}{value.uni_name}")
            new_uni.uni_students = self.uni_students + value.uni_students
            return new_uni
        elif isinstance(value, Talaba):
            self.add_students(value)
        else:
            print(f"Universityga {type(value)} qo'shib bo'lmaydi!")
    
class Fan:
    
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []
        
    def add_studnts(self, student):
        if isinstance(student, Talaba):
            self.talabalar.append(student)
        else:
            print("No such a student!")
        
    def __getitem__(self, student):
        return self.talabalar[student]
    
    def __setitem__(self, index,student):
        if isinstance(student, Talaba):
            self.talabalar[index] = student
            
    def __len__(self):
        return len(self.talabalar)
    
    def __repr__(self):
        return f"Fan nomi: {self.nomi}"
    
    def __add__(self, qiymat):
        if isinstance(qiymat, Talaba):
            self.talabalar.append(qiymat)
            return self
        elif isinstance(qiymat, Fan):
            yangi_fan = Fan(f"{self.nomi} va {qiymat.nomi}")
            yangi_fan.talabalar = self.talabalar + qiymat.talabalar
            return yangi_fan
        
    def __sub__(self, qiymat):
        if isinstance(qiymat, Talaba):
            if qiymat in self.talabalar:
                self.talabalar.remove(qiymat)
        elif isinstance(qiymat, str):
            for t in self.talabalar:
                if t.get_id() == qiymat or t.get_password() == qiymat:
                    self.talabalar.remove(t)
                    break
        return self
        
    def __call__(self, *param):
        if not param:
            return [t.get_info() for t in self.talabalar]
        else:
            for p in param:
                if isinstance(p, Talaba):
                    self.add_student(p)
    
    
    
odam1 = Shaxs("Anvar", "Hasanov", 2003, "AD12345")   
talaba1 =Talaba("Husan", "Hasanov", 2000, "AD12334", "N100011")
talaba2 =Talaba("Anvar", "Husanov", 2000, "AD112233", "N100017")
talaba3 =Talaba("Alijon", "Hasanov", 2000, "AD12334", "N100011")
talaba4 =Talaba("Hasan", "Husanov", 2000, "AD112233", "N100017")
talaba5 =Talaba("Anvar", "Hasanov", 2000, "AD12334", "N100011")
talaba6 =Talaba("Alijon", "Husanov", 2000, "AD112233", "N100017")

uni1 = University("Hasan")
uni2 = University("Husan")

fizika = Fan("Fizika")
fizika + talaba1
fizika + talaba2

uni1.add_students(talaba1, talaba2, talaba3)
uni2.add_students(talaba4, talaba5, talaba6)

print(f"Fizikadagi talabalar: {fizika()}")
fizika - "N100011" 
print(f"O'chirilgandan keyin: {len(fizika)} ta talaba qoldi")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    