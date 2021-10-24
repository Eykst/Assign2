from turtle import pd

import csvfile as csvfile
import np as np
from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://en.wikipedia.org/wiki/Comma-separated_values').text
soup = BeautifulSoup(html_text, 'lxml')
cars = soup.find('table', class_="wikitable")
header = cars.find_all('th')
firstcar = cars.find_all('tr')

csvFile = open("car.csv", 'wt', newline='', encoding='utf=8')
writer = csv.writer(csvFile)

try:
    for cell in firstcar:
        print("**CELL***:", cell)
        th = cell.find_all('th')
        print('**TH**:', th)
        th_data = [col.text.strip('\n') for col in th]
        print('***TH***:', th_data)
        td = cell.find_all('td')
        row = [i.text.replace('\n', '') for i in td]
        writer.writerow(th_data + row)

finally:
    csvFile.close()

# array1 = np.array([firstcar[0], firstcar[1], firstcar[2], firstcar[3], firstcar[4]])
# print(row)

# with open(cars.csv, 'w', newline='') as csvfile:
# headers =
