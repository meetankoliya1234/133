from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance_of_Star','Mass_of_Star','Radius_of_Star','Luminosity_of_Star'])
print(df)

df = df[df['Distance_of_Star'].notna()]
df = df[df['Mass_of_Star'].notna()]
df = df[df['Radius_of_Star'].notna()]
df = df[df['Luminosity_of_Star'].notna()]

df.to_csv('bright_stars.csv')