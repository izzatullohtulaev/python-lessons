#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:29:49 2023

@author: Tulayev Izzat
"""

# def multiple(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# print(multiple(2, 3))
# print(multiple(0))

def talaba_info(ism, familiya, **malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1 = talaba_info('aziz', 'nematov')    
talaba2 = talaba_info('olim', 'husanov', yosh=20, kurs=3)    
