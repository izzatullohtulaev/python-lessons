#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:31:28 2023

@author: muhammad
"""
# 1
# shaxs1 = {
#     'ism':'amir temur',
#     'tyil':1336,
#     'tjoy':"xo'jai-ilg'or qishlog'i",
#     'umr':70
#     }
# shaxs2 = {
#     'ism':'alisher navoiy',
#     'tyil':1441,
#     'tjoy':"hirot shahri",
#     'umr':60
#     }
# shaxs3 = {
#     'ism':'bobur mirzo',
#     'tyil':1483,
#     'tjoy':"andijon viloyati",
#     'umr':47
#     }
# shaxs4 = {
#     'ism':"ahmad farg'oniy",
#     'tyil':798,
#     'tjoy':"farg'ona shahri",
#     'umr':67
#     }
# shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]
# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()} {shaxs['tyil']}-yilda {shaxs['tjoy'].capitalize()}da tug'ilgan")

# 2
shaxs1 = {
    'ism':'amir temur',
    'tyil':1336,
    'tjoy':"xo'jai-ilg'or qishlog'i",
    'umr':70,
    'asarlar':['temur tuzuklari']
    }
shaxs2 = {
    'ism':'alisher navoiy',
    'tyil':1441,
    'tjoy':"hirot shahri",
    'umr':60,
    'asarlar':['hamsa', 'sittai zaruria', 'arbain', 'mahbubul qulub']
    }
shaxs3 = {
    'ism':'bobur mirzo',
    'tyil':1483,
    'tjoy':"andijon viloyati",
    'umr':47,
    'asarlar':['boburnoma', 'mubayyin']
    }
shaxs4 = {
    'ism':"ahmad farg'oniy",
    'tyil':798,
    'tjoy':"farg'ona shahri",
    'umr':67,
    'asarlar':['kitab fi javami', 'ilm al nujum']
    }
shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()}ning asarlari:")
#     for asar in shaxs['asarlar']:
#         print("\t", asar.title())

# 3
ali = {
       'ism':'ali',
       'kinolar':[]
       }
vali = {
        'ism':'vali',
        'kinolar':[]
        }
hasan = {
       'ism':'hasan',
       'kinolar':[]
       }
husan = {
        'ism':'husan',
        'kinolar':[]
        }
dostlar = [ali, vali, hasan, husan]
# for dost in dostlar:
#     print(f"{dost['ism'].title()}ning sevimli kinolarini kiriting: ")
#     for n in range(3):
#         dost['kinolar'].append(input("\t")) 
# for dost in dostlar:
#     print(f"{dost['ism'].title()}ning sevimli kinosi: ")
#     for kino in dost['kinolar']:
#         print(kino)

# 4
davlat1 = {
    'nomi':'uzbekiston',
    'poytaxt':'toshkent',
    'hududi':449000,
    'aholi':30_000_000,
    'valyuta':'som'
    }
davlat2 = {
    'nomi':'aqsh',
    'poytaxt':'vashington',
    'hududi':10_000_000,
    'aholi':327_000_000,
    'valyuta':'dollar'
    }
davlat3 = {
    'nomi':'rossiya',
    'poytaxt':'moskva',
    'hududi':17_09_82_46,
    'aholi':144_000_000,
    'valyuta':'rubl'
    }
davlat4 = {
    'nomi':'malayziya',
    'poytaxt':'kuala-lumpur',
    'hududi':32_97_50,
    'aholi':25_000_000,
    'valyuta':'ringgit'
    }
davlatlar = [davlat1, davlat2, davlat3, davlat4]
# for davlat in davlatlar:
#     print(f"{davlat['nomi'].title()}ning poytaxti {davlat['poytaxt'].title()}")
#     print(f"Hududi: {davlat['hududi']} kv.km")
#     print(f"Aholisi: {davlat['aholi']}")
#     print(f"Valyutasi: {davlat['valyuta']}\n\n")

# 5
# davlat1 = {
#     'nomi':'uzbekiston',
#     'poytaxt':'toshkent',
#     'hududi':449000,
#     'aholi':30_000_000,
#     'valyuta':'som'
#     }
# davlat2 = {
#     'nomi':'aqsh',
#     'poytaxt':'vashington',
#     'hududi':10_000_000,
#     'aholi':327_000_000,
#     'valyuta':'dollar'
#     }
# davlat3 = {
#     'nomi':'rossiya',
#     'poytaxt':'moskva',
#     'hududi':17_09_82_46,
#     'aholi':144_000_000,
#     'valyuta':'rubl'
#     }
# davlat4 = {
#     'nomi':'malayziya',
#     'poytaxt':'kuala-lumpur',
#     'hududi':32_97_50,
#     'aholi':25_000_000,
#     'valyuta':'ringgit'
#     }


davlatlar = {
    "uzbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    }
}


# davlatlar = [davlat1, davlat2, davlat3, davlat4]
davlat = input("Biror-bir davlat nomi: ")
if davlat.lower() in davlatlar.keys():
    info = davlatlar[davlat]
    print(f"{davlat.capitalize()}ning poytaxti {info['poytaxt']}\n"
    f"Hududi: {info['maydon']} kv.km\n"
    f"Aholisi: {info['aholi']}\n"
    f"Valyutasi: {info['pul birligi']}\n\n")
else:
    print("Bunaqa davlat topilmadi")













