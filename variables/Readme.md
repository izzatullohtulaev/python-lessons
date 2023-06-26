04-DARS. O'ZGARUVCHILAR
Pythonda o'zgaruvchilar bilan ishlashni o'rganamiz

![alt text](https://gblobscdn.gitbook.com/assets%2F-MGbkqs1tROquIT6oqUs%2F-MLgatxylpGtKv0LiiV1%2F-MLgfAikZVcuHp-u5tHP%2FPic-of-labeled-boxes.jpg?alt=media&token=4bdf283d-c483-4158-8ce3-90527594f363)

O'ZGARUVCHI (VARIABLE)
O'zgaruvchi — kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy. Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi narsani esa qiymat deb tasavvur qilish mumkin. Pythonda qiymatlar son, matn, ro'yxat va hokazo ko'rinishida bo'lishi mumkin.

Quyidagi misolga e'tibor bering, biz 2 ta o'zgaruvchi yaratdik (ism va yosh) va ularga qiymatlar yukladik (Pythonda boshqa tillardagi ka'bi o'zgaruvchilarni avvaldan e'lon qilish yo'q):

ism = "Abdulloh"
yosh = 25
print(ism)
print(yosh)
Abdulloh
25
O'zgaruvchi (variable) bunday deyilishiga sabab, uning qiymati istalgan vaqt o'zgartirilishi mumkin:

ism = "Abdulloh"
print(ism)
ism="Muhammad"
print(ism)
Abdulloh
Muhammad
Yuqoridagi misolda ism nomli o'zgaruvchiga avval Abdulloh keyin esa Muhammad qiymatlarini berdik.

O'ZGARUVCHILARNI NOMLASH
O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:

O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)
Qo'shimcha qoida sifatida:

O'zgaruvchi nomini kichik harflar bilan yozing.
O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (_) bilan ajrating (ism_sharif="Anvar Narzullaev")
O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, d="Korea" emas davlat = "Korea" va hokazo)
