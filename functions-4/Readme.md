# 22-DARS. MOSLASHUVCHAN FUNKSIYA (`*args`, `**kwargs`) 

`*args` va `**kwargs` bilan tanishamiz

![](https://gblobscdn.gitbook.com/assets%2F-MGbkqs1tROquIT6oqUs%2F-Mc-5yGQPZTBaGoehQdL%2F-Mc-7xpq4Puu3KEjmT0R%2FSD_YT_TG_logo_mini.png?alt=media&token=929fe67b-ec12-4f63-b33e-e9c5e3d8ad09)

# MOSLASHUVCHAN FUNKSIYA

Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar sonini aniq bilmasangiz, Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyati bor.

## `*args` USULI

Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona qiymatlar ko'rinishida uzatilsa, funksiya yaratishda argumentdan avval yulduzcha qo'yiladi (`*arguments`). 
Quyidagi misolni ko'raylik. `summa()`nomli funksiyamiz istalgancha sonlarni qabul qilib oladi, va ularning yi'gindisi hisoblaydi:
In [1]:
```
def summa(*sonlar):
      """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
      yigindi = 0
      for son in sonlar:
          yigindi += son
      return yigindi
```

Batafsil: https://www.youtube.com/watch?v=uzNp5XNOZ_I
