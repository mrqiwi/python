#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.velo-ostrov.ru/shtangi-ganteli/gantel-razbornaya-20-kg-otsinkovannaya-detail')

soup = BeautifulSoup(r.text, 'lxml')

spans = soup.find_all('span', attrs={'class':'text mark-1'})
for span in spans:
    print(span.string)

spans = soup.find_all('span', attrs={'class':'text mark2'})
for span in spans:
    print(span.string)
