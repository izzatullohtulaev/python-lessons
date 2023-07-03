#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:17:32 2023

@author: Tulayev Izzat
"""

# https://www.python.sariq.dev
# 1
# class Avto:
#     def __init__(self, model, rang, korobka, narh, kilometr=0):
#         self.model = model
#         self.rang = rang
#         self.kilometr = kilometr
#         self.korobka = korobka
#         self.narh = narh

# 2
class Avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.kilometr = kilometr
        self.korobka = korobka
        self.narh = narh
    def get_info(self):
        return f"{self.korobka} korobka {self.rang} {self.model}. "\
                f"{self.kilometr} kilometr yurgan. {self.narh}$"
    def update_km(self, new):
        if new>0:
            self.kilometr += new
        else:
            print("Cant decrease the distance of the car!")
        return self.kilometr

# # 3
# class Avto:
#     def __init__(self, model, rang, korobka, narh, kilometr=0):
#         self.model = model
#         self.rang = rang
#         self.kilometr = kilometr
#         self.korobka = korobka
#         self.narh = narh
#     def update_km(self, new):
#         if new>0:
#             self.kilometr += new
#         else:
#             print("Cant decrease the distance of the car!")
#         return self.kilometr

# # 4
# class Avtosalon:
#     def __init__(self, nom, manzil, cars_onsale, number_of_cars):
#         self.nom = nom
#         self.manzil = manzil
#         self.cars_on_sale = cars_on_sale
#         self.number_of_cars = number_of_cars

# # 5
# class Avtosalon:
#     def __init__(self, nom, manzil, cars_onsale, number_of_cars):
#         self.nom = nom
#         self.manzil = manzil
#         self.cars_on_sale = cars_on_sale
#         self.number_of_cars = number_of_cars
#     def add_car(self, car):
#         self.cars_on_sale.append(car)
#         return self.cars_on_sale

# 6
# class Avtosalon:
#     def __init__(self, nom, manzil, cars_on_sale, number_of_cars):
#         self.nom = nom
#         self.manzil = manzil
#         self.cars_on_sale = cars_on_sale
#         self.number_of_cars = number_of_cars
#     def add_car(self, car):
#         self.cars_on_sale.append(car)
#         self.number_of_cars+=1
#         return self.cars_on_sale
#     def tanishtir(self):
#         return [car.get_info() for car in self.cars_on_sale]    