#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:51:59 2023

@author: Tulayev Izzat
"""

user = {
    'username':'izzattulayev',
    'status':'user',
    'email':'izzatullohman@gmail.com',
    'phone':'+998 90 897 88 47'
}
key='email'
try:
    print(f"{key.title()}: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas")