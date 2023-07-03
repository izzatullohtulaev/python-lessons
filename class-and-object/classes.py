#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 05:32:32 2023

@author: Tulayev Izzat
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def get_age(self, yil):
        return yil-self.tyil
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. Tug'ilgan yilim {self.tyil}")
talaba1 = Talaba("Olim", "Hakimov", 2000)
talaba2 = Talaba("Ali", "Alimov", 2001)
talaba3 = Talaba("Husan", "Akbarov", 2002)
