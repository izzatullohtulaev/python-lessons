import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://kun.uz/news/main"
response = requests.get(url)
# pprint(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
news = soup.find_all(class_='news-title')
for i in range(len(news)):
    print(news[i].text)