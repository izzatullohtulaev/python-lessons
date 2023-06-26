# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:24:38 2023

@author: ENVY
"""

# 1
# son = int(input("Juft son kiriting: "))
# if son%2==0:
#     print("Rahmat!")
# else:
#     print("Siz juft son kiritmadingiz")

# 2
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4 or yosh>=60:
#     print("Sizga kirish bepul")
# elif yosh<18:
#     print("Sizga kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm")

# 3
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a>b:
#     print(a, '>', b)
# elif a<b:
#     print(a, '>', b)
# else:
#     print(a, '=', b)

# 4
# mahsulotlar = ['karam', 'sabzi', 'olma', 'piyoz', 'kartoshka', 'pomidor', 
#                'sarimsoqpiyoz', 'qatiq', 'qalampir', 'guruch']
# savat = []
# for i in range(5):
#     savat.append(input(f"{i+1}-mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} bizning do'konimizda bor")
#     else:
#         print(f"{mahsulot} bizning do'konimizda mavjud emas")

# 5
# mahsulotlar = ['karam', 'sabzi', 'olma', 'piyoz', 'kartoshka', 'pomidor', 
#                 'sarimsoqpiyoz', 'qatiq', 'qalampir', 'guruch']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for i in range(5):
#     savat.append(input(f"{i+1}-mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if len(mavjud_emas)==0:
#     print("Hamma mahsulotlar bor")
# else:
#     print("Quyidagi mahsulotlar do'konimizda mavjud emas:")
#     for n in range(len(mavjud_emas)):
#         print(mavjud_emas[n])

# 6
# foydalanuvchilar = ['anvar', 'olimjon68', 'izzatullohman', 'boyka777', 'afensiyus']
# login = input("Login tanlang: ")
# if login in foydalanuvchilar:
#     print("Yangi login tanlang, bu login boshqa foydalanuvchi tomonidan o'zlashtirilgan")
# else:
#     print("Xush kelibsiz!")

# 7
# son = int(input("Son kiriting: "))
# raqamlar = list(range(2, 11))
# for raqam in raqamlar:
#     if son%raqam==0:
#         print(f"Siz kiritgan son {raqam} soniga qoldiqsiz bo'linadi")