import pandas as pd

df = pd.read_csv("data.csv")

print("Numar randuri si coloane:", df.shape)

print("Numar jucatori unici:", df["Name"].nunique())