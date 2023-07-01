#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 05:16:59 2023

@author: Tulayev Izzat
"""

def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rang,
        'korobka':korobka,
        'yil':yil,
        'narh':narh
        }
    return avto

def avto_kirit():
    avtolar = []
    print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
    while True:
        kompaniya = input("Kompaniya: ")
        model = input("Model: ")
        rang = input("Rang: ")
        korobka = input("Korobka: ")
        yil = int(input("Yil: "))
        narh = int(input("Narh: "))
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
        takrorlash = input("Yana malumot kiritasizmi(yes/no): ")
        if takrorlash=='no':
            break
    return avtolar
def info_print(avto_info):
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$" )