import pandas as pd

df = pd.read_csv("data.csv")

rezultat = df[df["Age"] > 40].head(10)

print(rezultat)