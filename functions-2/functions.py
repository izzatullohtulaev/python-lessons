#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:56:51 2023

@author: Tulayev Izzat
"""

# def make_fullname(ism, familiya):
#     """To'liq ism yasovchi funksiya"""
#     return f"{ism.title()} {familiya.title()}"
# # print(make_fullname('izzat', 'tulayev'))
# talaba1 = make_fullname('olim', 'hakimov')
# talaba2 = make_fullname('hasan', 'husanov')
# print(f"Darsga kelmagan talabalar: {talaba1}, {talaba2}")

# def make_fullname(ism, familiya, otasining_ismi=''):
#     if otasining_ismi:
#         return f"{ism.title()} {familiya.title()} {otasining_ismi.capitalize()}"
#     else:
#         return f"{ism.title()} {familiya.title()}"
# talaba1 = make_fullname('izzat', 'tulayev')
# talaba2 = make_fullname('alisher', 'usmonov', 'olimovich')

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'korobka':korobka,
#         'yili':yili,
#         'narhi':narhi
#         }
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'Qora', 'avtomat', 2020)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'mexanika', 2018, 15000)
# avtolar = [avto1, avto2]
# print("Onlayn bozorda bor avtomashinalar: ")
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = "Nomalum"
#     print(avto['rang'], avto['model'],". Narhi: ", narh)

# def oraliq(min, max, qadam):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# print(oraliq(0, 10, 2 ))


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yili':yili,
        'narhi':narhi
        }
    return avto
avtolar = []
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
while True:
    kompaniya = input("Kompaniya: ")
    model = input("Model: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Yili: ")
    narhi = input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili))
    takrorlash = input("Yana malumot kiritasizmi(yes/no): ")
    if takrorlash=='no':
        break
print("Satimizdagi avtomobillar ro'yxati:")    
for avto in avtolar:
    print(avto['rang'], avto['model']+". Narhi:", avto['narhi'])














