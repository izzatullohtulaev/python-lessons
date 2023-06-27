# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:29:45 2023

@author: ENVY
"""

talaba_0 = {
    'ism':'alijon',
    'familya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
}
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print("Kalit: "+kalit)
#     print("Qiymat:", qiymat,'\n')

# telefonlar = {
#     'ali':'iphone x',
#     'hasan':'pixel 6',
#     'olim':'s20',
#     'orif':'mi 10 pro',
#     'anvar':'realme 30c'
#     }
# for k, q in telefonlar.items():
#     print(k.title(), q, "ishlatadi")

# .keys()
mahsulotlar = {
    'olma':26000,
    'anor':15000,
    'uzum':12000,
    'banan':45000,
    'anjir':23000,
    'qulupnay':45000
    }
# print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

bozorlik = ['anor', 'uzum', 'olcha', 'shaftoli', 'banan']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(mahsulot.title(), mahsulotlar[mahsulot], "so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print("Iltimos, do'koningizga", buyum, "ham olib keling")

# # Lug'atdagi elementlarni tartiblab chiqarish
# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
    # print(mahsulot.title())

# # .values()
# print(telefonlar.values())

telefonlar = {
    'ali':'iphone x',
    'hasan':'pixel 6',
    'olim':'s20',
    'orif':'mi 10 pro',
    'anvar':'realme 30c',
    'umar':'iphone x',
    'vali':'pixel 6',
    'husan':'realme 30c'
    }

print("Foydalanuvchilarimiz quyidagi telefonlarni ishlatishadi: ")
for telefon in telefonlar.values():
    print(telefon)

# .set()
print("Foydalanuvchilarimiz quyidagi telefonlarni ishlatishadi: ")
for telefon in set (telefonlar.values()):
    print(telefon)

toys = {'ball', 'car', 'bell', 'bear', 'car', 'ball'}








