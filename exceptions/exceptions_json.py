#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 20:07:29 2023

@author: muhammad
"""
import json

files = ['talaba1.json', 'talaba2.json', 'talaba3.json', 'talaba4.json']
for filename in files:
    try:
        with open(filename) as file:
            talaba = json.load(file)
    except FileNotFoundError:
        pass
    else:
        print(talaba)        