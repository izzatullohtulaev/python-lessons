#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 23:55:58 2023

@author: Tulayev Izzat
"""
import json

# 1
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
# print(data_json)

# 2
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 

# 3
with open('exercises_json.json', 'w') as file:
    json.dump(talaba_json, file)
    json.dump(data_json, file)

# 4
with open('students.json') as file:
    data = json.load(file)
for i in data['student']:
    # print(data['student'][i])
    print(f"{i['name']} {i['lastname']}, {i['year']}-kurs talabasi, {i['faculty']} fakultet talabasi")