# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:57:05 2022
"""

import requests
from bs4 import BeautifulSoup
import csv 

urls = ['https://bobs-burgers.fandom.com/wiki/Store_Next_Door',
        'https://bobs-burgers.fandom.com/wiki/Pest_Control_Truck']

sayings = []
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    temp = soup.find_all('b')    
    
    for item in temp:
        sayings.append([item.text])
    
    
with open('bob_signs.csv', 'w', newline='', encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerows(sayings) 