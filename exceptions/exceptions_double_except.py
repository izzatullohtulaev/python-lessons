#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 20:17:18 2023

@author: Tulayev Izzat
"""

n = input("Son kiriting: ")
try:
    n = int(n)
    x = (20/n)
except ValueError:
    print("Siz butun son kiritmadingiz")
except ZeroDivisionError:
    print("Sonni 0 ga bo'lish mumkin emas")
else:
    print(x)