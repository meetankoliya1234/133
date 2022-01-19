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

X = star_data.iloc[:,[7,8]].values 

wcss = [] 

for i in range(1,11): 
    kmeans = KMeans(n_clusters =i, init = 'k-means++', random_state = 42) 
    kmeans.fit(X) 
    wcss.append((kmeans.inertia_)) 
    
plt.plot(range(1,11),wcss) 
plt.title("elbow method") 
plt.xlabel('Number of clusters') 
plt.show()
