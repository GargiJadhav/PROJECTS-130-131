import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

START_URL =  'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'


data = requests.get(START_URL , verify=False)
soup = BeautifulSoup(data.text , 'html.parser')

star_table=soup.find('table')

temp_list=[]

table_rows=star_table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)


name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    print(name)

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)

df.to_csv("data2.csv")
    
















