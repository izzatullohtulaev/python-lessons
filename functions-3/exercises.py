#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:02:37 2023

@author: Tulayev Izzat
"""

# 1
# def return_capitalize(words):
#     for i in range(len(words)):
#         words[i] = words[i].title()
# ismlar = ['ali', 'vali', 'hasan', 'olim', 'zokir']
# return_capitalize(ismlar)
# print(ismlar)

# 2
# def return_capitalize(words):
#     words2 = words[:]
#     for i in range(len(words2)):
#         words2[i] = words2[i].title()
#     return words2
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = return_capitalize(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# 3
# def bahola(ismlar):
#     baholar = {}
#     ismlar_clone = ismlar[:]
#     while ismlar_clone:
#         ism = ismlar_clone.pop()
#         baho = int(input(f"Talaba {ism.title()}ning bahosi: "))
#         baholar[ism]=baho
#     return baholar
# talabalar = ['olim', 'ali', 'vali', 'zokir', 'jobir']
# baholar = bahola(talabalar)
# print(baholar)