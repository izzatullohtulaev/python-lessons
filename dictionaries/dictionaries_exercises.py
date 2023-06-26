#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:56:21 2023

@author: muhammad
"""

# 1
mushuk1 = {'ism':'boyka', 't_yil':2019, 'viloyat':'qashqadaryo'}
mushuk2 = {'ism':'milana', 't_yil':2019, 'viloyat':'boshqadaryo'}
izzat = {'ism':'izzat tulayev', 't_yil':2009, 'viloyat':'qashqadaryo'}
# print("1-mushugimni ismi", mushuk1['ism'].title(), ",", mushuk1['t_yil'], "yilda", mushuk1['viloyat'].title(), "viloyatida tug'ilgan. Malumoti yo'q")
# print("2-mushugimni ismi", mushuk2['ism'].title(), ",", mushuk2['t_yil'], "yilda", mushuk2['viloyat'].title(), "viloyatida tug'ilgan. Malumoti o'rta maxsus")
# print("Ismim", izzat['ism'].title(), ",", izzat['t_yil'], "yilda", izzat['viloyat'].title(), "viloyatida tug'ilgan. Malumoti oliy")

# 2
# sevimli_taom = {'boyka':'morojna', 'milana':"go'sht", 'izzat':"tuxum"}
# print("Boykaning sevimli taomi "+sevimli_taom['boyka'])
# print("Milananing sevimli taomi "+sevimli_taom['milana'])
# print("Mening sevimli taomi "+sevimli_taom['izzat'])

# 3
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
word = input("Word: ")
if word in py_dict:
    print(word.title(), "so'zi", py_dict[word].title(), "deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas")