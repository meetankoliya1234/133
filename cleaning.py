import pandas as pd
import csv

df = pd.read_csv('final.csv')
print(df.shape)
print(list(df))

del df["Luminosity_of_Star"]
del df["Constellation"]
del df["Sr no"]

print(df.shape)
print(list(df))

df.to_csv("cleaned_final.csv")