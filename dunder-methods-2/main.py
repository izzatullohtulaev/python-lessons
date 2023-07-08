#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:00:16 2023

@author: muhammad
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
        return f"{self.make} {self.model}"
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
        return f"{self.name}"
    def __getitem__(self, index):
        return self.avtolar[index]
    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat
    def __add__(self, another):
        if isinstance(another, AvtoSalon):
            new_salon = AvtoSalon(f"{self.name} {another.name}")
            new_salon.avtolar = self.avtolar+another.avtolar
            return new_salon
        elif isinstance(another, Avto):
            self.add_car(another)
    def __call__(self, *qiymatlar):
        if qiymatlar:
            for qiymat in qiymatlar:
                self.avtolar.append(qiymat)
        else: return [avto for avto in self.avtolar]
    def add_car(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting!")

salon1 = AvtoSalon("AutoRoom")
salon2 = AvtoSalon("iWash")

avto1 = Avto("Porsche", "911", "sariq", 2014, 70_000)
avto2 = Avto("BMW", "M5 CS", "qora", 2023, 70_000)
avto3 = Avto("GM", "Nexia", "qizil", 2023, 13_000)
avto4 = Avto("Merc", "GLS", "oq", 2020, 80_000)

salon1(avto1, avto2)
salon2(avto3, avto4)



 