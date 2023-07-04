#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 06:25:00 2023

@author: Tulayev Izzat
"""

class Talaba():
    def __init__(self, ism, familiya, pasport, tyil, idraqam):
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich       
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."\
            f"Student ID: {self.idraqam}"
    def join_subject(self, fan_nomi):
        self.fanlar.append(fan_nomi)
    def remove_subject(self, fan_nomi):
        if fan_nomi not in self.fanlar:
            print("Siz bu fanga yozilmagansiz!")
        else:
            self.fanlar.remove(fan_nomi)
class Fan:
    def __init__(self, nom):
        self.nom = nom
    def get_name(self):
        return self.nom

fan1 = Fan('Oliy Matematika')
fan2 = Fan('Biologiya')
fan3 = Fan('Kompyuter Savodxonligi')
