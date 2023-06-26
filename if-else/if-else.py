# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
        
# ism = 'Ali'
# ism.lower() == 'ali'

# ism = input("Ismingiz nima?: ")
# if(ism.lower() != 'ali'):
#     print(f"Uzr {ism.title()}, biz Alini kutyapmiz")
# else:
#     print("Salom Ali")

# javob = float(input("12x6 nechchi?\n>>>"))
# if(javob != 72):
#     print("Noto'g'ri javob!")

# yosh = int(input("Yoshingiz nechida?\n>>>"))
# if yosh>=18:
#     print("Xush kelibsiz")
# else:
#     print("Kirish faqat 18 yoshga to'lganlarga mumkin.")

# login = input("Yangi login tanlang: ")
# if len(login)>=5:
#     print("Login yangilandi")
# else:
#     print("Login matni 5 harfdan ko'proq bo'lishi kerak")

yil = int(input("Tug'ilgan yilingizni kiriting?\n>>>"))
yosh = 2023-yil
if yosh<18:
    print(f"Siz {yosh} yoshda ekansiz.")
    print("Sizga kirish mumkin emas.")
else:
    print("Xush kelibsiz!")