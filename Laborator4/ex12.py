import pandas as pd

df = pd.read_csv("data.csv")

df["Value"] = df["Value"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)
df["Wage"] = df["Wage"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)

df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["Wage"] = pd.to_numeric(df["Wage"], errors="coerce")

rezultat = df[df["Value"] > df["Wage"]]

print("Numar jucatori:", rezultat.shape[0])