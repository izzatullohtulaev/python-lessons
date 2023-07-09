#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 20:00:51 2023

@author: Tulayev Izzat
"""

filename = 'intro.py'
try:
    with open(filename) as file:
        text = file.read()
except FileNotFoundError:
    print(f"{filename} nomli fayl mavjud emas")