#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:34:52 2023

@author: muhammad
"""

# 1
# qiymat = ''
# while qiymat!='exit':
#     qiymat = input("Kitob: ")

# 2
# qiymat = ''
# while qiymat!='exit' or qiymat!='quit':
#     qiymat = input("Yosh: ")
#     if qiymat!='exit':
#         if int(qiymat)<7:
#             print("2 000 so'm")
#         elif int(qiymat)>=7 and int(qiymat)<18:
#             print("3 000 so'm")
#         elif int(qiymat)>=18 and int(qiymat)<65:
#             print("10 000 so'm")
#         else:
#             print("bepul")
#     else:
#         break

# 3
print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = True
while qiymat:
    qiymat = input(savol)
    if qiymat=='exit':
        qiymat = False
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")