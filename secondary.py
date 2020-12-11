import requests
from bs4 import BeautifulSoup
url = 'https://scrapingclub.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')
print(soup)

items = soup.find_all('')