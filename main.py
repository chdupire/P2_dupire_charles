import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)
results = {}

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.findAll('title')
print(title)

str = str(title)

for i in range(len(str) + 1):
    while str[i] != '>':
        i = i + 1
