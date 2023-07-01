#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 08:48:41 2023

@author: Tulayev Izzat 
"""

import math, random
# normal function
# def function_name(args):
#     return value

# lambda
# lambda args:value

# length = lambda pi, r:2*pi*r
# print(length(math.pi, 10))

# kvadrat = lambda x, y:x**y
# print(kvadrat(3, 2))

# def daraja(n):
#     return lambda x:x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 ning kvadrati {kvadrat(3)} ga, "
#       f"kubi {kub(3)} ga teng")

sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(sonlar)
# print(ildizlar)

# def daraja2(x):
#     """This function returns square root of x"""
#     return x*x
# print(list(map(daraja2, sonlar)))

# kvadratlar = list(map(lambda x:x*x, sonlar))

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x:x, a, b))
# print(a_plus_b)

sonlar = list(random.sample(list(range(100)), 10))
print(sonlar)

























