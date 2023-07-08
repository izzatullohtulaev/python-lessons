#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 19:56:08 2023

@author: Tulayev Izzat
"""
import json

# 1
x=10
x_json = json.dumps(x)

# 2
y=5.5
y_json = json.dumps(y)

# 3
m = True
m_json = json.dumps(m)

# 4
sonlar = (12, 13, 56, 57, -5)
sonlar_json = json.dumps(sonlar)

# 5
bemor = {
    'ism':'Olim Hakimov',
    'yosh':35,
    'oila':True,
    'farzandlar':('Aziz', 'Hafiz'),
    'allergiya':None,
    'dorilar':[
        {'nom':"Paratsetamol", 'miqdor':1},
        {'nom':"Turmol", 'miqdor':1.5}
    ]
}

bemor_json = json.dumps(bemor)
# print(bemor_json)

bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)

with open('bemor.json', 'w') as file:
    json.dump(bemor_json, file)

with open('sonlar.json', 'w') as file:
    json.dump(sonlar, file)

bemor2 = json.loads(bemor_json)

with open('bemor.json') as file:
    bemor3 = json.load(file)
print(bemor3)















