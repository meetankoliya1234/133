import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv

rows = []

with open("Star_with_gravity.csv", "r") as f:
    csvreader = csv.reader(f)
    for data in csvreader:
        rows.append(data)
    
headers = rows[0]
star_data = rows[1:]

rows2 = []

with open("cleaned_final.csv", "r") as a:
    csvreader2 = csv.reader(a)
    for data2 in csvreader2:
        rows2.append(data2)
        
headers2 = rows2[0]
star_data_2 = rows2[1:]

radius = []
mass = []
mass2 = []
    
for m in star_data:
    radius.append(m[8])
    mass.append(m[7])
    
for l in star_data_2:
    mass2.append(l[7])
    
X = []

for index, mass2 in enumerate(mass):
    temp_list = [
                  radius[index],
                  mass
              ]
    X.append(temp_list)
    
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

