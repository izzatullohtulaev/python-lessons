#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:11:21 2023

@author: Tulayev Izzat
"""

def get_fullname(ism, familiya, otasi=''):
    if otasi:      
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

# print(get_fullname('olim', 'hakimov'))