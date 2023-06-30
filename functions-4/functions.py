#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:54:32 2023

@author: Tulayev Izzat
"""

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

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))

# def summa(*sonlar): 

# def summa(x, y, *sonlar):
#     return x+y+sum(sonlar)
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# print(summa(2))

# def avto_info(kompaniya, model, **malumotlar):
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info('GM', 'Malibu', rang='Qora', yil=2020)
# avto2 = avto_info('GM', 'Gentra', rang='Oq', yil=2018, narx=15000, korobka='avtomat')



















