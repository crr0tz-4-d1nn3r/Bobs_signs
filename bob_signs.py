# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:57:05 2022

@author: cruffo
"""
import requests
from bs4 import BeautifulSoup
import csv 

url = 'https://bobs-burgers.fandom.com/wiki/Store_Next_Door'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

sayings = soup.find_all('b')

rows = []
for item in sayings:
    rows.append([item.text])
    
with open('bob_signs.csv', 'w', newline='', encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerows(rows) 