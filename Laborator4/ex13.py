import pandas as pd

df = pd.read_csv("data.csv")

df["Value"] = df["Value"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)
df["Wage"] = df["Wage"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)

df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["Wage"] = pd.to_numeric(df["Wage"], errors="coerce")

df["is_underpaid"] = df["Wage"] < (df["Value"] / 100)

print(df[["Name", "Value", "Wage", "is_underpaid"]])