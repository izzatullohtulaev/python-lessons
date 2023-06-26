# 09-DARS. `for` TAKRORLASH OPERATORI
`for` operatori bilan ishlashni o'rganamiz

![](https://gblobscdn.gitbook.com/assets%2F-MGbkqs1tROquIT6oqUs%2F-Mc-5yGQPZTBaGoehQdL%2F-Mc-7xpq4Puu3KEjmT0R%2FSD_YT_TG_logo_mini.png?alt=media&token=929fe67b-ec12-4f63-b33e-e9c5e3d8ad09)

for BILAN TANISHAMIZ
Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo.

Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi.

Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
	print(mehmon)
Ali
Vali
Hasan
Husan
Olim
Keling, kodni tahlil qilaylik:

1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.
2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib uni yangi, mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin. Biz tushunarli bo'lishi uchun mehmon deb atadik)
3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik. Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
"For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.

Yuqoridagi kodni oddiy tilga tarjima qilsak "Mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi.

