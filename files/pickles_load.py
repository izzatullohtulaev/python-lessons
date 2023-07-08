#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:13:57 2023

@author: Tulayev Izzat
""" 

import pickle

with open('info.pkl', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)
