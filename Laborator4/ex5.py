import pandas as pd

df = pd.read_csv("data.csv")

rezultat = df[df["Contract Valid Until"].astype(str).str.contains("2021", na=False)]

print(rezultat)