#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:59:32 2023

@author: Tulayev Izzat
"""

import pickle

talaba1 = {'ism':'Hoshim', 'familiya':'Olimov', 'yosh':19}
talaba2 = {'ism':'Odil', 'familiya':'Hakimov', 'yosh':21}

with open('info.pkl', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)
