#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:13:27 2023

@author: Tulayev Izzat
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    def set_bosqich(self, yangi):
        self.bosqich = yangi        
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."    
    def get_name(self):
        return self.ism
    def get_fullname(self):
        return self.ism+' '+self.familiya
    def update_bosqich(self):
        self.bosqich+=1
        return self.bosqich
    def get_bosqich(self):
        return self.bosqich
    def get_lastname(self):
        return self.familiya
    def get_age(self, yil):
        return yil-self.tyil
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. Tug'ilgan yilim {self.tyil}")

class Fan:
    def __init__(self, nom):
        self.nom = nom
        self.talabalar_soni = 0
        self.talabalar = []
    def add_student(self, talaba):
        self.talabalar.append(talaba)
    def get_talabalar(self):
        return [talaba.get_fullname() for talaba in self.talabalar]

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]


talaba1 = Talaba("Husan", 'Qayumov', 2002)
talaba2 = Talaba("Ali", 'Karimov', 2001)
talaba3 = Talaba("Asad", 'Orifov', 2003)
fan1 = Fan('Oliy Matematika')
fan1.add_student(talaba1)
fan1.add_student(talaba2)
fan1.add_student(talaba3)
print(fan1.get_talabalar())














