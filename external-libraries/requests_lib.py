import requests
from pprint import pprint

# response = requests.get('https://kun.uz/news/main')
# pprint(response.text)

# Restcountries API
response = requests.get("http://api.aladhan.com/v1/calendar/:year/:month")
r_json = response.json()
r_json['data'] = [41.2321651, 65.32165464, 2023]
print(r_json['data'])