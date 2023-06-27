#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:52:29 2023

@author: muhammad
"""

# 1
py_dict = {'integer':'butun son',
           'float':"o'nlik son",
           'string':'matn',
           'boolean':'mantiqiy malumot turi',
           'list':"ro'yxat",
           'dictionary':"lug'at",
           'python':'dasturlash tili',
           'spyder':'dasturlash muhiti',
           'if-else':'tarmoqlanuvchi operator',
           'if-elif-else':"ko'p tarmoqli operator"
           }
# for kalit, qiymat in py_dict.items():
#     print(kalit, "-", qiymat)

# 2
davlat_poytaxt = {
    "O'zbekiston":"Toshkent",
    'Rossiya':'Moskva',
    'Meksiko':'Mexika',
    'Usa':'Vashington',
    'Qozog\'iston':'Ostona',
    'Turkmaniston':'Ashg\'obod',
    'Afg\'oniston':'Qobul',
    "Qirg'iziston":'Bishkek',
    "Portugaliya":'Lissabon',
    "Turkiya":'Anqara',
    "Misr":'Qohira'
    }
# print("Dunyo davlatlari:")
# for davlat in sorted(davlat_poytaxt):
#     print(davlat.upper())

# print("\nDavlatlarning poytaxtlari")
# for poytaxt in sorted(davlat_poytaxt.values()):
#     print(poytaxt.title())

# 3
# davlat = input("Davlat: ")
# if davlat.title() in davlat_poytaxt.keys():
#     davlat = davlat.title()
#     print("Poytaxt: "+davlat_poytaxt[davlat])
# else:
#     print("Kechirasiz, bizning lug'atda bunday davlat yo'q!")

# 4
mahsulotlar = {
    'olma':26000,
    'anor':15000,
    'uzum':12000,
    'banan':45000,
    'anjir':23000,
    'qulupnay':45000
    }
bozorlik = []
for i in range(3):
    bozorlik.append(input(f"{i+1}-mahsulot:"))
for narsa in bozorlik:
    if narsa in mahsulotlar:
        print(f"{narsa} bizda {mahsulotlar[narsa]} so'm")
for mahsulot in bozorlik:
    if mahsulot not in mahsulotlar:
        print(f"Kechirasiz, {mahsulot} yo'q!")










