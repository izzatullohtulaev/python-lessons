"""
@author: Tulayev Izzat
"""
import requests, json

url = "https://nbu.uz/uz/exchange-rates/json/"
response = requests.get(url)
r_json = response.json()
for valyuta in r_json:
    if valyuta['code']=='USD' or valyuta['code']=='EUR' or valyuta['code']=='RUB':
        print(f"{valyuta['title']}({valyuta['code']}): {valyuta['nbu_buy_price']} so'm")
