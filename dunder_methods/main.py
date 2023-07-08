#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 18:08:15 2023

@author: Tulayev Izzat
"""

class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    # def __str__(self):
    #     return f"Avto: {self.make} {self.model}"
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    def __eq__(self, y):
        return self.narh==y.narh
    def __lt__(self, y):
        return self.narh<y.narh
    def __le__(self, y):
        return self.narh<=y.narh
    
class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def __getitem__(self, index):
        return self.avtolar[index]
    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat
    def add_car(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting!")

salon1 = AvtoSalon("AutoRoom")

avto1 = Avto("Porsche", "911", "sariq", 2014, 70_000)
avto2 = Avto("BMW", "M5 CS", "qora", 2023, 70_000)
avto3 = Avto("GM", "Nexia", "qizil", 2023, 13_000)
avto4 = Avto("Merc", "GLS", "oq", 2020, 80_000)
# print(avto1)