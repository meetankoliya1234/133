import plotly.express as px
import csv

rows = []

with open ("Star_with_gravity.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
        
headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows)

star_mass = []
star_radius = []
star_gravity = []

for star_data in star_data_rows:
    star_mass.append(star_data[7])
    star_radius.append(star_data[8])
    star_gravity.append(star_data[9])
    
fig = px.bar(x = star_mass, y = star_radius)
fig.show()

fig2 = px.scatter(x = star_mass, y = star_radius)
fig2.show()

fig3 = px.line(x = star_mass, y = star_radius)
fig3.show()

fig4 = px.bar(x = star_mass, y = star_gravity)
fig4.show()

fig5 = px.scatter(x = star_mass, y = star_gravity)
fig5.show()

fig6 = px.line(x = star_mass, y = star_gravity)
fig6.show()