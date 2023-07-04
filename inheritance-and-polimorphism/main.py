#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 05:32:36 2023

@author: Tulayev Izzat
"""

class Shaxs:
    def __init__(self, ism, familiya, pasport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
    def get_age(self, yil):
        return yil-self.tyil
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.tyil}-yilda tug'ilgan"
class Talaba(Shaxs):
    def __init__(self, ism, familiya, pasport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich       
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."\
            f"Student ID: {self.idraqam}"
class Manzil:
    def __init__(self, kocha, mahalla, tuman, viloyat):
        self.kocha = kocha
        self.mahalla = mahalla
        self.tuman = tuman
        self.viloyat = viloyat
    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.mahalla} mahallasi, {self.kocha} ko'chasi"
        return manzil
talaba1_manzil = Manzil(12, "o'rikzor", "Sergeliasd", "Toshkent")
talaba1 = Talaba('Karim', 'Olimov', 'FD0005554', 2000, 'T2S5F4G87', talaba1_manzil)











