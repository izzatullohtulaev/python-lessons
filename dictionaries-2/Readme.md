# 15-DARS. LUG'AT ELEMENTLARI BILAN ISHLASH
Lug'at ichida ro'yxat, lug'at ichida lug'at?

![](https://gblobscdn.gitbook.com/assets%2F-MGbkqs1tROquIT6oqUs%2F-Mc-5yGQPZTBaGoehQdL%2F-Mc-7xpq4Puu3KEjmT0R%2FSD_YT_TG_logo_mini.png?alt=media&token=929fe67b-ec12-4f63-b33e-e9c5e3d8ad09)

Avvalgi darsimizda lug'at bilan tanishdik, va lug'atdagi elementlarga kalit so'z bo'yicha murojat qilishni o'rgandik. Lug'atlar katta yoki kichik bo'lishi mumkin. Ba'zida lug'atdagi barcha kalitlarni yoki qiymatlarni bilmasligimiz mumkin. Bunday holatda qanday yo'l tutamiz? 

Ushbu darsimizda lug'at elementlarini turli usullar yordamida chiqarishni o'rganamiz.

# `.items()` METODI

Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

```
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())
```
> dict_items([('ism', 'alijon'), ('familiya', 'shamshiyev'), ('yosh', 22), ('fakultet', 'matematika'), ('kurs', 4)])

Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.

Batafsil: https://www.youtube.com/watch?v=ArIW3EAtNF4&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus&index=18
