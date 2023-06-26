#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:45:03 2023

@author: muhammad
"""

car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}

mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':10000}
# print(f"Olma narhi {mevalar['olma']} so'm")

# Lug'atda istalgan malumot turini saqlash mumkin
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2003}
# print(f"{talaba_0['ism'].title()}, \
#   {talaba_0['t_yil']}-yilda tug'ilgan, \
#   {talaba_0['yosh']} yoshda")
  
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'

# # Bo'sh lug'at
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs talabasi")

# Lug'atdan kalit so'z-qiymatni o'chirib tashlash
talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2003}
del talaba_0['yosh']
# print(talaba_0)

# Lug'atni bir nechta qatorda yozish
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s20',
    'hasan':'nokia 3310',
    'husan':'redmi 10 pro',
    'anvar':'pixel 3xl'
    }

phone = telefonlar.get('olim', "Bunday ism mavjud emas")








