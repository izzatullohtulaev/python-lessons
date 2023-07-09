#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:34:18 2023

@author: Izzat Tulayev
"""

x = 5
y = 10
try:
    z = (y/(x-5))
except ZeroDivisionError:
    print("Sonni 0 ga bo'lish mumkin emas!")
else:
    print(z)