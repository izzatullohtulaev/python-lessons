#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 07:35:14 2023

@author: Tulayev Izzat
"""
import pickle

# 1
# with open('pi_million_digits.txt', 'r') as file:
#     PI = file.read()
# PI = PI.replace('\n', '')
# yosh = input("Tug'ilgan sanangiz: ")
# yosh = yosh.replace('.', '')
# if yosh in PI:
#     print("Uchraydi!")
# else:
#     print("Uchramaydi!")

# 2
# with open('pi_million_digits.txt', 'r') as file:
#     PI = file.read()
# PI = PI.replace('\n', '')
# PI = PI.strip()
# PI = float(PI)
# with open('pi_float.pkl', 'wb') as file:
#     pickle.dump(PI, file)
# with open('pi_float.pkl', 'rb') as file:
#     pi = pickle.load(file)
# print(pi)

# 3

while True:
    malumot = input("Malumot kiriting: ")
    with open('malumotlar.txt', 'a') as file:
        file.write(malumot+'\n')
    takror = input("Davom ettirasizmi? (yes/no)\n>>>")
    if takror=='no':
        break
with open('malumotlar.txt', 'r') as file:
    malumotlar = file.readlines()
    for line in malumotlar:
        print(line.rstrip())
















