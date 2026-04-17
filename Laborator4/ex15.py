import pandas as pd

df = pd.read_csv("data.csv")

df["Value"] = df["Value"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)
df["Wage"] = df["Wage"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)

df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["Wage"] = pd.to_numeric(df["Wage"], errors="coerce")

nou_df = df[["Name", "Wage", "Value"]].copy()

nou_df["difference"] = nou_df["Value"] - nou_df["Wage"]

nou_df = nou_df.sort_values(by="difference", ascending=False)

print(nou_df)