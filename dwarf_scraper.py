from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')

temp_list= []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Dwarf_names = []
Distance =[]
Mass = []
Radius =[]
Constellation = []

for i in range(1,len(temp_list)):
    Dwarf_names.append(temp_list[i][0])
    Constellation.append(temp_list[i][1])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
    
df = pd.DataFrame(list(zip(Dwarf_names,Constellation,Distance,Mass,Radius)),columns=['Dwarf_name','Constellation','Distance_of_Dwarf','Mass_of_Dwarf','Radius_of_Dwarf'])
print(df)

df = df[df['Distance_of_Dwarf'].notna()]
df = df[df['Mass_of_Dwarf'].notna()]
df = df[df['Radius_of_Dwarf'].notna()]

df.to_csv('brown_dwarfs.csv')