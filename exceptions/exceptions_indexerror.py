#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:41:45 2023

@author: Tulayev Izzat
"""


mevalar = ['olma', 'anor', 'anjir', 'nok', 'olcha']
try:
    print(mevalar[5])
except IndexError:
    print(f"Ro'yxatda atigi {len(mevalar)} ta element bor")