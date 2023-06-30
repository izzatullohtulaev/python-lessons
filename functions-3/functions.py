#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 08:07:43 2023

@author: muhammad
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = int(input(f"Talaba {ism.title()}ning bahosi: "))
        baholar[ism]=baho
    return baholar
talabalar = ['olim', 'ali', 'vali', 'zokir', 'jobir']
baholar = bahola(talabalar[:])
print(baholar)
