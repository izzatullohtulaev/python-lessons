import requests
from googletrans import Translator
tarjimon = Translator()

url = 'https://api.adviceslip.com/advice'
response = requests.get(url)
r_json = response.json()
advice = r_json['slip']['advice']
print(advice)

tarjima = tarjimon.translate(advice, src='en', dest='uz')
print(tarjima.text)