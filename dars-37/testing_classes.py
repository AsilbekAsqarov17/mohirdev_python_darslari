import unittest
from dars_37_classes import Shaxs, Talaba



class TestCases(unittest.TestCase):
    
    def setUp(self):
        ism = 'Hasan'
        familiya = 'Husanov'
        phonenumber = 1234567
        tyil = 2000
        self.passport = 'AD12345'
        self.shaxs1 = Shaxs(ism, familiya, phonenumber, tyil)
        self.shaxs2 = Shaxs(ism, familiya, phonenumber, tyil, passport=self.passport )
        
    def test_created(self):
        
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.phonenumber)
        self.assertIsNotNone(self.shaxs1.tyil)
        self.assertIsNone(self.shaxs1.passport)
        
        self.assertEqual(25, self.shaxs1.get_age(2025))
        self.assertEqual(self.passport, self.shaxs2.passport)
        
    def test_get_info(self):
        shaxs_info = f"Hasan Husanov Phone Number:1234567, 2000-yilda tug'ilgan"
        self.assertEqual(shaxs_info, self.shaxs1.get_info())
        




unittest.main()
    
